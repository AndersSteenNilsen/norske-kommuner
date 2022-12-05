from norske_kommuner import kommuner
# import norske_kommuner

def test_get_kommune_by_nr():
    assert kommuner.get_kommune_by_nr('1103') == 'Stavanger'
