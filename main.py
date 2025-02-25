"""
main.py
"""
from review.generators.CSVReviewGenerator import CSVReviewGenerator

N = 30
OUTPUT_PATH = "./output_reviews/reviews_V1.csv"

if __name__ == '__main__':
    generator = CSVReviewGenerator()
    print("Start generating reviews...")
    generator.generate_reviews(N)
    print(f"Generated {N} reviews with {generator.retries} retries, storing...")
    generator.to_csv(OUTPUT_PATH)
    print(f"Stored reviews in {OUTPUT_PATH}. Enjoy your reviews of questionable quality.")