from fastapi.encoders import jsonable_encoder
from datetime import datetime
from service.models.api import Feature


def test_endpoint(call_endpoint):
    payload = jsonable_encoder(
        Feature(id=1, timestamp=datetime.now(), data={"test": 1234})
    )
    response = call_endpoint(payload)
    json_response = response.json()

    assert response.status_code == 200
    assert json_response == {"test": 1234}
