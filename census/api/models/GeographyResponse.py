from typing import List


class GeographyResponseItem:
    name: str
    geoLevelDisplay: str
    referenceData: str
    requires: list[str] = []
    wildcard: List[str] = []
    optionalWithWCFor: str = ''

    def __init__(self, jsonRes: dict) -> None:
        self.__dict__ = jsonRes


class GeographyResponse:
    fips: List[GeographyResponseItem] = []

    def __init__(self, fips: List[GeographyResponseItem], **_) -> None:
        for fip in fips:
            self.fips.append(GeographyResponseItem(fip))
