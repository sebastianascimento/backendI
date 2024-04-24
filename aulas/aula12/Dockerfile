FROM python:3.12-slim

RUN pip install poetry 

RUN poetry config virtualenvs.create false

RUN pip install fastapi uvicorn

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["uvicorn" , "api.main:api" , "--host" , "0.0.0.0" , "--reload"]



