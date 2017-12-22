from blueking.component.shortcuts import get_client_by_request, get_client_by_user


def celery_test():
    user = 'public'
    client = get_client_by_user(user)
    kwargs = {'app_id': '3'}
    result = client.cc.get_app_host_list(kwargs)
    return result


def execute(taskid):
    user = 'public'
    client = get_client_by_user(user)
    kwargs = {'app_id': '3', 'task_id': taskid}
    result = client.job.execute_task(kwargs)

    # result = client.cc.get_app_host_list(kwargs)
    return result


def query(task_instance_id):
    user = 'public'
    client = get_client_by_user(user)
    kwargs = {'app_id': '3', 'task_instance_id': task_instance_id}
    result = client.job.get_task_result(kwargs)
    return result


def get_hf_data():
    user = 'public'
    client = get_client_by_user(user)
    result = client.hf_sys.get_data()
    return result
