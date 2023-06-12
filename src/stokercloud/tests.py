import json
import pytest

from stokercloud.controller_data import ControllerData, PowerState, NotConnectedException, Unit, Value, State


def test_controller_data():
    test_data = """
        {
            "weatherdata": [
                {
                    "id": "weather-city",
                    "value": "Otterup",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                {
                    "id": 1,
                    "value": "21.8",
                    "unit": "lng_degree",
                    "name": "lng_weather_1",
                    "selection": ""
                },
                {
                    "id": "2",
                    "value": "4.69",
                    "unit": "lng_metersec",
                    "name": "lng_weather_2",
                    "selection": "weather1"
                },
                {
                    "id": "3",
                    "value": "ESE",
                    "unit": "",
                    "name": "lng_weather_3",
                    "selection": "weather2"
                },
                {
                    "id": "9",
                    "value": "0",
                    "unit": "lng_pct",
                    "name": "lng_weather_9",
                    "selection": "weather3"
                }
            ],
            "boilerdata": [
                {
                    "id": "17",
                    "value": "28.1",
                    "unit": "lng_degree",
                    "name": "lng_boil_17",
                    "selection": "boiler1"
                },
                {
                    "id": "5",
                    "value": "3.8",
                    "unit": "lng_kw",
                    "name": "lng_boil_5",
                    "selection": "boiler2"
                },
                {
                    "id": "4",
                    "value": "0",
                    "unit": "lng_pct",
                    "name": "lng_boil_4",
                    "selection": "boiler3"
                },
                {
                    "id": "6",
                    "value": "0",
                    "unit": "",
                    "name": "lng_boil_6",
                    "selection": "boiler4"
                },
                {
                    "id": "12",
                    "value": "0.0",
                    "unit": "lng_pct",
                    "name": "lng_boil_12",
                    "selection": "boiler5"
                },
                {
                    "id": "14",
                    "value": "129",
                    "unit": "lng_pct",
                    "name": "lng_boil_14",
                    "selection": "boiler6"
                },
                {
                    "id": "15",
                    "value": "89",
                    "unit": "lng_pct",
                    "name": "lng_boil_15",
                    "selection": "boiler7"
                },
                {
                    "id": "16",
                    "value": "89",
                    "unit": "lng_pct",
                    "name": "lng_boil_16",
                    "selection": "boiler8"
                },
                {
                    "id": "9",
                    "value": "100.0",
                    "unit": "lng_pct",
                    "name": "lng_boil_9",
                    "selection": "boiler9"
                },
                {
                    "id": "5",
                    "value": "0.0",
                    "unit": "lng_kw",
                    "name": "lng_boil_5",
                    "selection": "boiler10"
                }
            ],
            "hopperdata": [
                {
                    "id": "2",
                    "value": "1525",
                    "unit": "lng_g",
                    "name": "lng_hopper_2",
                    "selection": "hopper1"
                },
                {
                    "id": "3",
                    "value": "4.3",
                    "unit": "lng_kg",
                    "name": "lng_hopper_3",
                    "selection": "hopper2"
                },
                {
                    "id": "4",
                    "value": "7599",
                    "unit": "lng_kg",
                    "name": "lng_hopper_4",
                    "selection": "hopper3"
                },
                {
                    "id": "7",
                    "value": "2.5",
                    "unit": "lng_kw",
                    "name": "lng_hopper_7",
                    "selection": "hopper4"
                },
                {
                    "id": "8",
                    "value": "16",
                    "unit": "lng_kw",
                    "name": "lng_hopper_8",
                    "selection": "hopper5"
                },
                {
                    "id": "1",
                    "value": "-5208",
                    "unit": "lng_kg",
                    "name": "lng_hopper_1",
                    "selection": "hopper6"
                }
            ],
            "dhwdata": [
                {
                    "id": "3",
                    "value": "10",
                    "unit": "lng_degree",
                    "name": "lng_dhw_3",
                    "selection": "dhw1"
                },
                {
                    "id": "4",
                    "value": "N\/A",
                    "unit": "lng_pct",
                    "name": "lng_dhw_4",
                    "selection": "dhw2"
                }
            ],
            "frontdata": [
                {
                    "id": "hoppercontent",
                    "value": "-5208",
                    "unit": "lng_kg",
                    "name": "lng_hopper_1",
                    "selection": ""
                },
                {
                    "id": "boilertemp",
                    "value": "43.5",
                    "unit": "lng_degree",
                    "name": "lng_boil_1",
                    "selection": ""
                },
                {
                    "id": "-wantedboilertemp",
                    "value": "85.0",
                    "unit": "lng_degree",
                    "name": "lng_boil_2",
                    "selection": ""
                },
                {
                    "id": "dhw",
                    "value": 999.9,
                    "unit": "lng_degree",
                    "name": "lng_dhw_1",
                    "selection": ""
                },
                {
                    "id": "dhwwanted",
                    "value": "60",
                    "unit": "lng_degree",
                    "name": "lng_dhw_2",
                    "selection": ""
                },
                {
                    "id": "refoxygen",
                    "value": "0.0",
                    "unit": "lng_pct",
                    "name": "lng_boil_13",
                    "selection": ""
                },
                {
                    "id": "refair",
                    "value": "0",
                    "unit": "lng_m3hour",
                    "name": "lng_boil_13",
                    "selection": ""
                },
                {
                    "id": "smoketemp",
                    "value": 31.4,
                    "unit": "lng_degree",
                    "name": "lng_boil_3",
                    "selection": null
                },
                {
                    "id": "oxygen",
                    "value": "0.0",
                    "unit": "lng_pct",
                    "name": "lng_boil_12",
                    "selection": null
                },
                {
                    "id": "pressure",
                    "value": "3",
                    "unit": "lng_pascal",
                    "name": "lng_boil_24",
                    "selection": null
                },
                {
                    "id": "exhaust",
                    "value": "0",
                    "unit": "lng_pct",
                    "name": "",
                    "selection": null
                },
                {
                    "id": "hopperdistance",
                    "value": "49",
                    "unit": "lng_pct",
                    "name": "lng_hopper_14",
                    "selection": null
                },
                {
                    "id": "hopperimg",
                    "value": 2,
                    "unit": "",
                    "name": "",
                    "selection": null
                },
                {
                    "id": "ashdist",
                    "value": "100",
                    "unit": "lng_pct",
                    "name": "",
                    "selection": null
                }
            ],
            "miscdata": {
                "state": {
                    "id": "state",
                    "value": "lng_state_23",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "clock": {
                    "id": "clock",
                    "value": "14:23",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "substate": {
                    "id": "substate",
                    "value": "lng_substate_223",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "substatesecs": {
                    "id": "substatesecs",
                    "value": "0",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "alarm": 0,
                "running": 1,
                "output": 0,
                "outputpct": "0",
                "hopper.distance_max": "2",
                "vacuum.min_distance": "70",
                "vacuum.max_distance": "20",
                "vacuum.output_auger": "0",
                "backpressure": "100",
                "hopperdistance": "49"
            },
            "leftoutput": {
                "output-1": {
                    "val": "disabled",
                    "unit": "",
                    "image": "1-dhw.png"
                },
                "output-2": {
                    "val": "OFF",
                    "unit": "",
                    "image": "2-pump.png"
                },
                "output-3": {
                    "val": "disabled",
                    "unit": "",
                    "image": "3-weathervalve.png"
                },
                "output-4": {
                    "val": "disabled",
                    "unit": "",
                    "image": "4-weatherpump.png"
                },
                "output-5": {
                    "val": "0",
                    "unit": "%",
                    "image": "5-exhaustfan.png"
                },
                "output-6": {
                    "val": "disabled",
                    "unit": "LNG_KG",
                    "image": "6-ashauger.png"
                },
                "output-7": {
                    "val": "30.0",
                    "unit": "",
                    "image": "7-compressor.png"
                },
                "output-8": {
                    "val": "disabled",
                    "unit": "%",
                    "image": "8-weathervalve2.png"
                },
                "output-9": {
                    "val": "disabled",
                    "unit": "",
                    "image": "9-weatherpump2.png"
                }
            },
            "rightoutput": {
                "sunoutput-1": {
                    "val": "disabled",
                    "unit": "",
                    "image": "output-sun-pump.png"
                },
                "sunoutput-2": {
                    "val": "disabled",
                    "unit": "",
                    "image": "output-sun-valve.png"
                }
            },
            "infomessages": [
                "64",
                "84",
                ""
            ],
            "model": "0",
            "weathercomp": {
                "zone1active": 0,
                "zone2active": 0,
                "zone1-wanted": {
                    "val": 0,
                    "unit": "lng_degree"
                },
                "zone1-actual": {
                    "val": 0,
                    "unit": "lng_degree"
                },
                "zone1-valve": {
                    "val": "0",
                    "unit": "lng_pct"
                },
                "zone1-actualref": {
                    "val": 0,
                    "unit": "lng_degree"
                },
                "zone1-calc": {
                    "val": 0,
                    "unit": "lng_degree"
                },
                "zone2-wanted": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone2-actual": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone2-valve": {
                    "val": "0",
                    "unit": "lng_pct"
                },
                "zone2-actualref": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone2-calc": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone3active": 0,
                "zone3-wanted": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone3-actual": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone3-valve": {
                    "val": "0",
                    "unit": "lng_pct"
                },
                "zone3-actualref": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone3-calc": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone4active": 0,
                "zone4-wanted": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone4-actual": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone4-valve": {
                    "val": "0",
                    "unit": "lng_pct"
                },
                "zone4-actualref": {
                    "val": "0.0",
                    "unit": "lng_degree"
                },
                "zone4-calc": {
                    "val": "0.0",
                    "unit": "lng_degree"
                }
            },
            "notconnected": 0,
            "newuser": 0,
            "serial": "69173",
            "alias": "cytram",
            "expirydate": "2020-06-01 00:00:00",
            "expireflag": 3,
            "admin": 0,
            "type": "v16",
            "metrics": "EUR"
        }
    """
    cd = ControllerData(json.loads(test_data))

    assert cd.running == PowerState.ON
    assert cd.alarm == PowerState.OFF
    assert cd.serial_number == "69173"
    assert cd.boiler_kwh == Value("3.8", Unit.KWH)
    assert cd.hopper_distance == Value("49", Unit.PERCENT)
    assert cd.boiler_return_temperature == Value("28.1", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("43.5", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("85.0", Unit.DEGREE)
    assert cd.state == State.POWER
    assert cd.consumption_total == Value("7599", Unit.KILO_GRAM)


def test_controller_data_connected():
    test_data = '{"notconnected": 1}'
    with pytest.raises(NotConnectedException):
        ControllerData(json.loads(test_data))