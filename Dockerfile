# Dockerfile
FROM python:3.6-jessie
ENV PYTHONPATH $PWD/Django_blog
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install Django
RUN pip install Django-taggit
RUN pip install haystack
RUN pip install requests
RUN pip install markdown
RUN git clone http://github.com/tdworowy/Django_blog.git
CMD ["python","-u", "/Django_blog/Example/Example1/blog/Utils/run_migration.py"]
CMD ["python","-u", "/Django_blog/Example/Example1/blog/Utils/start_server.py"]