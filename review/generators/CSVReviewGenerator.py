"""
CSVReviewGenerator.py

Class that uses the MemoryReviewGenerator to allow for generation
of reviews that are kept in memory. When ready, the internal memory can
easily be converted to a CSV output format.
"""
import pandas as pd

from review.generators.MemoryReviewGenerator import MemoryReviewGenerator


class CSVReviewGenerator(MemoryReviewGenerator):

    # Columns for a CSV
    columns: list[str] = ["customer_id", "customer_name", "rating", "review"]

    def to_csv(self, fname) -> None:
        """ Store the generated reviews in a CSV """
        df = pd.DataFrame.from_records(
            {
                "customer_id": review.id,
                "customer_name": review.name,
                "rating": review.rating,
                "review": review.content
            }
            for review in self.reviews
        )
        df.columns = self.columns
        df.set_index("customer_id")
        df.to_csv(fname)