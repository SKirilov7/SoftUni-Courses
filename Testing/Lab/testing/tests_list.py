from unittest import TestCase, main
from list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.int_list = IntegerList(5, 6, 7)

    def test_is_init_added_the_data_properly(self):
        self.assertEqual([5, 6, 7], self.int_list.get_data())

    def test_if_adding_a_non_int_to_init_working(self):
        int_list = IntegerList(5.5, 'a', 'b')
        self.assertEqual([], int_list.get_data())

    def test_is_adding_an_element_appending_the_file_to_data(self):
        self.assertEqual([5, 6, 7], self.int_list.get_data())
        self.int_list.add(10)
        self.assertEqual([5, 6, 7, 10], self.int_list.get_data())

    def test_if_adding_a_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add('asd')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_removing_a_existing_index_removes_item(self):
        self.assertEqual([5, 6, 7], self.int_list.get_data())
        self.int_list.remove_index(0)
        self.assertEqual([6, 7], self.int_list.get_data())

    def test_if_removing_a_non_existing_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_is_get_returning_the_exact_element(self):
        self.assertEqual(5, self.int_list.get(0))

    def test_is_get_raising_after_receiving_out_of_index_index(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(15)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_is_insert_method_working_with_valid_index(self):
        self.assertEqual([5, 6, 7], self.int_list.get_data())
        self.int_list.insert(0, 0)
        self.assertEqual([0, 5, 6, 7], self.int_list.get_data())

    def test_is_insert_method_raising_after_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(5, 7)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_is_insert_raising_after_receiving_non_int(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(0, 'asd')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_is_get_biggest_returning_the_biggest_num(self):
        self.assertEqual(7, self.int_list.get_biggest())

    def test_is_biggest_raises_if_there_are_no_elements(self):
        int_list = IntegerList()
        with self.assertRaises(IndexError) as ex:
            int_list.get_biggest()
        self.assertEqual('list index out of range', str(ex.exception))

    def test_get_index(self):
        self.assertEqual(0, self.int_list.get_index(5))

    def test_get_index_raises_if_invalid_index_is_given(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(5)

        self.assertEqual('list index out of range', str(ex.exception))


if __name__ == '__main__':
    main()
