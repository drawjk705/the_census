"""
This type stub file was generated by pyright.
"""

from rich.progress import ProgressColumn

from .std import tqdm as std_tqdm

"""
`rich.progress` decorator for iterators.

Usage:
>>> from tqdm.rich import trange, tqdm
>>> for i in trange(10):
...     ...
"""
__author__ = { "github.com/": ["casperdcl"] }
class FractionColumn(ProgressColumn):
    """Renders completed/total, e.g. '0.5/2.3 G'."""
    def __init__(self, unit_scale=..., unit_divisor=...) -> None:
        ...
    
    def render(self, task):
        """Calculate common unit for completed and total."""
        ...
    


class RateColumn(ProgressColumn):
    """Renders human readable transfer speed."""
    def __init__(self, unit=..., unit_scale=..., unit_divisor=...) -> None:
        ...
    
    def render(self, task):
        """Show data transfer speed."""
        ...
    


class tqdm_rich(std_tqdm):
    """
    Experimental rich.progress GUI version of tqdm!
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        This class accepts the following parameters *in addition* to
        the parameters accepted by `tqdm`.

        Parameters
        ----------
        progress  : tuple, optional
            arguments for `rich.progress.Progress()`.
        """
        ...
    
    def close(self, *args, **kwargs):
        ...
    
    def clear(self, *_, **__):
        ...
    
    def display(self, *_, **__):
        ...
    
    def reset(self, total=...):
        """
        Resets to 0 iterations for repeated use.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        """
        ...
    


def trrange(*args, **kwargs):
    """
    A shortcut for `tqdm.rich.tqdm(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    ...

tqdm = tqdm_rich
trange = trrange
