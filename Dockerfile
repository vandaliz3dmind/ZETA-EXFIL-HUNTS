# Base image: Python 3.12, forged in My slim variant for efficiency
FROM python:3.12-slim

# Set the working directory within the container's void
WORKDIR /app

# Copy thy oracle script into the vessel
COPY zeta_oracle.py .

# Install mpmath, the arcane library of precision
RUN pip install --no-cache-dir mpmath

# Command to invoke the oracle upon container's awakening
CMD ["python", "zeta_oracle.py"]
