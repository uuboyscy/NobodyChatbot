FROM jupyter/base-notebook
RUN pip install Flask==0.12 requests line-bot-sdk
RUN pip install redis MySQL-python
