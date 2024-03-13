"""Playground API."""

import logging
from typing import Any, Tuple

from py_ocpi.core.enums import Action, ModuleID, RoleEnum
from py_ocpi.modules.versions.enums import VersionNumber
from py_ocpi.modules.cdrs.v_2_2_1.schemas import Cdr
from py_ocpi.modules.credentials.v_2_2_1.schemas import Credentials
from py_ocpi.modules.locations.v_2_2_1.schemas import Location
from py_ocpi.modules.sessions.v_2_2_1.schemas import Session
from py_ocpi.modules.tariffs.v_2_2_1.schemas import Tariff
from py_ocpi.modules.tokens.v_2_2_1.schemas import Token
from py_ocpi import get_application

from .factories import get_factory

logger = logging.getLogger(__name__)


class Crud:
    logger: logging.Logger = logger

    @classmethod
    async def get(cls, module: ModuleID, role: RoleEnum, id, *args, **kwargs) -> Any:
        factory = get_factory(module)
        cls.logger.debug(f"{factory=}")
        return factory.build(id=id).dict()

    @classmethod
    async def list(
        cls, module: ModuleID, role: RoleEnum, filters: dict, *args, **kwargs
    ) -> Tuple[list, int, bool]:
        factory = get_factory(module)
        cls.logger.debug(f"{factory=}")
        data = [l.dict() for l in factory.batch(5)]
        return (data, 5, True)

    @classmethod
    async def create(
        cls, module: ModuleID, role: RoleEnum, data: dict, *args, **kwargs
    ) -> Any: ...

    @classmethod
    async def update(
        cls, module: ModuleID, role: RoleEnum, data: dict, id, *args, **kwargs
    ) -> Any: ...

    @classmethod
    async def delete(cls, module: ModuleID, role: RoleEnum, id, *args, **kwargs): ...

    @classmethod
    async def do(
        cls,
        module: ModuleID,
        role: RoleEnum,
        action: Action,
        *args,
        data: dict = None,
        **kwargs,
    ) -> Any: ...


class Adapter:
    logger: logging.Logger = logger

    @classmethod
    def location_adapter(
        cls, data: dict, version: VersionNumber = VersionNumber.latest
    ):
        return Location(**data)

    @classmethod
    def session_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        return Session(**data)

    @classmethod
    def credentials_adapter(
        cls, data: dict, version: VersionNumber = VersionNumber.latest
    ):
        return Credentials(**data)

    @classmethod
    def cdr_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        return Cdr(**data)

    @classmethod
    def tariff_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        return Tariff(**data)

    @classmethod
    def token_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        return Token(**data)


app = get_application([VersionNumber.v_2_2_1], [RoleEnum.cpo], Crud, Adapter)
