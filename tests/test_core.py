"""Tests for ClinicalNlpToolkit."""
from src.core import ClinicalNlpToolkit
def test_init(): assert ClinicalNlpToolkit().get_stats()["ops"] == 0
def test_op(): c = ClinicalNlpToolkit(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = ClinicalNlpToolkit(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = ClinicalNlpToolkit(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = ClinicalNlpToolkit(); r = c.process(); assert r["service"] == "clinical-nlp-toolkit"
