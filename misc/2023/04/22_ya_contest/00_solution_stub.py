import io

class Solution:
    # The following code is mostly a boilerplate.
    # See the "<SOLUTION>" section below.

    def __init__(self, debug=False, input_lines=None) -> None:
        self.is_debug = debug
        self.input_lines = input_lines
        self.current_line = 0
        self.output_lines = []

    def _input(self) -> str:
        if self.is_debug:
            inp = self.input_lines[self.current_line]
            self.current_line += 1
            return inp
        else:
            return input()

    @staticmethod
    def _print_to_string(*args, **kwargs) -> None:
        output = io.StringIO()
        print(*args, file=output, **kwargs)
        contents = output.getvalue()
        output.close()
        return contents.rstrip("\n\r")

    def _output(self, *args, **kwargs) -> None:
        if self.is_debug:
            line = Solution._print_to_string(*args, **kwargs)
            self.output_lines.append(line)
        else:
            print(*args, **kwargs)

# ↓↓↓ input-output stuff

    def read_args(self):
        self._input()
        xs = list(map(int, self._input().split()))
        return xs

    def print_answer(self, answer):
        self._output(*answer)


    def run(self):
        self.output_lines = []
        xs = self.read_args()
        answer = self.solution1(xs)
        self.print_answer(answer)
        return self

# <SOLUTION>
    def solution0(self, xs):
        n = len(xs)

        # the distance is initially assumed to be infinit:
        ans = [float("+inf")] * n

        # distance from the last zero encountered 
        last_zero = float("+inf")
        for i in range(n): # going left to right
            # min distance to the left
            last_zero += 1
            if xs[i] == 0:
                last_zero = 0
            ans[i] = min(ans[i], last_zero)

        for i in range(n): # going right to left
            # min distance to the right
            last_zero += 1
            if xs[~i] == 0:
                last_zero = 0
            ans[~i] = min(ans[~i], last_zero)

        return ans

    def solution1(self, xs):
        # like solution0, but using xs as ans (saves memory)
        n = len(xs)
        last_zero = float("+inf")
        for i in range(n):
            last_zero += 1
            if xs[i] == 0:
                last_zero = 0
            xs[i] = last_zero
        for i in range(n):
            last_zero += 1
            if xs[~i] == 0:
                last_zero = 0
            xs[~i] = min(xs[~i], last_zero)
        return xs

# </SOLUTION>

# <TESTS>
# assert (
#     Solution(debug=True, input_lines=["5", "0 1 4 9 0"]).run().output_lines[0]
#     == "0 1 2 1 0"
# )
# assert (
#     Solution(debug=True, input_lines=["6", "0 7 9 4 8 20"]).run().output_lines[0]
#     == "0 1 2 3 4 5"
# )
# </TESTS>


Solution().run()
