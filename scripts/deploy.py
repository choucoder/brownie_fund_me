from brownie import FundMe, network, config, MockV3Aggregator 
from scripts.helpers import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # Pass the price feed address to our fundme contract

    # If we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config['networks'][network.show_active()].get('verify')
    )
    print(f"Contract deployed to {fund_me.address}")
    print(len(FundMe))

    return fund_me

def main():
    deploy_fund_me()