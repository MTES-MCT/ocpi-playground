"""Playground instance configuration."""

from typing import Any, List

from py_ocpi.core.enums import RoleEnum
from pydantic import BaseSettings


class Settings(BaseSettings):
    """OCPI server instance configuration."""

    ROLES: List[RoleEnum] = [RoleEnum.cpo]

    class Config:
        """Pydantic settings configuration."""

        case_sensitive = True
        env_file = ".env"
        env_nested_delimiter = "__"
        env_prefix = "PLAYGROUND_"

        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            """Parse custom field types."""
            if field_name == "ROLES":
                return [RoleEnum[role] for role in raw_val.split(",")]
            return cls.json_loads(raw_val)  # type: ignore[attr-defined]


settings = Settings()
