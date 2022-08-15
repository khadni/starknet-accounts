import asyncio
import sys
import json

sys.path.append('./')

from console import blue_strong, blue, red
from utils import deploy_account, print_n_wait, get_evaluator, fund_account, get_client
from starkware.starknet.public.abi import get_selector_from_name

with open("./hints.json", "r") as f:
  data = json.load(f)

async def main():
    blue_strong.print("Your mission:")
    # TODO: fill out the steps for the student to take 

    #
    # Initialize StarkNet Client
    #
    client = get_client()

    #
    # Compile and Deploy `factory.cairo`
    #
    factory, factory_addr = await deploy_account(client=client, contract_path=data['FACTORY'])

    #
    # Transfer ETH to pay for fees
    #
    reward_account = await fund_account(factory_addr)
    if reward_account == "":
      red.print("Account must have ETH to cover transaction fees")
      return

    #
    # Check answer against 'evaluator.cairo'
    #    
    evaluator, evaluator_address = await get_evaluator(client)

    #
    # TODO: deploy a contract with syscall from top level account contract
    # only views that adheres to evaluator interface 
    #

asyncio.run(main())
