from collections import Callable


def input_validated(prompt, validate: Callable, process: Callable = lambda v: v, error="Invalid input"):
    """
    Asks a user for input, validates it with `validate` then processes it with `process`
    :param prompt: The input prompt to show the user
    :param validate: Callable to validate the input, should return a bool indicating whether or not the input is valid
    :param process: Process the input, only called if `validate` returns true, value returned here is returned by the
                    function
    :param error: Error to show to the user if `validate` returns false
    :return: The value returned by `process`
    """
    while True:
        user_input = input(prompt)

        try:
            if validate(user_input):
                return process(user_input)
        except:
            pass

        print(error)


