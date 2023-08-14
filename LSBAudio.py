import wave

def encode(cipher, file):
	print("\nEncoding Starts..")
	audio = wave.open(file,mode="rb")
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	string = cipher
	print(string)
	string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
	for i, bit in enumerate(bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit
	frame_modified = bytes(frame_bytes)
	for i in range(0,10):
		print(frame_bytes[i])
	result = "encrypt.wav"
	newAudio =  wave.open(result, 'wb')
	newAudio.setparams(audio.getparams())
	newAudio.writeframes(frame_modified)

	newAudio.close()
	audio.close()
	print(" |---->succesfully encoded inside sampleStego.wav")

def decode(file):
	print("\nDecoding Starts..")
	audio = wave.open(file, mode='rb')
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	decoded = string.split("###")[0]
	print("Sucessfully decoded: "+decoded)
	audio.close()
	return decoded
