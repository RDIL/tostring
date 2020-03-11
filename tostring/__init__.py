"""The main class for tostring, a module which translates Python built-in types into their string equivalents."""

from json import dumps


def tostring(input_data):
    """The main tostring function, which returns a string representation of the item you pass."""

    if type(input_data) == str:
        return input_data
    elif type(input_data) == int:
        return str(input_data)
    elif type(input_data) == dict:
        return dumps(input_data)
    elif type(input_data) == list:
        # Join all the strings in list
        final_str = ", ".join(
            "\"{}\"".format(
                input_data
            )
        )
        return final_str
