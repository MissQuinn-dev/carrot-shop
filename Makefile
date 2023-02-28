build:	
	cd carrotshop && docker build . -t carrot-shop

run:
	docker run -it --rm -p 8000:8000 carrot-shop
