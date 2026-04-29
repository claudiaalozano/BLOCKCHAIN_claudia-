"""Module M2: Block Header Analyzer."""

import hashlib
import struct

import streamlit as st

from api.blockchain_client import get_block, get_latest_block


def bits_to_target(bits: int) -> int:
    """Convert compact bits representation to full target integer."""
    exponent = bits >> 24
    coefficient = bits & 0xFFFFFF
    return coefficient * (1 << (8 * (exponent - 3)))


def double_sha256(data: bytes) -> bytes:
    """Return SHA256(SHA256(data))."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def count_leading_zero_bits(hex_hash: str) -> int:
    """Count leading zero bits in a 256-bit hash."""
    binary = bin(int(hex_hash, 16))[2:].zfill(256)
    return len(binary) - len(binary.lstrip("0"))


def build_block_header(block: dict) -> bytes:
    """Reconstruct the 80-byte Bitcoin block header."""
    version = struct.pack("<L", block["ver"])
    prev_hash = bytes.fromhex(block["prev_block"])[::-1]
    merkle_root = bytes.fromhex(block["mrkl_root"])[::-1]
    timestamp = struct.pack("<L", block["time"])
    bits = struct.pack("<L", block["bits"])
    nonce = struct.pack("<L", block["nonce"])

    return version + prev_hash + merkle_root + timestamp + bits + nonce


def render() -> None:
    """Render the M2 panel."""
    st.header("M2 - Block Header Analyzer")
    st.write("Inspect the latest Bitcoin block header and verify its Proof of Work locally.")

    use_latest = st.checkbox("Use latest block automatically", value=True)

    block_hash = ""
    if use_latest:
        try:
            latest = get_latest_block()
            block_hash = latest["hash"]
            st.write(f"**Latest block hash:** `{block_hash}`")
        except Exception as exc:
            st.error(f"Error fetching latest block: {exc}")
            return
    else:
        block_hash = st.text_input(
            "Block hash",
            placeholder="Enter a block hash",
            key="m2_hash",
        )

    if st.button("Analyze block", key="m2_lookup") and block_hash:
        with st.spinner("Fetching and analyzing block..."):
            try:
                block = get_block(block_hash)

                st.subheader("Header Fields")
                st.write(f"**Version:** {block.get('ver')}")
                st.write(f"**Previous block hash:** {block.get('prev_block')}")
                st.write(f"**Merkle root:** {block.get('mrkl_root')}")
                st.write(f"**Timestamp:** {block.get('time')}")
                st.write(f"**Bits:** {block.get('bits')}")
                st.write(f"**Nonce:** {block.get('nonce')}")

                header = build_block_header(block)
                local_hash_little_endian = double_sha256(header)
                local_hash = local_hash_little_endian[::-1].hex()

                api_hash = block.get("hash")
                target = bits_to_target(block["bits"])
                hash_int = int(local_hash, 16)
                pow_valid = hash_int <= target
                leading_zero_bits = count_leading_zero_bits(local_hash)

                st.subheader("80-byte Header")
                st.code(header.hex())

                st.subheader("Local Proof of Work Verification")
                st.write(f"**Hash from API:** `{api_hash}`")
                st.write(f"**Hash computed locally:** `{local_hash}`")
                st.write(f"**Matches API hash:** {local_hash == api_hash}")
                st.write(f"**Target (decoded from bits):** `{target}`")
                st.write(f"**Hash as integer:** `{hash_int}`")
                st.write(f"**Hash < Target:** {pow_valid}")
                st.write(f"**Leading zero bits:** {leading_zero_bits}")

                if pow_valid and local_hash == api_hash:
                    st.success("Proof of Work verified correctly.")
                else:
                    st.error("Proof of Work verification failed.")

                st.subheader("Interpretation")
                st.write(
                    "The bits field is the compact representation of the mining target."
                )
                st.write(
                    "Bitcoin miners vary the nonce and other block contents until the double SHA-256 hash is below the target."
                )
                st.write(
                    "A valid block hash therefore contains many leading zero bits."
                )

            except Exception as exc:
                st.error(f"Error fetching block: {exc}")

    elif not use_latest:
        st.info("Enter a block hash and click Analyze block.")