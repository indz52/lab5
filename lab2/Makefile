# Название вашего основного файла без расширения .tex
FILENAME = lab2

# Команда компиляции
LATEX = pdflatex
# Флаги для неинтерактивной сборки (чтобы не замирал при ошибках)
FLAGS = -interaction=nonstopmode

all: pdf

pdf:
	# Первая сборка для создания вспомогательных файлов
	$(LATEX) $(FLAGS) $(FILENAME).tex
	# Вторая сборка для корректного оглавления и ссылок в Beamer
	$(LATEX) $(FLAGS) $(FILENAME).tex

clean:
	# Удаление всех временных файлов, которые создает LaTeX
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf

.PHONY: all pdf clean