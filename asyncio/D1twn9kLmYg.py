"""
https://www.youtube.com/watch?v=D1twn9kLmYg

David Beazley: Generators: The Final Frontier - PyCon 2014
"""

# VALUE = "ghdjuigitgf"
# def generator():
#     yield VALUE
#     x = yield VALUE
#     yield VALUE

# g = generator()
# assert next(g) == VALUE

# g.send("kljkjhbvl")


def generator():
    yield "01: simple yield"
    x = yield "02: yield + send"
    print(f">>> x = {x}")
    yield f"03: x = {x}"
    try:
        flag = None
        while flag != "break":
            flag = yield "04: break me if you can"
            print(f">>> The flag value is now: {flag}")
    except GeneratorExit as e:
        print(">>> Exception: GeneratorExit")
        return "The GeneratorExit End"
    except Exception as e:
        print(">>> Exception:", e)
    yield "05: this is the end"

    return "The End"


def test1():
    g1 = generator()

    assert next(g1) == "01: simple yield"
    assert next(g1) == "02: yield + send"
    assert next(g1) == "03: x = None"
    assert next(g1) == "04: break me if you can"
    assert next(g1) == "04: break me if you can"
    assert next(g1) == "04: break me if you can"
    assert g1.send(12) == "04: break me if you can"
    assert g1.send(None) == "04: break me if you can"
    assert g1.send([1, 2, 3]) == "04: break me if you can"
    assert g1.send("break") == "05: this is the end"
    try:
        next(g1)
    except StopIteration as e:
        print("# StopIteration:", e.value)

    print("\n###########################\n")


def test2():
    g2 = generator()
    assert g2.send(None) == "01: simple yield"
    assert g2.send(222) == "02: yield + send"
    assert g2.send(333) == "03: x = 333"
    assert g2.send(444) == "04: break me if you can"
    assert g2.send(555) == "04: break me if you can"
    g2.close()

    print("\n###########################\n")


def test3():
    g3 = generator()
    assert g3.send(None) == "01: simple yield"
    assert g3.send(222) == "02: yield + send"
    assert g3.send(333) == "03: x = 333"
    assert g3.send(444) == "04: break me if you can"
    assert g3.send(555) == "04: break me if you can"
    assert (
        g3.throw(ValueError("Hello, I'm a friendly value error 🙂"))
        == "05: this is the end"
    )
    try:
        g3.send(666)
    except StopIteration as e:
        print("# StopIteration:", e.value)


def all_tests():
    test1()
    test2()
    test3()


def main_say_hallo():
    def say_hallo_gen():
        first_name = yield "say your first name"
        last_name = yield "say your last name"
        return f"Hello, {first_name} {last_name}"

    try:
        gen = say_hallo_gen()
        request = gen.send(None)
        while True:
            print(request)
            request = gen.send(input())
    except StopIteration as e:
        print(e.value)


def main_try_context():
    import datetime
    from contextlib import contextmanager

    @contextmanager
    def timer(name: str):
        dt_start = datetime.datetime.now()
        try:
            yield
        finally:
            dt_stop = datetime.datetime.now()
            print(f"Timer {name} was started at: {dt_start}")
            print(f"Timer {name} is stopped at: {dt_stop}")
            print(f"Total time passed: {dt_stop - dt_start}")

    with timer("test"):
        acc = 0
        for i in range(10_000):
            acc += i
            acc %= 119
        print(f"acc={acc}")


if __name__ == "__main__":
    # all_tests()
    # main_say_hallo()
    main_try_context()
