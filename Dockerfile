FROM python:3.11.3-slim-bullseye

RUN apt update && apt install -y \
    curl \
    vim \
    wget \
    # needed for the odbc driver
    unixodbc \
    unixodbc-dev \
    gnupg
    

# define environment variables
ARG DATABASE_USERNAME
ENV DATABASE_USERNAME=$DATABASE_USERNAME

ARG DATABASE_PASSWORD
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD

# install the odbc driver for SQL Server, version 18
## Here this installs the driver based on instruction for Debian 11 since "bullseye" is based on it.
## https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=debian18-install%2Cubuntu17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt update && \
    ACCEPT_EULA=Y apt install -y mssql-tools18

# change workind directory before copying source files
WORKDIR /usr/src

# install dependencies
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# run the default command which starts the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]