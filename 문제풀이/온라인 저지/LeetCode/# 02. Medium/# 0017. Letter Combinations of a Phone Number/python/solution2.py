from itertools import product
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        groups = [chars[digit] for digit in digits]
        return [''.join(prod) for prod in product(*groups)]
