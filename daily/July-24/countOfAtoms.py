class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, n = 0, len(formula)
        count = Counter()
        stack = [count]

        while i < n:
            if formula[i] == '(':
                i += 1
                stack.append(Counter())
            elif formula[i] == ')':
                i += 1
                end = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[end:i] or 1)
                top = stack.pop()
                for name, v in top.items():
                    stack[-1][name] += v * mult
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i] or 1)
                stack[-1][name] += mult

        return "".join(name + (str(count[name]) if count[name] > 1 else '') for name in sorted(count))
