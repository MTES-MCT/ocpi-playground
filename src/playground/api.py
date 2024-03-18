"""Playground API."""

import logging
from typing import Any, Tuple

from py_ocpi import get_application
from py_ocpi.core.enums import Action, ModuleID, RoleEnum
from py_ocpi.modules.cdrs.v_2_2_1.schemas import Cdr
from py_ocpi.modules.credentials.v_2_2_1.schemas import Credentials
from py_ocpi.modules.locations.v_2_2_1.schemas import Location
from py_ocpi.modules.sessions.v_2_2_1.schemas import Session
from py_ocpi.modules.tariffs.v_2_2_1.schemas import Tariff
from py_ocpi.modules.tokens.v_2_2_1.schemas import Token
from py_ocpi.modules.versions.enums import VersionNumber

from .factories import OCPIModelFactory, get_factory

logger = logging.getLogger(__name__)


class Crud:
    """Handle generic CRUD operations on OCPI modules."""

    logger: logging.Logger = logger

    @classmethod
    async def get(cls, module: ModuleID, role: RoleEnum, id, *args, **kwargs) -> Any:
        """Get module."""
        factory: OCPIModelFactory = get_factory(module)
        cls.logger.debug(f"{factory=}")
        return factory.build(id=id).dict()

    @classmethod
    async def list(
        cls, module: ModuleID, role: RoleEnum, filters: dict, *args, **kwargs
    ) -> Tuple[list, int, bool]:
        """Get module objects.

        Returns a tuple with the object list, the total number of objects and
        a boolean to indicate weither its the last page or not.
        """
        factory: OCPIModelFactory = get_factory(module)
        cls.logger.debug(f"{factory=}")
        data = [item.dict() for item in factory.batch(5)]
        return (data, 5, True)

    @classmethod
    async def create(
        cls, module: ModuleID, role: RoleEnum, data: dict, *args, **kwargs
    ) -> Any:
        """Create a module."""
        ...

    @classmethod
    async def update(
        cls, module: ModuleID, role: RoleEnum, data: dict, id, *args, **kwargs
    ) -> Any:
        """Update a module."""
        ...

    @classmethod
    async def delete(cls, module: ModuleID, role: RoleEnum, id, *args, **kwargs):
        """Delete a module."""
        ...

    @classmethod
    async def do(
        cls,
        module: ModuleID,
        role: RoleEnum,
        action: Action,
        *args,
        data: dict = None,  # type: ignore[assignment]
        **kwargs,
    ) -> Any:
        """Perform an action on module."""
        ...


class Adapter:
    """Transform your DB stored modules to valid OCPI module objects."""

    logger: logging.Logger = logger

    @classmethod
    def location_adapter(
        cls, data: dict, version: VersionNumber = VersionNumber.latest
    ):
        """Location module adapter."""
        return Location(**data)

    @classmethod
    def session_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        """Session module adapter."""
        return Session(**data)

    @classmethod
    def credentials_adapter(
        cls, data: dict, version: VersionNumber = VersionNumber.latest
    ):
        """Credentials module adapter."""
        return Credentials(**data)

    @classmethod
    def cdr_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        """CDR module adapter."""
        return Cdr(**data)

    @classmethod
    def tariff_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        """Tariff module adapter."""
        return Tariff(**data)

    @classmethod
    def token_adapter(cls, data: dict, version: VersionNumber = VersionNumber.latest):
        """Token module adapter."""
        return Token(**data)


app = get_application([VersionNumber.v_2_2_1], [RoleEnum.cpo], Crud, Adapter)
