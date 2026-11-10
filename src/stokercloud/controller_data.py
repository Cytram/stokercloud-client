import decimal
from enum import Enum


class NotConnectedException(Exception):
    pass


class PowerState(Enum):
    ON = 1
    OFF = 0


class Unit(Enum):
    KWH = 'kwh'
    KW = 'kw'
    PERCENT = 'pct'
    DEGREE = 'deg'
    KILO_GRAM = 'kg'
    GRAM = 'g'
    CM = 'cm'
    PASCAL = 'pa'
    METER_PER_SECOND = 'm/s'
    LITER_HOUR = 'l/h'
    M3_HOUR = 'm3/h'
    HPA = 'hpa'
    SECOND = 's'
    NONE = ''


class State(Enum):
    HEATING_PROPE = 'lng_state_0'
    POWER_UP = 'lng_state_1'
    IGNITION_1 = 'lng_state_2'
    IGNITION_2 = 'lng_state_4'
    POWER = 'lng_state_5'
    HOT_WATER = 'lng_state_7'
    ALARM_BOILER_TEMPERATURE = 'lng_state_8'
    STOPPED_TEMPERATURE_REACHED = 'lng_state_9'
    ALARM_BURNER_TEMPERATURE = 'lng_state_11'
    PLUG_DISCONNECTED = 'lng_state_12'
    FAULT_IGNITION = 'lng_state_13'
    OFF = 'lng_state_14'
    ERROR_BOILER_SENSOR = 'lng_state_15'
    ERROR_BURNER_SENSOR = 'lng_state_17'
    ERROR_AUGER_OUTPUT = 'lng_state_19'
    ERROR_NO_FIRE = 'lng_state_20'
    STOPPED_BY_EXTERNAL_TEMP = 'lng_state_22'
    STOPPED_BY_TIMER = 'lng_state_23'
    STOPPED_BY_EXTERNAL_CONTACT = 'lng_state_24'
    STOPPED_BY_WEATHER_COMP = 'lng_state_25'
    ALARM_OVERHEAT = 'lng_state_29'
    STOPPED_BY_CASCADE = 'lng_state_30'
    ERROR_COMPRESSOR = 'lng_state_31'
    ERROR_AIRFLOW = 'lng_state_37'
    OUTLET_TEMPERATURE_TOO_HIGH = 'lng_state_38'
    ASH_BOX_NOT_CONNECTED = 'lng_state_39'
    ALARM_BOILER_VACUUM = 'lng_state_41'
    ERROR_OXYGEN_SENSOR = 'lng_state_42'
    COMPRESSOR_CLEANING = 'lng_state_43'
    ERROR_IGNITER = 'lng_state_44'
    ERROR_VACUUM_SENSOR = 'lng_state_45'
    STOPPED_EMPTY_HOPPER = 'lng_state_46'
    NO_DISTANCE_SENSOR_READING = 'lng_state_47'

STATE_BY_VALUE = {key.value: key for key in State}
# The API has also been seen sending these codes without the lng_ prefix.
STATE_BY_VALUE.update({key.value[len('lng_'):]: key for key in State})


