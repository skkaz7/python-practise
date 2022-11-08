class Python:
    age = 7
    tail = 'long'


p = 'Python'


class TestClass:
    def test_one(self):
        assert 'th' in p

    def test_two(self):
        pyt = Python()
        assert hasattr(pyt, 'tail')
