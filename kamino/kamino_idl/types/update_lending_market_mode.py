from __future__ import annotations
import typing
from dataclasses import dataclass
from anchorpy.borsh_extension import EnumForCodegen
import borsh_construct as borsh


class UpdateOwnerJSON(typing.TypedDict):
    kind: typing.Literal["UpdateOwner"]


class UpdateEmergencyModeJSON(typing.TypedDict):
    kind: typing.Literal["UpdateEmergencyMode"]


class UpdateLiquidationCloseFactorJSON(typing.TypedDict):
    kind: typing.Literal["UpdateLiquidationCloseFactor"]


class UpdateLiquidationMaxValueJSON(typing.TypedDict):
    kind: typing.Literal["UpdateLiquidationMaxValue"]


class DeprecatedUpdateGlobalUnhealthyBorrowJSON(typing.TypedDict):
    kind: typing.Literal["DeprecatedUpdateGlobalUnhealthyBorrow"]


class UpdateGlobalAllowedBorrowJSON(typing.TypedDict):
    kind: typing.Literal["UpdateGlobalAllowedBorrow"]


class UpdateRiskCouncilJSON(typing.TypedDict):
    kind: typing.Literal["UpdateRiskCouncil"]


class UpdateMinFullLiquidationThresholdJSON(typing.TypedDict):
    kind: typing.Literal["UpdateMinFullLiquidationThreshold"]


class UpdateInsolvencyRiskLtvJSON(typing.TypedDict):
    kind: typing.Literal["UpdateInsolvencyRiskLtv"]


class UpdateElevationGroupJSON(typing.TypedDict):
    kind: typing.Literal["UpdateElevationGroup"]


class UpdateReferralFeeBpsJSON(typing.TypedDict):
    kind: typing.Literal["UpdateReferralFeeBps"]


class DeprecatedUpdateMultiplierPointsJSON(typing.TypedDict):
    kind: typing.Literal["DeprecatedUpdateMultiplierPoints"]


class UpdatePriceRefreshTriggerToMaxAgePctJSON(typing.TypedDict):
    kind: typing.Literal["UpdatePriceRefreshTriggerToMaxAgePct"]


class UpdateAutodeleverageEnabledJSON(typing.TypedDict):
    kind: typing.Literal["UpdateAutodeleverageEnabled"]


class UpdateBorrowingDisabledJSON(typing.TypedDict):
    kind: typing.Literal["UpdateBorrowingDisabled"]


class UpdateMinNetValueObligationPostActionJSON(typing.TypedDict):
    kind: typing.Literal["UpdateMinNetValueObligationPostAction"]


class UpdateMinValueLtvSkipPriorityLiqCheckJSON(typing.TypedDict):
    kind: typing.Literal["UpdateMinValueLtvSkipPriorityLiqCheck"]


class UpdateMinValueBfSkipPriorityLiqCheckJSON(typing.TypedDict):
    kind: typing.Literal["UpdateMinValueBfSkipPriorityLiqCheck"]


class UpdatePaddingFieldsJSON(typing.TypedDict):
    kind: typing.Literal["UpdatePaddingFields"]


class UpdateNameJSON(typing.TypedDict):
    kind: typing.Literal["UpdateName"]


class UpdateIndividualAutodeleverageMarginCallPeriodSecsJSON(typing.TypedDict):
    kind: typing.Literal["UpdateIndividualAutodeleverageMarginCallPeriodSecs"]


@dataclass
class UpdateOwner:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "UpdateOwner"

    @classmethod
    def to_json(cls) -> UpdateOwnerJSON:
        return UpdateOwnerJSON(
            kind="UpdateOwner",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateOwner": {},
        }


@dataclass
class UpdateEmergencyMode:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "UpdateEmergencyMode"

    @classmethod
    def to_json(cls) -> UpdateEmergencyModeJSON:
        return UpdateEmergencyModeJSON(
            kind="UpdateEmergencyMode",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateEmergencyMode": {},
        }


@dataclass
class UpdateLiquidationCloseFactor:
    discriminator: typing.ClassVar = 2
    kind: typing.ClassVar = "UpdateLiquidationCloseFactor"

    @classmethod
    def to_json(cls) -> UpdateLiquidationCloseFactorJSON:
        return UpdateLiquidationCloseFactorJSON(
            kind="UpdateLiquidationCloseFactor",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateLiquidationCloseFactor": {},
        }


