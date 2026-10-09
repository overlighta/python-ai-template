from python_ai_template import greet


def test_greet():
    result = greet("Alice")
    assert result == "Hello, Alice!"
    # assert is a statement that checks if a condition is true.
    # If the condition is false,
    # it raises an AssertionError exception and stops that the execution of the program.
    #  If the condition is true, the program continues to execute normally.


def test_greet_empty_name():
    result = greet("")
    assert result == "Hello, !"
