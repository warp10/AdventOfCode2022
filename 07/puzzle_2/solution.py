#!/usr/bin/env python3


class File:
    def __init__(self, name, size, parent, is_directory):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_directory = is_directory

    def __repr__(self):
        return self.name


class FileSystem:
    def __init__(self, disk_space):
        self.disk_space = disk_space
        self.free_space = disk_space
        self.root = File("/", 0, None, True)
        self.pwd = self.root
        self.files_list = [
            self.root,
        ]

    def exists(self, name):
        return name in self.files_list

    def sum_file_size(self, file, size):
        file.size += size
        if file.parent:
            self.sum_file_size(file.parent, size)

    def shrink_free_space(self, size):
        self.free_space -= size

    def create(self, name, size, parent, is_directory):
        f = File(name, size, parent, is_directory)
        self.files_list.append(f)
        return f

    def search(self, name):
        if name == "/":
            return self.root
        for f in self.files_list:
            if f.name == name and f.parent == self.pwd:
                return f

    def smallest_dir_to_free(self, min_size):
        smallest_dir = self.root
        for f in self.files_list:
            if f.is_directory and self.free_space + f.size >= min_size:
                    if f.size < smallest_dir.size:
                        smallest_dir = f
        return smallest_dir.size

class Parser:
    def __init__(self, fs):
        self.fs = fs

    def change_directory(self, path):
        if path == "..":
            self.fs.pwd = self.fs.pwd.parent
        else:
            res = self.fs.search(path)
            self.fs.pwd = res

    def add_directory(self, path):
        if not self.fs.exists(path):
            return self.fs.create(path, 0, self.fs.pwd, True)

    def add_file(self, path, size):
        if not self.fs.exists(path):
            res = self.fs.create(path, size, self.fs.pwd, False)
            self.fs.sum_file_size(self.fs.pwd, int(res.size))
            self.fs.shrink_free_space(int(res.size))
            return res

    def parse_command(self, command):
        if command[0] == "cd":
            self.change_directory(command[1])

    def read_line(self, line):
        split_line = line.split(" ")
        if split_line[0] == "$":
            self.parse_command(split_line[1:])
        elif split_line[0] == "dir":
            self.add_directory(split_line[1])
        else:
            res = self.add_file(split_line[1], split_line[0])

    def load_file(self, filename):
        with open(filename) as f:
            data = f.read().splitlines()
            for line in data:
                self.read_line(line)


def main(filename):
    fs = FileSystem(70000000)

    parser = Parser(fs)
    parser.load_file(filename)

    return fs.smallest_dir_to_free(30000000)


if __name__ == "__main__":
    print(main("input.txt"))
