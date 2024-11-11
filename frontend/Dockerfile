# Frontend Dockerfile

# Use Node as the base image
FROM node:18

# Set working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the frontend code into the container
COPY . .

# Build the frontend
RUN npm run build

# Expose the frontend port (default for Vite is 5173)
EXPOSE 5173

# Command to start the frontend server
CMD ["npm", "run", "dev"]
