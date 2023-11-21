from norske_kommuner import kommuner, get_kommune_by_nr


def test_dummy():
    assert True


def test_get_kommune_by_nr():
    assert get_kommune_by_nr('1103').kommunenavn == 'Stavanger'
    assert get_kommune_by_nr('999999') is None


def test_poetry_kommune():
    assert len(kommuner) == 356
    assert kommuner['Stavanger'].kommunenummer == '1103'


def test_poetry_org_nr():
    assert len(kommuner) == 356
    assert kommuner['Stavanger'].orgnr == 964965226
