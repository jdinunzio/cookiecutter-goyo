FROM python:3.10-slim
WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y adduser gcc make && \
    pip install --upgrade setuptools pip poetry coverage xdoctest unittest-xml-reporting pytest pytest-env

# add the appropriate user
RUN adduser --system --home /app --uid 1000 --group appuser

# add all current files, install dependencies (including dev) and build package
COPY . /app/
RUN chown -R appuser:appuser /app/
COPY --chown=appuser:appuser .pip.conf /etc/pip.conf

# NOTE: This will install the packages in this app in the system package folder
# (/usr/local/lib/python3.10/site-packages/{{cookiecutter.distro_name}}), so if you need to edit files inside the docker
# image, don't edit src/
RUN pip install .

# Dev image:
#RUN make project-init && \
#    poetry build
#

# Run everything as the appuser
USER appuser

ENTRYPOINT ["/usr/bin/make", "tests"]
