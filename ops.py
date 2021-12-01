#op values
opnums = {
    "1" : "ADD",
    "2" : "SUB",
    "3" : "CALL",
    "4" : "STORE",
    "5" : "MULT",
    "6" : "DIV"
}
def getop(code):
    try:
        opnumber = code.split()[0]
    except:
        opnumber = "none"
    for opnum in opnums:
        if opnumber == "none":
            break
        if opnumber == opnum:
            return opnums[opnum]

def ADD(num1: float, num2: float) -> str:
    return str(num1 + num2)
def SUB(num1: float, num2: float) -> str:
    return str(num1 - num2)
def CALL(linenum: float, ret) -> str:
    print(ret[linenum])
    return str(ret[linenum])
def STORE(inp):
    return(inp)
def MULT(num1: float, num2: float) -> str:
    return str(num1 * num2)
def DIV(num1: float, num2: float) -> str:
    return str(num1 / num2)
