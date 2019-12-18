function! IcecreamInitialize()
python << EOF
class StrawberryIcecream:
	def __call__(self):
		print 'EAT ME'
EOF
endfunction

