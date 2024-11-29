import math
from enum import IntEnum
from typing import Dict, Tuple


class EnumAirQualityIndex(IntEnum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6


def get_aqi_level(value):
    """计算aqi的level
    value: aqi的值或iaqi的值
    """
    if value is None:
        return None
    if value < 51:
        return EnumAirQualityIndex.LEVEL_1.value
    elif value < 101:
        return EnumAirQualityIndex.LEVEL_2.value
    elif value < 151:
        return EnumAirQualityIndex.LEVEL_3.value
    elif value < 201:
        return EnumAirQualityIndex.LEVEL_4.value
    elif value < 301:
        return EnumAirQualityIndex.LEVEL_5.value
    else:
        return EnumAirQualityIndex.LEVEL_6.value


class AQICalc:
    """aqi计算算法 
    只对单一pollutant值计算iaqi以及aqi值
    
    Params:
        `calc_type`: day/hour aqi计算类型,决定iaqi分量。默认为day
    """
    # 该值用来标注6分量中缺失的情况下的iaqi,以取max(all_iaqi)来计算aqi
    INVALID_IAQI = -1

    def __init__(self,
                 co=None,
                 no2=None,
                 o3=None,
                 pm10=None,
                 pm25=None,
                 so2=None,
                 *,
                 calc_type='day',
                 **kwargs):
        self._co = co
        self._no2 = no2
        self._o3 = o3
        self._pm10 = pm10
        self._pm25 = pm25
        self._so2 = so2
        self._calc_type = calc_type
        self._aqi_index = (0, 50, 100, 150, 200, 300, 400, 500)
        self._day_index = {
            'pm25': (0, 35, 75, 115, 150, 250, 350, 500),
            'pm10': (0, 50, 150, 250, 350, 420, 500, 600),
            'co': (0, 2, 4, 14, 24, 36, 48, 60),
            'so2': (0, 50, 150, 475, 800, 1600, 2100, 2620),
            'no2': (0, 40, 80, 180, 280, 565, 750, 940),
            'o3': (0, 100, 160, 215, 265, 800, 1000, 1200)
        }
        self._hour_index = {
            'pm25': (0, 35, 75, 115, 150, 250, 350, 500),
            'pm10': (0, 50, 150, 250, 350, 420, 500, 600),
            'co': (0, 5, 10, 35, 60, 90, 120, 150),
            'so2': (0, 150, 500, 650, 800, 1600, 2100, 2620),
            'no2': (0, 100, 200, 700, 1200, 2340, 3090, 3840),
            'o3': (0, 160, 200, 300, 400, 800, 1000, 1200)
        }
        self._si = {
            'so2': 60,
            'no2': 40,
            'co': 4,
            'o3': 160,
            'pm10': 70,
            'pm25': 35
        }
        self._calc_aqi()

    @property
    def aqi(self):
        return self._aqi

    @property
    def composite_index(self):
        """综合指数
        """
        ci = []
        for factor, si in self._si.items():
            value = getattr(self, f'_{factor}')
            if value is not None:
                ci.append(round(value / si, 2))
        if ci:
            return round(sum(ci), 2)
        return None

    @property
    def iaqi(self):
        return self._iaqi

    @property
    def primary_pollutant(self):
        """首要污染物
        """
        return self._primary_pollutant[:]

    def get_level(self, factor='aqi'):
        if factor == 'aqi':
            return get_aqi_level(self.aqi)
        return get_aqi_level(self.iaqi[factor])

    def get_value(self, factor='aqi'):
        return getattr(self, f'_{factor}')

    def get_value_and_level(self) -> Dict[str, Tuple[int]]:
        """return:(浓度值,等级)
        >>> {
        ...    'aqi': (value, level),
        ...    'pm25': (value, level),
        ...    ...
        ... }
        """
        result = {}
        for factor, iaqi in self.iaqi.items():
            result[factor] = (getattr(self, f'_{factor}'), get_aqi_level(iaqi))
        result['aqi'] = (self.aqi, get_aqi_level(self.aqi))
        return result

    def __bool__(self):
        values = (self._co, self._no2, self._o3, self._pm10, self._pm25,
                  self._so2)
        valid_cnt = sum(False if v is None else True for v in values)
        return valid_cnt > 0

    def _calc_aqi(self):
        iaqi = {
            'co': self._calc_iaqi('co', self._co),
            'no2': self._calc_iaqi('no2', self._no2),
            'o3': self._calc_iaqi('o3', self._o3),
            'pm10': self._calc_iaqi('pm10', self._pm10),
            'pm25': self._calc_iaqi('pm25', self._pm25),
            'so2': self._calc_iaqi('so2', self._so2)
        }
        self._primary_pollutant = []
        if not self:
            self._aqi = None
        else:
            self._aqi = math.ceil(max(iaqi.values()))
            if self._aqi > 50:
                max_iaqi = max(iaqi.values())
                for factor, value in iaqi.items():
                    if value == max_iaqi:
                        self._primary_pollutant.append(factor)
        self._iaqi = {
            k: math.ceil(v) if v != self.INVALID_IAQI else None
            for k, v in iaqi.items()
        }

    def _calc_iaqi(self, pollutant, value):
        if value is None:
            return self.INVALID_IAQI
        if self._calc_type == 'day':
            pollutant_index = self._day_index[pollutant]
        else:
            pollutant_index = self._hour_index[pollutant]
        for index, pollution_value in enumerate(pollutant_index):
            if pollution_value > value:
                break
        bph = pollutant_index[index]
        bpl = pollutant_index[index - 1]
        iaqih = self._aqi_index[index]
        iaqil = self._aqi_index[index - 1]
        iaqip = (iaqih - iaqil) / (bph - bpl) * (value - bpl) + iaqil
        return iaqip
