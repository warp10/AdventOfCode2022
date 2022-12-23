#!/usr/bin/env python3

def is_ok(row, column, sensors, beacons):
    for sensor_x, sensor_y, distance in sensors:
        if distance >= abs(row - sensor_x) + abs(column - sensor_y) and (row, column) not in beacons:
            return False
    return True

def load_sensors_and_beacons(inputs):
    sensors = []
    beacons = []

    for line in inputs:
        items = line.split()
        sensor_x = int(items[2][2:-1])
        sensor_y = int(items[3][2:-1])
        beacon_x = int(items[8][2:-1])
        beacon_y = int(items[9][2:])
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensors.append((sensor_x, sensor_y, distance))
        beacons.append((beacon_x, beacon_y))

    return sensors, beacons

def calculate_tuning_frequency(sensors, beacons):
    MAX_COORD = 4000000

    for sensor_x, sensor_y, distance in sensors:
        for distance_x in range(distance + 2):
            distance_y = (distance + 1) - distance_x
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                full_x, full_y = sensor_x + (distance_x * mx), sensor_y + (distance_y * my)
                if not(0 <= MAX_COORD and 0 <= full_y <= MAX_COORD):
                    continue
                if is_ok(full_x, full_y, sensors, beacons):
                    return full_x * MAX_COORD + full_y

def main(filename):
    with open(filename) as f:
        inputs = f.read().splitlines()

    sensors, beacons = load_sensors_and_beacons(inputs)

    return calculate_tuning_frequency(sensors, beacons)

if __name__ == "__main__":
    print(main("input.txt"))
