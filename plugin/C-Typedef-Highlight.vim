
function! GSH()

	" python GetSyntaxHighlighting()
	python << EOF
	import sys, vim
	sys.path.append(vim.eval("expand('<sfile>:p:h')")  + '/../python/')
	print sys.path
	import sample
	GetSyntaxHighlighting()
	EOF

endfunction



