from src.config import *
from src.params import *


def adjust_dtypes(df_reviews):
    df_reviews.replace(',', '.', inplace=True, regex=True)
    for column in NUMERIC_COLS+LIUNARDS:
        df_reviews[column].replace(np.nan, -1, inplace=True)
        df_reviews[column] = df_reviews[column].astype(float)
    df_reviews.replace(np.nan, 0, inplace=True)
    return df_reviews


def clean_reviews():
    df = pd.read_csv(os.path.join(DATA, 'raw/reviews.csv'))
    df.columns = [c.lower() for c in df.columns]
    df.replace('checked', True, inplace=True)
    df = df.iloc[1:]
    df = adjust_dtypes(df)
    return df


def melted_reviews():
    score_columns = LIUNARDS
    columns_to_keep = [x for x in df.columns if x not in score_columns]
    df_melted = pd.melt(df, id_vars=columns_to_keep, var_name='liunard',
                        value_name='score')
    return df_melted


if __name__ == '__main__':
    df = clean_reviews()
    df_melted = melted_reviews()
    print(df_melted.head())
