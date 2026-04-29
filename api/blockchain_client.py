"""
Blockchain API client.

Provides helper functions to fetch blockchain data from public APIs.
"""

import requests

BASE_URL = "https://blockchain.info"


def get_latest_block() -> dict:
    """Return the latest block summary."""
    response = requests.get(f"{BASE_URL}/latestblock", timeout=10)
    response.raise_for_status()
    return response.json()


def get_block(block_hash: str) -> dict:
    """Return full details for a block identified by *block_hash*."""
    response = requests.get(
        f"{BASE_URL}/rawblock/{block_hash}", timeout=10
    )
    response.raise_for_status()
    return response.json()


def get_difficulty_history(n_points: int = 100) -> list[dict]:
    """Return the last *n_points* difficulty values as a list of dicts."""
    response = requests.get(
        f"{BASE_URL}/charts/difficulty",
        params={"timespan": "1year", "format": "json", "sampled": "true"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("values", [])[-n_points:]


def get_block_by_height(height: int) -> dict:
    """Return one block found at a given block height."""
    response = requests.get(
        f"{BASE_URL}/block-height/{height}",
        params={"format": "json"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    blocks = data.get("blocks", [])
    if not blocks:
        raise ValueError(f"No block found at height {height}")
    return blocks[0]


def get_latest_height() -> int:
    """Return the latest Bitcoin block height."""
    latest = get_latest_block()
    height = latest.get("height")
    if height is None:
        raise ValueError("Latest block height not available")
    return int(height)


if __name__ == "__main__":
    latest = get_latest_block()
    print("Latest block:")
    print("Height:", latest.get("height"))
    print("Hash:", latest.get("hash"))

    full_block = get_block(latest["hash"])
    print("Difficulty:", full_block.get("difficulty", "Not available in this endpoint"))
    print("Bits:", full_block.get("bits"))
    print("Nonce:", full_block.get("nonce"))
    print("Tx count:", full_block.get("n_tx"))
    

