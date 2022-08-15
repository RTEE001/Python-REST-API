create a REST api to interact with actual database (263)
For raw project instructions see: http://syllabus.africacode.net/projects/python-specific/flask-rest-api/part-1/

## Setup

Install the dependencies required using

```
pip install -r requirements.txt
```

Create a ".env" file in the root directory
In your .env file you should have the following details

```
PASSWORD = <YOUR_PASSWORD>
USERNAME= <YOUR_USERNAME>
URL = <A_VALID_CONNECTION_URL>
```

Run the docker file using

```
docker compose up
```

Run the umuzi_computers.py scipt using

```
python3 umuzi_computers.py
```

Run the umuzi_api.py script using

```
python3 umuzi_api.py
```

On the terminal it will show the address on which the app is running.

To list all the available computers, use:

```
curl -v <address on which the app running>/get-computers
```

To add a computer, use:

```
curl -d '{<details of the computer>}' -H 'Content-Type: application/json' <address on which the app running>/add-computer
```

To edit a compter, use:

```
curl -d '{ <updated details of the computer>}' -H 'Content-Type: application/json' -X PUT <address on which the app running>/edit-computer?id=<id to be deleted>
```

To delete a computer, use:

```
curl -X DELETE <address on which the app running>/delete-computer?id=<id to be deleted>
```
