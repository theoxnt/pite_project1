import sys
import pytest
from pite_project1.cli import get_parser

def test_parser_file_argument(monkeypatch):
    parser = get_parser()
    test_args = ["prog", "--file", "data.json"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse_args()
    assert args.file == "data.json"
    assert args.all is False
    assert args.thres is None

def test_parser_all_flag(monkeypatch):
    parser = get_parser()
    test_args = ["prog", "--all"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse_args()
    assert args.all is True
    assert args.file is None
    assert args.thres is None

def test_parser_threshold(monkeypatch):
    parser = get_parser()
    test_args = ["prog", "--thres", "10"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse_args()
    assert args.thres == "10"
    assert args.file is None
    assert args.all is False

def test_parser_all_arguments(monkeypatch):
    parser = get_parser()
    test_args = ["prog", "--file", "data.json", "--all", "--thres", "5"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parser.parse_args()
    assert args.file == "data.json"
    assert args.all is True
    assert args.thres == "5"
