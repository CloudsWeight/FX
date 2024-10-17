# Use the official MongoDB image from Docker Hub
FROM mongo:latest

# Set environment variables (optional)
# You can set MongoDB environment variables like username, password, and database name
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=P@$$w0rd
ENV MONGO_INITDB_DATABASE=fx-data

# Copy initialization scripts if needed (optional)
# For example, you could initialize the database with collections or seed data
#COPY ./init-mongo.js /docker-entrypoint-initdb.d/

# Expose the MongoDB port
#EXPOSE 27017

# MongoDB uses the default entrypoint and runs automatically