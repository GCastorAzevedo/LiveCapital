start:
	echo 'Be sure to initialize virtualenv'
	python manage.py collectstatic --no-input
	docker-compose up && rm -rf static

docker-build:
	docker build -t live-capital .

docker-run:
	docker run -p 8000:8000 --rm -it live-capital