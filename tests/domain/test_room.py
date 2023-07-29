import uuid
from rootmatic.domain.room import Room

def test_room_model_init():
    code = uuid.uuid4
    room = Room(code, size=200, price=10, longitude=-0.09998975, lantitude=51.75436293)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.lantitude == 51.75436293
