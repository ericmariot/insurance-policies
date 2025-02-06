# Insurance policies

This is a REST API for managing insurance policies.

You can check a live demonstration at [insurance-policies](https://insurance-policies.fly.dev/policies/) that was deployed with [fly.io](https://fly.io/)

---

## How to run the application with Docker

1. Clone and Move to the project:
```
git@github.com:ericmariot/insurance-policies.git
cd insurance-policies
```

2. Build the docker image
```
docker build -t insurance-policies . 
```

3. Run the project
```
docker run -p 8000:8000 insurance-policies
```

It should be up at the designated port, in this case [http://0.0.0.0:8000/policies/](http://0.0.0.0:8000/policies/)

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

And more documentation at the endpoint `/swagger/` or in the [deployed project](https://insurance-policies.fly.dev/swagger/)

7. Tests can be ran with
```
pytest
```

## API Collection

You can find a full postman collection at [`insurance-policies.postman_collection.json`](https://github.com/ericmariot/insurance-policies/blob/main/insurance-policies.postman_collection.json).

```
api = 127.0.0.1:8000

[DOCS] {{api}}/swagger/

[POST] {{api}}/policies/
[GET] {{api}}/policies/
[GET] {{api}}/policies/11ef0546-f682-4ee8-ae5b-55dbae196163/
[PUT] {{api}}/policies/11ef0546-f682-4ee8-ae5b-55dbae196163/
[DEL] {{api}}/policies/11ef0546-f682-4ee8-ae5b-55dbae196163/
```