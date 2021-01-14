"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Any, Callable, Type, Union
from typing_extensions import Literal
from ..dtypes.base import _ArrayLike, _DtypeObj
from .masked import BaseMaskedArray, BaseMaskedDtype

"""
This type stub file was generated by pyright.
"""

class _IntegerDtype(BaseMaskedDtype):
    def __repr__(self) -> str: ...
    def is_signed_integer(self) -> bool: ...
    def is_unsigned_integer(self) -> bool: ...
    def numpy_dtype(self) -> np.dtype: ...
    def kind(self) -> str: ...
    def itemsize(self) -> int: ...
    @classmethod
    def construct_array_type(cls) -> Type[IntegerArray]: ...
    def __from_arrow__(self, array: Any) -> IntegerArray: ...

class IntegerArray(BaseMaskedArray):
    def dtype(self) -> _IntegerDtype: ...
    def __init__(
        self, values: np.ndarray, mask: np.ndarray, copy: bool = ...
    ) -> None: ...
    def __array_ufunc__(
        self,
        ufunc: Callable[..., Any],
        method: Literal["reduce", "accumulate", "reduceat", "outer", "at", "__call__"],
        *inputs: Any,
        **kwargs: Any
    ) -> Any: ...
    def astype(self, dtype: Union[str, _DtypeObj], copy: bool = ...) -> _ArrayLike: ...
    def sum(
        self, skipna: bool = ..., min_count: int = ..., **kwargs: Any
    ) -> _IntegerDtype: ...

class Int8Dtype(_IntegerDtype): ...
class Int16Dtype(_IntegerDtype): ...
class Int32Dtype(_IntegerDtype): ...
class Int64Dtype(_IntegerDtype): ...
class UInt8Dtype(_IntegerDtype): ...
class UInt16Dtype(_IntegerDtype): ...
class UInt32Dtype(_IntegerDtype): ...
class UInt64Dtype(_IntegerDtype): ...
