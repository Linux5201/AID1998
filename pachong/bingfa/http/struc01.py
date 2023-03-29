import struct

st = struct.Struct('i4sf')


data = st.pack(1, b'Lily', 1.65)
print(data)

data2 = st.unpack(data)
print(data2)





