# USE PYTHON AS BASE IMAGE
FROM python
WORKDIR /backend

# INSTALL BACKEND DEPENDENCIES
COPY ./requirements.txt /demo/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /demo/requirements.txt

# COPY FILES USED BY APP AND API
COPY . /backend
ADD ./.env .

# EXPOSE BACKEND API PORT
EXPOSE 8000


# START
CMD ["uvicorn", "test_api:app", "--reload", "--port=8000", "--host=0.0.0.0"]
