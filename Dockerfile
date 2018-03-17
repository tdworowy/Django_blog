# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.6-jessie
ENV PYTHONPATH $PWD/Django_test
EXPOSE 8082:8082
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install Django
RUN pip install Django-taggit
RUN pip install haystack
RUN git clone http://github.com/tdworowy/Django_blog.git
