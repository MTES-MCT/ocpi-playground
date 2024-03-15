"""Tests for the Location factory."""

from py_ocpi.core.enums import ModuleID

from playground import factories


def test_cdr():
    """CdrFactory base test."""
    factories.CdrFactory.build()


def test_credentials():
    """CredentialsFactory base test."""
    factories.CredentialsFactory.build()


def test_location():
    """LocationFactory base test."""
    factories.LocationFactory.build()


def test_session():
    """SessionFactory base test."""
    factories.SessionFactory.build()


def test_tariff():
    """TariffFactory base test."""
    factories.TariffFactory.build()


def test_token():
    """TokenFactory base test."""
    factories.TokenFactory.build()


def test_get_factory():
    """Test the get_factory utility."""
    assert factories.CdrFactory == factories.get_factory(ModuleID.cdrs)
    assert factories.CredentialsFactory == factories.get_factory(
        ModuleID.credentials_and_registration
    )
    assert factories.LocationFactory == factories.get_factory(ModuleID.locations)
    assert factories.SessionFactory == factories.get_factory(ModuleID.sessions)
    assert factories.TariffFactory == factories.get_factory(ModuleID.tariffs)
    assert factories.TokenFactory == factories.get_factory(ModuleID.tokens)
