FROM node:23-bookworm

WORKDIR /app
COPY /app .
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
CMD ["cd", "app"]
RUN apt update 
RUN apt install -y python3-pip 
CMD ["whoami"]
RUN sudo pip install -r requirements.txt
EXPOSE 3333
RUN sudo pip freeze
#CMD ["python3", "main.py"]
