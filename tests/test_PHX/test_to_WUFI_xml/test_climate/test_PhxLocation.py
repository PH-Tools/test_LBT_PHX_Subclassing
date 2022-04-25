from PHX.model import climate
from PHX.to_WUFI_XML.xml_builder import generate_WUFI_XML_from_object
from tests.test_PHX.test_to_WUFI_xml._utils import xml_string_to_list


def test_default_PhxLocation(reset_class_counters):
    l1 = climate.PhxLocation()
    result = generate_WUFI_XML_from_object(l1, _header="")
    assert xml_string_to_list(result) == [
        '<Selection>1</Selection>',
        '<Latitude_DB unit="°">40.6</Latitude_DB>',
        '<Longitude_DB unit="°">-73.8</Longitude_DB>',
        '<HeightNN_DB unit="m">3.0</HeightNN_DB>',
        '<dUTC_DB>-4</dUTC_DB>',
        '<Albedo choice="User defined">-2</Albedo>',
        '<GroundReflShort unit="-">0.2</GroundReflShort>',
        '<GroundReflLong unit="-">0.1</GroundReflLong>',
        '<GroundEmission unit="-">0.9</GroundEmission>',
        '<CloudIndex unit="-">0.66</CloudIndex>',
        '<CO2concenration unit="mg/m³">350</CO2concenration>',
        '<Unit_CO2concentration choice="ppmv">48</Unit_CO2concentration>',
        '<PH_ClimateLocation>',
        '<Selection>1</Selection>',
        '<DailyTemperatureSwingSummer>8.0</DailyTemperatureSwingSummer>',
        '<AverageWindSpeed>4.0</AverageWindSpeed>',
        '<Latitude>40.6</Latitude>',
        '<Longitude>-73.8</Longitude>',
        '<HeightNNWeatherStation>3.0</HeightNNWeatherStation>',
        '<dUTC>-4</dUTC>',
        '<ClimateZone>1</ClimateZone>',
        '<GroundThermalConductivity>2</GroundThermalConductivity>',
        '<GroundHeatCapacitiy>1000</GroundHeatCapacitiy>',
        '<GroundDensity>2000</GroundDensity>',
        '<DepthGroundwater>3</DepthGroundwater>',
        '<FlowRateGroundwater>0.05</FlowRateGroundwater>',
        '<TemperatureMonthly count="0"/>',
        '<DewPointTemperatureMonthly count="0"/>',
        '<SkyTemperatureMonthly count="0"/>',
        '<NorthSolarRadiationMonthly count="0"/>',
        '<EastSolarRadiationMonthly count="0"/>',
        '<SouthSolarRadiationMonthly count="0"/>',
        '<WestSolarRadiationMonthly count="0"/>',
        '<GlobalSolarRadiationMonthly count="0"/>',
        '<TemperatureHeating1>0</TemperatureHeating1>',
        '<NorthSolarRadiationHeating1>0</NorthSolarRadiationHeating1>',
        '<EastSolarRadiationHeating1>0</EastSolarRadiationHeating1>',
        '<SouthSolarRadiationHeating1>0</SouthSolarRadiationHeating1>',
        '<WestSolarRadiationHeating1>0</WestSolarRadiationHeating1>',
        '<GlobalSolarRadiationHeating1>0</GlobalSolarRadiationHeating1>',
        '<TemperatureHeating2>0</TemperatureHeating2>',
        '<NorthSolarRadiationHeating2>0</NorthSolarRadiationHeating2>',
        '<EastSolarRadiationHeating2>0</EastSolarRadiationHeating2>',
        '<SouthSolarRadiationHeating2>0</SouthSolarRadiationHeating2>',
        '<WestSolarRadiationHeating2>0</WestSolarRadiationHeating2>',
        '<GlobalSolarRadiationHeating2>0</GlobalSolarRadiationHeating2>',
        '<TemperatureCooling>0</TemperatureCooling>',
        '<NorthSolarRadiationCooling>0</NorthSolarRadiationCooling>',
        '<EastSolarRadiationCooling>0</EastSolarRadiationCooling>',
        '<SouthSolarRadiationCooling>0</SouthSolarRadiationCooling>',
        '<WestSolarRadiationCooling>0</WestSolarRadiationCooling>',
        '<GlobalSolarRadiationCooling>0</GlobalSolarRadiationCooling>',
        '<TemperatureCooling2>0</TemperatureCooling2>',
        '<NorthSolarRadiationCooling2>0</NorthSolarRadiationCooling2>',
        '<EastSolarRadiationCooling2>0</EastSolarRadiationCooling2>',
        '<SouthSolarRadiationCooling2>0</SouthSolarRadiationCooling2>',
        '<WestSolarRadiationCooling2>0</WestSolarRadiationCooling2>',
        '<GlobalSolarRadiationCooling2>0</GlobalSolarRadiationCooling2>',
        '<SelectionPECO2Factor>6</SelectionPECO2Factor>',
        '<PEFactorsUserDef count="16">',
        '<PEF0 unit="kWh/kWh">1.1</PEF0>',
        '<PEF1 unit="kWh/kWh">1.1</PEF1>',
        '<PEF2 unit="kWh/kWh">1.1</PEF2>',
        '<PEF3 unit="kWh/kWh">1.1</PEF3>',
        '<PEF4 unit="kWh/kWh">0.2</PEF4>',
        '<PEF5 unit="kWh/kWh">1.8</PEF5>',
        '<PEF6 unit="kWh/kWh">1.7</PEF6>',
        '<PEF7 unit="kWh/kWh">0.8</PEF7>',
        '<PEF8 unit="kWh/kWh">1.1</PEF8>',
        '<PEF9 unit="kWh/kWh">1.5</PEF9>',
        '<PEF10 unit="kWh/kWh">0.7</PEF10>',
        '<PEF11 unit="kWh/kWh">1.1</PEF11>',
        '<PEF12 unit="kWh/kWh">1.5</PEF12>',
        '<PEF13 unit="kWh/kWh">0.8</PEF13>',
        '<PEF14 unit="kWh/kWh">1.1</PEF14>',
        '<PEF15 unit="kWh/kWh">1.5</PEF15>',
        '</PEFactorsUserDef>',
        '<CO2FactorsUserDef count="16">',
        '<CO2F0 unit="g/kWh">309.9966</CO2F0>',
        '<CO2F1 unit="g/kWh">250.0171</CO2F1>',
        '<CO2F2 unit="g/kWh">270.0102</CO2F2>',
        '<CO2F3 unit="g/kWh">439.9864</CO2F3>',
        '<CO2F4 unit="g/kWh">53.4289</CO2F4>',
        '<CO2F5 unit="g/kWh">680.0068</CO2F5>',
        '<CO2F6 unit="g/kWh">250.0171</CO2F6>',
        '<CO2F7 unit="g/kWh">239.9864</CO2F7>',
        '<CO2F8 unit="g/kWh">319.9932</CO2F8>',
        '<CO2F9 unit="g/kWh">409.9966</CO2F9>',
        '<CO2F10 unit="g/kWh">-70.0102</CO2F10>',
        '<CO2F11 unit="g/kWh">129.9898</CO2F11>',
        '<CO2F12 unit="g/kWh">319.9932</CO2F12>',
        '<CO2F13 unit="g/kWh">100</CO2F13>',
        '<CO2F14 unit="g/kWh">250.0171</CO2F14>',
        '<CO2F15 unit="g/kWh">409.9966</CO2F15>',
        '</CO2FactorsUserDef>',
        '</PH_ClimateLocation>'
    ]
