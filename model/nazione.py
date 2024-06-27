from dataclasses import dataclass


@dataclass
class Nazione:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash((self.StateAbb, self.CCode))
