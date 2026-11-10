import json
import pytest

from stokercloud.controller_data import ControllerData, PowerState, NotConnectedException, Unit, Value, State, InfoMessage

def test_controller_probe_heating():
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
          "value": "19",
          "unit": "lng_degree",
          "name": "lng_weather_1",
          "selection": ""
        },
        {
          "id": "2",
          "value": "2.53",
          "unit": "lng_metersec",
          "name": "lng_weather_2",
          "selection": "weather1"
        },
        {
          "id": "3",
          "value": "N",
          "unit": "",
          "name": "lng_weather_3",
          "selection": "weather2"
        },
        {
          "id": "9",
          "value": "100",
          "unit": "lng_pct",
          "name": "lng_weather_9",
          "selection": "weather3"
        }
      ],
      "boilerdata": [
        {
          "id": "17",
          "value": "43.1",
          "unit": "lng_degree",
          "name": "lng_boil_17",
          "selection": "boiler1"
        },
        {
          "id": "5",
          "value": "0.0",
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
          "value": "134",
          "unit": "lng_pct",
          "name": "lng_boil_14",
          "selection": "boiler6"
        },
        {
          "id": "15",
          "value": "88",
          "unit": "lng_pct",
          "name": "lng_boil_15",
          "selection": "boiler7"
        },
        {
          "id": "16",
          "value": "83",
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
          "value": "2.2",
          "unit": "lng_kg",
          "name": "lng_hopper_3",
          "selection": "hopper2"
        },
        {
          "id": "4",
          "value": "7631",
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
          "value": "-5241",
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
          "value": "N/A",
          "unit": "lng_pct",
          "name": "lng_dhw_4",
          "selection": "dhw2"
        }
      ],
      "frontdata": [
        {
          "id": "hoppercontent",
          "value": "-5241",
          "unit": "lng_kg",
          "name": "lng_hopper_1",
          "selection": ""
        },
        {
          "id": "boilertemp",
          "value": "62.7",
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
          "value": 40.6,
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
          "value": "1",
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
          "value": "39",
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
          "value": "lng_state_0",
          "unit": "",
          "name": "",
          "selection": ""
        },
        "clock": {
          "id": "clock",
          "value": "09:27",
          "unit": "",
          "name": "",
          "selection": ""
        },
        "substate": {
          "id": "substate",
          "value": "lng_substate_24",
          "unit": "",
          "name": "",
          "selection": ""
        },
        "substatesecs": {
          "id": "substatesecs",
          "value": "257",
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
        "hopperdistance": "39"
      },
      "leftoutput": {
        "output-1": {
          "val": "disabled",
          "unit": "",
          "image": "1-dhw.png"
        },
        "output-2": {
          "val": "ON",
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
        "92",
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
    assert cd.boiler_kwh == Value("0", Unit.KWH)
    assert cd.hopper_capacity == Value("39", Unit.CM)
    assert cd.boiler_return_temperature == Value("43.1", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("62.7", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("85.0", Unit.DEGREE)
    assert cd.state == State.HEATING_PROPE
    assert cd.consumption_total == Value("7631", Unit.KILO_GRAM)
    assert cd.consumption_day == Value("2.2", Unit.KILO_GRAM)

def test_controller_igniting_1():
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
          "value": "19",
          "unit": "lng_degree",
          "name": "lng_weather_1",
          "selection": ""
        },
        {
          "id": "2",
          "value": "2.53",
          "unit": "lng_metersec",
          "name": "lng_weather_2",
          "selection": "weather1"
        },
        {
          "id": "3",
          "value": "N",
          "unit": "",
          "name": "lng_weather_3",
          "selection": "weather2"
        },
        {
          "id": "9",
          "value": "100",
          "unit": "lng_pct",
          "name": "lng_weather_9",
          "selection": "weather3"
        }
      ],
      "boilerdata": [
        {
          "id": "17",
          "value": "46.9",
          "unit": "lng_degree",
          "name": "lng_boil_17",
          "selection": "boiler1"
        },
        {
          "id": "5",
          "value": "0.0",
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
          "value": "20.6",
          "unit": "lng_pct",
          "name": "lng_boil_12",
          "selection": "boiler5"
        },
        {
          "id": "14",
          "value": "134",
          "unit": "lng_pct",
          "name": "lng_boil_14",
          "selection": "boiler6"
        },
        {
          "id": "15",
          "value": "88",
          "unit": "lng_pct",
          "name": "lng_boil_15",
          "selection": "boiler7"
        },
        {
          "id": "16",
          "value": "83",
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
          "value": "2.2",
          "unit": "lng_kg",
          "name": "lng_hopper_3",
          "selection": "hopper2"
        },
        {
          "id": "4",
          "value": "7631",
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
          "value": "-5241",
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
          "value": "N/A",
          "unit": "lng_pct",
          "name": "lng_dhw_4",
          "selection": "dhw2"
        }
      ],
      "frontdata": [
        {
          "id": "hoppercontent",
          "value": "-5241",
          "unit": "lng_kg",
          "name": "lng_hopper_1",
          "selection": ""
        },
        {
          "id": "boilertemp",
          "value": "56.6",
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
          "value": 43.2,
          "unit": "lng_degree",
          "name": "lng_boil_3",
          "selection": null
        },
        {
          "id": "oxygen",
          "value": "20.6",
          "unit": "lng_pct",
          "name": "lng_boil_12",
          "selection": null
        },
        {
          "id": "pressure",
          "value": "39",
          "unit": "lng_pascal",
          "name": "lng_boil_24",
          "selection": null
        },
        {
          "id": "exhaust",
          "value": "100",
          "unit": "lng_pct",
          "name": "",
          "selection": null
        },
        {
          "id": "hopperdistance",
          "value": "39",
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
          "value": "lng_state_2",
          "unit": "",
          "name": "",
          "selection": ""
        },
        "clock": {
          "id": "clock",
          "value": "09:31",
          "unit": "",
          "name": "",
          "selection": ""
        },
        "substate": {
          "id": "substate",
          "value": "lng_substate_1",
          "unit": "",
          "name": "",
          "selection": ""
        },
        "substatesecs": {
          "id": "substatesecs",
          "value": "9",
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
        "hopperdistance": "39"
      },
      "leftoutput": {
        "output-1": {
          "val": "disabled",
          "unit": "",
          "image": "1-dhw.png"
        },
        "output-2": {
          "val": "ON",
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
          "val": "100",
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
        "92",
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
    assert cd.boiler_kwh == Value("0", Unit.KWH)
    assert cd.hopper_capacity == Value("39", Unit.CM)
    assert cd.boiler_return_temperature == Value("46.9", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("56.6", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("85.0", Unit.DEGREE)
    assert cd.state == State.IGNITION_1
    assert cd.consumption_total == Value("7631", Unit.KILO_GRAM)
    assert cd.consumption_day == Value("2.2", Unit.KILO_GRAM)

def test_controller_igniting_2():
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
                "value": "3.5",
                "unit": "lng_degree",
                "name": "lng_weather_1",
                "selection": ""
            },
            {
                "id": "2",
                "value": "7.87",
                "unit": "lng_metersec",
                "name": "lng_weather_2",
                "selection": "weather1"
            },
            {
                "id": "3",
                "value": "WNW",
                "unit": "",
                "name": "lng_weather_3",
                "selection": "weather2"
            },
            {
                "id": "9",
                "value": "62",
                "unit": "lng_pct",
                "name": "lng_weather_9",
                "selection": "weather3"
            }
        ],
        "boilerdata": [
            {
                "id": "17",
                "value": "51.8",
                "unit": "lng_degree",
                "name": "lng_boil_17",
                "selection": "boiler1"
            },
            {
                "id": "5",
                "value": "0.0",
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
                "value": "18.7",
                "unit": "lng_pct",
                "name": "lng_boil_12",
                "selection": "boiler5"
            },
            {
                "id": "14",
                "value": "171",
                "unit": "lng_pct",
                "name": "lng_boil_14",
                "selection": "boiler6"
            },
            {
                "id": "15",
                "value": "95",
                "unit": "lng_pct",
                "name": "lng_boil_15",
                "selection": "boiler7"
            },
            {
                "id": "16",
                "value": "96",
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
                "id": "10",
                "value": null,
                "unit": "lng_literhour",
                "name": "lng_boil_10",
                "selection": "boiler10"
            }
        ],
        "hopperdata": [
            {
                "id": "2",
                "value": "1639",
                "unit": "lng_g",
                "name": "lng_hopper_2",
                "selection": "hopper1"
            },
            {
                "id": "3",
                "value": "15.2",
                "unit": "lng_kg",
                "name": "lng_hopper_3",
                "selection": "hopper2"
            },
            {
                "id": "4",
                "value": "11639",
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
                "value": "-1077",
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
                "value": "-1077",
                "unit": "lng_kg",
                "name": "lng_hopper_1",
                "selection": ""
            },
            {
                "id": "boilertemp",
                "value": "55.0",
                "unit": "lng_degree",
                "name": "lng_boil_1",
                "selection": ""
            },
            {
                "id": "-wantedboilertemp",
                "value": "65.0",
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
                "value": 52.8,
                "unit": "lng_degree",
                "name": "lng_boil_3",
                "selection": null
            },
            {
                "id": "oxygen",
                "value": "18.7",
                "unit": "lng_pct",
                "name": "lng_boil_12",
                "selection": null
            },
            {
                "id": "pressure",
                "value": "21",
                "unit": "lng_pascal",
                "name": "lng_boil_24",
                "selection": null
            },
            {
                "id": "exhaust",
                "value": "15",
                "unit": "lng_pct",
                "name": "",
                "selection": null
            },
            {
                "id": "hopperdistance",
                "value": "82",
                "unit": "lng_pct",
                "name": "lng_hopper_14",
                "selection": null
            },
            {
                "id": "hopperimg",
                "value": 4,
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
                "value": "lng_state_4",
                "unit": "",
                "name": "",
                "selection": ""
            },
            "clock": {
                "id": "clock",
                "value": "12:32",
                "unit": "",
                "name": "",
                "selection": ""
            },
            "substate": {
                "id": "substate",
                "value": "lng_substate_4",
                "unit": "",
                "name": "",
                "selection": ""
            },
            "substatesecs": {
                "id": "substatesecs",
                "value": "186",
                "unit": "",
                "name": "",
                "selection": ""
            },
            "alarm": 0,
            "running": 1,
            "output": 0,
            "outputpct": "0",
            "hopper.distance_max": "0",
            "vacuum.min_distance": "70",
            "vacuum.max_distance": "20",
            "vacuum.output_auger": "0",
            "backpressure": "100",
            "hopperdistance": "82"
        },
        "leftoutput": {
            "output-1": {
                "val": "disabled",
                "unit": "",
                "image": "1-dhw.png"
            },
            "output-2": {
                "val": "ON",
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
                "val": "15",
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
            "4",
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
    assert cd.boiler_kwh == Value("0", Unit.KWH)
    assert cd.hopper_capacity == Value("82", Unit.CM)
    assert cd.boiler_return_temperature == Value("51.8", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("55.0", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("65.0", Unit.DEGREE)
    assert cd.state == State.IGNITION_2
    assert cd.consumption_total == Value("7631", Unit.KILO_GRAM)
    assert cd.consumption_day == Value("2.2", Unit.KILO_GRAM)
def test_controller_running():
    test_data = """
    {
       "weatherdata":[
          {
             "id":"weather-city",
             "value":"Otterup",
             "unit":"",
             "name":"",
             "selection":""
          },
          {
             "id":1,
             "value":"19.6",
             "unit":"lng_degree",
             "name":"lng_weather_1",
             "selection":""
          },
          {
             "id":"2",
             "value":"0.99",
             "unit":"lng_metersec",
             "name":"lng_weather_2",
             "selection":"weather1"
          },
          {
             "id":"3",
             "value":"E",
             "unit":"",
             "name":"lng_weather_3",
             "selection":"weather2"
          },
          {
             "id":"9",
             "value":"56",
             "unit":"lng_pct",
             "name":"lng_weather_9",
             "selection":"weather3"
          }
       ],
       "boilerdata":[
          {
             "id":"17",
             "value":"59.7",
             "unit":"lng_degree",
             "name":"lng_boil_17",
             "selection":"boiler1"
          },
          {
             "id":"5",
             "value":"10.9",
             "unit":"lng_kw",
             "name":"lng_boil_5",
             "selection":"boiler2"
          },
          {
             "id":"4",
             "value":"66",
             "unit":"lng_pct",
             "name":"lng_boil_4",
             "selection":"boiler3"
          },
          {
             "id":"6",
             "value":"0",
             "unit":"",
             "name":"lng_boil_6",
             "selection":"boiler4"
          },
          {
             "id":"12",
             "value":"12.2",
             "unit":"lng_pct",
             "name":"lng_boil_12",
             "selection":"boiler5"
          },
          {
             "id":"14",
             "value":"134",
             "unit":"lng_pct",
             "name":"lng_boil_14",
             "selection":"boiler6"
          },
          {
             "id":"15",
             "value":"89",
             "unit":"lng_pct",
             "name":"lng_boil_15",
             "selection":"boiler7"
          },
          {
             "id":"16",
             "value":"86",
             "unit":"lng_pct",
             "name":"lng_boil_16",
             "selection":"boiler8"
          },
          {
             "id":"9",
             "value":"100.0",
             "unit":"lng_pct",
             "name":"lng_boil_9",
             "selection":"boiler9"
          },
          {
             "id":"5",
             "value":"10.9",
             "unit":"lng_kw",
             "name":"lng_boil_5",
             "selection":"boiler10"
          }
       ],
       "hopperdata":[
          {
             "id":"2",
             "value":"1525",
             "unit":"lng_g",
             "name":"lng_hopper_2",
             "selection":"hopper1"
          },
          {
             "id":"3",
             "value":"7.3",
             "unit":"lng_kg",
             "name":"lng_hopper_3",
             "selection":"hopper2"
          },
          {
             "id":"4",
             "value":"7628",
             "unit":"lng_kg",
             "name":"lng_hopper_4",
             "selection":"hopper3"
          },
          {
             "id":"7",
             "value":"2.5",
             "unit":"lng_kw",
             "name":"lng_hopper_7",
             "selection":"hopper4"
          },
          {
             "id":"8",
             "value":"16",
             "unit":"lng_kw",
             "name":"lng_hopper_8",
             "selection":"hopper5"
          },
          {
             "id":"1",
             "value":"-5237",
             "unit":"lng_kg",
             "name":"lng_hopper_1",
             "selection":"hopper6"
          }
       ],
       "dhwdata":[
          {
             "id":"3",
             "value":"10",
             "unit":"lng_degree",
             "name":"lng_dhw_3",
             "selection":"dhw1"
          },
          {
             "id":"4",
             "value":"N\/A",
             "unit":"lng_pct",
             "name":"lng_dhw_4",
             "selection":"dhw2"
          }
       ],
       "frontdata":[
          {
             "id":"hoppercontent",
             "value":"-5237",
             "unit":"lng_kg",
             "name":"lng_hopper_1",
             "selection":""
          },
          {
             "id":"boilertemp",
             "value":"77.8",
             "unit":"lng_degree",
             "name":"lng_boil_1",
             "selection":""
          },
          {
             "id":"-wantedboilertemp",
             "value":"85.0",
             "unit":"lng_degree",
             "name":"lng_boil_2",
             "selection":""
          },
          {
             "id":"dhw",
             "value":999.9,
             "unit":"lng_degree",
             "name":"lng_dhw_1",
             "selection":""
          },
          {
             "id":"dhwwanted",
             "value":"60",
             "unit":"lng_degree",
             "name":"lng_dhw_2",
             "selection":""
          },
          {
             "id":"refoxygen",
             "value":"12.1",
             "unit":"lng_pct",
             "name":"lng_boil_13",
             "selection":""
          },
          {
             "id":"refair",
             "value":"0",
             "unit":"lng_m3hour",
             "name":"lng_boil_13",
             "selection":""
          },
          {
             "id":"smoketemp",
             "value":133.5,
             "unit":"lng_degree",
             "name":"lng_boil_3",
             "selection":null
          },
          {
             "id":"oxygen",
             "value":"12.2",
             "unit":"lng_pct",
             "name":"lng_boil_12",
             "selection":null
          },
          {
             "id":"pressure",
             "value":"11",
             "unit":"lng_pascal",
             "name":"lng_boil_24",
             "selection":null
          },
          {
             "id":"exhaust",
             "value":"27",
             "unit":"lng_pct",
             "name":"",
             "selection":null
          },
          {
             "id":"hopperdistance",
             "value":"40",
             "unit":"lng_pct",
             "name":"lng_hopper_14",
             "selection":null
          },
          {
             "id":"hopperimg",
             "value":2,
             "unit":"",
             "name":"",
             "selection":null
          },
          {
             "id":"ashdist",
             "value":"100",
             "unit":"lng_pct",
             "name":"",
             "selection":null
          }
       ],
       "miscdata":{
          "state":{
             "id":"state",
             "value":"lng_state_5",
             "unit":"lng_kw",
             "name":"",
             "selection":""
          },
          "clock":{
             "id":"clock",
             "value":"20:21",
             "unit":"",
             "name":"",
             "selection":""
          },
          "substate":{
             "id":"substate",
             "value":"",
             "unit":"",
             "name":"",
             "selection":""
          },
          "substatesecs":{
             "id":"substatesecs",
             "value":0,
             "unit":"",
             "name":"",
             "selection":""
          },
          "alarm":0,
          "running":1,
          "output":10.9,
          "outputpct":"66",
          "hopper.distance_max":"2",
          "vacuum.min_distance":"70",
          "vacuum.max_distance":"20",
          "vacuum.output_auger":"0",
          "backpressure":"100",
          "hopperdistance":"40"
       },
       "leftoutput":{
          "output-1":{
             "val":"disabled",
             "unit":"",
             "image":"1-dhw.png"
          },
          "output-2":{
             "val":"ON",
             "unit":"",
             "image":"2-pump.png"
          },
          "output-3":{
             "val":"disabled",
             "unit":"",
             "image":"3-weathervalve.png"
          },
          "output-4":{
             "val":"disabled",
             "unit":"",
             "image":"4-weatherpump.png"
          },
          "output-5":{
             "val":"27",
             "unit":"%",
             "image":"5-exhaustfan.png"
          },
          "output-6":{
             "val":"disabled",
             "unit":"LNG_KG",
             "image":"6-ashauger.png"
          },
          "output-7":{
             "val":"27.1",
             "unit":"",
             "image":"7-compressor.png"
          },
          "output-8":{
             "val":"disabled",
             "unit":"%",
             "image":"8-weathervalve2.png"
          },
          "output-9":{
             "val":"disabled",
             "unit":"",
             "image":"9-weatherpump2.png"
          }
       },
       "rightoutput":{
          "sunoutput-1":{
             "val":"disabled",
             "unit":"",
             "image":"output-sun-pump.png"
          },
          "sunoutput-2":{
             "val":"disabled",
             "unit":"",
             "image":"output-sun-valve.png"
          }
       },
       "infomessages":[
          "64",
          "90",
          ""
       ],
       "model":"0",
       "weathercomp":{
          "zone1active":0,
          "zone2active":0,
          "zone1-wanted":{
             "val":0,
             "unit":"lng_degree"
          },
          "zone1-actual":{
             "val":0,
             "unit":"lng_degree"
          },
          "zone1-valve":{
             "val":"0",
             "unit":"lng_pct"
          },
          "zone1-actualref":{
             "val":0,
             "unit":"lng_degree"
          },
          "zone1-calc":{
             "val":0,
             "unit":"lng_degree"
          },
          "zone2-wanted":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone2-actual":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone2-valve":{
             "val":"0",
             "unit":"lng_pct"
          },
          "zone2-actualref":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone2-calc":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone3active":0,
          "zone3-wanted":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone3-actual":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone3-valve":{
             "val":"0",
             "unit":"lng_pct"
          },
          "zone3-actualref":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone3-calc":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone4active":0,
          "zone4-wanted":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone4-actual":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone4-valve":{
             "val":"0",
             "unit":"lng_pct"
          },
          "zone4-actualref":{
             "val":"0.0",
             "unit":"lng_degree"
          },
          "zone4-calc":{
             "val":"0.0",
             "unit":"lng_degree"
          }
       },
       "notconnected":0,
       "newuser":0,
       "serial":"69173",
       "alias":"cytram",
       "expirydate":"2020-06-01 00:00:00",
       "expireflag":3,
       "admin":0,
       "type":"v16",
       "metrics":"EUR"
    }
    """
    cd = ControllerData(json.loads(test_data))

    assert cd.running == PowerState.ON
    assert cd.alarm == PowerState.OFF
    assert cd.serial_number == "69173"
    assert cd.boiler_kwh == Value("10.9", Unit.KWH)
    assert cd.hopper_capacity == Value("40", Unit.CM)
    assert cd.boiler_return_temperature == Value("59.7", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("77.8", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("85.0", Unit.DEGREE)
    assert cd.state == State.POWER
    assert cd.consumption_total == Value("7628", Unit.KILO_GRAM)
    assert cd.consumption_day == Value("7.3", Unit.KILO_GRAM)

def test_controller_shutdown():
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
    assert cd.hopper_capacity == Value("49", Unit.CM)
    assert cd.boiler_return_temperature == Value("28.1", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("43.5", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("85.0", Unit.DEGREE)
    assert cd.state == State.STOPPED_BY_TIMER
    assert cd.consumption_total == Value("7599", Unit.KILO_GRAM)
    assert cd.consumption_day == Value("4.3", Unit.KILO_GRAM)

def test_controller_external_temp():
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
                    "value": "8.5",
                    "unit": "lng_degree",
                    "name": "lng_weather_1",
                    "selection": ""
                },
                {
                    "id": "2",
                    "value": "6.29",
                    "unit": "lng_metersec",
                    "name": "lng_weather_2",
                    "selection": "weather1"
                },
                {
                    "id": "3",
                    "value": "W",
                    "unit": "",
                    "name": "lng_weather_3",
                    "selection": "weather2"
                },
                {
                    "id": "9",
                    "value": "92",
                    "unit": "lng_pct",
                    "name": "lng_weather_9",
                    "selection": "weather3"
                }
            ],
            "boilerdata": [
                {
                    "id": "17",
                    "value": "58.1",
                    "unit": "lng_degree",
                    "name": "lng_boil_17",
                    "selection": "boiler1"
                },
                {
                    "id": "5",
                    "value": "0.0",
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
                    "value": "20.3",
                    "unit": "lng_pct",
                    "name": "lng_boil_12",
                    "selection": "boiler5"
                },
                {
                    "id": "14",
                    "value": "196",
                    "unit": "lng_pct",
                    "name": "lng_boil_14",
                    "selection": "boiler6"
                },
                {
                    "id": "15",
                    "value": "127",
                    "unit": "lng_pct",
                    "name": "lng_boil_15",
                    "selection": "boiler7"
                },
                {
                    "id": "16",
                    "value": "131",
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
                    "id": "10",
                    "value": null,
                    "unit": "lng_literhour",
                    "name": "lng_boil_10",
                    "selection": "boiler10"
                }
            ],
            "hopperdata": [
                {
                    "id": "2",
                    "value": "1639",
                    "unit": "lng_g",
                    "name": "lng_hopper_2",
                    "selection": "hopper1"
                },
                {
                    "id": "3",
                    "value": "25.1",
                    "unit": "lng_kg",
                    "name": "lng_hopper_3",
                    "selection": "hopper2"
                },
                {
                    "id": "4",
                    "value": "12033",
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
                    "value": "-1470",
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
                    "value": "-1470",
                    "unit": "lng_kg",
                    "name": "lng_hopper_1",
                    "selection": ""
                },
                {
                    "id": "boilertemp",
                    "value": "66.9",
                    "unit": "lng_degree",
                    "name": "lng_boil_1",
                    "selection": ""
                },
                {
                    "id": "-wantedboilertemp",
                    "value": "65.0",
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
                    "value": 98.6,
                    "unit": "lng_degree",
                    "name": "lng_boil_3",
                    "selection": null
                },
                {
                    "id": "oxygen",
                    "value": "20.3",
                    "unit": "lng_pct",
                    "name": "lng_boil_12",
                    "selection": null
                },
                {
                    "id": "pressure",
                    "value": "63",
                    "unit": "lng_pascal",
                    "name": "lng_boil_24",
                    "selection": null
                },
                {
                    "id": "exhaust",
                    "value": "100",
                    "unit": "lng_pct",
                    "name": "",
                    "selection": null
                },
                {
                    "id": "hopperdistance",
                    "value": "91",
                    "unit": "lng_pct",
                    "name": "lng_hopper_14",
                    "selection": null
                },
                {
                    "id": "hopperimg",
                    "value": 5,
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
                    "value": "lng_state_22",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "clock": {
                    "id": "clock",
                    "value": "13:37",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "substate": {
                    "id": "substate",
                    "value": "lng_substate_6",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "substatesecs": {
                    "id": "substatesecs",
                    "value": "95",
                    "unit": "",
                    "name": "",
                    "selection": ""
                },
                "alarm": 0,
                "running": 1,
                "output": 0,
                "outputpct": "0",
                "hopper.distance_max": "0",
                "vacuum.min_distance": "70",
                "vacuum.max_distance": "20",
                "vacuum.output_auger": "0",
                "backpressure": "100",
                "hopperdistance": "91"
            },
            "leftoutput": {
                "output-1": {
                    "val": "disabled",
                    "unit": "",
                    "image": "1-dhw.png"
                },
                "output-2": {
                    "val": "ON",
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
                    "val": "100",
                    "unit": "%",
                    "image": "5-exhaustfan.png"
                },
                "output-6": {
                    "val": "disabled",
                    "unit": "LNG_KG",
                    "image": "6-ashauger.png"
                },
                "output-7": {
                    "val": "17.2",
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
            "infomessages": [],
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
    assert cd.boiler_kwh == Value("0.0", Unit.KWH)
    assert cd.hopper_capacity == Value("91", Unit.CM)
    assert cd.boiler_return_temperature == Value("58.1", Unit.DEGREE)
    assert cd.boiler_temperature_current == Value("66.9", Unit.DEGREE)
    assert cd.boiler_temperature_requested == Value("65", Unit.DEGREE)
    assert cd.state == State.STOPPED_BY_EXTERNAL_TEMP
    assert cd.consumption_total == Value("12033", Unit.KILO_GRAM)
    assert cd.consumption_day == Value("25.1", Unit.KILO_GRAM)

def test_controller_data_connected():
    test_data = '{"notconnected": 1}'
    with pytest.raises(NotConnectedException):
        ControllerData(json.loads(test_data))


@pytest.mark.parametrize('value, expected', [
    ('lng_state_14', State.OFF),
    ('lng_state_23', State.STOPPED_BY_TIMER),
    ('lng_state_46', State.STOPPED_EMPTY_HOPPER),
    ('lng_state_7', State.HOT_WATER),
    ('state_7', State.HOT_WATER),
    ('state_13', State.FAULT_IGNITION),
    ('lng_state_99', 'lng_state_99'),
])
def test_state_mapping(value, expected):
    cd = ControllerData({'miscdata': {'state': {'value': value}}, 'notconnected': 0, 'serial': 'x'})
    assert cd.state == expected


FULL_SCREEN_DATA = """
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
            "value": "5.8",
            "unit": "lng_degree",
            "name": "lng_weather_1",
            "selection": ""
        },
        {
            "id": "2",
            "value": "3.5",
            "unit": "lng_metersec",
            "name": "lng_weather_2",
            "selection": "weather1"
        },
        {
            "id": "3",
            "value": "SW",
            "unit": "",
            "name": "lng_weather_3",
            "selection": "weather2"
        },
        {
            "id": "9",
            "value": "98",
            "unit": "lng_pct",
            "name": "lng_weather_9",
            "selection": "weather3"
        },
        {
            "id": "4",
            "value": "96",
            "unit": "lng_pct",
            "name": "lng_weather_4",
            "selection": "weather4"
        },
        {
            "id": "5",
            "value": "1009",
            "unit": "",
            "name": "lng_weather_5",
            "selection": "weather5"
        }
    ],
    "boilerdata": [
        {
            "id": "17",
            "value": "32.9",
            "unit": "lng_degree",
            "name": "lng_boil_17",
            "selection": "boiler1"
        },
        {
            "id": "5",
            "value": "0.0",
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
            "value": "0.1",
            "unit": "lng_pct",
            "name": "lng_boil_12",
            "selection": "boiler5"
        },
        {
            "id": "14",
            "value": "202",
            "unit": "lng_pct",
            "name": "lng_boil_14",
            "selection": "boiler6"
        },
        {
            "id": "15",
            "value": "117",
            "unit": "lng_pct",
            "name": "lng_boil_15",
            "selection": "boiler7"
        },
        {
            "id": "16",
            "value": "127",
            "unit": "lng_pct",
            "name": "lng_boil_16",
            "selection": "boiler8"
        },
        {
            "id": "9",
            "value": "99.1",
            "unit": "lng_pct",
            "name": "lng_boil_9",
            "selection": "boiler9"
        },
        {
            "id": "7",
            "value": 22.6,
            "unit": "lng_degree",
            "name": "lng_boil_7",
            "selection": "boiler10"
        }
    ],
    "hopperdata": [
        {
            "id": "2",
            "value": "1639",
            "unit": "lng_g",
            "name": "lng_hopper_2",
            "selection": "hopper1"
        },
        {
            "id": "3",
            "value": "21.9",
            "unit": "lng_kg",
            "name": "lng_hopper_3",
            "selection": "hopper2"
        },
        {
            "id": "4",
            "value": "28771",
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
            "value": "-18245",
            "unit": "lng_kg",
            "name": "lng_hopper_1",
            "selection": "hopper6"
        },
        {
            "id": "9",
            "value": "3.20",
            "unit": "lng_pct",
            "name": "lng_hopper_9",
            "selection": "hopper7"
        },
        {
            "id": "10",
            "value": "20.5",
            "unit": "lng_pct",
            "name": "lng_hopper_10",
            "selection": "hopper8"
        },
        {
            "id": "5",
            "value": "18245",
            "unit": "lng_kg",
            "name": "lng_hopper_5",
            "selection": "hopper9"
        },
        {
            "id": "13",
            "value": "28837",
            "unit": "lng_kg",
            "name": "lng_hopper_13",
            "selection": "hopper10"
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
            "value": "N/A",
            "unit": "lng_pct",
            "name": "lng_dhw_4",
            "selection": "dhw2"
        }
    ],
    "frontdata": [
        {
            "id": "hoppercontent",
            "value": "-18245",
            "unit": "lng_kg",
            "name": "lng_hopper_1",
            "selection": ""
        },
        {
            "id": "boilertemp",
            "value": "51.0",
            "unit": "lng_degree",
            "name": "lng_boil_1",
            "selection": ""
        },
        {
            "id": "-wantedboilertemp",
            "value": "65.0",
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
            "value": "70",
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
            "value": 18.7,
            "unit": "lng_degree",
            "name": "lng_boil_3",
            "selection": null
        },
        {
            "id": "oxygen",
            "value": "0.1",
            "unit": "lng_pct",
            "name": "lng_boil_12",
            "selection": null
        },
        {
            "id": "pressure",
            "value": "1",
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
            "value": "103",
            "unit": "lng_pct",
            "name": "lng_hopper_14",
            "selection": null
        },
        {
            "id": "hopperimg",
            "value": 5,
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
            "value": "22:24",
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
        "hopper.distance_max": "0",
        "vacuum.min_distance": "70",
        "vacuum.max_distance": "20",
        "vacuum.output_auger": "0",
        "backpressure": "100",
        "hopperdistance": "103"
    },
    "leftoutput": {
        "output-1": {
            "val": "disabled",
            "unit": "",
            "image": "1-dhw.png"
        },
        "output-2": {
            "val": "ON",
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
        "6",
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


def test_controller_full_screen():
    cd = ControllerData(json.loads(FULL_SCREEN_DATA))

    assert cd.alias == "cytram"
    assert cd.controller_type == "v16"
    assert cd.clock == "22:24"
    assert cd.state == State.STOPPED_BY_TIMER
    assert cd.substate == "lng_substate_223"
    assert cd.substate_seconds == 0
    assert cd.info_messages == [InfoMessage(64, "6", "")]
    assert cd.info_messages[0].text == "Errors during cleaning"

    # boiler
    assert cd.power_output == Value("0", Unit.KW)
    assert cd.power_percent == Value("0", Unit.PERCENT)
    assert cd.smoke_temperature == Value("18.7", Unit.DEGREE)
    assert cd.drop_shaft_temperature == Value("22.6", Unit.DEGREE)
    assert cd.photo_sensor == Value("0", Unit.NONE)
    assert cd.oxygen == Value("0.1", Unit.PERCENT)
    assert cd.oxygen_requested == Value("0.0", Unit.PERCENT)
    assert cd.oxygen_regulation_low == Value("202", Unit.PERCENT)
    assert cd.oxygen_regulation_mid == Value("117", Unit.PERCENT)
    assert cd.oxygen_regulation_high == Value("127", Unit.PERCENT)
    assert cd.air_requested == Value("0", Unit.M3_HOUR)
    assert cd.pressure == Value("1", Unit.PASCAL)
    assert cd.exhaust_fan == Value("0", Unit.PERCENT)
    assert cd.online_time == Value("99.1", Unit.PERCENT)
    assert cd.flow is None  # not requested in this screen
    assert cd.ash_distance == Value("100", Unit.PERCENT)
    assert cd.back_pressure == Value("100", Unit.PERCENT)

    # hopper
    assert cd.hopper_content == Value("-18245", Unit.KILO_GRAM)
    assert cd.hopper_level == Value("5", Unit.NONE)
    assert cd.auger_capacity == Value("1639", Unit.GRAM)
    assert cd.auger_low == Value("3.20", Unit.PERCENT)
    assert cd.auger_high == Value("20.5", Unit.PERCENT)
    assert cd.consumption_day == Value("21.9", Unit.KILO_GRAM)
    assert cd.consumption_total == Value("28771", Unit.KILO_GRAM)
    assert cd.trip_1 == Value("18245", Unit.KILO_GRAM)
    assert cd.trip_2 == Value("28837", Unit.KILO_GRAM)
    assert cd.power_10_percent == Value("2.5", Unit.KW)
    assert cd.power_100_percent == Value("16", Unit.KW)

    # hot water: no sensor fitted
    assert cd.hotwater_sensor_connected is False
    assert cd.hotwater_temperature_requested == Value("70", Unit.DEGREE)
    assert cd.hotwater_difference == Value("10", Unit.DEGREE)

    # weather
    assert cd.weather_city == "Otterup"
    assert cd.outdoor_temperature == Value("5.8", Unit.DEGREE)
    assert cd.wind_speed == Value("3.5", Unit.METER_PER_SECOND)
    assert cd.wind_direction == "SW"
    assert cd.clouds == Value("98", Unit.PERCENT)
    assert cd.humidity == Value("96", Unit.PERCENT)
    assert cd.air_pressure == Value("1009", Unit.HPA)
    zones = cd.weather_zones
    assert [z.active for z in zones] == [False, False, False, False]
    assert zones[0].valve == Value("0", Unit.PERCENT)

    # outputs
    outputs = cd.outputs
    assert outputs["boiler_pump"].is_on is True
    assert outputs["dhw_valve"].enabled is False
    assert outputs["exhaust_fan"].value == Value("0", Unit.NONE).value
    assert outputs["compressor"].value == Value("30.0", Unit.NONE).value
    assert outputs["sun_pump"].enabled is False
    assert len(outputs) == 11


def test_missing_and_na_values_are_none():
    cd = ControllerData({
        'notconnected': 0,
        'serial': 'x',
        'miscdata': {},
        'boilerdata': [{'id': '10', 'value': None}],
        'hopperdata': [{'id': '11', 'value': 'N/A'}],
    })
    assert cd.flow is None
    assert cd.drop_shaft_temperature is None
    assert cd.smoke_temperature is None
    assert cd.info_messages == []
    assert cd.outputs == {}
