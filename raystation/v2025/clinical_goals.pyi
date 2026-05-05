from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Sequence, Tuple, Union

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from raystation.v2025.beam import BeamFractionDose
    from raystation.v2025.dose import DoseBasedRoiFunction
    from raystation.v2025.ml import MachineLearningDose
    from raystation.v2025.patient_db_types import AuxiliaryDataInDoseGrid, CompositeDose, CompositeFunction, EQD2Dose, FractionDose, GoalEvaluation, MappedDose, PredictedMachineLearningDose



class ClinicalGoal:
    @property
    def ForDoseDistribution(self) -> Union[AuxiliaryDataInDoseGrid, BeamFractionDose, CompositeDose, EQD2Dose, FractionDose, MachineLearningDose, MappedDose, PredictedMachineLearningDose]: ...
    @ForDoseDistribution.setter
    def ForDoseDistribution(self, value: Union[AuxiliaryDataInDoseGrid, BeamFractionDose, CompositeDose, EQD2Dose, FractionDose, MachineLearningDose, MappedDose, PredictedMachineLearningDose]) -> None: ...
    @property
    def ForFunction(self) -> Union[CompositeFunction, DoseBasedRoiFunction]: ...
    @ForFunction.setter
    def ForFunction(self, value: Union[CompositeFunction, DoseBasedRoiFunction]) -> None: ...
    @property
    def GoalEvaluation(self) -> GoalEvaluation: ...
    @GoalEvaluation.setter
    def GoalEvaluation(self, value: GoalEvaluation) -> None: ...
