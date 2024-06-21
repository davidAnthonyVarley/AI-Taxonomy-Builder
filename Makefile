.PHONY: frontend backend

all: frontend backend

ifeq ($(OS),Windows_NT)
    frontend:
	@echo "Starting frontend..."
	cd taxonomy-builder-app/demos/react-demo/frontend && npm i && npm start

    backend:
	@echo "Starting backend..."
	cd taxonomy-builder-app/demos/react-demo/backend && uvicorn test_api:app --reload --port=8000 --host=0.0.0.0
else
    frontend:
    	@echo "Starting frontend..."
    	gnome-terminal --working-directory=./taxonomy-builder-app/demos/react-demo/frontend -e 'npm start'
    
    backend:
    	@echo "Starting backend..."
    	gnome-terminal --working-directory=./taxonomy-builder-app/demos/react-demo/backend -e 'uvicorn test_api:app --reload --port=8000 --host=0.0.0.0'
endif
