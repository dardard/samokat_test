import configuration
import data
import requests
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER,
                         json=body,
                         headers=data.order_headers)
def get_order(track):
    return requests.get(configuration.URL_SERVICE+configuration.GET_ORDER,
                        params={"t": track})
