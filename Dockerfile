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
#
RUN mkdir -p /var/chatbot-docker
COPY ./ /var/chatbot-docker
WORKDIR /var/chatbot-docker/chatbotbackend

#ADD environment.yml /var/chatbot-docker/environment.yml

RUN conda env create -f /var/chatbot-docker/environment.yml
ENV PATH /opt/conda/envs/robo-warsaw/bin:$PATH
RUN /bin/bash -c "source activate robo-warsaw"

RUN conda uninstall -n robo-warsaw nltk
RUN conda install -n robo-warsaw nltk

RUN cd /var/chatbot-docker/chatbotbackend

#RUN conda install -n robo-warsaw nltk

#RUN python manage.py makemigrations
#RUN python manage.py migrate

RUN ls /opt/conda/envs/robo-warsaw
EXPOSE 8000:8000
ENTRYPOINT python manage.py runserver localhost:8000 