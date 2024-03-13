"""Playground API."""

from typing import Any, Tuple

from py_ocpi.core.enums import Action, ModuleID, RoleEnum
from py_ocpi.modules.versions.enums import VersionNumber
from py_ocpi.modules.locations.v_2_2_1.schemas import Location
from py_ocpi import get_application


class Crud:
    @classmethod
    async def get(
        cls, module: ModuleID, role: RoleEnum, id, *args, **kwargs
    ) -> Any: ...

    @classmethod
    async def list(
        cls, module: ModuleID, role: RoleEnum, filters: dict, *args, **kwargs
    ) -> Tuple[list, int, bool]: ...

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
    @classmethod
    def location_adapter(
        cls, data: dict, version: VersionNumber = VersionNumber.latest
    ):
        return Location(**data)


app = get_application([VersionNumber.v_2_2_1], [RoleEnum.cpo], Crud, Adapter)
