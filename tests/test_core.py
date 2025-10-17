# tests/test_core.py
import pytest
from unittest.mock import patch, MagicMock
from pite_project1.core import main  # ton fichier principal

def test_main_default(monkeypatch):
    # Simuler sys.argv sans arguments
    monkeypatch.setattr("sys.argv", ["prog"])

    # Mock load_config et load_json
    with patch("core.load_config") as mock_load_config, \
         patch("core.load_json") as mock_load_json, \
         patch("core.Config") as mock_config:

        # Config par défaut
        mock_conf = MagicMock()
        mock_conf.path = "default.json"
        mock_conf.encoding = "utf-8"
        mock_conf.threshold = 0
        mock_conf.mode = "default"
        mock_load_config.return_value = mock_conf

        # Données de test
        mock_load_json.return_value = [
            {"STATUS":"ok","value":3},
            {"STATUS":"bad","value":"x"},
            {"STATUS":"ok","value":7}
        ]

        # Appel de la fonction
        res = main(display=False)

        # Assertions sur le résultat
        assert res["count"] == 2  # seulement les "ok"
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

        # Appel de la fonction
        res = main(display=False)

        # Threshold = 5 → exclut 3
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

        # Avec --all, le mode change mais les données filtrées restent basées sur le threshold (0)
        assert res["count"] == 2
        assert res["sum"] == 6
        assert res["avg"] == 3
