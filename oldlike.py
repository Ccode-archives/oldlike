#import operations library
try:
    import ops
except:
    print("Please run in main project folder!!!")
    quit()
import sys

def error(errname: str, linenumber: int):
    print(errname + " error on line " + str(linenumber))
    quit()

#get args
args = sys.argv

#check if args are invalid
if len(args) < 2:
    print("Args missing!!!")
    quit()

#get code to run
try:
    file = open(args[1], 'r')
    codefile = file.readlines()
    file.close()
except:
    print("Error getting file!!!")
    quit()

#init variables used by operations
lineret = [""]
line = 0
for code in codefile:
    #get needed info
    line += 1
    op = ops.getop(code)
    code = code.strip()
    varcount = 0
    #variables
    for value in lineret:
        code = code.replace("ln" + str(varcount), lineret[varcount])
        varcount += 1
    out = ""
    if op == "ADD":
        nums = code.split()
        out = ops.ADD(int(nums[1]), int(nums[2]))
        lineret.append(out)
    elif op == "SUB":
        nums = code.split()
        out = ops.SUB(int(nums[1]), int(nums[2]))
        lineret.append(out)
    elif op == "CALL":
        nums = code.split()
        ops.CALL(int(nums[1]), lineret)
        lineret.append("null")
    elif op == "STORE":
        values = code.split(" ", 1)[1]
        out = ops.STORE(values)
        lineret.append(out)
    elif code == "" or code.startswith(";"):
        out = "null"
        lineret.append(out)
    else:
        error("Op not found ")
