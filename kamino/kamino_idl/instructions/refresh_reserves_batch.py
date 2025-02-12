from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class RefreshReservesBatchArgs(typing.TypedDict):
    skip_price_updates: bool


layout = borsh.CStruct("skip_price_updates" / borsh.Bool)


def refresh_reserves_batch(
    args: RefreshReservesBatchArgs,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = []
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x90n\x1ag\xa2\xcc\xfc\x93"
    encoded_args = layout.build(
        {
            "skip_price_updates": args["skip_price_updates"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
