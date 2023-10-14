%.pdf: %.tex
	pdflatex $*
	pdflatex $*
	pdflatex $*

all: $(patsubst %.tex,%.pdf,*.tex)

fullclean:
	rm $(ALL) *.log *.dvi *.aux *.bbl *.blg

dummy:
