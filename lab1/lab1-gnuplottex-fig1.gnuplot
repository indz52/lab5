set terminal pdf
set output './lab1-gnuplottex-fig1.pdf'
set xlabel "x"
set ylabel "y"
set title "График функции x^2"
plot x**2 title "f(x) = x^2" with lines
