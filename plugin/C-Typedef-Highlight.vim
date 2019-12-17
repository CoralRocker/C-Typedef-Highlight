python << EOF
import sys, vim
sys.path.append(vim.eval("expand('<sfile>:p:h')")  + '/../plugin/')
import sample
EOF

function! GSH()

	rd :GetSyntaxHighlighting

endfunction



