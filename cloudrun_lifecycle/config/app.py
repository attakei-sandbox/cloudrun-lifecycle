from dataclasses import dataclass

from . import TypeCastingMixin, filter_envmap


@dataclass
class AppConfig(TypeCastingMixin):
    debug: bool = False
    url_prefix: str = ""


DEFAULT_CONFIG = AppConfig(debug=False, caches=[])


def create_config_from_env(base_config: AppConfig = None) -> AppConfig:
    """Generate config from environment variables.

    :params base_config: inherit based config.
    """
    if base_config is None:
        base_config = DEFAULT_CONFIG
    app_config = AppConfig(**filter_envmap("APP_"))
    return app_config
