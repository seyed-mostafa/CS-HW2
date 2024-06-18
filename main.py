from bitarray import bitarray
import numpy as np

# Definition of permutation and substitution functions
def permutation_function(block):
    # Simple permutation function (for example, reversing the block)
    permuted_block = block[::-1]
    return permuted_block

def substitution_function(block):
    # Example substitution function (e.g., XOR with a constant value)
    substituted_block = block ^ 0xFFFFFFFFFFFFFFFF
    return substituted_block

# Feistel encryption algorithm
def feistel_encryption(input_block, key):
    # Initial setup
    left_half = input_block[:64]  # Initial left half
    right_half = input_block[64:]  # Initial right half

    # Splitting the key into two 64-bit halves
    key_left = key[:64]
    key_right = key[64:]

    # Number of rounds
    rounds = 12

    # Performing rounds
    for round_num in range(rounds):
        # Generating subkeys
        subkey_left = key_left[round_num % 64:] + key_left[:round_num % 64]
        subkey_right = key_right[round_num % 64:] + key_right[:round_num % 64]

        # Applying permutation and substitution functions
        new_left_half = right_half
        f_result = permutation_function(right_half)
        new_right_half = left_half ^ f_result

        # Updating halves
        left_half = new_left_half
        right_half = new_right_half

    # Combining halves into output block
    output_block = left_half + right_half

    return output_block

# Example usage
if __name__ == "__main__":
    # Input as bit arrays
    input_bits = bitarray('0101010101010101010101010101010101010101010101010101010101010101')

    # Key as bit arrays
    key_bits = bitarray('1100110011001100110011001100110011001100110011001100110011001100')

    # Applying encryption
    encrypted_bits = feistel_encryption(input_bits, key_bits)

    print("Input Block (64 bits):", input_bits)
    print("Encrypted Block (64 bits):", encrypted_bits)
