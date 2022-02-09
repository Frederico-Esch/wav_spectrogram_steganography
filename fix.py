with open("sample.wav", "rb") as file:
    with open("target.wav", "wb") as target:
        data = file.read(4)
        target.write(data)


        size = file.read(4)
        size = int.from_bytes(size, byteorder='little', signed=False)

        header = file.read(32)
        
        data_size = file.read(4)

        skip = int.from_bytes(data_size, byteorder='little', signed=False)
        data = file.read(skip)
        
        print(file.read(4))
        sub = 4 + len(file.read())

        size -= sub
        target.write(size.to_bytes(4, 'little'))
        target.write(header)
        target.write(data_size)
        target.write(data)
