
function! GSH()

	" python GetSyntaxHighlighting()
	python << EN
	import sys, vim
	sys.path.append(vim.eval("expand('<sfile>:p:h')")  + '/../python/')
	print sys.path
	import sample
	GetSyntaxHighlighting()
	EN

endfunction