# Info message texts from StokerCloud's locale file (lng_info_<id>), for the
# messages that have a text. Used by ControllerData.info_messages.
INFO_MESSAGES = {
    4: "No light on photo sensor for more than 1 minute",
    9: "You got a new message on Stokercloud.dk",
    10: "Power is restricted by weathercompensation",
    14: "No connection to extension board",
    21: "Safety run on solar heating, fail temperature sensor",
    22: "Excess solar heating",
    23: "Woodpellet level low",
    25: "Power is restricted by high air temperature",
    26: "Error on calorifere room temp.sensor",
    27: "Error on calorifere exhaust temp.sensor T2",
    28: "Error on calorifere outlet temp.sensor T3",
    29: "Error on weathercomp. 1 forward sensor",
    30: "Error on weathercomp. 1 reference sensor",
    31: "Error on weathercomp. 2 forward sensor",
    32: "Error on weathercomp. 2 reference sensor",
    33: "Error on DHW temperature sensor T4",
    34: "Error on boiler return temperature sensor T3",
    35: "Error on solar sunpanel 1 temperature sensor",
    36: "Error on solar sunpanel 2 temperature sensor",
    37: "Error on solar DHW bottom temperature sensor",
    38: "Error on solar excess temperature sensor",
    39: "Boiler cleaning blocked by timer",
    40: "Alarm ext. feed: Distance sensor out of range for given time",
    41: "Alarm external feed: failure to increase pellets",
    42: "Error in vacuum transport was reset by user",
    43: "Ash tray full and must be emptied!",
    44: "Ash box contact switched from On to Off",
    48: "External feed started",
    49: "External feed stopped",
    50: "Cooling device in stopped/error state",
    52: "Power limited due to reduced airflow",
    53: "Power reduced due to missing boiler vacuum",
    60: "Circulation pump boiler exerciser",
    61: "Weathercomp. 1 pump exercise",
    62: "Weathercomp. 2 pump exercise",
    63: "Sun pump exercise",
    64: "Errors during cleaning",
    69: "Flame stabilization on",
    70: "Flame stabilization off",
    73: "Power is no longer reduced by airflow",
    74: "Weather comp. reduced by return temp.",
    75: "Weather comp. not reduced by return temp.",
    76: "Power is no longer reduced, vacuum ok",
    77: "Auger capacity has been reset to the value 3 hours ago",
    80: "Forward sensor error on weather compensation zone 3",
    81: "Reference sensor error on weather compensation zone 3",
    82: "Forward sensor error on weather compensation zone 4",
    83: "Reference sensor error on weather compensation zone 4",
    84: "Weather zone 3 pump motion",
    85: "Weather zone 4 pump motion",
    86: "Oxygen sensor MUST be calibrated",
    87: "Awaiting start",
    100: "Error vacuum, possible cause exhaust fan switched off / defect",
    101: "Error vacuum, possible cause exhaust fan blocked",
    102: "Error ash motor, possible cause disconnected plug / defect motor / blocked boiler",
    103: "Error ash motor, possible cause blocked motor / defect motor / blocked boiler",
    104: "Error vacuum, possible cause broken hose",
    105: "Error vacuum, possible cause hose/boiler/chimney blocked",
    106: "Error vacuum, possible error vacuum module",
    107: "Error airflow, possible cause disconnected plug / defect fan",
    108: "Error airflow, possible cause blocked fan / defect fan",
    109: "Error airflow, possible cause broken hose",
    110: "Error airflow, possible cause defect fan / blocked filter / defect airflow module",
    111: "Error airflow, possible cause defect airflow module",
    122: "Exhaust fan speed > 90% in more than 40% of the time",
    123: "Exhaust fan speed no longer > 90% in more than 40% of the time",
}

# The controller reports this value for temperature sensors that are not fitted.
SENSOR_NOT_CONNECTED = decimal.Decimal('999.9')


class Value:
    def __init__(self, value, unit):
        self.value = decimal.Decimal(value)
        self.unit = unit

    def __eq__(self, other):
        if not isinstance(other, Value):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.value == other.value and self.unit == other.unit

    def __repr__(self):
        return "%s %s" % (self.value, self.unit)


class InfoMessage:
    def __init__(self, _id, value, unit):
        self.id = _id
        self.value = value
        self.unit = unit

    @property
    def text(self):
        return INFO_MESSAGES.get(self.id)

    def __eq__(self, other):
        if not isinstance(other, InfoMessage):
            return NotImplemented
        return (self.id, self.value, self.unit) == (other.id, other.value, other.unit)

    def __repr__(self):
        return "InfoMessage(%s, %r, %r)" % (self.id, self.value, self.unit)


