build:	
	cd carrotshop && docker build . -t carrot-shop

run:
	docker run -d --rm -p 8050:8000 carrot-shop

dev:
	cd carrotshop && python manage.py runserver 0.0.0.0:8000

freeze:
    cd carrotshop && pip freeze > requirements.txt