reset

set terminal pngcairo dash font "Arial-Bold,12" fontscale 1.0 size 900, 700 
set output 'standing_hridoy.png'

set multiplot

set title "Testing Clustered UltraSound Sensor\n Position : Standing Hridoy"

set xlabel "TIME(in H:M:S)"
set ylabel "Distance of Ping (UltraSound Sensor)"
set yrange [0:225]
set xdata time
set timefmt "%H:%M:%S"
set format x "%H:%M:%S"
set datafile separator ","
set grid
set key

plot ["17:20:33":"17:21:20"][:]"standing_hridoy.csv" using 2:3 w l lw 2 lc rgb 'red' title 'Left',\
"standing_hridoy.csv" using 2:4 w l lw 2 lc rgb 'green' title 'Right',\
"standing_hridoy.csv" using 2:5 w l lw 2 lc rgb 'blue' title 'Middle',\

unset multiplot
