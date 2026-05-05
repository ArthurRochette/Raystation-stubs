from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Sequence, Tuple, Union

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from raystation.v2025.brachy import BrachyAfterloader, BrachyApplicationSetup, BrachySource
    from raystation.v2025.machine import CyberKnifeNodeSet, TreatmentMachine



class MachineDB:
    def GetAfterloader(self, AfterloaderName: str, LockMode: Literal['NoLock', 'Read', 'Write', 'Snapshot'] = ...) -> BrachyAfterloader:
        """Returns the afterloader with the indicated name. The returned afterloader can be uncommissioned, commissioned or deprecated. If there are multiple matches, the non-deprecated is returned, if no non-deprecated -> the latest deprecated afterloader is returned."""
        ...
    def GetApplicationSetup(self, ApplicationSetupName: str, LockMode: Literal['NoLock', 'Read', 'Write', 'Snapshot'] = ...) -> BrachyApplicationSetup:
        """Returns the application setup with the indicated name. The returned application setup can be uncommissioned, commissioned or deprecated. If there are multiple matches, the non-deprecated is returned, if no non-deprecated -> the latest deprecated application setup is returned."""
        ...
    def GetBrachySource(self, SourceSerialNumber: str, LockMode: Literal['NoLock', 'Read', 'Write', 'Snapshot'] = ...) -> BrachySource:
        """Returns the source with the indicated name. The returned source can be uncommissioned, commissioned or deprecated. If there are multiple matches, the non-deprecated is returned, if no non-deprecated -> the latest deprecated source is returned."""
        ...
    def GetCbctImagingSystemsNameAndCommissionTime(self) -> Dict[str, Any]:
        """Retrieves a list of imaging system that may be assigned to an image set. Only commissioned CBCT imaging machines will be listed."""
        ...
    def GetCtImagingSystemsNameAndCommissionTime(self) -> Dict[str, Any]:
        """Retrieves a list of imaging system that may be assigned to an image set. Only commissioned CT imaging machines will be listed."""
        ...
    def GetCyberKnifeNodeSet(self, machineName: str, machineCommissioningTime: str, nodeSetName: str, rampVersion: str) -> CyberKnifeNodeSet:
        """Returns the CyberKnife node set with the specified name and ramp version referenced by the specified CyberKnife machine."""
        ...
    def GetLatestCyberKnifeMachineParametersInfo(self, machineName: str, machineCommissioningTime: str) -> Any:
        """Returns the latest machine parameters info for the specified CyberKnife machine."""
        ...
    def GetTreatmentMachine(self, machineName: str, lockMode: Optional[Literal['NoLock', 'Read', 'Write', 'Snapshot']] = ...) -> TreatmentMachine:
        """Returns the treatment machine with the indicated name. The returned machine can be"""
        ...
    def QueryCommissionedMachineInfo(self, Filter: Dict[str, Any]) -> List[Any]:
        """Returns info on all commissioned treatment machines in the machine database."""
        ...
    def QueryTemplateMachineInfo(self, Filter: Dict[str, Any]) -> List[Any]:
        """Returns info on all template treatment machines in the machine database."""
        ...
    def QueryUncommissionedMachineInfo(self, Filter: Dict[str, Any]) -> List[Any]:
        """Returns info on all uncommissioned treatment machines in the machine database."""
        ...
