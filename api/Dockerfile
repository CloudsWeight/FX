FROM node:23-bookworm


# Run the application as a non-root user.
USER node

# Copy the rest of the source files into the image.
COPY /app .


# Expose the port that the application listens on.
EXPOSE 43451
CMD ["cd", "/app"]
CMD ["npm", "install"]
CMD ["node", "server.cjs"]
CMD ["python", "main.py"]
