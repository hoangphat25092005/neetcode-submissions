class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token in "+-*/":
                b = st.pop()
                a = st.pop()

                if token == '+':
                    s = a + b
                elif token == '-':
                    s = a - b
                elif token == '*':
                    s = a * b
                elif token == '/':
                    s = int(a / b)

                st.append(s)
            else:
                st.append(int(token))

        return st[-1]
            