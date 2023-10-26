from typing import Dict, Any


class GymClassCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details
