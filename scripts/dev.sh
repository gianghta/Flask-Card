#!/bin/bash

# Run a local dev environment
set -e
export MODE=development

# Register cleanup function on exit
clean_up () {
    ARG=$?
		echo 'Stopping the database container...'
		docker-compose down
    exit $ARG
}
trap clean_up EXIT

# Run the project in Docker environment
docker-compose up