@dataclass
class UpdateLiquidationMaxValue:
    discriminator: typing.ClassVar = 3
    kind: typing.ClassVar = "UpdateLiquidationMaxValue"

    @classmethod
    def to_json(cls) -> UpdateLiquidationMaxValueJSON:
        return UpdateLiquidationMaxValueJSON(
            kind="UpdateLiquidationMaxValue",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateLiquidationMaxValue": {},
        }


@dataclass
class DeprecatedUpdateGlobalUnhealthyBorrow:
    discriminator: typing.ClassVar = 4
    kind: typing.ClassVar = "DeprecatedUpdateGlobalUnhealthyBorrow"

    @classmethod
    def to_json(cls) -> DeprecatedUpdateGlobalUnhealthyBorrowJSON:
        return DeprecatedUpdateGlobalUnhealthyBorrowJSON(
            kind="DeprecatedUpdateGlobalUnhealthyBorrow",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "DeprecatedUpdateGlobalUnhealthyBorrow": {},
        }


@dataclass
class UpdateGlobalAllowedBorrow:
    discriminator: typing.ClassVar = 5
    kind: typing.ClassVar = "UpdateGlobalAllowedBorrow"

    @classmethod
    def to_json(cls) -> UpdateGlobalAllowedBorrowJSON:
        return UpdateGlobalAllowedBorrowJSON(
            kind="UpdateGlobalAllowedBorrow",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateGlobalAllowedBorrow": {},
        }


@dataclass
class UpdateRiskCouncil:
    discriminator: typing.ClassVar = 6
    kind: typing.ClassVar = "UpdateRiskCouncil"

    @classmethod
    def to_json(cls) -> UpdateRiskCouncilJSON:
        return UpdateRiskCouncilJSON(
            kind="UpdateRiskCouncil",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateRiskCouncil": {},
        }


@dataclass
class UpdateMinFullLiquidationThreshold:
    discriminator: typing.ClassVar = 7
    kind: typing.ClassVar = "UpdateMinFullLiquidationThreshold"

    @classmethod
    def to_json(cls) -> UpdateMinFullLiquidationThresholdJSON:
        return UpdateMinFullLiquidationThresholdJSON(
            kind="UpdateMinFullLiquidationThreshold",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateMinFullLiquidationThreshold": {},
        }


@dataclass
class UpdateInsolvencyRiskLtv:
    discriminator: typing.ClassVar = 8
    kind: typing.ClassVar = "UpdateInsolvencyRiskLtv"

    @classmethod
    def to_json(cls) -> UpdateInsolvencyRiskLtvJSON:
        return UpdateInsolvencyRiskLtvJSON(
            kind="UpdateInsolvencyRiskLtv",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateInsolvencyRiskLtv": {},
        }


@dataclass
class UpdateElevationGroup:
    discriminator: typing.ClassVar = 9
    kind: typing.ClassVar = "UpdateElevationGroup"

    @classmethod
    def to_json(cls) -> UpdateElevationGroupJSON:
        return UpdateElevationGroupJSON(
            kind="UpdateElevationGroup",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateElevationGroup": {},
        }


@dataclass
class UpdateReferralFeeBps:
    discriminator: typing.ClassVar = 10
    kind: typing.ClassVar = "UpdateReferralFeeBps"

    @classmethod
    def to_json(cls) -> UpdateReferralFeeBpsJSON:
        return UpdateReferralFeeBpsJSON(
            kind="UpdateReferralFeeBps",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateReferralFeeBps": {},
        }


@dataclass
class DeprecatedUpdateMultiplierPoints:
    discriminator: typing.ClassVar = 11
    kind: typing.ClassVar = "DeprecatedUpdateMultiplierPoints"

    @classmethod
    def to_json(cls) -> DeprecatedUpdateMultiplierPointsJSON:
        return DeprecatedUpdateMultiplierPointsJSON(
            kind="DeprecatedUpdateMultiplierPoints",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "DeprecatedUpdateMultiplierPoints": {},
        }


