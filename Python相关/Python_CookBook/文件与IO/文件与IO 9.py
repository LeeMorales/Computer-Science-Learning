import pickle
def serailize_object():
    data = [1, 2, 3]
    f = open('somefile', 'wb')
    pickle.dump(data, f)
    s = pickle.dumps(data)
# Restore from a file
    f = open('somefile', 'rb')
    data = pickle.load(f)
# Restore from a string
    data = pickle.loads(s)
f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
if __name__ == '__main__':
    serailize_object()
# countdown.py
import time
import threading
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()
def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
def __getstate__(self):
        return self.n
def __setstate__(self, n):
        self.__init__(n)
