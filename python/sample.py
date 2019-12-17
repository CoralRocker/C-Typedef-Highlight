import vim
import re
# print vim.eval('expand(\'%:p\')')

def gsh():
    filePath = vim.eval('expand(\'%:p\')')
    fileBuffer = open(filePath, "r");
    structList = []
    for line in fileBuffer:
        txt = re.findall("^\s*typedef\s+(struct|union|enum)\s+\w+", line)
        print txt

# GetSyntaxHighlighting()
