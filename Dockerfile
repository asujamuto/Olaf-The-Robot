FROM continuumio/anaconda3


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/chatbot-docker
COPY ./ /var/chatbot-docker
WORKDIR /var/chatbot-docker/chatbotbackend


RUN conda env create -f /var/chatbot-docker/environment.yml
ENV PATH /opt/conda/envs/olaf/bin:$PATH
RUN /bin/bash -c "source activate olaf"


RUN cd /var/chatbot-docker/chatbotbackend



EXPOSE 8000:8000
ENTRYPOINT python manage.py runserver localhost:8000 