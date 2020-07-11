from src.utils import save_processed
from src.main import preprocess_reviews


def main():
    df = preprocess_reviews()
    save_processed(df, "processed_reviews.csv")


if __name__ == '__main__':
    main()
