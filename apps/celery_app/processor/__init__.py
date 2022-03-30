from celery import Task
class MyTask(Task):
    def before_start(self, task_id, args, kwargs):
        return super().before_start(task_id, args, kwargs)
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        return super().after_return(status, retval, task_id, args, kwargs, einfo)
    def on_success(self, retval, task_id, args, kwargs):
        return super().on_success(retval, task_id, args, kwargs)
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        return super().on_failure(exc, task_id, args, kwargs, einfo)
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        return super().on_retry(exc, task_id, args, kwargs, einfo)