import neovim
import re
@neovim.plugin
class Main(object):

    def __init__(self, vim):
        self.vim = vim
    
    @neovim.function('GetList')
    def getFiles(self, args):
        filePath = self.vim.eval('expand(\'%:p\')')
        fileBuffer = open(filePath, "r");
        fileList = []
        for line in fileBuffer:
            txt = re.search("^#include\s+\"([\w.]+)\"", line)
            if txt != None:
                fileList.append(open(txt.group(1), "r")
                #self.vim.command("echo \"" + txt.group(1) + "\"")
        fileBuffer.close()
        fileList.append(open(filePath, "r"))
        self.vim.command("echo \""+' '.join(fileList)+"\"")

    def getList(self, files):
        for line in fileBuffer:
            txt = re.search("^\s*typedef\s+struct\s+(\w+)\s*{*", line)
            if txt != None:
                structList.append(txt.group(1)) 

    def HighLightSyntax(self, structList):
        if len(structList) > 0:
            self.vim.command("syntax keyword Custom_Python_Identifiers " + ' '.join(structList))
            self.vim.command("highlight link Custom_Python_Identifiers Identifier")
