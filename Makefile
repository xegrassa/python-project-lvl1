#makefile
install:
	poetry install 
lint:
	poetry run flake8 brain_games
del:
	pip uninstall -y xegrassa-brain-games
	pip uninstall -y prompt
