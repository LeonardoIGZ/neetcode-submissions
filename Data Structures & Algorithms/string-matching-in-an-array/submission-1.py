class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subs = dict()
        for reference in words:
            for word in words:
                if word != reference and reference in word:
                    subs[reference] = subs.get(reference, 1)

        return list(subs.keys())