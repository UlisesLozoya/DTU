from unitgrade import Report, UTestCase, hide
from unittest.mock import patch
import cp
import numpy as np
from io import StringIO

class Task01_EventProbability(UTestCase):
    def test_event_probability_0(self):
        from cp.exam2023fall.tasks.event_probability import event_probability
        self.assertAlmostEqual(event_probability(100, 25), 0.22217864060085335, places=7)

    def test_event_probability_1(self):
        from cp.exam2023fall.tasks.event_probability import event_probability
        self.assertAlmostEqual(event_probability(100, 100), 0.6339676587267709, places=7)

    def test_event_probability_2(self):
        from cp.exam2023fall.tasks.event_probability import event_probability
        self.assertAlmostEqual(event_probability(100, 0), 0.0, places=7)

    def test_event_probability_3(self):
        from cp.exam2023fall.tasks.event_probability import event_probability
        self.assertAlmostEqual(event_probability(100, 50), 0.39499393286246365, places=7)

    def test_event_probability_4(self):
        from cp.exam2023fall.tasks.event_probability import event_probability
        self.assertAlmostEqual(event_probability(500, 75), 0.13942129246327162, places=7)

class Task02_ArrivalTimes(UTestCase):
    def test_arrival_times_0(self):
        from cp.exam2023fall.tasks.arrival_times import arrival_times
        self.assertEqual(arrival_times(['12:37', '08:10'], 25), ['13:02', '08:35'])

    def test_arrival_times_1(self):
        from cp.exam2023fall.tasks.arrival_times import arrival_times
        self.assertEqual(arrival_times(['11:10'], 55), ['12:05'])

    def test_arrival_times_2(self):
        from cp.exam2023fall.tasks.arrival_times import arrival_times
        self.assertEqual(arrival_times(['23:10', '00:00'], 55), ['00:05', '00:55'])

    def test_arrival_times_3(self):
        from cp.exam2023fall.tasks.arrival_times import arrival_times
        self.assertEqual(arrival_times(['15:58', '16:22', '19:04', '20:01'], 102), ['17:40', '18:04', '20:46', '21:43'])

    def test_arrival_times_4(self):
        from cp.exam2023fall.tasks.arrival_times import arrival_times
        self.assertEqual(arrival_times(['09:20', '10:00', '10:14', '10:59'], 0), ['09:20', '10:00', '10:14', '10:59'])

class Task03_SpecialOccurrence(UTestCase):
    def test_special_occurrence_0(self):
        from cp.exam2023fall.tasks.special_occurrence import special_occurrence
        self.assertEqual(special_occurrence([2, 8, 11, 3, 12, 5, 7, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6]), 11)

    def test_special_occurrence_1(self):
        from cp.exam2023fall.tasks.special_occurrence import special_occurrence
        self.assertEqual(special_occurrence([2, 8, 11, 5, 5, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6]), 3)

    def test_special_occurrence_2(self):
        from cp.exam2023fall.tasks.special_occurrence import special_occurrence
        self.assertEqual(special_occurrence([11, 3, 12, 5, 2, 5, 7, 7, 6, 2, 8, 11, 3, 12, 5, 7, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6]), 20)

    def test_special_occurrence_3(self):
        from cp.exam2023fall.tasks.special_occurrence import special_occurrence
        self.assertEqual(special_occurrence([5, 8, 7, 3, 12, 5, 7, 7, 11, 3, 12, 5, 2, 7, 5, 7, 2, 6]), 0)

    def test_special_occurrence_4(self):
        from cp.exam2023fall.tasks.special_occurrence import special_occurrence
        self.assertEqual(special_occurrence([2, 8, 11, 3, 12, 5, 7, 7, 11, 3, 12, 5, 7, 7, 5, 7, 7, 5]), -1)

class Task04_PunctuationRatio(UTestCase):
    def test_punctuation_ratio_0(self):
        text = ('Sara and Emma like to travel, bike, and hike, and when they are traveling they always ' +
            'take their bikes, hiking shoes, and sleeping bags. Last year, Sarah and Emma traveled to ' +
            'Italy, France, and Spain. And that was fun, and, according to Sara and Emma, very expensive!')
        from cp.exam2023fall.tasks.punctuation_ratio import punctuation_ratio
        self.assertAlmostEqual(punctuation_ratio(text), 4/3, places=7)

    def test_punctuation_ratio_1(self):
        text = ('This is some text and not just any text, and more than just text. ')
        from cp.exam2023fall.tasks.punctuation_ratio import punctuation_ratio
        self.assertAlmostEqual(punctuation_ratio(text), 1.0, places=7)

    def test_punctuation_ratio_2(self):
        text = ('Martin and Emma, and Simon and Mia, and Sara, and Ella are all here.')
        from cp.exam2023fall.tasks.punctuation_ratio import punctuation_ratio
        self.assertAlmostEqual(punctuation_ratio(text), 1.5, places=7)

    def test_punctuation_ratio_3(self):
        text = ('Text without and.')
        from cp.exam2023fall.tasks.punctuation_ratio import punctuation_ratio
        self.assertAlmostEqual(punctuation_ratio(text), 0.0, places=7)

    def test_punctuation_ratio_4(self):
        text = ('Text with only one type of and, and with a comma.')
        from cp.exam2023fall.tasks.punctuation_ratio import punctuation_ratio
        self.assertAlmostEqual(punctuation_ratio(text), 0.0, places=7)

class Task05_CheckerboardSum(UTestCase):
    def test_checkerboard_sum_0(self):
        from cp.exam2023fall.tasks.checkerboard_sum import checkerboard_sum
        A = np.array([[1.42, 4.0, 55.56, 63.0], [2.22, 2.22, 33.73, 40.11], [12.1, 17.24, 18.0, 33.5], [21.15, 14.76, 17.3, 22.1], [5.34, 6.0, 9.8, 8.18]])
        self.assertAlmostEqual(checkerboard_sum(A), 181.41, places=2)

    def test_checkerboard_sum_1(self):
        from cp.exam2023fall.tasks.checkerboard_sum import checkerboard_sum
        A = np.array([[10.42, 4.0]])
        self.assertAlmostEqual(checkerboard_sum(A), 10.42, places=2)

    def test_checkerboard_sum_2(self):
        from cp.exam2023fall.tasks.checkerboard_sum import checkerboard_sum
        A = np.array([[10.42, 4.0, 15.06]])
        self.assertAlmostEqual(checkerboard_sum(A), 25.48, places=2)

    def test_checkerboard_sum_3(self):
        from cp.exam2023fall.tasks.checkerboard_sum import checkerboard_sum
        A = np.array([[1.42], [0.22], [17.1], [13.15], [25.34]])
        self.assertAlmostEqual(checkerboard_sum(A), 43.86, places=2)

    def test_checkerboard_sum_4(self):
        from cp.exam2023fall.tasks.checkerboard_sum import checkerboard_sum
        A = np.array([[0.08, 2.11, 2.99], [0.79, 83.31, 14.59]])
        self.assertAlmostEqual(checkerboard_sum(A), 86.38, places=2)

class Task06_CollatzConjecture(UTestCase):
    def test_collatz_conjecture_0(self):
        from cp.exam2023fall.tasks.collatz_conjecture import collatz_conjecture
        self.assertEqual(collatz_conjecture(3), 7)

    def test_collatz_conjecture_1(self):
        from cp.exam2023fall.tasks.collatz_conjecture import collatz_conjecture
        self.assertEqual(collatz_conjecture(9), 19)

    def test_collatz_conjecture_2(self):
        from cp.exam2023fall.tasks.collatz_conjecture import collatz_conjecture
        self.assertEqual(collatz_conjecture(12), 9)

    def test_collatz_conjecture_3(self):
        from cp.exam2023fall.tasks.collatz_conjecture import collatz_conjecture
        self.assertEqual(collatz_conjecture(1), 0)

    def test_collatz_conjecture_4(self):
        from cp.exam2023fall.tasks.collatz_conjecture import collatz_conjecture
        self.assertEqual(collatz_conjecture(5), 5)

class Task07_BankAccount(UTestCase):
    def str_cmp(self, mock_stdout, expected):
        out = mock_stdout.getvalue().strip().replace('dkk', 'DKK')
        if out.endswith('.'):
            out = out[:-1]
        self.assertEqual(out, expected)

    def check_withdraw(self, my_account, withdraw_amount, expected_message=""):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_account.withdraw(withdraw_amount)
            self.str_cmp(mock_stdout, expected_message)
    
    def check_print_balance(self, my_account, expected):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_account.print_balance()
            self.str_cmp(mock_stdout, expected)

    def test_case_from_pdf(self):
        from cp.exam2023fall.tasks.bank_account import BankAccount
        my_account = BankAccount(1000)
        self.assertAlmostEqual(my_account.balance, 1000)
        my_account.deposit(500)
        self.assertAlmostEqual(my_account.balance, 1500)
        self.check_withdraw(my_account, 200)
        self.assertAlmostEqual(my_account.balance, 1300)
        self.check_withdraw(my_account, 2000, "Withdraw failed: Insufficient funds")
        self.assertAlmostEqual(my_account.balance, 1300)

    def test_bank_account_print_balance_1(self):
        from cp.exam2023fall.tasks.bank_account import BankAccount
        my_account = BankAccount(35)
        self.check_print_balance(my_account, "Balance: 35 DKK")

    def test_bank_account_withdraw_1(self):
        from cp.exam2023fall.tasks.bank_account import BankAccount
        my_account = BankAccount(3090)
        self.check_withdraw(my_account, 3000)
        self.assertAlmostEqual(my_account.balance, 90)

    def test_bank_account_withdraw_2(self):
        from cp.exam2023fall.tasks.bank_account import BankAccount
        my_account = BankAccount(403)
        self.check_withdraw(my_account, 550, "Withdraw failed: Insufficient funds")
        self.assertAlmostEqual(my_account.balance, 403)

    def test_bank_account_deposit_1(self):
        from cp.exam2023fall.tasks.bank_account import BankAccount
        my_account = BankAccount(123)
        my_account.deposit(7000)
        self.assertAlmostEqual(my_account.balance, 7123)

class Task08_PhonebookMerge(UTestCase):        
    def test_phonebook_merge_0(self):
        from cp.exam2023fall.tasks.phonebook_merge import phonebook_merge
        phonebook1 =   {'Liv': ['55511112', '18777890'], 
                        'Mads': ['27274445', '48533336'],
                        'Steve': ['45455555', '25455525']}
        phonebook2 =   {'Anna': ['89577772'], 
                        'Steve': ['25257755', '25455525'],
                        'Mads': ['48533336', '27274445']}
        correct = {'Liv': ['55511112', '18777890'], 
                    'Mads': ['27274445', '48533336'],
                    'Steve': ['45455555', '25455525', '25257755'],
                    'Anna': ['89577772']}   
        self.assertIsNone(phonebook_merge(phonebook1, phonebook2))
        self.assertDictEqual(phonebook1, correct)
    
    def test_phonebook_merge_1(self):
        from cp.exam2023fall.tasks.phonebook_merge import phonebook_merge
        phonebook1 =   {'Morten': ['19199112', '88777890'], 
                        'Anders': ['27274445', '48533336'],
                        'Vedrana': ['45455555', '25455525']}
        phonebook2 =   {'Tina': ['89577772'], 
                        'Mickey': ['25257755', '25455525'],
                        'Sally': ['48533336', '27274445']}
        correct = {'Morten': ['19199112', '88777890'], 
                    'Anders': ['27274445', '48533336'],
                    'Vedrana': ['45455555', '25455525'],
                    'Tina': ['89577772'], 
                    'Mickey': ['25257755', '25455525'],
                    'Sally': ['48533336', '27274445']} 
        self.assertIsNone(phonebook_merge(phonebook1, phonebook2))
        self.assertDictEqual(phonebook1, correct)

    def test_phonebook_merge_2(self):
        from cp.exam2023fall.tasks.phonebook_merge import phonebook_merge
        phonebook1 =   {'Adam': ['000000'], 
                        'Bertram': ['111111'],
                        'Carl': ['222222', '222233'],
                        'David': ['333333', '333344']}
        phonebook2 =   {'Adam': ['000000'],
                        'Bertram': ['111111'],
                        'Carl': ['222222', '222233'],
                        'David': ['333333', '333344', '333355']}
        correct = {'Adam': ['000000'],
                        'Bertram': ['111111'],
                        'Carl': ['222222', '222233'],
                        'David': ['333333', '333344', '333355']}
        self.assertIsNone(phonebook_merge(phonebook1, phonebook2))
        self.assertDictEqual(phonebook1, correct)

    def test_phonebook_merge_3(self):
        from cp.exam2023fall.tasks.phonebook_merge import phonebook_merge
        phonebook1 = {'Alina': ['14101903', '45644435'],
                        'Birgitte': ['12345678'],
                        'Cecilie': ['87654321', '12345678']}
        phonebook2 = {'Alina': ['15101903', '45644435'],
                        'Birgitte': ['12345678'],
                        'Cecilie': ['87654321', '12345678'],
                        'Dagmar': ['12345678', '87654321'],
                        'Eva': ['12345678', '34567890'],
                        'Frida': ['12345678', '43463426'],
                        'Gudrun': ['12345678'],
                        'Hanna': ['12345678'],
                        'Ida': ['12345678']}
        correct = {'Alina': ['14101903', '45644435', '15101903'],
                    'Birgitte': ['12345678'],
                    'Cecilie': ['87654321', '12345678'],
                    'Dagmar': ['12345678', '87654321'],
                    'Eva': ['12345678', '34567890'],
                    'Frida': ['12345678', '43463426'],
                    'Gudrun': ['12345678'],
                    'Hanna': ['12345678'],
                    'Ida': ['12345678']}       
        self.assertIsNone(phonebook_merge(phonebook1, phonebook2))
        self.assertDictEqual(phonebook1, correct)

    def test_phonebook_merge_4(self):
        from cp.exam2023fall.tasks.phonebook_merge import phonebook_merge
        phonebook1 = {'Marko': ['091456996', '098353245', '043245632', '051432445'],
                        'Ivan': ['091456996', '043245632', '051432445'],
                        'Ana': ['091456996', '098353245', '046245632', '051432445'],
                        'Ivana': ['091456996', '098353245', '01023456', '051432445'],
                        'Ivona': ['091456996', '098353245', '089654332', '057444765'],
                        'Hrvoje': ['091284234', '098353245', '043245632', '058432445'],
                        'Helena': ['091399838', '0782345656', '043245632', '055432445'],
                        'Mirela': ['091486331', '021344555', '045999324', '0619993459']}
        phonebook2 = {'Marko': ['051432445'],
                        'Helena': ['091399838', '078446444', '23322234'],
                        'Cecilie': ['87654321', '12345678'],
                        'Dagmar': ['12345678', '87654321'],
                        'Eva': ['12345678', '34567890'],
                        'Frida': ['12345678', '43463426'],
                        'Mirela': ['091486331', '021344555', '045999324', '0619993459']}
        correct = {'Marko': ['091456996', '098353245', '043245632', '051432445'],
                    'Ivan': ['091456996', '043245632', '051432445'],
                    'Ana': ['091456996', '098353245', '046245632', '051432445'],
                    'Ivana': ['091456996', '098353245', '01023456', '051432445'],
                    'Ivona': ['091456996', '098353245', '089654332', '057444765'],
                    'Hrvoje': ['091284234', '098353245', '043245632', '058432445'],
                    'Helena': ['091399838', '0782345656', '043245632', '055432445', '078446444', '23322234'],
                    'Mirela': ['091486331', '021344555', '045999324', '0619993459'],
                    'Cecilie': ['87654321', '12345678'],
                    'Dagmar': ['12345678', '87654321'],
                    'Eva': ['12345678', '34567890'],
                    'Frida': ['12345678', '43463426']}      
        self.assertIsNone(phonebook_merge(phonebook1, phonebook2))
        self.assertDictEqual(phonebook1, correct)

class Task09_NitrateLevels(UTestCase):   
    def test_nitrate_levels_0(self):
        from cp.exam2023fall.tasks.nitrate_levels import nitrate_levels
        self.assertEqual(nitrate_levels('cp/exam2023fall/tasks/files/nitrate_data_A.txt'), (0, 0, 8, 2, 0))

    def test_nitrate_levels_1(self):
        from cp.exam2023fall.tasks.nitrate_levels import nitrate_levels
        self.assertEqual(nitrate_levels('cp/exam2023fall/tasks/files/nitrate_data_B.txt'), (0, 0, 21, 16, 5))

    def test_nitrate_levels_2(self):
        from cp.exam2023fall.tasks.nitrate_levels import nitrate_levels
        self.assertEqual(nitrate_levels('cp/exam2023fall/tasks/files/nitrate_data_C.txt'), (0, 0, 8, 2, 0))

    def test_nitrate_levels_3(self):
        from cp.exam2023fall.tasks.nitrate_levels import nitrate_levels
        self.assertEqual(nitrate_levels('cp/exam2023fall/tasks/files/nitrate_data_D.txt'), (6, 6, 17, 0, 0))

    def test_nitrate_levels_4(self):
        from cp.exam2023fall.tasks.nitrate_levels import nitrate_levels
        self.assertEqual(nitrate_levels('cp/exam2023fall/tasks/files/nitrate_data_E.txt'), (0, 0, 0, 5, 22))

