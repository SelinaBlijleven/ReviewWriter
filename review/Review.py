"""
Review.py

Representation of a single review
"""
from dataclasses import dataclass

@dataclass
class Review:
    id: int
    name: str
    rating: int
    content: str
