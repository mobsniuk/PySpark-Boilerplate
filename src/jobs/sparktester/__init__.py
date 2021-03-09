from shared.ConfigManager import getConfig
import pandas as pd
import numpy as np
from pyspark.sql.functions import col  # pylint: disable=E0401(


def analyze(spark, **job_args):
    print("Running sparktest")

    config = getConfig(**job_args)

    dataframe = do_etl(spark, config)
    dataframe = do_spark_work(dataframe)
    save_dataframe(dataframe, config)


def do_spark_work(dataframe):
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a[0])
    return dataframe.filter(col('year') >= 2000)


def do_etl(spark, config):
    print(config.get('COMMON', 'ENTCLAIMS_SCHEMA'))
    data_pandas = pd.DataFrame({'make': ['Jaguar', 'MG', 'MINI', 'Rover', 'Lotus'],
                                'registration': ['AB98ABCD', 'BC99BCDF', 'CD00CDE', 'DE01DEF', 'EF02EFG'],
                                'year': [1998, 1999, 2000, 2001, 2002]})

    return spark.createDataFrame(data_pandas)


def save_dataframe(dataframe, config):
    directory = config.get('COMMON', 'ENTCLAIMS_DIR')
    print("Save location is: " + directory)
    dataframe.show()
    # dataframe.write....
