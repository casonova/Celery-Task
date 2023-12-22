
# Timezone Update Project


The Project creates dummy data of 100 customers and update their time from utc to pst after every 5 minutes thorough cron job.

# Key Features
- Create Records of Customer Create dummy data of 100 customers by runing custom management command.
- Update Records Fetch records of 10 customer and update their timeformat from utc to pst after every 5 minutes through implementation of django-celery






## Installation
To install and run the project locally, follow the steps:

1. Clone the repository:


```bash
https://github.com/casonova/Celery-Task.git
```
2. Make Virtual environment:

```bash
python3 -m venv env
```  

3. Install dependencies:

```bash
pip install -r requirements.txt
```    
4. Apply database migrations:
```bash
python manage.py makemigrations
```  

```bash
python manage.py migrate
```    
5. Make data of 100 customer by runing management commands
```bash
python manage.py create_data
```
6. Run redis by command
```
redis-server
```
7. Run celery in project terminal by command
```
celery -A project worker -l info
```
8. Run celery beat by 
```
celery -A project beat -l info  
```

 
 
## Usage
1. Create a superuser:

```javascript
python manage.py createsuperuser
```
4. Make groups by runing custom management command.
```
python manage.py make_groups
```

5. Access the admin panel at `http://127.0.0.1:8000/admin/` to see the data.







## Credits

- [Django Framework](https://www.djangoproject.com/)
- [Redis](https://redis.io/)





