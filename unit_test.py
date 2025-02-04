# 유닛 테스트 작성 예제
import unittest

# 테스트할 함수 정의
def add(a, b):
    return a + b

# 유닛 테스트 클래스 정의
class TestAddFunction(unittest.TestCase):

    # 각 테스트 케이스마다 호출되는 메서드
    def setUp(self):
        print("테스트를 시작합니다.")

    # 테스트 케이스 1
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)

    # 테스트 케이스 2
    def test_add_floats(self):
        self.assertEqual(add(1.1, 2.2), 3.3)

    # 테스트 후 정리 작업
    def tearDown(self):
        print("테스트가 종료되었습니다.")

# 유닛 테스트 실행
if __name__ == '__main__':
    unittest.main()
    