import sys
import pandas as pd


def main():
    if len(sys.argv) != 3:
        print("Required both arguments: raw text input and comma separated coordinates")
        sys.exit(1)
    raw_in = sys.argv[1]
    coordinates = sys.argv[2]
    print("Processing raw input: " + raw_in + " coordinates: " + coordinates)

    my_df = create_df()
    my_df = load_raw_input(raw_in, my_df)
    # print(my_df)
    # print("after: size: " + str(my_df.size) + " shape:" + str(my_df.shape))

    print("Processing coordinates: " + coordinates)
    # process coordinates
    coord_list = coordinates.split(",")

    print_output(my_df, coord_list)


def print_output(df, cols):
    print(df[cols].to_csv(index=False))


def create_df():
    # creating 96 column names in a 8x12 nested loop
    columns = "ABCDEFGH"
    rfu_columns = []
    for char in columns:
        for i in range(1, 13):
            column_name = char + str(i)
            rfu_columns.append(column_name)
    df = pd.DataFrame(columns=rfu_columns)
    return df


def load_raw_input(raw_in, in_df):
    # read in the file skipping header including column names and footer rows
    df = pd.read_table(raw_in, skiprows=3, skipfooter=2, header=None, sep='\t', engine='python')

    # file format creates two empty columns at the end, drop these
    df.dropna(axis=1, how="all", inplace=True)

    # create a new data frame with the first two columns which contain time and temp
    # time_and_temp = df.iloc[:, 0:2]

    # drop those first two columns and we now only have pure data, ie. relative fluorescence units RFU
    rfu = df.iloc[:, 2:]

    # scroll in increments of 9 to account for blank row at the end of each chunk
    for i in range(0, rfu.shape[0], 9):
        # only take top 8 rows, 9th row is blank
        rfu1 = rfu.iloc[i:i+8, :]
        my_series = pd.Series(rfu1.to_numpy(copy=True).flatten(), index=in_df.columns)
        in_df = in_df.append(my_series, ignore_index=True)
    return in_df


if __name__ == '__main__':
    main()
