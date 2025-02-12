from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class MarkObligationForDeleveragingArgs(typing.TypedDict):
    autodeleverage_target_ltv_pct: int


layout = borsh.CStruct("autodeleverage_target_ltv_pct" / borsh.U8)


class MarkObligationForDeleveragingAccounts(typing.TypedDict):
    risk_council: Pubkey
    obligation: Pubkey
    lending_market: Pubkey


def mark_obligation_for_deleveraging(
    args: MarkObligationForDeleveragingArgs,
    accounts: MarkObligationForDeleveragingAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["risk_council"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["obligation"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["lending_market"], is_signer=False, is_writable=False
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xa4#\xb6\x13\x00t\xf3\x7f"
    encoded_args = layout.build(
        {
            "autodeleverage_target_ltv_pct": args["autodeleverage_target_ltv_pct"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
