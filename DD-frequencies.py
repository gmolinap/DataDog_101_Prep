"""
Given an unsorted array of n integers that can contain integers from 1 to n. 
Some elements can be repeated multiple times and some other elements can be absent from the array. 
Count the frequency of all elements that are present and print the missing elements.

Input: arr[] = {2, 3, 3, 2, 5}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 2
        3 -> 2
        4 -> 0
        5 -> 1

"""


def counting_frequencies(arr, n):
    hash = [0 for i in range(n)] #initialize the hash array with 0
    #why this is a hash? 

    i = 0 

    while (i<n):
        hash[arr[i]-1] += 1
        i += 1

    for i in range(n):
        print(i+1,"-> ", hash[i]) 
        print()





arr5 = [ 1, 2, 3, 4, 5, 
         6, 7, 8, 9, 10, 11 ]
counting_frequencies(arr5, len(arr5))