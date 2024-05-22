/* eslint-disable */
import ClassRoom from "./0-classroom";
/* eslint-disable */

export default function initializeRooms() {
  const roomsSize = [19, 20, 34]
  const rooms = roomsSize.map((size) => new ClassRoom(size))
  return rooms
}
