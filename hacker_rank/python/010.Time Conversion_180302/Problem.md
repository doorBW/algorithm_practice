Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

## Function Description

Complete the timeConversion function in the editor below. It has one parameter:

1. A string, s, denoting the time.
The function must return a string denoting the 24-hour formatted time.

## Raw Input Format

A single string  containing a time in -hour clock format (i.e.: ![](http://latex.codecogs.com/gif.latex?hh%3Amm%3AssAM) or ![](http://latex.codecogs.com/gif.latex?hh%3Amm%3AssPM)), where !()[http://latex.codecogs.com/gif.latex?01%5Cleq%20hh%5Cleq%2012] and ![](http://latex.codecogs.com/gif.latex?00%5Cleq%20mm%2Css%5Cleq%2059).

## Sample Input 0

07:05:45PM
## Sample Output 0

19:05:45