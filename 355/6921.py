class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            tmpRes = word.split(separator)
            tmpRes = filter(lambda x:x!='', tmpRes)
            res += tmpRes

        return res


