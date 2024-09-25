import pendulum
from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from common.config import TimeRangeExternalTaskSensor, default_args
from airflow.operators.python import PythonOperator
from common.taskhelper import taskhelper
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.trigger_rule import trigger_rule

k8_namespace = Variable.get('namespace', d_var = 'dhy0-jobs-dev')
img_pull_secret = Variable.get('image-pull-secrets', d_var = 'dtrdev')
env = Variable.get('ENV', d_var = 'DEV')
appCode = Variable.get('APPCODE', d_var = 'DHY0')
schedule_intervel = Variable.get()
dag_name = Variable.get()
dag_name_sat = Variable.get()


# override start_date in default_args.
local_timezone = pendulum.timezone('America/New_York')
default_args['start_date'] = datetime(2021, 1, 1, tzinfo = local_timezone)

overall_sns_updater = DAG(
    dag_id = '',
    schedule_intervel = schedule_intervel,
    description = '',
    tags = [],
    default_args = default_args
)

tskHelper = TaskHelper(env, appCode, dag_name)
tskHelper_sat = TaskHelper(env, appCode, dag_name_sat, task_id = "dreamio_status_sat")
tskHelper_sun = TaskHelper(env, appCode, dag_name_sat, task_id = "dreamio_status_sun")

# return the weekday_path (tue-sat, sun, mon..)
def get_day(**kwargs):
    run_date = tskHelper.config.run_date
    dag_run_config = kwargs['dag_run'].conf
    if dag_run_config:
        if "RUN_DATE" in dag_run_config.keys():
            run_date = dag_run_config.get("RUN_DATE")
    weekday = datetime.now().isoweekday()
    if run_date != "":
        weekday = datetime.strftime(run_date, '%Y-%m-%d').isoweekday()
    if weekday in [2,3,4,5,6]:
        select = "tue-sat"
    elif weekday == 1:
        select = "mon"
    elif weekday == 7:
        select = "sun"
    kwargs['ti'].xcom_push(key='select_path',value = select)