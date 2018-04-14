from typing import Any, Dict, Optional
from models.room import Room

rooms: Dict[str, Room] = {}


def register_room(room: Room) -> None:
    rooms[room.room_id.lower()] = room


def get_room(room_id: str, default: Any = None) -> Optional[Room]:
    return rooms[room_id] if room_exist(room_id) else default


def room_exist(room_id: str):
    return room_id in rooms
