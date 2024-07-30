class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        B_pre = [0] * n
        A_suff = [0] * n

        B_pre[0] = 1 if s[0] == 'b' else 0
        for i in range(1, n):
            B_pre[i] = B_pre[i - 1] + (1 if s[i] == 'b' else 0)

        A_suff[-1] = 1 if s[-1] == 'a' else 0
        for i in range(n - 2, -1, -1):
            A_suff[i] = A_suff[i + 1] + (1 if s[i] == 'a' else 0)

        count = n
        for i in range(n):
            count = min(count, B_pre[i] + A_suff[i] - 1)

        return count
