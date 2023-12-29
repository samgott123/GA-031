from typing import List

class Data:
    def __init__(self, source_data: List[str]):
        self.source_data = source_data
        self.processed_data = []

    def clean_data(self):
        pass

    def transform_data(self):
        pass


class Assembler:
    def __init__(self):
        self.raw_data = None

    def assemble_data(self, source_data: List[str]) -> Data:
        self.raw_data = Data(source_data)
        self.raw_data.clean_data()
        self.raw_data.transform_data()
        return self.raw_data