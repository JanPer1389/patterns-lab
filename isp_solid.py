from abc import abstractmethod

class Mashine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultifunctionPrinter(Mashine):
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self):
        pass

class OldFashinePrinter(MultifunctionPrinter):
    def print(self, document):
        pass
    
    def fax(self, document):
        # nope
        pass
    
    
    def scan(self):
        """Not supported"""
        raise NotImplementedError('Printer cannot scan!')

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        pass
    def scan(self, document):
        pass