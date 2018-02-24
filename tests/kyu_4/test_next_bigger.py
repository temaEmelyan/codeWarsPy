from unittest import TestCase

from kyu_4.Nextbiggernumberwiththesamedigits import next_bigger


class TestNext_bigger(TestCase):
    def test_next_bigger(self):
        self.assert_equals = self.assertEqual
        self.assert_equals(next_bigger(12), 21)
        self.assert_equals(next_bigger(513), 531)
        self.assert_equals(next_bigger(2017), 2071)
        self.assert_equals(next_bigger(414), 441)
        self.assert_equals(next_bigger(144), 414)
