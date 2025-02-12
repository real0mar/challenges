class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0

        while s:
            if "IV" in s:
                number += 4
                s = s.replace("IV", "")
            elif "IX" in s:
                number += 9
                s = s.replace("IX", "")
            elif "XL" in s:
                number += 40
                s = s.replace("XL", "")
            elif "XC" in s:
                number += 90
                s = s.replace("XC", "")
            elif "CD" in s:
                number += 400
                s = s.replace("CD", "")
            elif "CM" in s:
                number += 900
                s = s.replace("CM", "")
            else:
                break

        while s:
            char = s[-1]
            if char == "I":
                number += 1
            elif char == "V":
                number += 5
            elif char == "X":
                number += 10
            elif char == "L":
                number += 50
            elif char == "C":
                number += 100
            elif char == "D":
                number += 500
            elif char == "M":
                number += 1000
            s = s[:-1]
        return number
