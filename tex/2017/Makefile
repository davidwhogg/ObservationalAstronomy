ALL= midterm.pdf

DEPEND_TEX= physics1.tex

%.dvi: %.tex 
	latex $*; latex $*; latex $*

%.pdf: %.dvi $(DEPEND_TEX)
	dvips -Ppdf -N0 -o $*.ps $*.dvi
	ps2pdf $*.ps
	rm $*.ps

all: $(ALL)

fullclean:
	rm $(ALL) *.log *.dvi *.aux *.bbl *.blg

dummy:
