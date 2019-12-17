function! CReSyntax()

let s:filePath = expand('%:p')

python << EOF
import vim
print vim.eval('s:filePath')
EOF	

endfunction
