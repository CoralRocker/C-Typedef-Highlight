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
            txt = re.findall("^\s*typedef\s+(struct|union|enum)\s+\w+", line)
            # output = f'echo "{txt}"'
            # print txt
            self.vim.command("echo \"" + str(txt) + "\"")

