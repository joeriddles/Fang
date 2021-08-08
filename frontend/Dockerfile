FROM node:latest as build
WORKDIR /usr/local/app
COPY ./frontend /usr/local/app/
RUN npm install
ENTRYPOINT [ "npm" ]
CMD [ "run", "start" ]
# RUN npm run build

# FROM nginx:latest
# COPY --from=build /usr/local/app/dist/frontend /usr/share/nginx/html
# EXPOSE 4200