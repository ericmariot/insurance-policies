# Insurance policies

This is a REST API for managing insurance policies.

---

## How to run the application locally

1. Clone and Move to the project:
```
git@github.com:ericmariot/insurance-policies.git
cd insurance-policies
```

2. Create a `.env` file, use the `.env.example` as example.

3. Create a venv and start it:
```
python -m venv .venv
source .venv/bin/activate
```

4. Install the requirements:
```
pip install -r requirements-dev.txt
```

5. Run the migrations
```
python manage.py migrate
```


6. Start the server
```
python manage.py runserver
```

You can check the server heatlh at [127.0.0.1:8000/healthz](127.0.0.1:8000/healthz)

And more endpoints at the [API Collection](#api-collection)

7. Tests can be ran with
```
pytest
```

## API Collection

You can find a full postman collection at [`insurance-policies.postman_collection.json`](https://github.com/ericmariot/insurance-policies/blob/main/insurance-policies.postman_collection.json).

```
api = 127.0.0.1:800

[POST] {{api}}/policies/
[GET] {{api}}/policies/
[GET] {{api}}/policies/1/
[PUT] {{api}}/policies/1/
[DEL] {{api}}/policies/1/
```