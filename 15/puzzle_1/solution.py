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

def calculate_ko_positions(sensors, beacons, target_row):
    ko_positions = 0
    for row in range(
        min(row - distance for row, _, distance in sensors),
        max(row + distance for row, _, distance in sensors)
    ):
        if not is_ok(row, target_row, sensors, beacons) and (row, target_row) not in beacons:
            ko_positions += 1

    return ko_positions

def main(filename, target_row):
    with open(filename) as f:
        inputs = f.read().splitlines()

    sensors, beacons = load_sensors_and_beacons(inputs)

    return calculate_ko_positions(sensors, beacons, target_row)

if __name__ == "__main__":
    print(main("input.txt", 2000000))
