"""Test cases for the main module."""

import io
import sys
from unittest.mock import patch

import pytest

from pmt.main import main


def test_main_prints_hello_message():
    """Test that main() prints the expected hello message."""
    # Capture stdout to verify the output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the main function
    main()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Get the printed output
    output = captured_output.getvalue()

    # Assert the output contains the expected message
    assert "Hello from python-module-template!" in output
