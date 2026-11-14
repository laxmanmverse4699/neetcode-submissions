class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # my approach

        # group = collections.defaultdict(list)

        # for word in strs:
        #     group[str(sorted(word))].append(word)
        # return list(group.values())

        # this approach solve the problem but time complexity is n.klogk it's expensive.

        # new way is to count the each letter - ord is unicode point
        group = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1    # this is the clever idea to reduce sorting way
            group[tuple(count)].append(word)
        return list(group.values())