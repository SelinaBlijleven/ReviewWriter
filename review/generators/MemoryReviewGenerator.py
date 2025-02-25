"""
MemoryReviewGenerator.py

A review generator that keeps a memory of the reviews it has generated.
Useful for converting to all kinds of output formats.
"""
from typing import override

from review.Review import Review
from review.generators.ReviewGenerator import ReviewGenerator

class MemoryReviewGenerator(ReviewGenerator):

    # Hold our reviews after generation
    reviews: list[Review]

    def __init__(self):
        """ Initialize the generator with memory """
        super().__init__()

        # List to keep results in
        self.reviews = []

    @override
    def generate_review(self):
        """ Generate a review and store it in our internal memory """
        review = super().generate_review()
        # Update our memory
        self.reviews.append(review)
        return review

    @override
    def generate_reviews(self, n: int) -> list[Review]:
        """ Generate n reviews and keep them in internal memory """
        reviews = super().generate_reviews(n)
        # Update our memory
        self.reviews.extend(reviews)
        return reviews
