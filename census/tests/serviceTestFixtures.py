from typing import Any, Generic, TypeVar, cast
from unittest.mock import MagicMock
from _pytest.monkeypatch import MonkeyPatch


from pytest_mock.plugin import MockerFixture  # type: ignore
import pytest


_T = TypeVar("_T")


@pytest.mark.usefixtures(
    "injectMockerToClass", "serviceFixture", "injectMonkeyPatchToClass"
)
class ServiceTestFixture(Generic[_T]):
    _service: _T
    mocker: MockerFixture
    monkeypatch: MonkeyPatch

    def castMock(self, dependency: Any) -> MagicMock:
        return cast(MagicMock, dependency)


@pytest.mark.usefixtures("apiFixture")
class ApiServiceTestFixture(ServiceTestFixture[_T]):
    requestsMock: MagicMock
