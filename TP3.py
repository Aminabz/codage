from conversions import *

BASE64_SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z', '0', '1', '2', '3',
                  '4', '5', '6', '7', '8', '9', '+', '/']

def bytes_to_symbols(l):
    if len(l)==0:
        return t
    p=''
    for i in range(len(l)):
        assert type(l[i])== int and l[i]<(2**8)
        b = bin(l[i])
        s = b[2:]
        
    
        s= (8-len(s))*'0'+s
        p=p+s
    t=''
    k=0
    
    if len(l)==1:
        p=p+'0'*4
    elif len(l)==2:
        p=p+'0'*2
    #si la longueur est >0
    for i in range(6,len(p)+1,6):
            t=t+BASE64_SYMBOLS[binary_str_to_integer(p[k:i])]
            k=i
    return t+('='* (4-len(t)))
    

def  base64_encode(source):
    '''
    Encode a file in base64 and outputs the result on standard output.

    :param source: the source filename
    :type source: str
    '''
    input = open(source, 'rb')
    data = input.read(3)
    nb = 4   #4 car le programme lit 3 caracteres à chaque fois ce qui represente 4 code en base64
    while len(data) > 0:
        if nb==76:
            print (bytes_to_symbols(data), end='\n')
            nb=4
        print (bytes_to_symbols(data), end='')
        nb+=4
        data = input.read(3)
        
    print()
    input.close();


def decode_base64_symbol(s):
    assert len(s)==1 and s in BASE64_SYMBOLS, 'the symbol is not part of base64'
    return BASE64_SYMBOLS.index(s)

def symbols_to_bytes(s):
    """

    Examples:
    >>> symbols_to_bytes('HFll')
    [28, 89, 101]
    >>> symbols_to_bytes('BKM=')
    [4, 163]
    >>> symbols_to_bytes('BQ==')
    [5]
    """
    assert len(s) == 4
    p=''
    i=0
    while i<len(s) and s[i]!='=':
        d= decode_base64_symbol(s[i])
        r= bin(d)[2:]
        r= (6-len(r))*'0' + r
        p=p+r
        i=i+1
    p= binary_str_to_integer(p)
    nb= s.count('=')
    p= p >> (nb*2)
    l=[]
    while p>0:
        l.insert(0, p%(2**8))
        p= p>>8
    return l


def process_base64_line(s):
    """

    Examples:
    >>> process_base64_line('Q29kYWdl')
    Codage
    >>> process_base64_line('Q29kYWdlcw==')
    Codages
    >>> process_base64_line('Q29kYWdlcy4=')
    Codages.
    """
    assert len(s)%4==0
    for i in (s):
        assert i in BASE64_SYMBOLS or i=='=' or i== '\n'
    k=0
    for i in range(4,len(s)+1,4):
        for f in symbols_to_bytes(s[k:i]):
            print(chr(f), end='')   
        k=i
         

            
def base64_decode(source):
    assert type(source)==str
    with open(source, 'r') as inp:
        
        s= inp.read(1)
        line=''
        while len(s)>0:
            line=line+s
            s= inp.read(1)
            if not s in BASE64_SYMBOLS:
                s=inp.read(1)
        process_base64_line(line)
            
