from src.utils import np, pd, itertools, get_logger
from src.consts import CAT_THRESHOLD
import sklearn
from sklearn.preprocessing import MultiLabelBinarizer
logger = get_logger(__name__)


def _list_to_dict(x):
    if isinstance(x, list):
        awards_dict = {}
        for award in x:
            name = award[1].strip().lower()
            if name.endswith('s'):
                name = name[:-1]
            awards_dict[name] = int(award[0])
        return awards_dict
    return {}


def _get_top(df, c, top_n):
    col = df[c].to_frame().explode(c)
    col['count'] = 1
    col = col.groupby(c, as_index=False)['count'].sum()
    col = col.sort_values('count', ascending=False)
    col = col[~col[c].isin(['Unknown', ''])]
    return col.iloc[:top_n][c].values


def parse_awards(df, award_col):
    logger.info(f"Parsing awards column")
    df[award_col] = df[award_col].str.findall(
        "(?P<count>\d+) (?P<award>[^(.&)]+)")
    awards_dict = df.apply(lambda x: _list_to_dict(
        x[award_col]), axis=1)
    df_awards = pd.json_normalize(awards_dict)
    df_awards.fillna(0, inplace=True)
    df = pd.concat([df.drop(award_col, 1), df_awards], axis=1)
    return df


def binarize_list_columns(df, c, limit_top):
    logger.info(f"Creating dummy features for {c} column")
    df[c] = df[c].replace(to_replace={np.nan: 'Unknown', ', ': ',', ' ,': ','},
                          regex=True)
    df[c] = df[c].str.split(',')
    mlb = MultiLabelBinarizer()
    mlb.fit_transform(df[c])
    df_bin = pd.DataFrame(mlb.fit_transform(
        df[c]), columns=mlb.classes_, index=df.index)
    if limit_top:
        val_to_keep = _get_top(df, c, limit_top)
        df_bin = df_bin[val_to_keep]
    df = pd.concat([df.drop(c, 1), df_bin], axis=1)
    return df


def feature_engineer(df):
    logger.info("Feature engineering")
    df = parse_awards(df, 'awards')
    for col in CAT_THRESHOLD:
        df = binarize_list_columns(df, col, limit_top=CAT_THRESHOLD[col])
    return df
