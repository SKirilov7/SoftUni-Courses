from Tests.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student_card = StudentReportCard('student', 12)

    def test_init_attaches_correctly(self):
        self.assertEqual('student', self.student_card.student_name)
        self.assertEqual(12, self.student_card.school_year)
        self.assertEqual({}, self.student_card.grades_by_subject)

    def test_if_empty_value_for_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_must_be_between_1_and_12(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.student_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_with_non_existing_subject(self):
        self.assertEqual({}, self.student_card.grades_by_subject)
        self.student_card.add_grade('Math', 5.2)
        self.assertEqual({'Math': [5.2]}, self.student_card.grades_by_subject)

    def test_add_grade_with_existing_subject(self):
        self.student_card.grades_by_subject = {'Math': [5.2]}
        self.student_card.add_grade('Math', 6)
        self.assertEqual({'Math': [5.2, 6]}, self.student_card.grades_by_subject)

    def test_average_grade_with_non_existing_subjects(self):
        self.assertEqual({}, self.student_card.grades_by_subject)
        return_message = self.student_card.average_grade_by_subject()
        self.assertEqual('', return_message)

    def test_average_grade_with_existing_subjects(self):
        self.student_card.grades_by_subject = {'Math': [5, 6], 'Art': [6, 5]}
        expected = 'Math: 5.50\nArt: 5.50'
        return_message = self.student_card.average_grade_by_subject()
        self.assertEqual(expected, return_message)

    def test_average_grade_for_all_subjects(self):
        self.student_card.grades_by_subject = {'Math': [5, 6], 'Art': [6, 5]}
        expected = 'Average Grade: 5.50'
        return_message = self.student_card.average_grade_for_all_subjects()
        self.assertEqual(expected, return_message)

    def test_average_grade_for_all_subjects_with_no_subjects(self):
        with self.assertRaises(ZeroDivisionError) as ex:
            self.student_card.average_grade_for_all_subjects()
        self.assertEqual('division by zero', str(ex.exception))

    def test_represent_method(self):
        self.student_card.grades_by_subject = {'Math': [5, 6], 'Art': [6, 5]}
        expected = f"Name: student\n" \
                   f"Year: 12\n" \
                   f"----------\n" \
                   f"Math: 5.50\n" \
                   f"Art: 5.50\n" \
                   f"----------\n" \
                   f"Average Grade: 5.50"
        return_message = repr(self.student_card)
        self.assertEqual(expected, return_message)


if __name__ == '__main__':
    main()
