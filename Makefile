.PHONY: dissertation.pdf

all: dissertation.pdf

dissertation.pdf:
	pdflatex dissertation
	bibtex dissertation
	pdflatex dissertation
	makeindex dissertation
	pdflatex dissertation

clean:
	rm -rf dissertation.aux dissertation.bbl dissertation.blg dissertation.idx dissertation.ilg dissertation.ind dissertation.loa dissertation.lof dissertation.log dissertation.lot dissertation.out dissertation.pdf dissertation.toc

