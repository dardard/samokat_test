import data
import samokat_request
def get_track():
    response = samokat_request.post_new_order(data.order_body)
    track = response.json()['track']
    return track;
def test_code_equals_200():
    response=samokat_request.get_order(get_track())
    assert response.status_code == 200
    # Дарья Дараганова, 17-я когорта — Финальный проект. Инженер по тестированию плюс