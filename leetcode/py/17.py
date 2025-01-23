class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ret_val: list[str] = []
        mapping: dict[int,str] = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        for digit in digits:
            if not ret_val:
                ret_val = [i for i in mapping[int(digit)]]
            else:
                ret_val = [i+j for i in ret_val for j in mapping[int(digit)]]
        return ret_val