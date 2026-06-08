set terminal pdf
set output './lab1-gnuplottex-fig2.pdf'
set xlabel "x"
set ylabel "y"
set key right bottom
plot sin(x) title "\sin x", cos(x) title "\cos x"
