from conftest import marc2record


def test_rero_id():
    record = marc2record({
        '035__': {'a': 'R1234'}
    })
    assert record.get('rero_id') == 'http://data.rero.ch/01-R1234'
