# Configuration file for the Sphinx documentation builder.
import os
import sys

# -- Пути к проекту ---------------------------------------------------------
# Указываем Sphinx, где искать твой Python-код (поднимаемся на уровень выше папки source)
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'lvl_system'
copyright = '2026, Павлов Александр'
author = 'Павлов Александр'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Автоматически извлекает docstrings из твоего кода
    'sphinx.ext.todo',     # Позволяет использовать блоки .. todo::
    'sphinx.ext.viewcode', # Добавляет ссылки на исходный код прямо в документацию
    'myst_parser'          # Позволяет использовать README.md в качестве страниц
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# Включаем отображение блоков TODO в финальной сборке
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# Меняем стандартный 'alabaster' на современный 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 4,       # Глубина меню слева
    'collapse_navigation': False, # Не сворачивать меню автоматически
    'sticky_navigation': True,   # Зафиксировать меню при скроллинге
}

html_static_path = ['_static']