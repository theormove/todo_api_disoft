# todo api
# Stack
Python 3.10
Django 4.1 
Django Rest Framework
# Endpoints
## tasks/ 
(list all tasks GET, and POST task)
## tasks/{SLUG} 
(filter by status)
## task/{ID} 
(PATCH task)
{"status":str
...}
## task/{ID}/image 
(POST image)
{
"task":int(task_id),
"file":imagefile
}
## /comments 
(GET or POST comments )
{
"task":int(task_id),
"text":imagefile
optional
"parent":int(comment_id)
}
# To run yourself install packages from requirements.txt
#Note
comments are raw
did not add gitignore file so there are some unnesesary files like _pycache_...
coverage only shows 83% and 58% on views.py so need to write more tests
