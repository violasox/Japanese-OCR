class Extract:
    def __init__(self):
        self.chunkSize = 2745

    def parseFile(self, filename):
        f = open(filename, 'rb')
        self.samples = []
        # Read the contents of one character image
        chunk = f.read(self.chunkSize)
        while chunk is not None:
            sample = Sample()
            # Convert 6-bit characters to bytes
            bytes = self.convertChunk(chunk)
            # Get the serial number
            serialNumByte = bytes[0:6]
            sample.serialNum = int.from_bytes(serialNumByte, byteorder='big')
            # Get the print style
            sample.style = bytes[6]
            # Get the character type
            self.type = bytes[12:18]
            # Get the character code
            self.character = bytes[28:30]
            # Get the image of the character
            self.image = bytes[50:3660]
            self.samples.append(sample)
            chunk = f.read(self.chunkSize)
            break

        f.close()

        

    # Get a 4-char (24-bit, 3-byte) chunk and return 4 bytes
    def convertChunk(self, chunk):
        bytes = []
        for i in range(0, len(chunk), 3):
            bitStr = chunk[i:i+3]
            bytes.append((bitStr[0] >> 2) & 7)
            bytes.append(((bitStr[0] << 4) & 0x30) | (bitStr[1] >> 4))
            bytes.append(((bitStr[1] << 2) & 0x3F) | ((bitStr[2] >> 6) & 0x03))
            bytes.append(bitStr[2] & 0x3F)
        return bytes

class Sample:
    def __init__(self):
        self.serialNum = None
        self.style = None
        self.type = None
        self.character = None
        self.image = None
