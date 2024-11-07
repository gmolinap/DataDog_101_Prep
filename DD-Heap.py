"""
1)
            ◯9 i   ←largest
            /  \
        13◯  ◯18

2) 
            ◯9 i   
            /  \
largest 13◯  ◯18

3) 
            ◯9 i   
            /  \
         13◯  ◯18 largest

"""

def max_heapify(arr, heap_size, index):
    left = 2*index
    right = 2 * index + 1

    largest = index

    if left < heap_size and arr[left] > arr[index]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right     

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        #print("SWAP", arr)
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr): #builds a max heap from an unsorted array
    heap_size = len(arr) 
    print("Heap size", heap_size)
    for i in range(heap_size//2,0,-1): #iterating from the last parent node to the root. Leaves are already max heaps so we don't need to check them.
           
        max_heapify(arr,heap_size,i) 
        print(arr)

def heap_sort(arr):
    build_max_heap(arr)
    for i in range(len(arr)-1,0,-1): #iterating from the last element to the second element
        arr[i], arr[1] = arr[1], arr[i]
        max_heapify(arr,i,1)
        


def main():
    # root is at index 1
    a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    heap_sort(a)
    # print heap starting with the root at index 1
    print(f'Heap sort: {a[1:]}')
    build_max_heap(a)


    # print heap starting with the root at index 1
    print(f'Max Heap: {a[1:]}')
    


main()

"""

"""
