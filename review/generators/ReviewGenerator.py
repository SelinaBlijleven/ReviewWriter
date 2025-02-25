"""
ReviewGenerator.py

This generator uses an LLM to write a review based on the configured
prompt. Sometimes we need to force a re-write, because the LLM did not
respond with proper JSON.

This version of the generator does not store the reviews in memory, making
it more suitable for prompting in small batches.
"""
import json
from typing import Optional, override

from review.IGenerator import IGenerator
from review.Review import Review
from review.generators.FakeCustomerGenerator import FakeCustomerGenerator
from review.writer.ReviewWriter import ReviewWriter


class ReviewGenerator(IGenerator):

    # Fake customer generator
    customer_gen: FakeCustomerGenerator

    # Content writer
    writer: ReviewWriter

    # Next customer ID
    next_id: int = 1

    # Number of retries used to write the reviews
    retries: int = 0

    def __init__(self):
        """ Create the generator """
        # Construct our customer info generator
        self.customer_gen = FakeCustomerGenerator()

        # Construct our writer
        self.writer = ReviewWriter()

    @override
    def generate_reviews(self, n: int) -> list[Review]:
        """ Generate a specific number of fake reviews """
        reviews: list[Review] = []

        for i in range(n):
            review = self.generate_review()
            reviews.append(review)
            if i % 5 == 0:
                print("Another 5...")

        return reviews

    @override
    def generate_review(self) -> Review:
        """ Generate a fake review """
        # Let our writer write until we have valid JSON
        decoded = self.write_review()

        # Construct the review
        review: Review = Review(
            id=self.next_id,
            name=self.customer_gen.fake_name(),
            rating=decoded["rating"],
            content=decoded["review_content"]
        )

        # Increment ID assigner
        self.next_id += 1
        return review

    def write_review(self):
        """ Bother the LLM until it writes in the correct JSON format """
        decoded: Optional[dict] = None

        # Attempt to write reviews until we get something parseable
        while not decoded:
            attempt: str = self.writer.generate_review()
            decoded: Optional[dict] = self._decode_response(attempt)

            # If we haven't managed to decode, we need to try again
            if decoded is None:
                self.retries += 1
                continue

            # Reset the review if it does not meet formatting criteria
            if "rating" not in decoded or "review_content" not in decoded:
                decoded = None
                self.retries += 1

        return decoded

    def _decode_response(self, attempt: str) -> Optional[dict]:
        """ Helper method that attempts to decode JSON that might be unparseable. """
        try:
            data = json.loads(attempt)
            return data
        except json.JSONDecodeError as e:
            return None
        except TypeError as e:
            return None