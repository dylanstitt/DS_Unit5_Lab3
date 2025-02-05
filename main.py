# Dylan Stitt
# Unit 5 Lab 3
# Reverse Linked Lists

from SinglyLinkedList import *
from DoublyLinkedList import *
import os

def reverseLL(LL):
    if len(LL) == 1:
        return LL

    value = LL.head_remove()
    LL = reverseLL(LL)
    LL.tail_insert(value)
    return LL


def main():
    SLL = SinglyLinkedList()
    DLL = DoublyLinkedList()

    for i in range(10):
        SLL.tail_insert(i+1)
        DLL.tail_insert(i+1)

    print(f'Original SLL: {SLL}')
    reversedSLL = reverseLL(SLL)
    print(f'Reversed SLL: {reversedSLL}\n')

    print(f'Original DLL: {DLL}')
    reversedDLL = reverseLL(DLL)
    print(f'Reversed DLL: {reversedDLL}')


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
