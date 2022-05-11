from robusta.api import *


@action
def delete_pod(event: PrometheusKubernetesAlert):
if not event.get_pod():
    logging.info("alert is not related to pod")
    return

event.get_pod().delete()
