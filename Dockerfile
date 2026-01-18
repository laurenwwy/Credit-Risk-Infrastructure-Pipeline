# The Content (python:3.9-slim):
# Instead of starting with a blank computer and installing Windows/Linux, you are starting with a lightweight version of Linux that already has Python 3.9 installed.
# The word slim means it is a small version with no unnecessary junk, making it faster to download and more secure (fewer files for hackers to attack).
FROM python:3.9-slim
# The Command (WORKDIR): This stands for "Working Directory."
# The Content (/app):
# Inside the virtual computer, this creates a folder called /app and "walks into it" (like the cd command in your terminal).
# Every command after this will happen inside this folder. It keeps the computer organized.
WORKDIR /app
# The Content (. .):
# The first dot means "everything in my current folder on my laptop."
# The second dot means "the current folder inside the Docker image" (which is /app).
# In short: It copies your Python scripts, your CSV data, and your README into the container.
COPY . .
# The Command (RUN): This tells Docker to execute a command during the setup phase.
# The Content: This installs all the libraries your project needs.
# The Benefit: This is why Docker is powerful. You don't have to tell your coworker 
# "Hey, you need to install these 3 libraries." Docker does it automatically when the container is built.
RUN pip install pandas pyspark pyarrow
# The Command (CMD): This stands for "Command." It is the final instruction.
# The Content: It tells the virtual computer: "The moment you start up, immediately run python risk_engine.py."
# Difference between RUN and CMD:
# RUN happens when you are building the computer (installing tools).
# CMD happens when you turn on the computer (running the actual work).
CMD ["python", "risk_engine.py"]