@dataclass
class UpdatePriceRefreshTriggerToMaxAgePct:
    discriminator: typing.ClassVar = 12
    kind: typing.ClassVar = "UpdatePriceRefreshTriggerToMaxAgePct"

    @classmethod
    def to_json(cls) -> UpdatePriceRefreshTriggerToMaxAgePctJSON:
        return UpdatePriceRefreshTriggerToMaxAgePctJSON(
            kind="UpdatePriceRefreshTriggerToMaxAgePct",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdatePriceRefreshTriggerToMaxAgePct": {},
        }


@dataclass
class UpdateAutodeleverageEnabled:
    discriminator: typing.ClassVar = 13
    kind: typing.ClassVar = "UpdateAutodeleverageEnabled"

    @classmethod
    def to_json(cls) -> UpdateAutodeleverageEnabledJSON:
        return UpdateAutodeleverageEnabledJSON(
            kind="UpdateAutodeleverageEnabled",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateAutodeleverageEnabled": {},
        }


@dataclass
class UpdateBorrowingDisabled:
    discriminator: typing.ClassVar = 14
    kind: typing.ClassVar = "UpdateBorrowingDisabled"

    @classmethod
    def to_json(cls) -> UpdateBorrowingDisabledJSON:
        return UpdateBorrowingDisabledJSON(
            kind="UpdateBorrowingDisabled",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateBorrowingDisabled": {},
        }


@dataclass
class UpdateMinNetValueObligationPostAction:
    discriminator: typing.ClassVar = 15
    kind: typing.ClassVar = "UpdateMinNetValueObligationPostAction"

    @classmethod
    def to_json(cls) -> UpdateMinNetValueObligationPostActionJSON:
        return UpdateMinNetValueObligationPostActionJSON(
            kind="UpdateMinNetValueObligationPostAction",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateMinNetValueObligationPostAction": {},
        }


@dataclass
class UpdateMinValueLtvSkipPriorityLiqCheck:
    discriminator: typing.ClassVar = 16
    kind: typing.ClassVar = "UpdateMinValueLtvSkipPriorityLiqCheck"

    @classmethod
    def to_json(cls) -> UpdateMinValueLtvSkipPriorityLiqCheckJSON:
        return UpdateMinValueLtvSkipPriorityLiqCheckJSON(
            kind="UpdateMinValueLtvSkipPriorityLiqCheck",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateMinValueLtvSkipPriorityLiqCheck": {},
        }


@dataclass
class UpdateMinValueBfSkipPriorityLiqCheck:
    discriminator: typing.ClassVar = 17
    kind: typing.ClassVar = "UpdateMinValueBfSkipPriorityLiqCheck"

    @classmethod
    def to_json(cls) -> UpdateMinValueBfSkipPriorityLiqCheckJSON:
        return UpdateMinValueBfSkipPriorityLiqCheckJSON(
            kind="UpdateMinValueBfSkipPriorityLiqCheck",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateMinValueBfSkipPriorityLiqCheck": {},
        }


@dataclass
class UpdatePaddingFields:
    discriminator: typing.ClassVar = 18
    kind: typing.ClassVar = "UpdatePaddingFields"

    @classmethod
    def to_json(cls) -> UpdatePaddingFieldsJSON:
        return UpdatePaddingFieldsJSON(
            kind="UpdatePaddingFields",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdatePaddingFields": {},
        }


@dataclass
class UpdateName:
    discriminator: typing.ClassVar = 19
    kind: typing.ClassVar = "UpdateName"

    @classmethod
    def to_json(cls) -> UpdateNameJSON:
        return UpdateNameJSON(
            kind="UpdateName",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateName": {},
        }


@dataclass
class UpdateIndividualAutodeleverageMarginCallPeriodSecs:
    discriminator: typing.ClassVar = 20
    kind: typing.ClassVar = "UpdateIndividualAutodeleverageMarginCallPeriodSecs"

    @classmethod
    def to_json(cls) -> UpdateIndividualAutodeleverageMarginCallPeriodSecsJSON:
        return UpdateIndividualAutodeleverageMarginCallPeriodSecsJSON(
            kind="UpdateIndividualAutodeleverageMarginCallPeriodSecs",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "UpdateIndividualAutodeleverageMarginCallPeriodSecs": {},
        }


