from dataclasses import dataclass


@dataclass
class Confine:
    conttype: int
    dyad: int
    state1ab: str
    state1no: int
    state2ab: str
    state2no: int
    version: float
    year: int