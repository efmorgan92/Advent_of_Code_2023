class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

        data_set = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data_set.append(line.strip())
        self.data_set = data_set


