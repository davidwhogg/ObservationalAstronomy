%.pdf: %.tex
	pdflatex $*
	pdflatex $*
	pdflatex $*

ALL: $(patsubst %.tex,%.pdf,*.tex)

fullclean:
	rm $(ALL) *.log *.dvi *.aux *.bbl *.blg
