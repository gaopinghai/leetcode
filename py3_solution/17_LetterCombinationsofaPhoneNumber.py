class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyBoards = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}
        
        if digits == '':
            return []
        
        def combinations(combs, digit):
            if not digit or digit == '1':
                return combs
            combsN = []
            if combs == []:
                combsN = [v for v in keyBoards[digit]]
            else:
                for v in keyBoards[digit]:
                    combsN += [d + v for d in combs]
            return combsN
        
        combs = []
        for digit in digits:
            combs = combinations(combs, digit)
            
        return combs
            
            
