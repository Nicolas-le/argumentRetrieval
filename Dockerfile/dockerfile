FROM jupyter/base-notebook:latest

USER root  

RUN mkdir -p /src/app

WORKDIR src/app


RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y \
        gcc \
        build-essential \
        zlib1g-dev \
        wget \
        unzip \
        cmake \
        python3-dev \
        gfortran \
        libblas-dev \
        liblapack-dev \
        libatlas-base-dev \
    && apt-get clean

# Install Python packages
RUN pip install --upgrade pip \
    && pip install \
        ipython[all] \
        numpy \
        nose \
        matplotlib \
        pandas \
        scipy \
        sympy \
        cython \
		scikit-learn\
    && rm -fr /root/.cache

COPY requirments.txt  .  

RUN pip install -r requirments.txt

EXPOSE 8888

CMD ["jupyter", "notebook", "--port=8888", "--allow-root","--no-browser", "--ip=0.0.0.0"]


