%.500.png: %.pov
	povray +w500 +h500 +FN +Q9 +A0.3 +AM2 +D -Lbin -Lbin/include -i$< -O$@
%.2000.png: %.pov
	povray +w2000 +h2000 +FN +Q9 +A0.3 +AM2 +D -Lbin -Lbin/include -i$< -O$@