class Task10_OverdraftAccount(UTestCase):
    def str_cmp(self, mock_stdout, expected):
        out = mock_stdout.getvalue().strip().replace('dkk', 'DKK')
        if out.endswith('.'):
            out = out[:-1]
        self.assertEqual(out, expected)

    def check_withdraw(self, my_account, withdraw_amount, expected_message=""):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_account.withdraw(withdraw_amount)
            self.str_cmp(mock_stdout, expected_message)

    def check_print_balance(self, my_account, expected):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_account.print_balance()
            self.str_cmp(mock_stdout, expected)

    def test_case_from_pdf(self):
        from cp.exam2023fall.tasks.bank_account import OverdraftAccount, BankAccount
        self.assertTrue(issubclass(OverdraftAccount, BankAccount))
        my_account = OverdraftAccount(0, 500)
        self.assertAlmostEqual(my_account.balance, 0.00)
        my_account.deposit(1000)
        self.assertAlmostEqual(my_account.balance, 1000)
        self.check_withdraw(my_account, 1300)
        self.assertAlmostEqual(my_account.balance, -300)
        self.check_withdraw(my_account, 500, "Withdraw failed: Overdraft limit exceeded")
        self.assertAlmostEqual(my_account.balance, -300)

    def test_overdraft_account_print_balance_1(self):
        from cp.exam2023fall.tasks.bank_account import OverdraftAccount, BankAccount
        self.assertTrue(issubclass(OverdraftAccount, BankAccount))
        my_account = OverdraftAccount(31, 200)
        my_account.withdraw(50)
        self.check_print_balance(my_account, "Balance: -19 DKK")

    def test_overdraft_account_withdraw_1(self):
        from cp.exam2023fall.tasks.bank_account import OverdraftAccount, BankAccount
        self.assertTrue(issubclass(OverdraftAccount, BankAccount))
        my_account = OverdraftAccount(3090.54, 300)
        self.check_withdraw(my_account, 3200)
        self.assertAlmostEqual(my_account.balance, -109.46)

    def test_overdraft_account_withdraw_2(self):
        from cp.exam2023fall.tasks.bank_account import OverdraftAccount, BankAccount
        self.assertTrue(issubclass(OverdraftAccount, BankAccount))
        my_account = OverdraftAccount(403, 200)
        self.check_withdraw(my_account, 550)
        self.assertAlmostEqual(my_account.balance, -147)
        self.check_withdraw(my_account, 300, "Withdraw failed: Overdraft limit exceeded")
        self.assertAlmostEqual(my_account.balance, -147)

    def test_overdraft_account_deposit_1(self):
        from cp.exam2023fall.tasks.bank_account import OverdraftAccount, BankAccount
        self.assertTrue(issubclass(OverdraftAccount, BankAccount))
        my_account = OverdraftAccount(500, 200)
        my_account.deposit(300)
        self.assertAlmostEqual(my_account.balance, 800)

questions = [
            (Task01_EventProbability, 10),
            (Task02_ArrivalTimes, 10),
            (Task03_SpecialOccurrence, 10),
            (Task04_PunctuationRatio, 10),
            (Task05_CheckerboardSum, 10),
            (Task06_CollatzConjecture, 10),
            (Task07_BankAccount, 10),
            (Task08_PhonebookMerge, 10),
            (Task09_NitrateLevels, 10),
            (Task10_OverdraftAccount, 10),
            ]

class Exam2023Fall(Report):
    title = "Computer Programming Exam Fall 2023"
    pack_imports = [cp]
    individual_imports = []
    questions = questions

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Exam2023Fall())
