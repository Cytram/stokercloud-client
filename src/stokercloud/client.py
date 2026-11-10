import json
from http.client import HTTPResponse
from urllib import request
from urllib.parse import urljoin
import logging
import time
from stokercloud.controller_data import ControllerData

logger = logging.getLogger(__name__)


class TokenInvalid(Exception):
    pass


class Client:
    BASE_URL = "http://www.stokercloud.dk/"

    # Which values the API returns in boilerdata/hopperdata/dhwdata/weatherdata.
    # Format is <slot>,<id> where the id is the lng_boil_/lng_hopper_/lng_dhw_/
    # lng_weather_ number. The API accepts at most 10 boiler, 10 hopper,
    # 10 DHW and 5 weather slots; 0 means empty.
    SCREEN = ",".join([
        # boiler: return temp, kW, power %, photo sensor, O2,
        # O2 regulation low/mid/high, online time, drop shaft temp
        "b1,17", "b2,5", "b3,4", "b4,6", "b5,12",
        "b6,14", "b7,15", "b8,16", "b9,9", "b10,7",
        # DHW: difference, heat/DHW
        "d1,3", "d2,4", "d3,0", "d4,0", "d5,0",
        "d6,0", "d7,0", "d8,0", "d9,0", "d10,0",
        # hopper: auger capacity, consumption 24h, consumption total,
        # power 10%, power 100%, content, auger low, auger high, trip 1, trip 2
        "h1,2", "h2,3", "h3,4", "h4,7", "h5,8",
        "h6,1", "h7,9", "h8,10", "h9,5", "h10,13",
        # weather: wind speed, wind direction, clouds, humidity, air pressure
        # (city and outdoor temperature are always included)
        "w1,2", "w2,3", "w3,9", "w4,4", "w5,5",
    ])

    def __init__(self, name: str, password: str = None, cache_time_seconds: int = 10):
        self.name = name
        self.password = password
        self.token = None
        self.state = None
        self.last_fetch = None
        self.cache_time_seconds = cache_time_seconds

    def refresh_token(self):
        with request.urlopen(
                urljoin(
                    self.BASE_URL,
                    'v16bckbeta/dataout2/login.php?user=%s' % self.name
                )
        ) as response:
            data = json.loads(response.read())
            self.token = data['token']  # actual token
            self.state = data['credentials']  # readonly

    def make_request(self, url, *args, **kwargs):
        try:
            if self.token is None:
                raise TokenInvalid()
            absolute_url = urljoin(
                self.BASE_URL,
                "%s&token=%s" % (url, self.token)
            )
            logger.debug(absolute_url)
            with request.urlopen(absolute_url) as data:
                return json.load(data)
        except TokenInvalid:
            self.refresh_token()
            return self.make_request(url, *args, **kwargs)

    def update_controller_data(self):
        self.cached_data = self.make_request(
            "v16bckbeta/dataout2/controllerdata2.php?screen=%s" % self.SCREEN
        )
        self.last_fetch = time.time()

    def controller_data(self):
        if not self.last_fetch or (time.time() - self.last_fetch) > self.cache_time_seconds:
            self.update_controller_data()
        return ControllerData(self.cached_data)
