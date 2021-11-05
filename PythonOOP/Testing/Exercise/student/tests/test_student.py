from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Ivan')
        self.second_student = Student('Pesho', {'course': [1, 2]})

    def test_if_init_adds_instance_attributes_correctly_without_courses(self):
        self.assertEqual('Ivan', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_if_init_works_with_courses_added_in_init(self):
        self.assertEqual('Pesho', self.second_student.name)
        self.assertEqual({'course': [1, 2]}, self.second_student.courses)

    def test_enroll_with_already_having_the_same_course_if_adds_and_returns_properly(self):
        self.assertEqual({'course': [1, 2]}, self.second_student.courses)
        return_message = self.second_student.enroll('course', [3])
        self.assertEqual({'course': [1, 2, 3]}, self.second_student.courses)
        self.assertEqual("Course already added. Notes have been updated.", return_message)

    def test_enroll_with_new_course_new_message_with_y_add_notes_message(self):
        self.assertEqual({}, self.student.courses)
        return_message = self.student.enroll('course', [1], 'Y')
        self.assertEqual({'course': [1]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", return_message)

    def test_enroll_with_new_course_default_add_course_notes_message(self):
        self.assertEqual({}, self.student.courses)
        return_message = self.student.enroll('course', [1])
        self.assertEqual({'course': [1]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", return_message)

    def test_enroll_with_different_than_y_and_default_add_course_notes(self):
        self.assertEqual({}, self.student.courses)
        return_message = self.student.enroll('course', [1], 'N')
        self.assertEqual({'course': []}, self.student.courses)
        self.assertEqual("Course has been added.", return_message)

    def test_add_notes_method_with_a_existing_course_name_for_student(self):
        self.assertEqual({'course': [1, 2]}, self.second_student.courses)
        return_message = self.second_student.add_notes('course', 3)
        self.assertEqual({'course': [1, 2, 3]}, self.second_student.courses)
        self.assertEqual("Notes have been updated", return_message)

    def test_add_notes_with_non_existing_course_name_for_student(self):
        self.assertEqual({}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('course', 2)
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course_for_student(self):
        self.assertEqual({'course': [1, 2]}, self.second_student.courses)
        return_message = self.second_student.leave_course('course')
        self.assertEqual({}, self.second_student.courses)
        self.assertEqual("Course has been removed", return_message)

    def test_leave_course_with_non_existing_course_for_student(self):
        self.assertEqual({'course': [1, 2]}, self.second_student.courses)
        with self.assertRaises(Exception) as ex:
            self.second_student.leave_course('non_existing_course')
        self.assertEqual({'course': [1, 2]}, self.second_student.courses)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
