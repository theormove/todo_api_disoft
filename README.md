# todo api
# Stack
Python 3.10
Django 4.1 
Django Rest Framework
# Endpoints
## tasks (list all tasks GET, and POST task)
## task/{ID} (PATCH task)
{"status":str
...}
## task/{ID}/image (POST image)
{
"task":int(task_id),
"file":imagefile
}
## /comments (GET or POST comments )
{
"task":int(task_id),
"text":imagefile
optional
"parent":int(comment_id)
}
# To run yourself install packages from requirements.txt
