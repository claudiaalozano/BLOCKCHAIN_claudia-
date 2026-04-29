"""Blockchain API client with retries and fallback providers."""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URLS = [
    "https://blockstream.info/api",
    "https://mempool.space/api",
]
TIMEOUT = 10


def _build_session() -> requests.Session:
    session = requests.Session()

    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=0.8,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=frozenset(["GET"]),
        raise_on_status=False,
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(
        {"User-Agent": "CryptoChainAnalyzerDashboard/1.0"}
    )
    return session


SESSION = _build_session()


def _get_json(path: str):
    last_error = None

    for base_url in BASE_URLS:
        try:
            response = SESSION.get(f"{base_url}{path}", timeout=TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            last_error = exc

    raise RuntimeError(f"All API providers failed: {last_error}")


def _get_text(path: str) -> str:
    last_error = None

    for base_url in BASE_URLS:
        try:
            response = SESSION.get(f"{base_url}{path}", timeout=TIMEOUT)
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as exc:
            last_error = exc

    raise RuntimeError(f"All API providers failed: {last_error}")


def get_latest_block():
    """Return latest block hash and height."""
    return {
        "hash": _get_text("/blocks/tip/hash"),
        "height": int(_get_text("/blocks/tip/height")),
    }


def get_block(block_hash: str):
    """Return a block normalized to the fields used by the dashboard."""
    data = _get_json(f"/block/{block_hash}")

    previous_hash = data.get("previousblockhash")
    merkle_root = data["merkle_root"]
    timestamp = data["timestamp"]
    tx_count = data["tx_count"]

    return {
        "hash": data["id"],
        "id": data["id"],
        "height": data["height"],
        "ver": data["version"],
        "version": data["version"],
        "prev_block": previous_hash,
        "previousblockhash": previous_hash,
        "mrkl_root": merkle_root,
        "merkle_root": merkle_root,
        "time": timestamp,
        "timestamp": timestamp,
        "bits": data["bits"],
        "nonce": data["nonce"],
        "n_tx": tx_count,
        "tx_count": tx_count,
        "difficulty": data.get("difficulty"),
    }


def get_latest_height():
    """Return the current blockchain height."""
    return int(_get_text("/blocks/tip/height"))


def get_block_by_height(height: int):
    """Return the block at a given height."""
    block_hash = _get_text(f"/block-height/{height}")
    return get_block(block_hash)
