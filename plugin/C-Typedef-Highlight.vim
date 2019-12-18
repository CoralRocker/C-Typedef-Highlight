python << EOF
import sys, vim
sys.path.append(vim.eval("expand('<sfile>:p:h')")  + '/../plugin/')
print sys.path
import sample
EOF

function! GSH()

	python GetSyntaxHighlighting()

endfunction



