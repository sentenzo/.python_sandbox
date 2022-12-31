from expression import Expression

def main():
    while True:
        print("(lisp-repl) >> ", end="")
        inp = input()
        if inp == "(exit)":
            return
        exp = Expression(inp)
        out = exp.eval()
        print(out)
		
# (lisp-repl) >> (+ 1 2 3 (+ 2 2))
# 10
# (lisp-repl) >> (= 1 2)
# False
# (lisp-repl) >> (= (* 2 2) (+ 2 2) (- 4 0))
# True
# (lisp-repl) >> (exit)

if __name__ == "__main__":
    main()