FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

ENV FELIPE_API_KEY=replace_with_your_api_key
ENV FELIPE_ASSISTANT_ID=replace_with_your_api_key
ENV SERGIO_API_KEY=replace_with_your_api_key
ENV SERGIO_ASSISTANT_ID=replace_with_your_api_key

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
