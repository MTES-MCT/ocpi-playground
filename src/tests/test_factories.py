"""Tests for the Location factory."""

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
