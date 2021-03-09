from jobs.sparktester import do_spark_work
from nose import with_setup
import pandas as pd
from tests._jobs import setup_package, sparkSession, teardown_package


@with_setup(setup_package, teardown_package)
def test_do_word_counts():
    spark = sparkSession.getContext()

    print(spark.version)

    data_pandas = pd.DataFrame({'make': ['Jaguar', 'MG', 'MINI', 'Rover', 'Lotus'],
                                'registration': ['AB98ABCD', 'BC99BCDF', 'CD00CDE', 'DE01DEF', 'EF02EFG'],
                                'year': [1998, 1999, 2000, 2001, 2002]})

    data_spark = spark.createDataFrame(data_pandas)

    assert do_spark_work(data_spark).count() == 3
