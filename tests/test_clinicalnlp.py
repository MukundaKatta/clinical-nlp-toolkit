"""Tests for ClinicalNLP."""
import pytest
from src.clinicalnlp import ClinicalNLP

def test_init():
    obj = ClinicalNLP()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = ClinicalNLP()
    result = obj.extract_entities(input="test")
    assert result["processed"] is True
    assert result["operation"] == "extract_entities"

def test_multiple_ops():
    obj = ClinicalNLP()
    for m in ['extract_entities', 'extract_medications', 'detect_negation']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = ClinicalNLP()
    r1 = obj.extract_entities(key="same")
    r2 = obj.extract_entities(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = ClinicalNLP()
    obj.extract_entities()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = ClinicalNLP()
    obj.extract_entities(x=1)
    obj.extract_medications(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
