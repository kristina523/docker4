FROM nginx:alpine

LABEL version="1.0.1"
LABEL description="Static HTML Website"

COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

