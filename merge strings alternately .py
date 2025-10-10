class Solution(object):
    def mergeAlternatly(self, word1, word2):

        merged = []

         # zip stops when the shorter string ends

        for a, b in zip(word1 , word2):
            merged.append(a)
            merged.append(b)

        # add any leftover characters from the longer string

        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)