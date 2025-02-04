
# pytest 테스트 함수 작성
def add(a, b):
    return a + b

def test_add_integers():
    assert add(1, 2) == 3

def test_add_floats():
    assert add(1.1, 2.2) == 3.3