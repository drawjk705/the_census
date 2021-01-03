import logging
from time import perf_counter
from typing import Any, Callable, Dict, TypeVar, cast

_Func = TypeVar("_Func", bound=Callable[..., Any])


def timer(func: _Func) -> _Func:
    def wrapper(*args: Any, **kwargs: Dict[Any, Any]) -> Any:
        startTime = perf_counter()

        retval = func(*args, **kwargs)

        endTime = perf_counter()

        elapsedMs = (endTime - startTime) * 1000

        logging.debug(f"[{func.__qualname__}] - duration: {elapsedMs:.2f}ms")

        return retval

    return cast(_Func, wrapper)  # type: ignore
