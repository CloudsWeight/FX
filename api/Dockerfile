FROM node:23-bookworm


RUN useradd -m -d /home/new_user new_user
# change the uid of new_user to ensure it has whatever it was assigned plus 1 (e.g. if UID was 1000, now it'll be 1001)
RUN id -u new_user | awk '{print $1+1}' | xargs -I{} usermod -u {} new_user
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y

# Copy the rest of the source files into the image.

COPY /app .
#RUN sudo chown -R $(id -u):$(id -g) ~/.npm

# Expose the port that the application listens on.
EXPOSE 43451

RUN npm install 
CMD node server.cjs

