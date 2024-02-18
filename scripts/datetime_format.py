from utils import setNumericDatesForDataframe, getDatasetDataframe

# ! RUN ONLY ONCE TO PROPERLY SET DATAVALUES TO NUMERIC DAT FORMAT
def main():
    df_csv = getDatasetDataframe()
    setNumericDatesForDataframe(df_csv)

if __name__ == '__main__':
    main()