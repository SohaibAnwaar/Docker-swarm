FROM continuumio/miniconda

MAINTAINER sohaibanwaar36@gmail.com

RUN mkdir /working_dir

COPY  . /working_dir

WORKDIR working_dir


RUN apt-get update -qq && apt-get install -y build-essential bash

RUN conda init bash && conda update -n base -c defaults conda && conda create -n mongo_testing python=3.6 pymongo

RUN  . ~/.bashrc


Run echo "source activate mongo_testing && python CSR.py" > driver.sh

ENTRYPOINT ["/bin/bash", "driver.sh"]
