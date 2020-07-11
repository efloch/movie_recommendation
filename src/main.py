from src.preprocess.clean_reviews import clean_reviews
from src.preprocess.feature_engineer import feature_engineer


def preprocess_reviews():
    df = clean_reviews()
    df = feature_engineer(df)
    return df


if __name__ == '__main__':
    df = get_reviews()
