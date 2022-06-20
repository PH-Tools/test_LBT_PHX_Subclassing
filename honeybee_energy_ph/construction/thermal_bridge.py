# -*- Python Version: 2.7 -*-
# -*- coding: utf-8 -*-

"""HBPH Thermal Bridge Objects"""

try:
    from typing import Any, Union
except ImportError:
    pass  # IronPython 2.7

from honeybee_energy_ph.construction import _base
from honeybee_ph_utils import enumerables


class PhThermalBridgeType(enumerables.CustomEnum):
    allowed = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "15-Ambient",
        "16-Perimeter",
        "17-FS/BC"
    ]

    def __init__(self, _value=15, _index_offset=0):
        super(PhThermalBridgeType, self).__init__(_value, _index_offset)


class PhThermalBridge(_base._Base):
    """A single PhThermalBridge object"""

    def __init__(self, _identifier):
        super(PhThermalBridge, self).__init__(_identifier)
        self.display_name = "_unnamed_thermal_bridge_"
        self.quantity = 1.0
        self._group_type = PhThermalBridgeType(15)
        self.psi_value = 0.1
        self.fRsi_value = 0.75
        self.length = 0.0

    @property
    def group_type(self):
        # type: () -> PhThermalBridgeType
        return self._group_type

    @group_type.setter
    def group_type(self, _in):
        # type: (Union[str, int]) -> None
        self._group_type = PhThermalBridgeType(_in)

    def to_dict(self):
        # type: () -> dict[str, Any]
        d = super(PhThermalBridge, self).to_dict()
        d['display_name'] = self.display_name
        d['quantity'] = self.quantity
        d['_group_type'] = self._group_type.to_dict()
        d['psi_value'] = self.psi_value
        d['fRsi_value'] = self.fRsi_value
        d['length'] = self.length
        return d

    @classmethod
    def from_dict(cls, _input_dict):
        # type: (dict) -> PhThermalBridge
        new_obj = cls(_input_dict['identifier'])
        new_obj.set_base_attrs_from_dict(_input_dict)
        new_obj.display_name = _input_dict['display_name']
        new_obj.quantity = _input_dict['quantity']
        new_obj._group_type = PhThermalBridgeType.from_dict(_input_dict['_group_type'])
        new_obj.psi_value = _input_dict['psi_value']
        new_obj.fRsi_value = _input_dict['fRsi_value']
        new_obj.length = _input_dict['length']
        return new_obj

    def duplicate(self):
        # type: () -> PhThermalBridge
        return self.__copy__()

    def __copy__(self):
        # type: () -> PhThermalBridge
        new_obj = self.__class__(self.identifier)
        new_obj.set_base_attrs_from_obj(self)
        new_obj.display_name = self.display_name
        new_obj.quantity = self.quantity
        new_obj.group_type = self.group_type.value
        new_obj.psi_value = self.psi_value
        new_obj.fRsi_value = self.fRsi_value
        new_obj.length = self.length
        return new_obj

    def __str__(self):
        return '{}(display_name={}, psi_value={:.3f}, fRsi_value={:.3f}, length={:.3f})'.format(
            self.__class__.__name__, self.display_name, self.psi_value, self.fRsi_value, self.length)

    def __repr__(self):
        return str(self)

    def ToString(self):
        return str(self)
