pip install -r requirements.txt
python3.9 manage.py migrate
echo yes | python3.9 manage.py collectstatic