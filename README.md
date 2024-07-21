# Test task

Training notebook: `train_model.ipynb` - used Google Colab to train the model.

To run the server locally:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `fastapi dev server.py`

Example request:
```
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "A quick brown fox jumps over a lazy dog"
}'
```

or from Swagger interface on http://127.0.0.1:8000/docs.
