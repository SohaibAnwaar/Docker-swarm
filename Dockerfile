FROM continuumio/miniconda

MAINTAINER sohaibanwaar36@gmail.com

RUN mkdir /working_dir

COPY  . /working_dir

WORKDIR working_dir

RUN apt-get update 

RUN conda create -n "mongo_testing" python=3.6 pymongo

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["conda run -n mongo_testing python CSR.py"]