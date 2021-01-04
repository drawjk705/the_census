from abc import abstractmethod
from collections import OrderedDict
from census.variables.models import Group, GroupVariable, VariableCode
from census.api.models import GeographyItem
from typing import Any, Dict, Generic, List, TypeVar

T = TypeVar("T")


class IDataTransformer(Generic[T]):
    """
    This takes care of converting parsed API data
    into more meaningfully consumable data (e.g., DataFrames)
    """

    @abstractmethod
    def supportedGeographies(self, supportedGeos: OrderedDict[str, GeographyItem]) -> T:
        pass

    @abstractmethod
    def geographyCodes(self, geoCodes: List[List[str]]) -> T:
        pass

    @abstractmethod
    def groups(self, groups: Dict[str, Group]) -> T:
        pass

    @abstractmethod
    def variables(self, variables: List[GroupVariable]) -> T:
        pass

    @abstractmethod
    def stats(
        self,
        results: List[List[Any]],
        queriedVariables: List[VariableCode],
        typeConversions: Dict[str, Any],
    ) -> T:
        pass
