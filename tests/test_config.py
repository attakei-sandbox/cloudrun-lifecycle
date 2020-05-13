import unittest
from dataclasses import dataclass
from typing import List

import pytest
from cloudrun_lifecycle import config


@pytest.mark.parametrize(
    "type_,src,attr",
    [
        (str, "sample", "sample"),
        (int, "10", 10),
        (bool, "1", True),
        (bool, "", False),
        (List[int], ["1", "2"], [1, 2]),
        (List[str], ["1", "2"], ["1", "2"]),
    ],
)
def test_TypeCastingMixin_types(type_, src, attr):
    @dataclass
    class Config(config.TypeCastingMixin):
        data: type_

    cfg = Config(data=src)
    assert cfg.data == attr


class TestsForTypeCastingMixin_Misc(unittest.TestCase):
    def test_value_error(self):
        @dataclass
        class Config(config.TypeCastingMixin):
            data: int

        with pytest.raises(ValueError):
            Config(data="sample")

    def test_nullable(self):
        @dataclass
        class Config(config.TypeCastingMixin):
            data: int = None

        assert Config().data is None

    def test_skip_nested(self):
        @dataclass
        class Config(config.TypeCastingMixin):
            data: List[str]

        @dataclass
        class ConfigEx(config.TypeCastingMixin):
            data: Config

        cfg = Config(data=["1", "2"])
        ConfigEx(data=cfg)


@pytest.mark.parametrize(
    "prefix,lowering,src,dst",
    [
        ("APP_", True, {"APPS_": "sample"}, {}),
        ("APP_", True, {"APP_KEY": "sample"}, {"key": "sample"}),
        ("APP_", False, {"APP_KEY": "sample"}, {"KEY": "sample"}),
        (
            "APP_",
            True,
            {"APP_DEBUG": "1", "APP_URL": "/sample"},
            {"debug": "1", "url": "/sample"},
        ),
    ],
)
def test_filter_envmap(prefix, lowering, src, dst):
    assert config.filter_envmap(prefix, src, lowering) == dst
