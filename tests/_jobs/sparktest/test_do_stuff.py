from jobs.sparktester import do_spark_work
from shared.TestUtils import assert_dataframe_equal_with_sort
import pandas as pd
from nose import with_setup
from tests._jobs import setup_package, sparkSession, teardown_package


@with_setup(setup_package, teardown_package)
def test_do_stuff():
    spark = sparkSession.getContext()

    data_pandas = pd.DataFrame({'make': ['Jaguar', 'MG', 'MINI', 'Rover', 'Lotus'],
                                'registration': ['AB98ABCD', 'BC99BCDF', 'CD00CDE', 'DE01DEF', 'EF02EFG'],
                                'year': [1998, 1999, 2000, 2001, 2002]})

    expected_pandas = pd.DataFrame(
        {'make': ['Rover', 'Lotus', 'MINI'], 'registration': ['DE01DEF', 'EF02EFG', 'CD00CDE'],
         'year': [2001, 2002, 2000]})

    data_spark = spark.createDataFrame(data_pandas)
    expected_df = spark.createDataFrame(expected_pandas)

    result = do_spark_work(data_spark)
    assert_dataframe_equal_with_sort(result, expected_df, 'make')
