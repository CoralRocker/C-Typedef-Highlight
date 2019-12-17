import vim
# print vim.eval('expand(\'%:p\')')

def GetSyntaxHighlighting():
    filePath = vim.eval('expand(\'%:p\')')
    fileBuffer = open(filepath, "r");
    print fileBuffer.read()

GetSyntaxHighlighting()
