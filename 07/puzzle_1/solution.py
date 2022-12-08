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
    def __init__(self):
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

    def get_directories_up_to_size(self, size):
        res = []
        for f in self.files_list:
            if f.is_directory and f.size <= size:
                res.append(f)
        return res


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
    fs = FileSystem()

    parser = Parser(fs)
    parser.load_file(filename)

    res = fs.get_directories_up_to_size(100000)
    return sum([f.size for f in res])


if __name__ == "__main__":
    print(main("input.txt"))
