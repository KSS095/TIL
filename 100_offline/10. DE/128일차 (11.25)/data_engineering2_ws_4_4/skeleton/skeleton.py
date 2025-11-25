from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

#  DAG 정의 시작
with DAG(
    dag_id="dags_email_operator",  # DAG의 고유 ID 설정
    schedule="0 8 1 * *",  # 매월 1일 오전 8시에 실행되도록 스케줄 설정 (cron 표현식)
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),  # DAG 시작 날짜 및 시간대 설정
    catchup=False,  # 과거 실행을 자동으로 수행하지 않도록 설정
    dagrun_timeout=datetime.timedelta(minutes=60),  # DAG 실행 시간이 특정 시간 초과 시 타임아웃 설정
) as dag:
    
    # EmailOperator를 사용하여 이메일 전송 작업 정의
    send_email_task = EmailOperator(
        task_id='send_email_task',  # 작업의 고유 ID
        to='tmdtn339@gmail.com',  # 이메일 수신자 지정
        subject='Airflow 성공메일',  # 이메일 제목
        html_content='Airflow 작업이 완료되었습니다.'  # 이메일 본문 내용
    )
