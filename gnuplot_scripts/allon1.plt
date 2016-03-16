reset

set terminal pngcairo dash font "Arial-Bold,12" fontscale 1.0 size 900, 700 
set output 'archana1A.png'

set multiplot

set title "6 Sensor Plot archana1A"

set xlabel "TIME(in HRS.)"
set ylabel "DISTANCE(in cms)"
set xdata time
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set datafile separator ","
set grid
set key

plot "archana1A.csv" using 2:3 w l lw 1 lc rgb 'red' title 'S1',\
"archana1A.csv" using 2:4 w l lw 1 lc rgb 'green' title 'S2',\
"archana1A.csv" using 2:5 w l lw 1 lc rgb 'blue' title 'S3',\
"archana1A.csv" using 2:6 w l lw 1 lc rgb 'orange' title 'S4',\
"archana1A.csv" using 2:7 w l lw 1 lc rgb 'pink' title 'S5',\
"archana1A.csv" using 2:8 w l lw 1 lc rgb 'black' title 'S6'

unset multiplot
