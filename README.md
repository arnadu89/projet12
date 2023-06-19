# Projet10

Clone the project :
```commandline
git clone git@github.com:arnadu89/projet12.git
```

Create virtual environment inside the cloned repository :
```commandline
python3 -m venv venv
```

Activate venv :
```commandline
source venv/bin/activate
```

Install dependencies :
```commandline
pip install -r requirements.txt
```

Import database from file :
```commandline
sudo -u postgres pg_restore -c -F t -d db_p12 db_p12.tar
```

Launch server :
```commandline
python3 manage.py runserver
```
