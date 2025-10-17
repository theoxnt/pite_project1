# tests/test_core.py
import pytest
from unittest.mock import patch, MagicMock
from pite_project1.core import main 

def test_main_default(monkeypatch):
    # Simulate sys.argv without arguments
    monkeypatch.setattr("sys.argv", ["prog"])

    # Mock load_config et load_json
    with patch("core.load_config") as mock_load_config, \
         patch("core.load_json") as mock_load_json, \
         patch("core.Config") as mock_config:

        # Default configuration
        mock_conf = MagicMock()
        mock_conf.path = "default.json"
        mock_conf.encoding = "utf-8"
        mock_conf.threshold = 0
        mock_conf.mode = "default"
        mock_load_config.return_value = mock_conf

        # Data test
        mock_load_json.return_value = [
            {"STATUS":"ok","value":3},
            {"STATUS":"bad","value":"x"},
            {"STATUS":"ok","value":7}
        ]

        # Call the main function
        res = main(display=False)

        # assertions of the results
        assert res["count"] == 2 
        assert res["sum"] == 10
        assert res["avg"] == 5

def test_main_with_file_and_threshold(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog", "--file", "myfile.json", "--thres", "5"])

    with patch("core.load_config") as mock_load_config, \
         patch("core.load_json") as mock_load_json, \
         patch("core.Config") as mock_config:

        mock_conf = MagicMock()
        mock_conf.path = "default.json"
        mock_conf.encoding = "utf-8"
        mock_conf.threshold = 0
        mock_conf.mode = "default"
        mock_load_config.return_value = mock_conf

        # Mock load_json pour retourner des valeurs
        mock_load_json.return_value = [
            {"STATUS":"ok","value":3},
            {"STATUS":"ok","value":7},
            {"STATUS":"ok","value":10}
        ]

        # Call the main function
        res = main(display=False)

        # Threshold = 5 → remove 3
        assert res["count"] == 2
        assert res["sum"] == 17
        assert res["avg"] == 8.5

def test_main_with_all_flag(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog", "--all"])

    with patch("core.load_config") as mock_load_config, \
         patch("core.load_json") as mock_load_json, \
         patch("core.Config") as mock_config:

        mock_conf = MagicMock()
        mock_conf.path = "default.json"
        mock_conf.encoding = "utf-8"
        mock_conf.threshold = 0
        mock_conf.mode = "default"
        mock_load_config.return_value = mock_conf

        mock_load_json.return_value = [
            {"STATUS":"ok","value":2},
            {"STATUS":"bad","value":5},
            {"STATUS":"ok","value":4}
        ]

        res = main(display=False)

        # With --all, the mode changes, but the filtered data remain based on the threshold (0)
        assert res["count"] == 2
        assert res["sum"] == 6
        assert res["avg"] == 3
