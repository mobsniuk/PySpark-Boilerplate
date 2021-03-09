#!/usr/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

job_list=("sparktester")

conf_path=$DIR/config.ini

export EXEC_MEM=1G
export DRIVER_MEM=1G
export NUM_EXEC=1

for job in "${job_list[@]}"
do
  spark-submit \
  --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./environment/bin/python \
  --conf spark.yarn.dist.archives=$DIR/pyspark_env.tar.gz#environment \
  --name $job \
  --master yarn \
  --verbose \
  --executor-memory $EXEC_MEM \
  --driver-memory $DRIVER_MEM \
  --num-executors $NUM_EXEC \
  --deploy-mode cluster \
  --py-files $DIR/jobs.zip \
  $DIR/main.py \
  --job $job \
  --job-args conf=$conf_path

  if [ $? -eq 0 ]; then
    echo "$job succeeded"
  else
    echo "$job failed"
    exit $?
  fi
done