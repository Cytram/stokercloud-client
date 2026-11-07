import decimal
from enum import Enum


class NotConnectedException(Exception):
    pass


class PowerState(Enum):
    ON = 1
    OFF = 0


class Unit(Enum):
    KWH = 'kwh'
    PERCENT = 'pct'
    DEGREE = 'deg'
    KILO_GRAM = 'kg'
    GRAM = 'g'
    CM = 'cm'


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

def get_from_list_by_key(lst, key, value):
    for itm in lst:
        if itm.get(key) == value:
            return itm

class ControllerData:
    def __init__(self, data):
        if data['notconnected'] != 0:
            raise NotConnectedException("Furnace/boiler not connected to StokerCloud")
        self.data = data

    def get_sub_item(self, submenu, _id):
        return get_from_list_by_key(self.data[submenu], 'id', _id)

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
    def boiler_temperature_current(self):
        return Value(self.get_sub_item('frontdata', 'boilertemp')['value'], Unit.DEGREE)\

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
    def state(self):
        value = self.data['miscdata']['state']['value']
        return STATE_BY_VALUE.get(value, value)
    @property
    def hotwater_temperature_current(self):
        return Value(self.get_sub_item('frontdata', 'dhw')['value'], Unit.DEGREE)

    @property
    def hotwater_temperature_requested(self):
        return Value(self.get_sub_item('frontdata', 'dhwwanted')['value'], Unit.DEGREE)

    @property
    def hopper_capacity(self):
        return Value(self.data['miscdata'].get('hopperdistance'), Unit.CM)

    @property
    def consumption_total(self):
        return Value(self.get_sub_item('hopperdata', '4')['value'], Unit.KILO_GRAM)
    
    @property
    def consumption_day(self):
        return Value(self.get_sub_item('hopperdata', '3')['value'], Unit.KILO_GRAM)
