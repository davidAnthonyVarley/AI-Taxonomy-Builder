# USE NODE AS BASE IMAGE
FROM node
WORKDIR /frontend

# INSTALL FRONTEND DEPENDENCIES
COPY ./package*.json .
RUN npm install 


# COPY FILES USED BY REACT APP
COPY ./src /frontend/src
COPY ./public /frontend/public

# EXPOSE REACT APP PORT
EXPOSE 3000

# START
CMD ["npm", "start"]
