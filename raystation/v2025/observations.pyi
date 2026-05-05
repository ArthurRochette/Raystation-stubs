from __future__ import annotations

from raystation.v2025._collection import ScriptObjectCollection
from typing import Any, Dict, List, Literal, Optional, Sequence, Tuple, Union

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from raystation.v2025.patient_db_types import MedicationStatement, Vitals



class Observations:
    @property
    def PatientAggregateId(self) -> str: ...
    @property
    def MedicationStatements(self) -> ScriptObjectCollection[MedicationStatement]: ...
    @MedicationStatements.setter
    def MedicationStatements(self, value: List[MedicationStatement]) -> None: ...
    @property
    def Vitals(self) -> ScriptObjectCollection[Vitals]: ...
    @Vitals.setter
    def Vitals(self, value: List[Vitals]) -> None: ...
