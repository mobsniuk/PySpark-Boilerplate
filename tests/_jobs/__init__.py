import findspark  # this needs to be the first import

findspark.init()

import logging  # noqa: E402

try:
    import pyspark
except Exception:
    import findspark  # pylint: disable=W0404

    findspark.init()
    import pyspark


class TestSparkContext:
    """
    Holds a spark context for the duration of unit tests
    """

    def __init__(self):
        self.context = None

    def initialize(self):
        self.context = pyspark.sql.SparkSession.builder.master('local[2]').appName(
            'my-local-testing-pyspark-context').enableHiveSupport().getOrCreate()

        logger = logging.getLogger('py4j')
        logger.setLevel(logging.WARN)

    def getContext(self):
        return self.context


sparkSession = TestSparkContext()


def setup_package():
    """
    Runs once for all unit tests in the _jobs package. Creates a spark context that will be shared by all unit tests
    in this package
    """
    print("Creating Spark context...")
    sparkSession.initialize()


def teardown_package():
    """
    Runs once for all unit tests in the _jobs package. Stops a spark context that is shared by all unit tests in this package.
    """
    print("Stopping spark context...")
    sparkContext = sparkSession.getContext()
    sparkContext.stop()
