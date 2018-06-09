class Extract:
    def __init__(self):
        self.chunkSize = 2745

    def parseFile(self, filename):
        f = open(filename, 'rb')
        serialNumChar1 = f.read(3)
        serialNumChar2 = f.read(3)
        serialNumByte1 = self.convertChunk(serialNumChar1)
        serialNumByte2 = self.convertChunk(serialNumChar2)
        serialNumByte = serialNumByte1 + serialNumByte2[0:2]
        serialNum = int.from_bytes(serialNumByte, byteorder='big')
        print(serialNum)
        

    # Get a 4-char (24-bit, 3-byte) chunk and return 4 bytes
    def convertChunk(self, bitStr):
        bytes = []
        bytes.append((bitStr[0] >> 2) & 7)
        bytes.append(((bitStr[0] << 4) & 0x30) | (bitStr[1] >> 4))
        bytes.append(((bitStr[1] << 2) & 0x3F) | ((bitStr[2] >> 6) & 0x03))
        bytes.append(bitStr[2] & 0x3F)
        return bytes
