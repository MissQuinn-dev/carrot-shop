build:	
	cd carrotshop && docker build . -t carrot-shop

run:
	docker run -d --rm -p 8050:8000 carrot-shop
