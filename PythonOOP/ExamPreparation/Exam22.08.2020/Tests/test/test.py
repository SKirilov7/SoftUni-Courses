from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student_card = StudentReportCard('Pesho', 12)

    def test_init_attaches_correctly(self):
        self.assertEqual('Pesho', self.student_card.student_name)
        self.assertEqual(12, self.student_card.school_year)
        self.assertEqual({}, self.student_card.grades_by_subject)

    def test_student_name_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard('', 10)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))
        self.student_card.student_name = 'Slavi'
        self.assertEqual('Slavi', self.student_card.student_name)

    def test_school_year_less_than_1_and_more_than_12_raises(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard('Kiro', 0)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))
        with self.assertRaises(ValueError) as exception_error:
            student = StudentReportCard('Kiro', 13)
        self.assertEqual("School Year must be between 1 and 12!", str(exception_error.exception))
        self.student_card.school_year = 1
        self.assertEqual(1, self.student_card.school_year)

    def test_add_grade_with_non_existing_and_existing_subject(self):
        self.assertEqual({}, self.student_card.grades_by_subject)
        self.student_card.add_grade('Math', 5)
        self.assertEqual({'Math': [5]}, self.student_card.grades_by_subject)
        self.student_card.add_grade('Math', 6)
        self.assertEqual({'Math': [5, 6]}, self.student_card.grades_by_subject)
        self.student_card.add_grade('Physics', 6)
        self.assertEqual({'Math': [5, 6], 'Physics': [6]}, self.student_card.grades_by_subject)

    def test_average_grade_by_subject_method(self):
        self.assertEqual({}, self.student_card.grades_by_subject)
        actual = self.student_card.average_grade_by_subject()
        self.assertEqual(actual, '')
        self.student_card.grades_by_subject = {'Math': [5, 6], 'Physics': [5, 6]}
        expected = 'Math: 5.50\nPhysics: 5.50'
        actual = self.student_card.average_grade_by_subject()
        self.assertEqual(actual, expected)

    def test_average_grade_for_all_subjects(self):
        self.student_card.grades_by_subject = {'Math': [5, 5], 'Physics': [6, 6]}
        expected = 'Average Grade: 5.50'
        actual = self.student_card.average_grade_for_all_subjects()
        self.assertEqual(actual, expected)

    def test_represent_method(self):
        self.student_card.grades_by_subject = {'Math': [5, 6], 'Physics': [5, 6]}
        self.assertEqual({'Math': [5, 6], 'Physics': [5, 6]}, self.student_card.grades_by_subject)
        expected = 'Name: Pesho\n' \
                   'Year: 12\n' \
                   '----------\n' \
                   'Math: 5.50\n' \
                   'Physics: 5.50\n' \
                   '----------\n' \
                   'Average Grade: 5.50'
        actual = self.student_card.__repr__()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
