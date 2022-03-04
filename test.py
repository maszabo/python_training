from unittesthez import get_max

def test_get_max():
    a=5
    b=10
    result=get_max(a,b)

    assert result == 10


def test_get_max_when_first_value_greater():
    assert get_max(200, 5) == 200
