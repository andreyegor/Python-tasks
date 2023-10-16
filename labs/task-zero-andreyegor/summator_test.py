import summator

verbose = False


def check(test_number: int):
    with open(f"./tests/{test_number}.in", "r") as inp:
        with open(f"./tests/{test_number}.out", "r") as out:
            data = inp.read()
            result = out.read()
            if verbose:
                print(f"\nTesting on:\n{data}\nExpected result: {result}")
            assert summator.solution(data) == int(result)


def test1():
    check(1)


def test2():
    check(2)


def test3():
    check(3)


def test4():
    check(4)


def test5():
    check(5)