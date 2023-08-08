RM = /bin/rm -fv
DVIPS = dvips -Ppdf
DVIPDF = dvipdf
PS2PDF = ps2pdf

.SUFFIXES: .bbl .tex .dvi .ps .pdf

ALLFILES = $(patsubst %.tex,%.ps,$(wildcard *.tex)) \
           $(patsubst %.tex,%.pdf,$(wildcard *.tex))
all: $(ALLFILES)

.bbl.tex:
	touch $*.tex

.tex.dvi:
	latex $* ; latex $* ; latex $*

.dvi.pdf:
	$(DVIPDF) $*

.dvi.ps:
	$(DVIPS) $* -o

clean:
	$(RM) *.log *.aux *.dvi *.toc *.bbl *.blg

spotless: clean
	$(RM) *.ps *.pdf
