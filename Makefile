.PHONY = build clean run test

build:
	docker build -t app:v1 .

clean:
	docker rmi app:v1

run:
	docker run -d app:v1
    # docker run -it --rm app:test1 /bin/bash

test:
	python -m pytest