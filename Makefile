.PHONY: all test format imports runserver migrate help

all: imports format migrate runserver

test:
	$(PYTHON) -m pytest

format:
	ruff format $(SRC_DIR) $(TESTS_DIR)

imports:
	isort .

runserver:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

help:
	@echo "Available targets:"
	@echo "  all           - Run format, migrate, runserver"
	@echo "  format        - Format code using ruff"
	@echo "  imports       - Format imports using isort"
	@echo "  runserver     - runs Django server"
	@echo "  migrate       - runs migrations"
	@echo "  help          - Show this help message"
	@echo "  test          - Run all tests"
