from celery import shared_task
from user.models import User
from purchase.models import Purchase


@shared_task
def my_task_user_create():
    print('+++++ User created +++++')


@shared_task
def print_user_count():
    users = User.objects.all()
    print(f'Users: {users.count()}')


@shared_task
def my_task_list():
    print('++++++ Just a message to print something…')


@shared_task
def my_task_retrieve(user_id):
    purchases = Purchase.objects.filter(user_id=user_id)
    print(f'User #{user_id} has done {purchases.count()} purchases')





# celery задачу, яка буде друкувати будь-який текст.
# celery задачу, яка буде приймати параметр user_id і друкувати кількість
# purchases для цього користувача.
