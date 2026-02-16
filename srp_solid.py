class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    def add_entry(self, text):
        self.count +=1
        self.entries.append(f'{self.count}: {text}')
    def remove_entry(self, pos):
        del self.entries[pos]
    def __str__(self):
        return '\n'.join(self.entries)
    #Its, wrong way
    
    # def save_to_filename(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    
    # def load(self, filename):
    #     pass
    
    # def load_from_web(self, url):
    #     pass


# Its correct
class PersistenceManager:
    @staticmethod
    def save_to_filename(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
        

notes = Journal()
notes.add_entry('I cried today') 
notes.add_entry('I ate a bug')
file = r'c:\temp\journal.txt'

PersistenceManager.save_to_filename(notes, file)

print(notes) 