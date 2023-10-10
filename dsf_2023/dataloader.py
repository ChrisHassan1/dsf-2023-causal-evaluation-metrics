import pandas as pd
import os


def _get_root_path():
    root_path = os.path.dirname(os.path.abspath(__file__))
    return root_path


def load_data():
    """
    
    """
    root_path = _get_root_path()

    invest_email_rnd_df = pd.read_csv(f"{root_path}/data/invest_email_rnd.csv")
    invest_email_biased_df = pd.read_csv(f"{root_path}/data/invest_email_biased.csv")
    invest_email_df = pd.read_csv(f"{root_path}/data/invest_email.csv")

    data = dict(
        invest_email_rnd_df=invest_email_rnd_df,
        invest_email_biased_df=invest_email_biased_df,
        invest_email_df=invest_email_df
    )

    return data