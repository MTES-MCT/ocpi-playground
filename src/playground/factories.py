"""Factories for OCPI models."""

from datetime import timedelta
from typing import Any, Dict, Type

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


def generate_price(
    left_digits=2,
    right_digits=4,
    positive=True,
    min_value=5,
    max_value=100,
    vat_rate=0.2,
):
    """Generate a random price"""
    excl_vat = fake.pyfloat(left_digits, right_digits, positive, min_value, max_value)
    incl_vat = excl_vat * (1 + vat_rate)
    return {"excl_vat": excl_vat, "incl_vat": incl_vat}


class OCPIDataTypesMixin:
    """Add support for py_ocpi custom data types."""

    @classmethod
    def get_provider_map(cls) -> Dict[Type, Any]:
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


class CredentialsFactory(OCPIDataTypesMixin, ModelFactory[Credentials]):
    """Credentials model factory."""


class LocationFactory(OCPIDataTypesMixin, ModelFactory[Location]):
    """Location model factory."""


class SessionFactory(OCPIDataTypesMixin, ModelFactory[Session]):
    """Session model factory."""


class TariffFactory(OCPIDataTypesMixin, ModelFactory[Tariff]):
    """Tariff model factory."""


class TokenFactory(OCPIDataTypesMixin, ModelFactory[Token]):
    """Token model factory."""


def get_factory(module: ModuleID):
    """Get the factory for a given module."""
    factory_name = module.value
    if module.value != "credentials":
        factory_name = module.value.rstrip("s")
    factory_name = factory_name.title() + "Factory"
    return eval(factory_name)
