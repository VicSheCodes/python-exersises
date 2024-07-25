'''

i: Represents a 4-byte integer (int).
f: Represents a 4-byte floating-point number (float).
s: Represents a string of bytes. The length of the string is variable and not explicitly defined with this format.

'''
import struct
from pytest import approx

format_string = 'i f 5s'

def pack_data():
    data  = struct.pack(format_string, 42, 3.14, b'Hello')
    print(f"Packed Data: {data}")
    return data
    
def unpack_data(packed_data):
    unpacked_data = struct.unpack(format_string, packed_data)
    print(f"Unpacked data: {unpacked_data}")
    return unpacked_data

def test_pack_data():
    packed_data = pack_data()
    assert packed_data == b'*\x00\x00\x00\xc3\xf5H@Hello'
    
def test_unpacking():
    packed_data = pack_data()
    unpacked_data = unpack_data(packed_data)

    # Expected 
    expected_int = 42
    expected_float = 3.14
    expected_bytes = b'Hello'
    
    # Assertions with tolerance for floating-point comparison
    assert unpacked_data[0] == expected_int
    assert unpacked_data[1] == approx(expected_float)
    assert unpacked_data[2] == expected_bytes 

if __name__ == '__main__':
    unpack_data(pack_data())
    
    

    