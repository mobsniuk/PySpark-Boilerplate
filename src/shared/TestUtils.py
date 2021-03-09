from pandas.testing import assert_frame_equal


def assert_pandaframe_equal_with_sort(results, expected, keycolumns):
    """
    Assert pandas dataframe equal with sort takes in two pandas dataframes, sorts them on a key field.

    :param results: results pandas dataframe
    :param expected: expected results pandas dataframe
    :param keycolumns: name of column to sort data on
    """
    results_sorted = results.sort_values(by=keycolumns).reset_index(drop=True)
    expected_sorted = expected.sort_values(by=keycolumns).reset_index(drop=True)
    assert_frame_equal(results_sorted, expected_sorted)


def assert_dataframe_equal_with_sort(results_df, expected_df, keycolumns):
    """
    Assert dataframe equal with sort takes in two Spark dataframes, sorts them on a key field.

    :param results_df: results dataframe
    :param expected_df: expected results dataframe
    :param keycolumns:  name of column to sort data on
    """
    results = results_df.toPandas()
    expected = expected_df.toPandas()
    results_sorted = results.sort_values(by=keycolumns).reset_index(drop=True)
    expected_sorted = expected.sort_values(by=keycolumns).reset_index(drop=True)
    assert_frame_equal(results_sorted, expected_sorted)
