"""
This type stub file was generated by pyright.
"""

from .std import tqdm as std_tqdm

"""
Asynchronous progressbar decorator for iterators.
Includes a default `range` iterator printing to `stderr`.

Usage:
>>> from tqdm.asyncio import trange, tqdm
>>> async for i in trange(10):
...     ...
"""
__author__ = { "github.com/": ["casperdcl"] }
class tqdm_asyncio(std_tqdm):
    """
    Asynchronous-friendly version of tqdm (Python 3.5+).
    """
    def __init__(self, iterable=..., *args, **kwargs) -> None:
        ...
    
    def __aiter__(self):
        ...
    
    async def __anext__(self):
        ...
    
    def send(self, *args, **kwargs):
        ...
    
    @classmethod
    def as_completed(cls, fs, *, loop=..., timeout=..., total=..., **tqdm_kwargs):
        """
        Wrapper for `asyncio.as_completed`.
        """
        ...
    


def tarange(*args, **kwargs):
    """
    A shortcut for `tqdm.asyncio.tqdm(range(*args), **kwargs)`.
    """
    ...

tqdm = tqdm_asyncio
trange = tarange
