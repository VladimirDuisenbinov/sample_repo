# syntax=docker/dockerfile:1

# -----------------------Base Layer-----------------------
FROM node:14-alpine as base

WORKDIR /web

# Netcat for Entrypoint
RUN apk add --no-cache netcat-openbsd

# Packages
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Entrypoint
COPY /docker/entrypoint.sh /react_env/entrypoint.sh
RUN sed -i 's/\r$//g' /react_env/entrypoint.sh
RUN chmod +x /react_env/entrypoint.sh

# Nginx Configuration
COPY /docker/nginx/nginx.conf /react_env/nginx.conf
RUN sed -i 's/\r$//g' /react_env/nginx.conf

COPY . .

RUN npm run build
# -----------------------Base Layer-----------------------

# --------------------Development Layer-------------------
FROM base as dev

USER root
RUN deluser --remove-home node

ENTRYPOINT ["/react_env/entrypoint.sh"]
# --------------------Development Layer-------------------

# --------------------Production Layer--------------------
FROM nginx:1.21.0-alpine as prod

COPY --from=base /web/build /usr/share/nginx/html
COPY --from=base /react_env/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=base /react_env/entrypoint.sh /react_env/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/react_env/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
# --------------------Production Layer--------------------
