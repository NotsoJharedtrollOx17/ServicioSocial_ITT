import pandas as pd
from utils import setNumericDatesForDataframe, getDatasetDataframe

def main():
    df_csv = getDatasetDataframe()
    setNumericDatesForDataframe(df_csv)

if __name__ == '__main__':
    main()