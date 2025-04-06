from obamas import obamas
def test_is_obama_true():
    assert obamas.is_obama(2008) is True
    assert obamas.is_obama(2012) is True

def test_is_obama_false():
    assert obamas.is_obama(2016) is False