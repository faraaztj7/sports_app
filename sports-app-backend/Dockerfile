# Use Python as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the backend requirements file and install dependencies
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv /venv

# Install dependencies in the virtual environment
RUN /venv/bin/pip install --upgrade pip && /venv/bin/pip install -r requirements.txt

# Copy the backend code into the container
COPY . .

# Step 7: Copy the tests directory (if you want to include test files in the image)
COPY tests/ /tests/

# Step 8: (Optional) Run tests during the build process (if needed)
# If you want to run tests during the build process, update the path to your test files
RUN /venv/bin/python -m pytest tests/test_*.py --disable-warnings -q

# Expose the backend port
EXPOSE 5000

# Command to activate the virtual environment and start the Flask server
CMD ["/bin/bash", "-c", "source /venv/bin/activate && exec python run.py"]
