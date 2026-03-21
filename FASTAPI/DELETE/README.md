# FastAPI DELETE Example

This is a simple example of a `DELETE` request in FastAPI, used to remove an existing resource.

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

## Testing the DELETE Endpoint

You can test the endpoint using the interactive documentation at `http://127.0.0.1:8000/docs` or by using `curl`:

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json'
```

You can then verify the deletion by visiting `http://127.0.0.1:8000/items/` in your browser.
