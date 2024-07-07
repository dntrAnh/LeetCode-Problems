class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        encrypted_string = ""

        for i in range(n):
            new_idx = (i + k) % n
            encrypted_string += s[new_idx]

        return encrypted_string
