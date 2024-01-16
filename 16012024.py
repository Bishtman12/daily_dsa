#!Problem Link : https://www.geeksforgeeks.org/problems/sequence-of-sequence1155/1


def numberSequence(m, n):
    if(m<n):
        return 0
    if n ==1 :
        return m
    return (helper(m//2, n-1) + helper(m-1,n))


numberSequence(5,2)