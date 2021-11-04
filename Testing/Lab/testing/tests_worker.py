from unittest import main, TestCase
from worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Pesho', 1200, 100)

    def test_if_init_creates_instance_attributes_correctly(self):
        self.assertEqual('Pesho', self.worker.name)
        self.assertEqual(1200, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_is_energy_is_added_after_rest(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_is_worker_tries_to_work_without_energy(self):
        worker = Worker('Ivan', 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_is_salary_added_after_work(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(1200, self.worker.money)

    def test_is_energy_decreased_after_work(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_is_get_info_method_returns_properly_data(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()
