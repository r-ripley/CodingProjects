def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for ch in s.lower().strip(' '):
            if ch.isalpha():
                stripped += ch
        return stripped == stripped[::-1]