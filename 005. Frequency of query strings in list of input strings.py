# Count the frequency of query strings in list of input strings: https://www.hackerrank.com/challenges/sparse-arrays/problem

# Following is an O(n square) appraoch using nested loops

def matchingStrings(stringList, queries):
    size_of_list = len(stringList)
    number_of_queries = len(queries)
    result = []
    
    for i in range(0,number_of_queries):
        query_occurance=0
        for j in range (0,size_of_list):
            if(queries[i]==stringList[j]):
                query_occurance=query_occurance+1
        result.append(query_occurance)
    return result

#--------------------------------------------------------------#

# Following is an O(n) approach using hashmap

def matchingStrings(stringList, queries):
    # create a dict of all elements in stringList with their frequency
    size = len(stringList)
    dict = {}
    for i in range (0,size):
        if stringList[i] in dict: 
            dict[stringList[i]] = dict[stringList[i]] + 1
        else:
            dict[stringList[i]] = 1
    
    # query the dictionary and store the results
    size = len(queries)
    answer = [0] * size
    
    for i in range (0, size):
        if queries[i] in dict:
            answer[i] = dict[queries[i]]
        else:
            answer[i] = 0
    
    return answer
