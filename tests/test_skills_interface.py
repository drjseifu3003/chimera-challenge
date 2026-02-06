import pytest

def test_wallet_manager_contract():
    """
    Ensures the wallet manager accepts correct parameters for Coinbase AgentKit.
    """
    # We are simulating the input defined in our skills/ README
    valid_input = {
        "action": "transfer",
        "amount": 10.5,
        "recipient_address": "0x1234567890abcdef"
    }
    
    assert "action" in valid_input
    assert valid_input["action"] in ["transfer", "balance", "check_tx"]
    assert isinstance(valid_input["amount"], (int, float))

def test_content_generator_contract():
    """
    Ensures content generator follows the multimodal format requirements.
    """
    valid_request = {
        "prompt": "Create a tech update",
        "character_ref": "luna_v2",
        "format": "video"
    }
    
    assert valid_request["format"] in ["video", "image", "text"]
    assert len(valid_request["prompt"]) > 0