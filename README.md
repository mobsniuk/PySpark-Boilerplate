# PySpark-Boilerplate
A boilerplate for writing PySpark Jobs.

 A test job called sparktester is included to demonstrate how to setup your module and unit tests.

# Setup

On Windows - instal_deps.bat
On Linux - make .venv

## Python Virtual Environment

Currently all dependencies are included. Even those that are only required for testing purposes. The --copies is used
 to assist in making the job portable. C libraries that are external to Python may not be included and rely on
  identical OS versions to run. Numpy is an example of a python modele that includes a C component. A C component
   that is used by the python binary itself may be linked to an external libary and versioning is critical as python
    has no control over this. 

# Coding

## Module/Model Code

The src/jobs folder contains the code for a specific module/model. Each sub-component of the system will have its own
 folder. The folder name will be used as the entry point into running that specific component.
 
 Each model/module must have a 
 
 <pre>
 def analyze(spark, **job_args):
 </pre>
 
 Function defined. This will be called from main with the spark context and job arguments.
 It is the responsibility of your job to do all steps within that call. For example sparktester does
 
 <pre>
     config = getConfig(**job_args)
 
     dataframe = do_etl(spark, config)
     dataframe = do_spark_work(dataframe)
     save_dataframe(dataframe, config)
 </pre>

## Shared Code

The src/shared folder holds common code for all modules/models.


## Unit test Code

Unit test goes into the test/_jobs folder. The convention is to create a new folder that matches the job name.


## Linter

On windows - run_linter.bat
On Linux - make lint

## Unit Tests

On windows - run_tests.bat
On Linux - make test (dependencies must be installed first)

# Distribution

The Makefile will after success python virtual environment creation, linting, testing will create dist folder with
 all that is needed to run a pyspark job on the cluster.
 
- run_pyspark.sh - is the driving program (editing the list of jobs will allow you to customize the sequence of jobs")
- config.ini - comes from conf folder. Needs to be customized for the specific environment.
- main.py - the driving code for the app
- jobs.zip - the code for the app
- pyspark_env.tar.gz - the pyspark environment for the job


## run_pyspark.sh

The run_pyspark.sh relies on a list of modules that will be invoked.
<pre>
job_list=("sparktester")
</pre>

The above list will be called, in this case just sparktester. The script is called once but the script may invoke
 spark-submit many times. Once for each job listed in the job_list. If any job fails the sequence of jobs following
  the failed job will not be executed.
  