# BlockchainCryptocurrencies
In this repository you will find some code and notes related with cryptocurrencies

#### Bitcoin Header Example 
In the [bitcoin_header_example](bitcoin_header_example) directory, you will
find a python code which emulate a real bitcoin block header, this code help to
understand the mining process. You can try to change the nounce value
`42a14695` by another value and see how the resulting hash change. In this case
the value `42a14695` meets the condition to solve the block.

```py
import hashlib
header_hex = ("01000000" + #version 
 "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" + #hashprev
 "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" + #merkleroot, hash de todas las transacciones en el bloque
 "c7f5d74d" + # Time
 "f2b9441a" + # Bits
 "42a14695") # Nonce
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print( hash[::-1].encode('hex_codec') )
```

to try the code use the command
```
python bitcoin_header_example_python2.py
```
Output: `00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d`



you can try to chance  
