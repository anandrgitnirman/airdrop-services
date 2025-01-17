from airdrop.config import LoyaltyAirdropConfig
from airdrop.constants import USER_REGISTRATION_SIGNATURE_LOYALTY_AIRDROP_FORMAT, USER_CLAIM_SIGNATURE_DEFAULT_FORMAT
from airdrop.processor.base_airdrop import BaseAirdrop


class LoyaltyAirdrop(BaseAirdrop):
    def __init__(self, airdrop_id, airdrop_window_id=None):
        self.airdrop_id = airdrop_id
        self.airdrop_window_id = airdrop_window_id
        self.register_all_window_at_once = True
        self.domain_name = "SingularityNet"
        self.chain_context = {
            "deposit_address": LoyaltyAirdropConfig.deposit_address.value,
            "amount": LoyaltyAirdropConfig.pre_claim_transfer_amount.value["amount"],
            "chain": LoyaltyAirdropConfig.chain.value
        }
        self.is_claim_signature_required = False
        self.reward_processor_name = ""
        self.claim_address = LoyaltyAirdropConfig.claim_address.value

    def format_user_registration_signature_message(self, address, signature_parameters):
        block_number = signature_parameters["block_number"]
        cardano_address = signature_parameters["cardano_address"]
        formatted_message = USER_REGISTRATION_SIGNATURE_LOYALTY_AIRDROP_FORMAT
        formatted_message["message"] = {
            "Airdrop": {
                "airdropId": self.airdrop_id,
                "airdropWindowId": self.airdrop_window_id,
                "blockNumber": block_number,
                "walletAddress": address,
                "cardanoAddress": cardano_address
            },
        }
        formatted_message["domain"]["name"] = self.domain_name
        return formatted_message

    @staticmethod
    def check_user_eligibility(user_eligible_for_given_window, unclaimed_reward):
        if user_eligible_for_given_window:
            return True
        elif unclaimed_reward > 0:
            return True
        return False

    def format_user_claim_signature_message(self, receipt):
        formatted_message = USER_CLAIM_SIGNATURE_DEFAULT_FORMAT
        formatted_message["message"] = {
            "Airdrop": {
                "airdropWindowId": int(self.airdrop_window_id),
                "receipt": receipt
            },
        }
        formatted_message["domain"]["name"] = self.domain_name
        return formatted_message
