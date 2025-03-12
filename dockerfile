# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Run database migrations (if using Flask-Migrate)
RUN flask db upgrade || true

# Ensure database migrations run at container startup
CMD ["sh", "-c", "flask db upgrade || true && flask run"]

