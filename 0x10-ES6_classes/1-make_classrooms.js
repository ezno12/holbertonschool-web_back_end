import ClassRoom from './0-classroom'
let num = [19, 20, 34]

export default function initializeRooms(num) {
    return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)]
}