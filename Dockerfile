FROM python:3.10-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1




RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt


RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S -G app app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME



RUN pip install --upgrade pip
COPY ./requirements.txt $APP_HOME 
RUN pip install -r requirements.txt
# copy project

COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

