class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    #本题目其实就是两部，1. 双向构建dict 2. 双向比较w1,w2
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if not words1 and not words2:
            return True 
        if not words1 or not words2:
            return False 
        if len(words1) != len(words2):
            return False 

        d = {}

        for pair in pairs:
            w1 = pair[0]
            w2 = pair[1]

            d.setdefault(w1, set())
            d[w1].add(w2)
            d.setdefault(w2, set())
            d[w2].add(w1)

        length = len(words1)
        for i in range(length):
            if words1[i] == words2[i]:
                continue 
            # words1[i]不在pairs中 或者 words[i]的对应不是words2[i]，一个条件为true就不符合题意
            if words1[i] not in d or words2[i] not in d[words1[i]]:
                return False 
        
        
        return True 


# #单向构建字典，双向比较
#     def isSentenceSimilarity(self, words1, words2, pairs):
#         # write your code here
#         if not words1 and not words2:
#             return True 
#         if not words1 or not words2:
#             return False 
#         if len(words1) != len(words2):
#             return False 

#         d = {}

#         for pair in pairs:
#             w1 = pair[0]
#             w2 = pair[1]

#             d.setdefault(w1, set())
#             d[w1].add(w2)
#             # d.setdefault(w2, set())
#             # d[w2].add(w1)

#         length = len(words1)
#         for i in range(length):
#             if words1[i] == words2[i]:
#                 continue 
#             # words1[i]不在pairs中 or words[i]的对应不是words2[i]
#             w1_status = words1[i] not in d or words2[i] not in d[words1[i]]
#             w2_status = words2[i] not in d or words1[i] not in d[words2[i]]
#             if w1_status and w2_status:
#                 return False 
        
        
#         return True 