"""
Your task is to create a new file type with a “Buffer”.
Every time you write data to this file, you use the Write method like write(“hello world”), 
but if you have enough buffer in memory (buffer_size), you write to buffer first. Only write to disk when the buffer is full (using the flush method to write to disk).
Implement both the Write and flush functions


Questions?
1. What is the size of the Buffer?
2. What is the type of data that we are writing/inserting?
3. So, for instance, we will first implement Write and Flush, we don't mind what happen after the buffer became available, right?
4. This file will be implemented in concurrent systems? (smth like that)
5. Do we need to access the values inside?
6. What happens when bytearray > len(array)

IMPORTANT QUESTION 
If data size is less than or equal to buffer size -> write in both buffer and file together? or just the buffer(which makes more sense)? 
Follow up if it is just buffer, do we write to file in fixed chunks of buffer_size or anything less than buffer_size is okay

If data is larger than buffer_size -> do we write directly to file?

Approach

class New_File:
Methods Buffer and Disk
flush(str)
write(str) → if len() == buffer_size() then flush()
buffer_size()

I will define two classes, Buffer and Disk, in both i will define each corresponding method.

AS DS, we can define a SET in case we want to access only the last value added, this is fast however, we need to take into acc
That we can have the same value added, this could lead with problem as this DD add unique values.

We can define a Linked List, as getting the lenght will be O(1) if we keep a counter of the size

BUFFER OVERFLOW

But a naive solution, will be just with an Array


"""

class File:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def write(self, bytes: bytearray):
        #Write bytes to file immediately
        with open(self.file_name, 'ab') as fp: # A-ppend B-ytes to existing file
            fp.write(bytes)

class BufferedFile(File):
    #Write data to file, using an additional memory buffer to reduce disk writes.
    def __init__(self, f: File, buffer_size: int):
        self.f = f
        self.buffer_size = buffer_size 
        self.buffer = bytearray() #Buffer to store data before writing to disk

    def write(self, bytes: bytearray):
        #Write data to file, flush to disk everytime when the buffer is full
        pointer = 0

        while True:
            bytes_to_write = min(self.buffer_size - len(self.buffer),len(bytes[pointer:])) #How many bytes can be written to buffer, without overflowing it.
            print(bytes_to_write)
            if not bytes_to_write: #Buffer is full
                break #Exit loop

            #actual write
            self.buffer.extend(bytes[pointer:pointer+bytes_to_write]) #Add bytes to buffer 
            # buffer.extend() is a method that adds the specified list elements (or any iterable) to the end of the current list.
            if len(self.buffer) >= self.buffer_size: #Buffer is full
                self.flush() #Write buffer to disk

            pointer += bytes_to_write #Move pointer to next byte

    def flush(self):
        if self.buffer: #Buffer is not empty
            self.f.write(self.buffer) #Write buffer to disk
            self.buffer = bytearray() #Clear buffer

bf = BufferedFile(File("test.log"), buffer_size=4)
print(bf)
bf.write(bytearray(b'123456789'))


""" 
Examples:
data = bytearray(b"Hello world!")
view = memoryview(data)
print(view)
print(data)

data = bytearray(b"abcdef")
view = memoryview(data)
slice_view = view[2:5]
print(slice_view.tobytes())  # Output: b'cde'


import numpy as np 

arr = np.array([ 1 , 2 , 3 , 4 ], dtype=np.int32) 
vista = memoryview (arr) 
print(vista) 
print(vista.tolist())   # Salida: [1, 2, 3, 4]


import socket

# Create a socket and connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('gooogle.com', 80))

# Send an HTTP GET request
request = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
s.sendall(request)

# Read response using memoryview
response = bytearray()
buffer = memoryview(bytearray(1024))
while True:
    nbytes = s.recv_into(buffer)
    if not nbytes:
        break
    response.extend(buffer[:nbytes])

print(response.decode('utf-8'))
"""
