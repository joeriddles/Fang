FROM node:14 as base
EXPOSE 4200
WORKDIR /app
COPY ["./frontend/package.json", "./frontend/package-lock.json", "./"]
RUN npm ci
ENTRYPOINT [ "npm" ]
CMD [ "run", "watch" ]

FROM base as build
COPY ./frontend /app/
RUN npm run build
CMD [ "run", "start" ]


FROM nginx as prod
COPY --from=build /app/dist /usr/share/nginx/html
