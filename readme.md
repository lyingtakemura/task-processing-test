celery periodic check is set to run every one minute

tasks.py/add_waiting_time_to_task:
upon object creation this task will be triggered with newly created object inside
inside this task we take current time with django built-in timezone.now() (works the same way as datetime.now but considers timezone from config)
then we generate random timedelta between 1 and 8 minutes maximum
current time + timedelta = waiting_time

tasks.py/update_status_if_waiting_time_is_expired:
filter out from tasks all object where waiting_time timestamp is less then or equals to current_time (by the moment of celery periodic run), if there's any - update in bulk statuses to 'done'

endpoints (drf browsable api is available):
- GET http://localhost:8000/tasks/
- GET http://localhost:8000/tasks/TASK_ID
- POST http://localhost:8000/tasks/