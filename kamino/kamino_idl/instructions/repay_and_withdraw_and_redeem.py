from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from spl.token.constants import TOKEN_PROGRAM_ID
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class RepayAndWithdrawAndRedeemArgs(typing.TypedDict):
    repay_amount: int
    withdraw_collateral_amount: int


layout = borsh.CStruct(
    "repay_amount" / borsh.U64, "withdraw_collateral_amount" / borsh.U64
)


class RepayAndWithdrawAndRedeemAccounts(typing.TypedDict):
    repay_accounts: RepayAccountsNested
    withdraw_accounts: WithdrawAccountsNested


class RepayAccountsNested(typing.TypedDict):
    owner: Pubkey
    obligation: Pubkey
    lending_market: Pubkey
    repay_reserve: Pubkey
    reserve_liquidity_mint: Pubkey
    reserve_destination_liquidity: Pubkey
    user_source_liquidity: Pubkey
    instruction_sysvar_account: Pubkey


class WithdrawAccountsNested(typing.TypedDict):
    owner: Pubkey
    obligation: Pubkey
    lending_market: Pubkey
    lending_market_authority: Pubkey
    withdraw_reserve: Pubkey
    reserve_liquidity_mint: Pubkey
    reserve_source_collateral: Pubkey
    reserve_collateral_mint: Pubkey
    reserve_liquidity_supply: Pubkey
    user_destination_liquidity: Pubkey
    placeholder_user_destination_collateral: typing.Optional[Pubkey]
    collateral_token_program: Pubkey
    liquidity_token_program: Pubkey
    instruction_sysvar_account: Pubkey


class RepayAccountsNested(typing.TypedDict):
    owner: Pubkey
    obligation: Pubkey
    lending_market: Pubkey
    repay_reserve: Pubkey
    reserve_liquidity_mint: Pubkey
    reserve_destination_liquidity: Pubkey
    user_source_liquidity: Pubkey
    instruction_sysvar_account: Pubkey


def repay_and_withdraw_and_redeem(
    args: RepayAndWithdrawAndRedeemArgs,
    accounts: RepayAndWithdrawAndRedeemAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["repay_accounts"]["owner"],
            is_signer=True,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["obligation"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["lending_market"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["repay_reserve"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["reserve_liquidity_mint"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["reserve_destination_liquidity"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["user_source_liquidity"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["repay_accounts"]["instruction_sysvar_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["owner"],
            is_signer=True,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["obligation"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["lending_market"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["lending_market_authority"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["withdraw_reserve"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["reserve_liquidity_mint"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["reserve_source_collateral"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["reserve_collateral_mint"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["reserve_liquidity_supply"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["user_destination_liquidity"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"][
                "placeholder_user_destination_collateral"
            ],
            is_signer=False,
            is_writable=False,
        )
        if accounts["withdraw_accounts"]["placeholder_user_destination_collateral"]
        else AccountMeta(pubkey=program_id, is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["collateral_token_program"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["liquidity_token_program"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["withdraw_accounts"]["instruction_sysvar_account"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x026\x98\x03\x94`m\xda"
    encoded_args = layout.build(
        {
            "repay_amount": args["repay_amount"],
            "withdraw_collateral_amount": args["withdraw_collateral_amount"],
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
