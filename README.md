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
PASSWORD = <YOUR_PASSWORD FOR DOCKER>, Example PASSWORD = password
USERNAME= <YOUR_USERNAME FOR DOCKER>, Example USERNAME = user
SQLALCHEMY_DATABASE_URI = <A_VALID_CONNECTION_URL for your database>,
Example SQLALCHEMY_DATABASE_URI = postgresql+psycopg2://user:password@localhost:5435/computers
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

### Using curl:

To list all the available computers, use:

```
curl -v <address on which the app running>/computers
```

To add a computer, use:

```
curl -d '<details of the computer>' -H 'Content-Type: application/json' <address on which the app running>/computers

details should be a json, for example
{
        "form_factor": "mini",
        "harddrive_space": 256,
        "harddrive_type": "hdd",
        "max_ram": 8,
        "processor": "intel",
        "ram_amount": 7.6
}
```

To edit a compter, use:

```
curl -d '<updated details of the computer>' -H 'Content-Type: application/json' -X PUT <address on which the app running>/computers/<id to be edited>

details should be a json, for example
{
        "form_factor": "mini",
        "harddrive_space": 256,
        "harddrive_type": "hdd",
        "max_ram": 8,
        "processor": "intel",
        "ram_amount": 7.6
}

You may opt to edit all the details or just do partial edits
```

To delete a computer, use:

```
curl -X DELETE <address on which the app running>/computers/<id to be deleted>
```

### Using postman:

To list all the available computers:

```
Select 'GET' from the dropdown on the left
Type in <address on which the app is running>/computers in the address bar
Click send on the far right

```

To add a computer:

```
Select 'POST' from the dropdown on the left
Type in <address on which the app is running>/computers in the address bar
Selct body, then raw and switch from the default text to json
Add details of the computer you want to add under body, in json format, for example:
{
        "form_factor": "mini",
        "harddrive_space": 256,
        "harddrive_type": "hdd",
        "max_ram": 8,
        "processor": "intel",
        "ram_amount": 7.6
}
Click send on the far right

```

To edit a computer

```
Select 'PUT' from the dropdown on the left
Type in <address on which the app is running>/computers/<id of computer to edit> in the address bar
Selct body, then raw and switch from the default text to json
Add details of the computer you want to add under body, in json format, for example:
{
        "form_factor": "mini",
        "harddrive_space": 256,
        "harddrive_type": "hdd",
        "max_ram": 8,
        "processor": "intel",
        "ram_amount": 7.6
}
Click send on the far right
You may opt to edit all the details or just do partial edits
```

To delete a computer, use:

```
Select 'DELETE' from the dropdown on the left
Type in <address on which the app is running>/computers<id of computer to delete> in the address bar
Click send on the far right
```