UpdateLendingMarketModeKind = typing.Union[
    UpdateOwner,
    UpdateEmergencyMode,
    UpdateLiquidationCloseFactor,
    UpdateLiquidationMaxValue,
    DeprecatedUpdateGlobalUnhealthyBorrow,
    UpdateGlobalAllowedBorrow,
    UpdateRiskCouncil,
    UpdateMinFullLiquidationThreshold,
    UpdateInsolvencyRiskLtv,
    UpdateElevationGroup,
    UpdateReferralFeeBps,
    DeprecatedUpdateMultiplierPoints,
    UpdatePriceRefreshTriggerToMaxAgePct,
    UpdateAutodeleverageEnabled,
    UpdateBorrowingDisabled,
    UpdateMinNetValueObligationPostAction,
    UpdateMinValueLtvSkipPriorityLiqCheck,
    UpdateMinValueBfSkipPriorityLiqCheck,
    UpdatePaddingFields,
    UpdateName,
    UpdateIndividualAutodeleverageMarginCallPeriodSecs,
]
UpdateLendingMarketModeJSON = typing.Union[
    UpdateOwnerJSON,
    UpdateEmergencyModeJSON,
    UpdateLiquidationCloseFactorJSON,
    UpdateLiquidationMaxValueJSON,
    DeprecatedUpdateGlobalUnhealthyBorrowJSON,
    UpdateGlobalAllowedBorrowJSON,
    UpdateRiskCouncilJSON,
    UpdateMinFullLiquidationThresholdJSON,
    UpdateInsolvencyRiskLtvJSON,
    UpdateElevationGroupJSON,
    UpdateReferralFeeBpsJSON,
    DeprecatedUpdateMultiplierPointsJSON,
    UpdatePriceRefreshTriggerToMaxAgePctJSON,
    UpdateAutodeleverageEnabledJSON,
    UpdateBorrowingDisabledJSON,
    UpdateMinNetValueObligationPostActionJSON,
    UpdateMinValueLtvSkipPriorityLiqCheckJSON,
    UpdateMinValueBfSkipPriorityLiqCheckJSON,
    UpdatePaddingFieldsJSON,
    UpdateNameJSON,
    UpdateIndividualAutodeleverageMarginCallPeriodSecsJSON,
]


def from_decoded(obj: dict) -> UpdateLendingMarketModeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "UpdateOwner" in obj:
        return UpdateOwner()
    if "UpdateEmergencyMode" in obj:
        return UpdateEmergencyMode()
    if "UpdateLiquidationCloseFactor" in obj:
        return UpdateLiquidationCloseFactor()
    if "UpdateLiquidationMaxValue" in obj:
        return UpdateLiquidationMaxValue()
    if "DeprecatedUpdateGlobalUnhealthyBorrow" in obj:
        return DeprecatedUpdateGlobalUnhealthyBorrow()
    if "UpdateGlobalAllowedBorrow" in obj:
        return UpdateGlobalAllowedBorrow()
    if "UpdateRiskCouncil" in obj:
        return UpdateRiskCouncil()
    if "UpdateMinFullLiquidationThreshold" in obj:
        return UpdateMinFullLiquidationThreshold()
    if "UpdateInsolvencyRiskLtv" in obj:
        return UpdateInsolvencyRiskLtv()
    if "UpdateElevationGroup" in obj:
        return UpdateElevationGroup()
    if "UpdateReferralFeeBps" in obj:
        return UpdateReferralFeeBps()
    if "DeprecatedUpdateMultiplierPoints" in obj:
        return DeprecatedUpdateMultiplierPoints()
    if "UpdatePriceRefreshTriggerToMaxAgePct" in obj:
        return UpdatePriceRefreshTriggerToMaxAgePct()
    if "UpdateAutodeleverageEnabled" in obj:
        return UpdateAutodeleverageEnabled()
    if "UpdateBorrowingDisabled" in obj:
        return UpdateBorrowingDisabled()
    if "UpdateMinNetValueObligationPostAction" in obj:
        return UpdateMinNetValueObligationPostAction()
    if "UpdateMinValueLtvSkipPriorityLiqCheck" in obj:
        return UpdateMinValueLtvSkipPriorityLiqCheck()
    if "UpdateMinValueBfSkipPriorityLiqCheck" in obj:
        return UpdateMinValueBfSkipPriorityLiqCheck()
    if "UpdatePaddingFields" in obj:
        return UpdatePaddingFields()
    if "UpdateName" in obj:
        return UpdateName()
    if "UpdateIndividualAutodeleverageMarginCallPeriodSecs" in obj:
        return UpdateIndividualAutodeleverageMarginCallPeriodSecs()
    raise ValueError("Invalid enum object")


