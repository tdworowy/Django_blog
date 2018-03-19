# Dockerfile
#TODO
# jest problem z ENTRYPOINT albo z CMD (albo z obu)
# FROM directive instructing base image to build upon
FROM python:3.6-jessie
ENV PYTHONPATH $PWD/Django_blog
#ENTRYPOINT ["python", "/Django_blog/TestFile.py]"]
 # może być tylko 1,  to albo CMD
#EXPOSE 8083
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install Django
RUN pip install Django-taggit
RUN pip install haystack
RUN git clone http://github.com/tdworowy/Django_blog.git
# CMD powinno się samo uruchomić, nie wiem czy da się wiecej
#CMD ["python", "-u","/Django_blog/TestFile.py"]
#CMD ["python","-u", "/Django_blog/Example/Example1/blog/Utils/runMigration.py"]
CMD ["python","-u", "/Django_blog/Example/Example1/blog/Utils/startServer.py"]