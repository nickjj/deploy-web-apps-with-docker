# Use the barebones version of Python 2.7.10.
FROM python:2.7.10-slim
MAINTAINER Nick Janetakis <nick.janetakis@gmail.com>

# Install any packages that must be installed.
RUN apt-get update && apt-get install -qq -y build-essential --fix-missing --no-install-recommends

# Set up the install path for this service.
ENV INSTALL_PATH /rediscounter
RUN mkdir -p $INSTALL_PATH

# Update the workdir to be where our app is installed.
WORKDIR $INSTALL_PATH

# Ensure packages are cached and only get updated when necessary. If we didn’t do this step then every time we pushed an app change it would also re-run pip install, even if no packages changed.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the source from your workstation to the image at the WORKDIR path.
COPY . .

# Create a volume so that nginx can read from it.
VOLUME ["$INSTALL_PATH/build/public"]

# The default command to run if no command is specified.
CMD python app.py
