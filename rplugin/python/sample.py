import neovim
import re
@neovim.plugin
class Main(object):

    def __init__(self, vim):
        self.vim = vim
    @neovim.function('GetList')
    def getList(self, args):
        filePath = self.vim.eval('expand(\'%:p\')')
        fileBuffer = open(filePath, "r");
        structList = []
        for line in fileBuffer:
            txt = re.search("^\s*typedef\s+struct\s+(\w+)\s*{*", line)
            if txt != None:
                structList.append(txt.group(1))
        self.vim.command("echo \"" + str(structList) + "\"")
        
        self.vim.command("syntax keyword MyStructs " + ' '.join(structList))
        self.vim.command("highglight link MyStructs Identifier")
