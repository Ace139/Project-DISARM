reset

set terminal pngcairo dash font "Arial-Bold,12" fontscale 1.0 size 900, 700 
set output 'demo.png'

set multiplot

set title "NO2 vs TIME (CSE Dept. vs Hall9)"

set xlabel "TIME(in HRS.)"
set ylabel "VALUES (in Parts Per Million)"
#set yrange [0:60]
set xdata time
set timefmt "%H:%M:%S"
set format x "%H"
set datafile separator ","
set grid
set key

plot ["10:30:00":"21:30:00"][:]"output.csv" using 1:2 w l lw 2 lc rgb 'red' title 'CSE Dec-17',\
"hall917.csv" using 2:3 w l lw 2 lc rgb 'green' title 'Hall9 Dec-17',\

unset multiplot
