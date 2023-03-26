"""
Yaakov Haimoff
"""

def group_by(func, seq):
    """
    Groups elements of a sequence by the result of applying a function to each element.

    Parameters:
    func (function): The function to apply to each element.
    seq (list): The sequence of elements to group.

    Returns:
    dict: A dictionary where the keys are the results of applying the function to the elements
    in the sequence, and the values are lists of elements in the sequence that have the same function result.
    """
    return {func(x): [x for x in seq if func(x) == func(x)] for x in seq}


print(group_by(len, ["hi", "bye", "yo", "try"]))

