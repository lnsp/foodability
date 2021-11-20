FROM node:16-alpine as node

WORKDIR /app

ADD . /app
RUN yarn install
RUN yarn run generate

FROM nginx:alpine

COPY --from=node /app/dist /usr/share/nginx/html
EXPOSE 80

