class DataReader:
    def read(self):
        print("Reading Data")
    def read_csv(self):
        print("CSV is reading")
class DataCleaner:
    def clean(self):
        print("Cleaning Data")
class DataLoader:
    def load(self):
        print("Loading Data")
class DataPipeLine:
    def __init__(self):
        self.reader=DataReader()
        self.cleaner=DataCleaner()
        self.loader=DataLoader()
pipeline=DataPipeLine()
pipeline.reader.read_csv()
pipeline.cleaner.clean()
pipeline.loader.load()