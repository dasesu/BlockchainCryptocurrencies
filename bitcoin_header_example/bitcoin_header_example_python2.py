import hashlib
header_hex = ("01000000" + #version 
 "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" + #hashprev
 "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" + #merkleroot, hash de todas las transacciones en el bloque
 "c7f5d74d" + # Time
 "f2b9441a" + # Bits
 "42214695") # Nonce
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print( hash[::-1].encode('hex_codec') )
