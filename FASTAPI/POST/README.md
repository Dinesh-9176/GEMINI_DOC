# FastAPI POST Example

This is a simple example of a `POST` request in FastAPI using Pydantic for request body validation.

## How to Run

1.  Make sure you have FastAPI and Uvicorn installed:
    ```bash
    pip install fastapi uvicorn
    ```

2.  Run the application:
    ```bash
    fastapi dev app.py
    ```

3.  The API will be available at `http://127.0.0.1:8000`.

## Testing the POST Endpoint

You can test the endpoint using the interactive documentation at `http://127.0.0.1:8000/docs` or by using `curl`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Smartphone",
  "price": 599.99,
  "is_offer": true
}'
```