class Output:
    """A relay/output on the controller (pump, valve, fan, compressor, ...)."""

    def __init__(self, raw):
        self.raw = raw.get('val')
        self.unit = raw.get('unit') or ''

    @property
    def enabled(self):
        """False when the output is not configured on this controller."""
        return self.raw != 'disabled'

    @property
    def is_on(self):
        """True/False for on/off outputs, None for outputs that report a level."""
        if self.raw == 'ON':
            return True
        if self.raw == 'OFF':
            return False
        return None

    @property
    def value(self):
        """Numeric level (e.g. fan %) or None for on/off and disabled outputs."""
        return to_decimal(self.raw)

    def __repr__(self):
        return "Output(%r %s)" % (self.raw, self.unit)


class WeatherZone:
    def __init__(self, data, number):
        self.number = number
        self.active = data.get('zone%dactive' % number) == 1
        self.wanted = _zone_value(data, number, 'wanted', Unit.DEGREE)
        self.actual = _zone_value(data, number, 'actual', Unit.DEGREE)
        self.valve = _zone_value(data, number, 'valve', Unit.PERCENT)
        self.actual_reference = _zone_value(data, number, 'actualref', Unit.DEGREE)
        self.calculated = _zone_value(data, number, 'calc', Unit.DEGREE)

    def __repr__(self):
        return "WeatherZone(%d, active=%s)" % (self.number, self.active)


def _zone_value(data, number, key, unit):
    item = data.get('zone%d-%s' % (number, key)) or {}
    return to_value(item.get('val'), unit)


def to_decimal(raw):
    """Convert an API value to Decimal; None for missing/'N/A'/non-numeric values."""
    if raw is None or raw == '':
        return None
    try:
        return decimal.Decimal(str(raw))
    except decimal.InvalidOperation:
        return None


def to_value(raw, unit):
    number = to_decimal(raw)
    if number is None:
        return None
    return Value(number, unit)


def get_from_list_by_key(lst, key, value):
    for itm in lst:
        if itm.get(key) == value:
            return itm


# Outputs in "leftoutput", keyed by the API name.
LEFT_OUTPUTS = {
    'output-1': 'dhw_valve',
    'output-2': 'boiler_pump',
    'output-3': 'weather_valve_1',
    'output-4': 'weather_pump_1',
    'output-5': 'exhaust_fan',
    'output-6': 'ash_auger',
    'output-7': 'compressor',
    'output-8': 'weather_valve_2',
    'output-9': 'weather_pump_2',
}
RIGHT_OUTPUTS = {
    'sunoutput-1': 'sun_pump',
    'sunoutput-2': 'sun_valve',
}


