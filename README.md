# volleyball-rotation-visualizer

A small Django app that visualizes one side of a volleyball court for a **5-1 system**.

Included states:
- Serve
- Serve-receive
- After first touch on our side
- After first touch on opponent side

## Run locally

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.
