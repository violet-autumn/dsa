# Count the frequency of query strings in list of input strings: https://www.hackerrank.com/challenges/sparse-arrays/problem

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
