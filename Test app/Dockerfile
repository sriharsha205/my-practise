# Dockerfile
FROM alpine:latest

# Install nginx
RUN apk add --no-cache nginx

# Create necessary directories
RUN mkdir -p /run/nginx /usr/share/nginx/html

# Copy the index file
COPY index.html /usr/share/nginx/html/index.html

# Create a proper nginx.conf with newlines and structure
RUN printf 'events {}\n\
http {\n\
    server {\n\
        listen 80;\n\
        server_name localhost;\n\
        root /usr/share/nginx/html;\n\
        index index.html;\n\
    }\n\
}\n' > /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Run nginx in foreground (important for ECS & Docker)
CMD ["nginx", "-g", "daemon off;"]