class ControllerData:
    def __init__(self, data):
        if data['notconnected'] != 0:
            raise NotConnectedException("Furnace/boiler not connected to StokerCloud")
        self.data = data

    # -- helpers ---------------------------------------------------------

    def get_sub_item(self, submenu, _id):
        return get_from_list_by_key(self.data.get(submenu) or [], 'id', _id)

    def _sub_value(self, submenu, _id, unit):
        """Value for an item in boilerdata/hopperdata/dhwdata/weatherdata/frontdata.

        Returns None when the item was not requested in the screen parameter
        or the controller reports it as N/A.
        """
        item = self.get_sub_item(submenu, _id)
        if item is None:
            return None
        return to_value(item.get('value'), unit)

    def _sensor_value(self, submenu, _id):
        """Temperature value; None when the sensor is not connected (999.9)."""
        value = self._sub_value(submenu, _id, Unit.DEGREE)
        if value is None or value.value == SENSOR_NOT_CONNECTED:
            return None
        return value

    def _misc(self, key):
        return (self.data.get('miscdata') or {}).get(key)

    def _misc_item_value(self, key):
        item = self._misc(key)
        if isinstance(item, dict):
            return item.get('value')
        return item

    # -- general ---------------------------------------------------------

    @property
    def alarm(self):
        return {
            0: PowerState.OFF,
            1: PowerState.ON
        }.get(self.data['miscdata'].get('alarm'))

    @property
    def running(self):
        return {
            0: PowerState.OFF,
            1: PowerState.ON
        }.get(self.data['miscdata'].get('running'))

    @property
    def serial_number(self):
        return self.data['serial']

    @property
    def alias(self):
        return self.data.get('alias')

    @property
    def controller_type(self):
        return self.data.get('type')

    @property
    def model(self):
        return self.data.get('model')

    @property
    def clock(self):
        """Time of day on the controller, e.g. '17:58'."""
        return self._misc_item_value('clock')

    @property
    def state(self):
        value = self.data['miscdata']['state']['value']
        return STATE_BY_VALUE.get(value, value)

    @property
    def substate(self):
        """Raw substate code (e.g. 'lng_substate_223'), None when empty."""
        return self._misc_item_value('substate') or None

    @property
    def substate_seconds(self):
        value = to_decimal(self._misc_item_value('substatesecs'))
        return int(value) if value is not None else None

    @property
    def info_messages(self):
        """Active info messages as InfoMessage(id, value, unit).

        The API sends a flat list of (id, value, unit) triples, e.g.
        ["64", "5", ""] meaning "Errors during cleaning = 5".
        """
        raw = self.data.get('infomessages') or []
        messages = []
        for i in range(0, len(raw) - len(raw) % 3, 3):
            _id, value, unit = raw[i:i + 3]
            if _id in (None, ''):
                continue
            try:
                _id = int(_id)
            except (TypeError, ValueError):
                pass
            messages.append(InfoMessage(_id, value, unit))
        return messages

    # -- boiler ----------------------------------------------------------

    @property
    def boiler_temperature_current(self):
        return Value(self.get_sub_item('frontdata', 'boilertemp')['value'], Unit.DEGREE)

    @property
    def boiler_temperature_requested(self):
        return Value(self.get_sub_item('frontdata', '-wantedboilertemp')['value'], Unit.DEGREE)

    @property
    def boiler_kwh(self):
        return Value(self.get_sub_item('boilerdata', '5')['value'], Unit.KWH)

    @property
    def boiler_return_temperature(self):
        return Value(self.get_sub_item('boilerdata', '17')['value'], Unit.DEGREE)

    @property
    def power_output(self):
        """Current output in kW (miscdata.output)."""
        return to_value(self._misc('output'), Unit.KW)

    @property
    def power_percent(self):
        return to_value(self._misc('outputpct'), Unit.PERCENT)

    @property
    def smoke_temperature(self):
        return self._sub_value('frontdata', 'smoketemp', Unit.DEGREE)

    @property
    def drop_shaft_temperature(self):
        """Drop shaft (faldskakt) temperature, boilerdata id 7."""
        return self._sub_value('boilerdata', '7', Unit.DEGREE)

    @property
    def photo_sensor(self):
        return self._sub_value('boilerdata', '6', Unit.NONE)

    @property
    def oxygen(self):
        return self._sub_value('frontdata', 'oxygen', Unit.PERCENT)

    @property
    def oxygen_requested(self):
        return self._sub_value('frontdata', 'refoxygen', Unit.PERCENT)

    @property
    def oxygen_regulation_low(self):
        return self._sub_value('boilerdata', '14', Unit.PERCENT)

    @property
    def oxygen_regulation_mid(self):
        return self._sub_value('boilerdata', '15', Unit.PERCENT)

    @property
    def oxygen_regulation_high(self):
        return self._sub_value('boilerdata', '16', Unit.PERCENT)

    @property
    def air_requested(self):
        return self._sub_value('frontdata', 'refair', Unit.M3_HOUR)

    @property
    def pressure(self):
        """Boiler vacuum/pressure in Pa."""
        return self._sub_value('frontdata', 'pressure', Unit.PASCAL)

    @property
    def exhaust_fan(self):
        return self._sub_value('frontdata', 'exhaust', Unit.PERCENT)

    @property
    def online_time(self):
        return self._sub_value('boilerdata', '9', Unit.PERCENT)

    @property
    def flow(self):
        return self._sub_value('boilerdata', '10', Unit.LITER_HOUR)

    @property
    def ash_distance(self):
        return self._sub_value('frontdata', 'ashdist', Unit.PERCENT)

    @property
    def back_pressure(self):
        return to_value(self._misc('backpressure'), Unit.PERCENT)

    # -- hopper ----------------------------------------------------------

    @property
    def hopper_capacity(self):
        return Value(self.data['miscdata'].get('hopperdistance'), Unit.CM)

    @property
    def hopper_content(self):
        """Calculated hopper content in kg (filled minus consumed)."""
        return self._sub_value('frontdata', 'hoppercontent', Unit.KILO_GRAM)

    @property
    def hopper_level(self):
        """Hopper level image index 0-5 used by the StokerCloud UI."""
        return self._sub_value('frontdata', 'hopperimg', Unit.NONE)

    @property
    def auger_capacity(self):
        return self._sub_value('hopperdata', '2', Unit.GRAM)

    @property
    def auger_low(self):
        return self._sub_value('hopperdata', '9', Unit.PERCENT)

    @property
    def auger_high(self):
        return self._sub_value('hopperdata', '10', Unit.PERCENT)

    @property
    def consumption_total(self):
        return Value(self.get_sub_item('hopperdata', '4')['value'], Unit.KILO_GRAM)

    @property
    def consumption_day(self):
        return Value(self.get_sub_item('hopperdata', '3')['value'], Unit.KILO_GRAM)

    @property
    def trip_1(self):
        return self._sub_value('hopperdata', '5', Unit.KILO_GRAM)

    @property
    def trip_2(self):
        return self._sub_value('hopperdata', '13', Unit.KILO_GRAM)

    @property
    def power_10_percent(self):
        return self._sub_value('hopperdata', '7', Unit.KW)

    @property
    def power_100_percent(self):
        return self._sub_value('hopperdata', '8', Unit.KW)

    # -- hot water (DHW) -------------------------------------------------

    @property
    def hotwater_temperature_current(self):
        return Value(self.get_sub_item('frontdata', 'dhw')['value'], Unit.DEGREE)

    @property
    def hotwater_temperature_requested(self):
        return Value(self.get_sub_item('frontdata', 'dhwwanted')['value'], Unit.DEGREE)

    @property
    def hotwater_sensor_connected(self):
        return self._sensor_value('frontdata', 'dhw') is not None

    @property
    def hotwater_difference(self):
        return self._sub_value('dhwdata', '3', Unit.DEGREE)

    # -- weather ---------------------------------------------------------

    @property
    def weather_city(self):
        item = self.get_sub_item('weatherdata', 'weather-city')
        return item.get('value') if item else None

    @property
    def outdoor_temperature(self):
        # The API sends this id as an int, the others as strings.
        item = self.get_sub_item('weatherdata', 1) or self.get_sub_item('weatherdata', '1')
        return to_value(item.get('value'), Unit.DEGREE) if item else None

    @property
    def wind_speed(self):
        return self._sub_value('weatherdata', '2', Unit.METER_PER_SECOND)

    @property
    def wind_direction(self):
        item = self.get_sub_item('weatherdata', '3')
        return item.get('value') if item else None

    @property
    def humidity(self):
        return self._sub_value('weatherdata', '4', Unit.PERCENT)

    @property
    def air_pressure(self):
        return self._sub_value('weatherdata', '5', Unit.HPA)

    @property
    def clouds(self):
        return self._sub_value('weatherdata', '9', Unit.PERCENT)

    @property
    def weather_zones(self):
        data = self.data.get('weathercomp') or {}
        return [WeatherZone(data, n) for n in (1, 2, 3, 4)]

    # -- outputs ---------------------------------------------------------

    @property
    def outputs(self):
        """All controller outputs keyed by name (see LEFT_OUTPUTS/RIGHT_OUTPUTS)."""
        result = {}
        for section, names in (('leftoutput', LEFT_OUTPUTS), ('rightoutput', RIGHT_OUTPUTS)):
            for key, raw in (self.data.get(section) or {}).items():
                result[names.get(key, key)] = Output(raw)
        return result
