FROM continuumio/anaconda3


#ADD environment.yml /tmp/environment.yml
#RUN conda env create -f /tmp/environment.yml
#
## Pull the environment name out of the environment.yml
#RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
#ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH
#RUN mkdir -p /var/chatbot-docker
#WORKDIR /var/chatbot-docker/chatbotbackend
#COPY ./ /var/chatbot-docker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#tworzę folder 
#kopiuję pliki

RUN mkdir -p /var/chatbot-docker
COPY ./ /var/chatbot-docker
WORKDIR /var/chatbot-docker/chatbotbackend


RUN conda env create -f /var/chatbot-docker/environment.yml
ENV PATH /opt/conda/envs/olaf/bin:$PATH
RUN /bin/bash -c "source activate olaf"


RUN cd /var/chatbot-docker/chatbotbackend



EXPOSE 8000:8000
ENTRYPOINT python manage.py runserver localhost:8000 