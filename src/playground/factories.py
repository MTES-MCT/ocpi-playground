"""Factories for OCPI models."""

import inspect
import sys
from datetime import timedelta
from typing import Any, Dict, Optional, Type

from faker import Faker
from faker.providers import date_time, lorem, python
from polyfactory.factories.pydantic_factory import ModelFactory
from py_ocpi.core.data_types import DateTime, DisplayText, Price
from py_ocpi.core.enums import ModuleID
from py_ocpi.modules.cdrs.v_2_2_1.schemas import Cdr
from py_ocpi.modules.credentials.v_2_2_1.schemas import Credentials
from py_ocpi.modules.locations.v_2_2_1.schemas import Location
from py_ocpi.modules.sessions.v_2_2_1.schemas import Session
from py_ocpi.modules.tariffs.v_2_2_1.schemas import Tariff
from py_ocpi.modules.tokens.v_2_2_1.schemas import Token

fake = Faker()
fake.add_provider(date_time)
fake.add_provider(lorem)
fake.add_provider(python)


def generate_price(  # noqa: PLR0913
    left_digits=2,
    right_digits=4,
    positive=True,
    min_value=5,
    max_value=100,
    vat_rate=0.2,
):
    """Generate a random price."""
    excl_vat = fake.pyfloat(left_digits, right_digits, positive, min_value, max_value)
    incl_vat = excl_vat * (1 + vat_rate)
    return {"excl_vat": excl_vat, "incl_vat": incl_vat}


class OCPIDataTypesMixin:
    """Add support for py_ocpi custom data types."""

    @classmethod
    def get_provider_map(cls) -> Dict[Type, Any]:
        """Update provider map with py_ocpi custom types."""
        providers_map = super().get_provider_map()

        return {
            DateTime: lambda: fake.date_time_between(
                start_date=timedelta(days=-365)
            ).isoformat(),
            DisplayText: lambda: {"language": "en", "text": fake.sentence(nb_words=10)},
            Price: generate_price,
            **providers_map,
        }


class CdrFactory(OCPIDataTypesMixin, ModelFactory[Cdr]):
    """Cdr model factory."""

    _module: ModuleID = ModuleID.cdrs


class CredentialsFactory(OCPIDataTypesMixin, ModelFactory[Credentials]):
    """Credentials model factory."""

    _module: ModuleID = ModuleID.credentials_and_registration


class LocationFactory(OCPIDataTypesMixin, ModelFactory[Location]):
    """Location model factory."""

    _module: ModuleID = ModuleID.locations


class SessionFactory(OCPIDataTypesMixin, ModelFactory[Session]):
    """Session model factory."""

    _module: ModuleID = ModuleID.sessions


class TariffFactory(OCPIDataTypesMixin, ModelFactory[Tariff]):
    """Tariff model factory."""

    _module: ModuleID = ModuleID.tariffs


class TokenFactory(OCPIDataTypesMixin, ModelFactory[Token]):
    """Token model factory."""

    _module: ModuleID = ModuleID.tokens


def get_factory(module: ModuleID) -> Optional[ModelFactory]:
    """Get the factory for a given module."""
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if not inspect.isclass(obj):
            continue
        if hasattr(obj, "_module") and obj._module == module:
            return obj
    return None
