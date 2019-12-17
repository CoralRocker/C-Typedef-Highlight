import vim
# print vim.eval('expand(\'%:p\')')

def GetSyntaxHighlighting():
    filePath = vim.eval('expand(\'%:p\')')
    fileBuffer = open(filePath, "r");
    print fileBuffer.read()

GetSyntaxHighlighting()
