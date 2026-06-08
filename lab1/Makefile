DOCNAME = lab1

all: pdf

pdf: $(DOCNAME).tex
	pdflatex -shell-escape $(DOCNAME).tex
	pdflatex -shell-escape $(DOCNAME).tex
clean:
	rm -f *.aux *.log *.toc *.out *.dvi *.ps *.pdf *.lof *.lot *.vrb *.snm *.nav *.pgf-plot.*