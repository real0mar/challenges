class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
            def dfs(s: str, left: int, right: int):
                if len(s) == 2 * n:
                    result.append(s)
                    return
                if left < n:
                    dfs(s + "(", left + 1, right)
                if right < left:
                    dfs(s + ")", left, right + 1)
            
            result: list[str] = []
            dfs("", 0, 0)
            return result