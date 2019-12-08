
import sys




def selectionSort(A):
    A = A.copy()

    for i in range(len(A)): #Gennemtjekker længden af elementerne i array
   
   
        min_idx = i
    
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j


        A[i], A[min_idx] = A[min_idx], A[i]

    return(A)



def insertionSort(A):
    A = A.copy()
    for index in range(1, len(A)): # Længden af et tilfældigt objekt i listen A
        current = A[index] # Listen index er det nuværende
        position = index # indikationen af listen

        while position > 0 and A[position-1] > current: #Hvis den nuværende position er større end positionen af et objekt fra A og mindre end 0 
           
            A[position] = A[position-1] # Positionen -1 er nu = positionen i listen
           
            position -=1 # trækker en fra variablen i listen


        A[position] = current # det nurværende objekt i listen bliver rykket på plads

    return A

