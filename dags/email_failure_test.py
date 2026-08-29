from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.smtp.notifications.smtp import SmtpNotifier


def failing_task():
    raise Exception("Testing Airflow email notification")


email_failure_notifier = SmtpNotifier(
    smtp_conn_id="smtp_default",
    from_email="er.kumargaut@gmail.com",
    to=["gautam2001.007@gmail.com", "deep.rajcr16@gmail.com"],
    subject="Airflow Task Failed",
    html_content="""
    <h3>Airflow Task Failure</h3>
    <p>The task <b>failing_task</b> has failed.</p>
    <p>This is a test email notification.</p>
    """,
)


with DAG(
    dag_id="email_failure_test",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    successful_task = PythonOperator(
        task_id="successful_task",
        python_callable=lambda: print("Success"),
    )

    failing_task_operator = PythonOperator(
        task_id="failing_task",
        python_callable=failing_task,
        on_failure_callback=email_failure_notifier,
    )

    successful_task >> failing_task_operator