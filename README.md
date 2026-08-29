README.md -ItemType File

Example:

# Airflow Docker Email Notification

Apache Airflow running with Docker Compose, PostgreSQL, Redis, CeleryExecutor,
and Gmail SMTP email notifications.

## Project Structure

```text
airflow-docker/
├── dags/
├── logs/
├── plugins/
├── config/
├── .env.example
├── .gitignore
├── docker-compose.yaml
└── README.md
Prerequisites

Install:

Docker Desktop
Docker Compose

Check:

docker --version
docker compose version
Setup

Clone the repository:

git clone <YOUR_GITHUB_REPOSITORY>
cd airflow-docker

Create .env from .env.example:

Copy-Item .env.example .env

Edit .env:

AIRFLOW_UID=50000
AIRFLOW_EMAIL=your-email@gmail.com
GMAIL_APP_PASSWORD=your-gmail-app-password

Do not commit .env.

Start Airflow

Initialize the database:

docker compose up airflow-init

Start Airflow:

docker compose up -d

Check containers:

docker compose ps

Open:

http://localhost:8080

Stop Airflow
docker compose stop

Start again:

docker compose start

Or:

docker compose down

Do not use:

docker compose down -v

unless you intentionally want to delete the PostgreSQL data.

Check DAGs
docker compose exec airflow-worker airflow dags list
Trigger DAG
docker compose exec airflow-worker airflow dags trigger email_failure_test
Check Logs
docker compose logs airflow-worker --tail 100

Follow logs:

docker compose logs -f airflow-worker
SMTP Test
docker compose exec airflow-worker python -c "from airflow.providers.smtp.hooks.smtp import SmtpHook; h=SmtpHook(smtp_conn_id='smtp_default'); h.get_conn(); print('SMTP CONNECTION SUCCESS')"
Security

Never commit:

.env
Gmail App Password
API keys
passwords
tokens
private keys

Use .env.example to document required environment variables.


---

# 7. Before pushing, check what Git will upload

This step is **very important**.

Run:

```powershell
git status

You should NOT see:

.env

You should see things like:

docker-compose.yaml
.env.example
.gitignore
README.md
dags/...
8. Initialize Git

From:

C:\Users\erkum\airflow-docker

run:

git init

Then:

git add .

Check:

git status

Again verify that .env is not listed.

9. Commit
git commit -m "Initial Airflow Docker setup with email notifications"
10. Create GitHub repository

Go to GitHub and create a new repository.

For example:

airflow-docker-email-notification

I recommend:

Public → if you're comfortable sharing the project
Private → if this is just for your personal learning/work

Do not upload your .env manually through GitHub either.

11. Connect local project to GitHub

GitHub will give you a repository URL.

Then:

git remote add origin YOUR_GITHUB_REPOSITORY_URL

For example:

git remote add origin https://github.com/YOUR_USERNAME/airflow-docker-email-notification.git

Then:

git branch -M main

And:

git push -u origin main
12. What another person does

This is the important part.

They clone:

git clone https://github.com/YOUR_USERNAME/airflow-docker-email-notification.git

Then:

cd airflow-docker-email-notification

Create their own .env:

Copy-Item .env.example .env

Then they put their own Gmail credentials:

AIRFLOW_UID=50000
AIRFLOW_EMAIL=their-email@gmail.com
GMAIL_APP_PASSWORD=their-own-app-password

Then:

docker compose up airflow-init

and:

docker compose up -d