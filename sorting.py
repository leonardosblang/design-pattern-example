import random
from abc import ABC, abstractmethod
from sorting_techniques import pysort

sortObj = pysort.Sorting()


class Strategy(ABC):
    @abstractmethod
    def selection(self, thing_to_sort) -> None:
        pass


class BubbleSort(Strategy):

    def selection(self, thing_to_sort) -> str:
        new_sort = sortObj.bubbleSort(thing_to_sort)
        return new_sort


class QuickSort(Strategy):
    def selection(self, thing_to_sort) -> str:
        new_sort = sortObj.quickSort(thing_to_sort, 0, len(thing_to_sort) - 1)
        return new_sort


class HeapSort(Strategy):
    def selection(self, thing_to_sort) -> str:
        new_sort = sortObj.heapSort(thing_to_sort)
        return new_sort


class InsertionSort(Strategy):
    def selection(self, thing_to_sort) -> str:
        new_sort = sortObj.insertionSort(thing_to_sort)
        return new_sort


class PickRandomAlgorithm(Strategy):
    def selection(self, thing_to_sort) -> str:
        algorithms = ['bubbleSort', 'heapSort', 'insertionSort']
        random_algorithm = random.choice(algorithms)
        new_sort = sortObj.__getattribute__(random_algorithm)(thing_to_sort)
        return new_sort


class Sort:
    strategy: Strategy

    def __init__(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = PickRandomAlgorithm()

    def run(self, thing_to_sort) -> None:
        s1 = self.strategy.selection(thing_to_sort)
        if s1 is not None:
            print(s1)


if __name__ == "__main__":
    print("Enter a list of numbers to sort")
    print("Enter 'q' to quit")
    while True:
        user_input = input("Enter a list of numbers: ")
        if user_input == 'q':
            break
        else:
            try:
                user_input = [int(x) for x in user_input.split()]
            except ValueError:
                print("Enter a list of numbers")
                continue
            # ask user for sorting algorithm
            print("Enter a sorting algorithm")
            print("1. Bubble Sort")
            print("2. Quick Sort")
            print("3. Heap Sort")
            print("4. Insertion Sort")
            print("5. Random Algorithm")
            print("6. Quit")
            while True:
                user_input2 = input("Enter a number: ")
                if user_input2 == '1':
                    sort = Sort(BubbleSort())
                    sort.run(user_input)
                    break
                elif user_input2 == '2':
                    sort = Sort(QuickSort())
                    sort.run(user_input)
                    break
                elif user_input2 == '3':
                    sort = Sort(HeapSort())
                    sort.run(user_input)
                    break
                elif user_input2 == '4':
                    sort = Sort(InsertionSort())
                    sort.run(user_input)
                    break
                elif user_input2 == '5':
                    sort = Sort()
                    sort.run(user_input)
                    break
                elif user_input2 == '6':
                    break
                else:
                    print("Enter a number between 1 and 6")
                    continue
