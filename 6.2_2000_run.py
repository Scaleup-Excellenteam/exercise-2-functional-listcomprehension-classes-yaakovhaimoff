"""
Yaakov Haimoff
"""
import time

def timer(func, *args):
    """
    Times how long a function takes to execute.

    Parameters:
    func (function): The function to be timed.
    *args: Any arguments that need to be passed to the function.

    Returns:
    None
    """
    start_time = time.time()
    map(func, *args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds.")


timer(zip, [1, 2, 3], [4, 5, 6])
timer(sorted, [1, 2, 3], [4, 5, 6])
name = "Bug"
timer("Hi {name}".format, name)
