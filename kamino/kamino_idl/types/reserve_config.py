from __future__ import annotations
from . import (
    reserve_fees,
    withdrawal_caps,
    token_info,
    borrow_rate_curve,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class ReserveConfigJSON(typing.TypedDict):
    status: int
    asset_tier: int
    host_fixed_interest_rate_bps: int
    reserved2: list[int]
    reserved3: list[int]
    protocol_take_rate_pct: int
    protocol_liquidation_fee_pct: int
    loan_to_value_pct: int
    liquidation_threshold_pct: int
    min_liquidation_bonus_bps: int
    max_liquidation_bonus_bps: int
    bad_debt_liquidation_bonus_bps: int
    deleveraging_margin_call_period_secs: int
    deleveraging_threshold_decrease_bps_per_day: int
    fees: reserve_fees.ReserveFeesJSON
    borrow_rate_curve: borrow_rate_curve.BorrowRateCurveJSON
    borrow_factor_pct: int
    deposit_limit: int
    borrow_limit: int
    token_info: token_info.TokenInfoJSON
    deposit_withdrawal_cap: withdrawal_caps.WithdrawalCapsJSON
    debt_withdrawal_cap: withdrawal_caps.WithdrawalCapsJSON
    elevation_groups: list[int]
    disable_usage_as_coll_outside_emode: int
    utilization_limit_block_borrowing_above_pct: int
    autodeleverage_enabled: int
    reserved1: list[int]
    borrow_limit_outside_elevation_group: int
    borrow_limit_against_this_collateral_in_elevation_group: list[int]
    deleveraging_bonus_increase_bps_per_day: int


@dataclass
class ReserveConfig:
    layout: typing.ClassVar = borsh.CStruct(
        "status" / borsh.U8,
        "asset_tier" / borsh.U8,
        "host_fixed_interest_rate_bps" / borsh.U16,
        "reserved2" / borsh.U8[2],
        "reserved3" / borsh.U8[8],
        "protocol_take_rate_pct" / borsh.U8,
        "protocol_liquidation_fee_pct" / borsh.U8,
        "loan_to_value_pct" / borsh.U8,
        "liquidation_threshold_pct" / borsh.U8,
        "min_liquidation_bonus_bps" / borsh.U16,
        "max_liquidation_bonus_bps" / borsh.U16,
        "bad_debt_liquidation_bonus_bps" / borsh.U16,
        "deleveraging_margin_call_period_secs" / borsh.U64,
        "deleveraging_threshold_decrease_bps_per_day" / borsh.U64,
        "fees" / reserve_fees.ReserveFees.layout,
        "borrow_rate_curve" / borrow_rate_curve.BorrowRateCurve.layout,
        "borrow_factor_pct" / borsh.U64,
        "deposit_limit" / borsh.U64,
        "borrow_limit" / borsh.U64,
        "token_info" / token_info.TokenInfo.layout,
        "deposit_withdrawal_cap" / withdrawal_caps.WithdrawalCaps.layout,
        "debt_withdrawal_cap" / withdrawal_caps.WithdrawalCaps.layout,
        "elevation_groups" / borsh.U8[20],
        "disable_usage_as_coll_outside_emode" / borsh.U8,
        "utilization_limit_block_borrowing_above_pct" / borsh.U8,
        "autodeleverage_enabled" / borsh.U8,
        "reserved1" / borsh.U8[1],
        "borrow_limit_outside_elevation_group" / borsh.U64,
        "borrow_limit_against_this_collateral_in_elevation_group" / borsh.U64[32],
        "deleveraging_bonus_increase_bps_per_day" / borsh.U64,
    )
    status: int
    asset_tier: int
    host_fixed_interest_rate_bps: int
    reserved2: list[int]
    reserved3: list[int]
    protocol_take_rate_pct: int
    protocol_liquidation_fee_pct: int
    loan_to_value_pct: int
    liquidation_threshold_pct: int
    min_liquidation_bonus_bps: int
    max_liquidation_bonus_bps: int
    bad_debt_liquidation_bonus_bps: int
    deleveraging_margin_call_period_secs: int
    deleveraging_threshold_decrease_bps_per_day: int
    fees: reserve_fees.ReserveFees
    borrow_rate_curve: borrow_rate_curve.BorrowRateCurve
    borrow_factor_pct: int
    deposit_limit: int
    borrow_limit: int
    token_info: token_info.TokenInfo
    deposit_withdrawal_cap: withdrawal_caps.WithdrawalCaps
    debt_withdrawal_cap: withdrawal_caps.WithdrawalCaps
    elevation_groups: list[int]
    disable_usage_as_coll_outside_emode: int
    utilization_limit_block_borrowing_above_pct: int
    autodeleverage_enabled: int
    reserved1: list[int]
    borrow_limit_outside_elevation_group: int
    borrow_limit_against_this_collateral_in_elevation_group: list[int]
    deleveraging_bonus_increase_bps_per_day: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "ReserveConfig":
        return cls(
            status=obj.status,
            asset_tier=obj.asset_tier,
            host_fixed_interest_rate_bps=obj.host_fixed_interest_rate_bps,
            reserved2=obj.reserved2,
            reserved3=obj.reserved3,
            protocol_take_rate_pct=obj.protocol_take_rate_pct,
            protocol_liquidation_fee_pct=obj.protocol_liquidation_fee_pct,
            loan_to_value_pct=obj.loan_to_value_pct,
            liquidation_threshold_pct=obj.liquidation_threshold_pct,
            min_liquidation_bonus_bps=obj.min_liquidation_bonus_bps,
            max_liquidation_bonus_bps=obj.max_liquidation_bonus_bps,
            bad_debt_liquidation_bonus_bps=obj.bad_debt_liquidation_bonus_bps,
            deleveraging_margin_call_period_secs=obj.deleveraging_margin_call_period_secs,
            deleveraging_threshold_decrease_bps_per_day=obj.deleveraging_threshold_decrease_bps_per_day,
            fees=reserve_fees.ReserveFees.from_decoded(obj.fees),
            borrow_rate_curve=borrow_rate_curve.BorrowRateCurve.from_decoded(
                obj.borrow_rate_curve
            ),
            borrow_factor_pct=obj.borrow_factor_pct,
            deposit_limit=obj.deposit_limit,
            borrow_limit=obj.borrow_limit,
            token_info=token_info.TokenInfo.from_decoded(obj.token_info),
            deposit_withdrawal_cap=withdrawal_caps.WithdrawalCaps.from_decoded(
                obj.deposit_withdrawal_cap
            ),
            debt_withdrawal_cap=withdrawal_caps.WithdrawalCaps.from_decoded(
                obj.debt_withdrawal_cap
            ),
            elevation_groups=obj.elevation_groups,
            disable_usage_as_coll_outside_emode=obj.disable_usage_as_coll_outside_emode,
            utilization_limit_block_borrowing_above_pct=obj.utilization_limit_block_borrowing_above_pct,
            autodeleverage_enabled=obj.autodeleverage_enabled,
            reserved1=obj.reserved1,
            borrow_limit_outside_elevation_group=obj.borrow_limit_outside_elevation_group,
            borrow_limit_against_this_collateral_in_elevation_group=obj.borrow_limit_against_this_collateral_in_elevation_group,
            deleveraging_bonus_increase_bps_per_day=obj.deleveraging_bonus_increase_bps_per_day,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "status": self.status,
            "asset_tier": self.asset_tier,
            "host_fixed_interest_rate_bps": self.host_fixed_interest_rate_bps,
            "reserved2": self.reserved2,
            "reserved3": self.reserved3,
            "protocol_take_rate_pct": self.protocol_take_rate_pct,
            "protocol_liquidation_fee_pct": self.protocol_liquidation_fee_pct,
            "loan_to_value_pct": self.loan_to_value_pct,
            "liquidation_threshold_pct": self.liquidation_threshold_pct,
            "min_liquidation_bonus_bps": self.min_liquidation_bonus_bps,
            "max_liquidation_bonus_bps": self.max_liquidation_bonus_bps,
            "bad_debt_liquidation_bonus_bps": self.bad_debt_liquidation_bonus_bps,
            "deleveraging_margin_call_period_secs": self.deleveraging_margin_call_period_secs,
            "deleveraging_threshold_decrease_bps_per_day": self.deleveraging_threshold_decrease_bps_per_day,
            "fees": self.fees.to_encodable(),
            "borrow_rate_curve": self.borrow_rate_curve.to_encodable(),
            "borrow_factor_pct": self.borrow_factor_pct,
            "deposit_limit": self.deposit_limit,
            "borrow_limit": self.borrow_limit,
            "token_info": self.token_info.to_encodable(),
            "deposit_withdrawal_cap": self.deposit_withdrawal_cap.to_encodable(),
            "debt_withdrawal_cap": self.debt_withdrawal_cap.to_encodable(),
            "elevation_groups": self.elevation_groups,
            "disable_usage_as_coll_outside_emode": self.disable_usage_as_coll_outside_emode,
            "utilization_limit_block_borrowing_above_pct": self.utilization_limit_block_borrowing_above_pct,
            "autodeleverage_enabled": self.autodeleverage_enabled,
            "reserved1": self.reserved1,
            "borrow_limit_outside_elevation_group": self.borrow_limit_outside_elevation_group,
            "borrow_limit_against_this_collateral_in_elevation_group": self.borrow_limit_against_this_collateral_in_elevation_group,
            "deleveraging_bonus_increase_bps_per_day": self.deleveraging_bonus_increase_bps_per_day,
        }

    def to_json(self) -> ReserveConfigJSON:
        return {
            "status": self.status,
            "asset_tier": self.asset_tier,
            "host_fixed_interest_rate_bps": self.host_fixed_interest_rate_bps,
            "reserved2": self.reserved2,
            "reserved3": self.reserved3,
            "protocol_take_rate_pct": self.protocol_take_rate_pct,
            "protocol_liquidation_fee_pct": self.protocol_liquidation_fee_pct,
            "loan_to_value_pct": self.loan_to_value_pct,
            "liquidation_threshold_pct": self.liquidation_threshold_pct,
            "min_liquidation_bonus_bps": self.min_liquidation_bonus_bps,
            "max_liquidation_bonus_bps": self.max_liquidation_bonus_bps,
            "bad_debt_liquidation_bonus_bps": self.bad_debt_liquidation_bonus_bps,
            "deleveraging_margin_call_period_secs": self.deleveraging_margin_call_period_secs,
            "deleveraging_threshold_decrease_bps_per_day": self.deleveraging_threshold_decrease_bps_per_day,
            "fees": self.fees.to_json(),
            "borrow_rate_curve": self.borrow_rate_curve.to_json(),
            "borrow_factor_pct": self.borrow_factor_pct,
            "deposit_limit": self.deposit_limit,
            "borrow_limit": self.borrow_limit,
            "token_info": self.token_info.to_json(),
            "deposit_withdrawal_cap": self.deposit_withdrawal_cap.to_json(),
            "debt_withdrawal_cap": self.debt_withdrawal_cap.to_json(),
            "elevation_groups": self.elevation_groups,
            "disable_usage_as_coll_outside_emode": self.disable_usage_as_coll_outside_emode,
            "utilization_limit_block_borrowing_above_pct": self.utilization_limit_block_borrowing_above_pct,
            "autodeleverage_enabled": self.autodeleverage_enabled,
            "reserved1": self.reserved1,
            "borrow_limit_outside_elevation_group": self.borrow_limit_outside_elevation_group,
            "borrow_limit_against_this_collateral_in_elevation_group": self.borrow_limit_against_this_collateral_in_elevation_group,
            "deleveraging_bonus_increase_bps_per_day": self.deleveraging_bonus_increase_bps_per_day,
        }

    @classmethod
    def from_json(cls, obj: ReserveConfigJSON) -> "ReserveConfig":
        return cls(
            status=obj["status"],
            asset_tier=obj["asset_tier"],
            host_fixed_interest_rate_bps=obj["host_fixed_interest_rate_bps"],
            reserved2=obj["reserved2"],
            reserved3=obj["reserved3"],
            protocol_take_rate_pct=obj["protocol_take_rate_pct"],
            protocol_liquidation_fee_pct=obj["protocol_liquidation_fee_pct"],
            loan_to_value_pct=obj["loan_to_value_pct"],
            liquidation_threshold_pct=obj["liquidation_threshold_pct"],
            min_liquidation_bonus_bps=obj["min_liquidation_bonus_bps"],
            max_liquidation_bonus_bps=obj["max_liquidation_bonus_bps"],
            bad_debt_liquidation_bonus_bps=obj["bad_debt_liquidation_bonus_bps"],
            deleveraging_margin_call_period_secs=obj[
                "deleveraging_margin_call_period_secs"
            ],
            deleveraging_threshold_decrease_bps_per_day=obj[
                "deleveraging_threshold_decrease_bps_per_day"
            ],
            fees=reserve_fees.ReserveFees.from_json(obj["fees"]),
            borrow_rate_curve=borrow_rate_curve.BorrowRateCurve.from_json(
                obj["borrow_rate_curve"]
            ),
            borrow_factor_pct=obj["borrow_factor_pct"],
            deposit_limit=obj["deposit_limit"],
            borrow_limit=obj["borrow_limit"],
            token_info=token_info.TokenInfo.from_json(obj["token_info"]),
            deposit_withdrawal_cap=withdrawal_caps.WithdrawalCaps.from_json(
                obj["deposit_withdrawal_cap"]
            ),
            debt_withdrawal_cap=withdrawal_caps.WithdrawalCaps.from_json(
                obj["debt_withdrawal_cap"]
            ),
            elevation_groups=obj["elevation_groups"],
            disable_usage_as_coll_outside_emode=obj[
                "disable_usage_as_coll_outside_emode"
            ],
            utilization_limit_block_borrowing_above_pct=obj[
                "utilization_limit_block_borrowing_above_pct"
            ],
            autodeleverage_enabled=obj["autodeleverage_enabled"],
            reserved1=obj["reserved1"],
            borrow_limit_outside_elevation_group=obj[
                "borrow_limit_outside_elevation_group"
            ],
            borrow_limit_against_this_collateral_in_elevation_group=obj[
                "borrow_limit_against_this_collateral_in_elevation_group"
            ],
            deleveraging_bonus_increase_bps_per_day=obj[
                "deleveraging_bonus_increase_bps_per_day"
            ],
        )
