"""Simple progress bar for Python 3. Does NOT use any external libraries."""

import sys
from collections.abc import Iterable


Characters = int


def progress_bar(array: Iterable, bar_length: Characters = 50) -> Iterable:
    """Simple progress bar. Takes in any iterable and prints a progress bar.
    Do NOT use print or write to sys.stdout while using this function,
    or else the formatting will be weird.

    Args:
        array (Iterable): any iterable, can be an list, string, dictionary, etc.
        bar_length (Characters, optional): Length of the progress bar. Defaults to 50

    Raises:
        TypeError: array is not iterable.

    Yields:
        any: next(array)
    """
    if not isinstance(array, Iterable):
        raise TypeError(
            "'array' is not iterable. Please supply an iterable such as an list, string, dictionary, etc."
        )

    # length of the progress bar, does not include [, >, ], or the 6 characters for final percentage
    percentage = (1 / len(array)) * 100
    progress = 0
    array_iter = iter(array)
    while progress <= 100:
        # progress is marked by '=' and then closed with '>'
        # Fill gap with whitespace
        progress += percentage
        num_of_bars = int(bar_length * (progress / 100))
        whitespace_length = int(bar_length - num_of_bars)
        bar = (
            "["
            + "=" * num_of_bars
            + ">"
            + " " * whitespace_length
            + "]"
            + f" {progress:4.1f}%"
        )
        sys.stdout.write(
            "\b" * int(bar_length + 3 + 6)
        )  # Add 3 for [, >, and ] and 6 for ' xx.x%'
        sys.stdout.flush()
        sys.stdout.write(bar)
        sys.stdout.flush()
        yield next(array_iter)
