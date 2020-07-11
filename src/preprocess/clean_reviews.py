from src.utils import load_raw, get_logger, np, pd
from src.consts import LIUNARDS, NUMERIC_COLS
logger = get_logger(__name__)


def adjust_dtypes(df_reviews):
    for column in NUMERIC_COLS+LIUNARDS:
        df_reviews[column].replace(',', '.', inplace=True, regex=True)
        df_reviews[column].replace(np.nan, -1, inplace=True)
        df_reviews[column] = df_reviews[column].astype(float)
        df_reviews[column].replace(-1, np.nan, inplace=True)

    return df_reviews


def load_reviews():
    df = load_raw("reviews.csv")
    df.columns = [c.lower() for c in df.columns]
    df.replace('checked', True, inplace=True)
    df = df.iloc[1:]
    df = adjust_dtypes(df)
    return df


def melt_reviews(df):
    score_columns = LIUNARDS
    columns_to_keep = [x for x in df.columns if x not in score_columns]
    df_melted = pd.melt(df, id_vars=columns_to_keep, var_name='liunard',
                        value_name='score')
    return df_melted


def clean_reviews():
    logger.info("Cleaning review table")
    df = load_reviews()
    return melt_reviews(df)


if __name__ == '__main__':
    df = load_reviews()
    df_melted = processed_reviews(df)
    print(df_melted.head())
