"""
IGenerator.py

Interface for the generators.
"""
from abc import ABC, abstractmethod

from review.Review import Review

class IGenerator(ABC):

    # Keep track of needed retries
    retries: int

    @abstractmethod
    def generate_review(self) -> Review: pass

    @abstractmethod
    def generate_reviews(self, n: int) -> list[Review]: pass
