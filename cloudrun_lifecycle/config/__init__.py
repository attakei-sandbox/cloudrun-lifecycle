"""Configuration mid functions.
"""
import os
from typing import Dict


EnvMap = Dict[str, str]


class TypeCastingMixin(object):
    """Typ casting action mixin for ihnerited dataclass.

    Any environment variables are passed as str value type.
    This mixin convert from str value to dataclass filed value.
    """

    def __post_init__(self):
        """Convert fields types.
        """
        for k, v in self.__class__.__dataclass_fields__.items():
            val_ = getattr(self, k)
            if type(val_) == str:
                # Convert literal type
                setattr(self, k, v.type(val_))
                continue
            if type(val_) == list:
                # Convert list type
                v_args = v.type.__args__[0]
                setattr(self, k, [v_args(vv) for vv in val_])
                continue


def filter_envmap(prefix: str, src: EnvMap = None, lowering: bool = True) -> EnvMap:
    """Filter source dict by that has prefix.
    """
    if src is None:
        src = os.environ
    dst = {}
    for k, v in src.items():
        if not k.startswith(prefix):
            continue
        k_ = k.replace(prefix, "")
        if lowering:
            k_ = k_.lower()
        dst[k_] = v
    return dst
