
class FilePathLength:

    def __init__(self, path):

        if not isinstance(path,str):
            raise TypeError
        
        if len(path) == 0:
            raise ValueError

        self._path = path
    
    def __lt__(self, other):
        if isinstance(other, FilePathLength):
            return len(self._path) < len(other._path)
        
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, FilePathLength):
            return len(self._path) > len(other._path)
        
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, FilePathLength):
            return len(self._path) == len(other._path)
        
        return NotImplemented

fp1 = FilePathLength("/user/home/documents")
fp2 = FilePathLength("/user/home/documents/report.txt")
fp3 = FilePathLength("/user/notes.txt")
fp4 = FilePathLength("/user/home/documents")

try:
    fp5 = FilePathLength("")
except ValueError as e:
    print(f"Error: {e}")      # Prints an error message

print(fp1 < fp2)              # True
print(fp1 == fp3)             # False
print(fp2 > fp3)              # True
print(fp3 > fp1)              # False
print(fp1 == fp4)             # True