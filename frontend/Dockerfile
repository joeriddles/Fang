FROM node:14 as base
EXPOSE 4200
USER node
WORKDIR /app
COPY ["./frontend/package.json", "./frontend/package-lock.json", "./"]
RUN npm ci
ENTRYPOINT [ "npm" ]
CMD [ "run", "watch" ]

FROM base as build
COPY ./frontend /app/
RUN npm run build-prod

FROM nginx as prod
COPY --from=build /app/dist/frontend /usr/share/nginx/html