def from_json(obj: UpdateLendingMarketModeJSON) -> UpdateLendingMarketModeKind:
    if obj["kind"] == "UpdateOwner":
        return UpdateOwner()
    if obj["kind"] == "UpdateEmergencyMode":
        return UpdateEmergencyMode()
    if obj["kind"] == "UpdateLiquidationCloseFactor":
        return UpdateLiquidationCloseFactor()
    if obj["kind"] == "UpdateLiquidationMaxValue":
        return UpdateLiquidationMaxValue()
    if obj["kind"] == "DeprecatedUpdateGlobalUnhealthyBorrow":
        return DeprecatedUpdateGlobalUnhealthyBorrow()
    if obj["kind"] == "UpdateGlobalAllowedBorrow":
        return UpdateGlobalAllowedBorrow()
    if obj["kind"] == "UpdateRiskCouncil":
        return UpdateRiskCouncil()
    if obj["kind"] == "UpdateMinFullLiquidationThreshold":
        return UpdateMinFullLiquidationThreshold()
    if obj["kind"] == "UpdateInsolvencyRiskLtv":
        return UpdateInsolvencyRiskLtv()
    if obj["kind"] == "UpdateElevationGroup":
        return UpdateElevationGroup()
    if obj["kind"] == "UpdateReferralFeeBps":
        return UpdateReferralFeeBps()
    if obj["kind"] == "DeprecatedUpdateMultiplierPoints":
        return DeprecatedUpdateMultiplierPoints()
    if obj["kind"] == "UpdatePriceRefreshTriggerToMaxAgePct":
        return UpdatePriceRefreshTriggerToMaxAgePct()
    if obj["kind"] == "UpdateAutodeleverageEnabled":
        return UpdateAutodeleverageEnabled()
    if obj["kind"] == "UpdateBorrowingDisabled":
        return UpdateBorrowingDisabled()
    if obj["kind"] == "UpdateMinNetValueObligationPostAction":
        return UpdateMinNetValueObligationPostAction()
    if obj["kind"] == "UpdateMinValueLtvSkipPriorityLiqCheck":
        return UpdateMinValueLtvSkipPriorityLiqCheck()
    if obj["kind"] == "UpdateMinValueBfSkipPriorityLiqCheck":
        return UpdateMinValueBfSkipPriorityLiqCheck()
    if obj["kind"] == "UpdatePaddingFields":
        return UpdatePaddingFields()
    if obj["kind"] == "UpdateName":
        return UpdateName()
    if obj["kind"] == "UpdateIndividualAutodeleverageMarginCallPeriodSecs":
        return UpdateIndividualAutodeleverageMarginCallPeriodSecs()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
    "UpdateOwner" / borsh.CStruct(),
    "UpdateEmergencyMode" / borsh.CStruct(),
    "UpdateLiquidationCloseFactor" / borsh.CStruct(),
    "UpdateLiquidationMaxValue" / borsh.CStruct(),
    "DeprecatedUpdateGlobalUnhealthyBorrow" / borsh.CStruct(),
    "UpdateGlobalAllowedBorrow" / borsh.CStruct(),
    "UpdateRiskCouncil" / borsh.CStruct(),
    "UpdateMinFullLiquidationThreshold" / borsh.CStruct(),
    "UpdateInsolvencyRiskLtv" / borsh.CStruct(),
    "UpdateElevationGroup" / borsh.CStruct(),
    "UpdateReferralFeeBps" / borsh.CStruct(),
    "DeprecatedUpdateMultiplierPoints" / borsh.CStruct(),
    "UpdatePriceRefreshTriggerToMaxAgePct" / borsh.CStruct(),
    "UpdateAutodeleverageEnabled" / borsh.CStruct(),
    "UpdateBorrowingDisabled" / borsh.CStruct(),
    "UpdateMinNetValueObligationPostAction" / borsh.CStruct(),
    "UpdateMinValueLtvSkipPriorityLiqCheck" / borsh.CStruct(),
    "UpdateMinValueBfSkipPriorityLiqCheck" / borsh.CStruct(),
    "UpdatePaddingFields" / borsh.CStruct(),
    "UpdateName" / borsh.CStruct(),
    "UpdateIndividualAutodeleverageMarginCallPeriodSecs" / borsh.CStruct(),
)
