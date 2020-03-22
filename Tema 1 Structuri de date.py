from random import randint
import time
import sys
sys.setrecursionlimit(1500)

test=7
while test:
    print("Testul ", test, " : ")

    if test == 7:
        maxim = 10000000000
        n = 100000
    elif test == 6:
        maxim = 1000
        n = 1000000
    elif test == 5:
        maxim = 1000
        n = 100
    elif test == 4:
        maxim = 10000
        n = 1000
    elif test == 3:
        maxim = 1000000
        n = 1000
    elif test == 2:
        maxim = 1000000000
        n = 100

    elif test == 1:
        maxim = 10000000
        n = 100000
    lista_testare = []
    for i in range(n):
        nr = randint(1,maxim)
        lista_testare.append(nr)

    test -= 1
    #   functie verificare
    def test_sort(vector):
        for i in range(1, len(vector)):
            if vector[i] < vector[i - 1]:
                return False
        return True


    #   BUBBLESORT
    def bubbleSort(vec):
        if len(vec) < 10000:
            for i in range(len(vec)):
                for j in range(0,n-i-1):
                    if vec[j]>vec[j+1]:
                        vec[j],vec[j+1]=vec[j+1],vec[j]
            return vec
        else:
            print("Dureaza prea mult : ")
            return vec

    #   COUNTSORT
    def countSort(vec):
        size = len(vec)
        maxim = max(vec)
        if maxim <= 10000000:
            output = [0 for i in range(size)]
            count = [0 for i in range(maxim+1)]
            for i in range(size):
                count[vec[i]] = count[vec[i]] + 1

            for i in range(1, maxim+1):
                count[i] += count[i - 1]

            i = len(vec) - 1
            while i >= 0:
                output[count[vec[i]] - 1] = vec[i]
                count[vec[i]] -= 1
                i -= 1

            for i in range(0, len(vec)):
                vec[i] = output[i]
        else:
            print("Prea mare")
        return vec
    #   MERGESORT
    def mergeSort(vec):
        if len(vec) > 1:
            mid = len(vec) // 2
            L = vec[:mid]
            R = vec[mid:]

            mergeSort(L)
            mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    vec[k] = L[i]
                    i += 1
                else:
                    vec[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                vec[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                vec[k] = R[j]
                j += 1
                k += 1
        return vec

    #QUICKSORT
    def partition(vec, low, high):
        i = (low - 1)
        pivot = vec[high]

        for j in range(low, high):

            if vec[j] < pivot:
                i = i + 1
                vec[i], vec[j] = vec[j], vec[i]

        vec[i + 1], vec[high] = vec[high], vec[i + 1]
        return (i + 1)


    def quickSort(vec, low, high):
        if low < high:
            pi = partition(vec, low, high)
            quickSort(vec, low, pi - 1)
            quickSort(vec, pi + 1, high)
        return vec

    #   RADIXSORT
    def countingSort(vec, exp1):
        n = len(vec)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = (vec[i] // exp1)
            count[(index) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (vec[i] // exp1)
            output[count[(index) % 10] - 1] = vec[i]
            count[(index) % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(vec)):
            vec[i] = output[i]


    def radixSort(vec):
        max1 = max(vec)

        exp = 1
        while max1 / exp > 0:
            countingSort(vec, exp)
            exp *= 10
        return vec

   #verificare
    maxim = max(lista_testare)
    minim = min(lista_testare)

    print("Nr date de intrare : ", len(lista_testare))
    print("Maxim : ", maxim)
    print("Minim : ", minim)

    copie_lista = lista_testare.copy()
    copie1 = copie_lista.copy()
    copie2 = copie_lista.copy()
    copie3 = copie_lista.copy()
    copie4 = copie_lista.copy()
    copie5 = copie_lista.copy()
    #verif bubble
    print("1. BubbleSort : ")
    start = time.time()
    copie1 = bubbleSort(copie1)
    end = time.time()
    if test_sort(copie1) == 1:
        print("Sortat : ",end - start)
    else:
        print("Nesortat !")

    #verif count
    print("2. CountSort : ")
    start = time.time()
    copie2 = countSort(copie2)
    end = time.time()
    if test_sort(copie2) == 1:
        print("Sortat : ", end - start)
    else:
        print("Nesortat !")

    #verif merge
    print("3. MergeSort : ")
    start = time.time()
    copie3 = mergeSort(copie3)
    end = time.time()
    if test_sort(copie3) == 1:
        print("Sortat : ",end - start)
    else:
        print("Nesortat !")

    #verif quick
    print("4. QuickSort : ")
    start = time.time()
    copie4 = quickSort(copie4, 0, len(copie4)-1)
    end = time.time()
    if test_sort(copie4) == 1 :
        print("Sortat : ",end - start)
    else:
        print("Nesortat !")

    #verif radix
    print("5. RadixSort : ")
    start = time.time()
    copie5 = radixSort(copie5)
    end = time.time()
    if test_sort(copie5) == 1:
        print("Sortat : ", end - start)
    else:
        print("Nesortat !")
    print()