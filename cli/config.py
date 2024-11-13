# Configuration constants
STANDARD_INPUT_FILE_PATH = "input/original_sample.wav"
OUTPUT_BASIC_LSB = "output/basic_lsb_encoded.wav"
OUTPUT_ENHANCED_LSB_FLIP = "output/enhanced_lsb_encoded_flip.wav"
OUTPUT_ENHANCED_LSB_NO_FLIP = "output/enhanced_lsb_encoded_no_flip.wav"

# Import algorithm modules
from algorithms import (
    basic_lsb_steganography,
    enhanced_lsb_steganography_with_flip,
    enhanced_lsb_steganography_no_flip,
)

# Dictionary to store algorithms
ALGORITHMS = {
    1: {
        "name": "Basic LSB Steganography",
        "encode": basic_lsb_steganography.encode,
        "decode": basic_lsb_steganography.decode,
        "output_file": OUTPUT_BASIC_LSB
    }
}
