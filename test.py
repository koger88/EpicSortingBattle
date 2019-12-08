import unittest
import sorteringsAlgoritmer
import random

class TestAlgorithms(unittest.TestCase):

    def testSelectionSort(self):
        #Tilfældig liste med 100 elementer fra 0 til 99
        self.list = [random.randint(0,100) for i in range(100)]
        self.sortedList = sorteringsAlgoritmer.selectionSort(self.list)
        self.assertEqual(self.sortedList, sorted(self.list))

    def testInsertionSort(self):
        self.list = [random.randint(0,100) for i in range(100)]
        self.sortedList = sorteringsAlgoritmer.insertionSort(self.list)
        self.assertEqual(self.sortedList, sorted(self.list))


if __name__ == '__main__':
    unittest.main()