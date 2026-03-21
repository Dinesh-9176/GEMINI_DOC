# FastAPI PUT Example

This is a simple example of a `PUT` request in FastAPI, used to update an existing resource.

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

## Testing the PUT Endpoint

You can test the endpoint using the interactive documentation at `http://127.0.0.1:8000/docs` or by using `curl`:

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Gaming Laptop",
  "price": 1299.99,
  "is_offer": true
}'
```

You can then verify the update by visiting `http://127.0.0.1:8000/items/1` in your browser.
