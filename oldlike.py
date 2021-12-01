#import operations library
import sys
try:
    import ops
except:
    print("Please run in main project folder!!!")
    sys.exit()

def error(errname: str, linenumber: int):
    print(errname + " error on line " + str(linenumber))
    sys.exit()

#get args
args = sys.argv

#check if args are invalid
if len(args) > 2 or len(args) < 2:
    print("Args missing!!!")
    sys.exit()

#get code to run
try:
    file = open(args[1], 'r')
    codefile = file.readlines()
    file.close()
except:
    print("Error getting file!!!")
    sys.exit()

#init variables used by operations
lineret = ["dev0.1"]
line = 0
for code in codefile:
    #get needed info
    line += 1
    op = ops.getop(code)
    code = code.strip()
    varcount = 0
    #variables
    for value in lineret:
        code = code.replace("ln" + str(varcount) + "$", lineret[varcount])
        varcount += 1
    out = ""
    if op == "ADD":
        nums = code.split()
        if len(nums) > 3:
            error("To many arguments", line)
        if any(c.isalpha() for c in code):
            error("No letters please", line)
        out = ops.ADD(float(nums[1]), float(nums[2]))
        lineret.append(out)
    elif op == "SUB":
        nums = code.split()
        if len(nums) > 3:
            error("To many arguments", line)
        if any(c.isalpha() for c in code):
            error("No letters please", line)
        out = ops.SUB(float(nums[1]), float(nums[2]))
        lineret.append(out)
    elif op == "CALL":
        nums = code.split()
        if len(nums) > 2:
            error("To many arguments", line)
        if any(c.isalpha() for c in code):
            error("No letters please", line)
        if int(nums[1]) > line:
            error("Line return slot missing", line)
        ops.CALL(int(nums[1]), lineret)
        lineret.append("null")
    elif op == "STORE":
        values = code.split(" ", 1)[1]
        out = ops.STORE(values)
        lineret.append(out)
    elif op == "MULT":
        nums = code.split()
        if len(nums) > 3:
            error("To many arguments", line)
        if any(c.isalpha() for c in code):
            error("No letters please", line)
        out = ops.MULT(float(nums[1]), float(nums[2]))
        lineret.append(out)
    elif op == "DIV":
        nums = code.split()
        if len(nums) > 3:
            error("To many arguments", line)
        if any(c.isalpha() for c in code):
            error("No letters please", line)
        out = ops.DIV(float(nums[1]), float(nums[2]))
        lineret.append(out)
    elif code == "" or code.startswith(";"):
        out = "null"
        lineret.append(out)
    else:
        error("Op not found", line)
