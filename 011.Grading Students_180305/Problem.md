At HackerLand University, a passing grade is any grade 40 points or higher on a 100 point scale. Sam is a professor at the university and likes to round each student’s grade according to the following rules:

- If the difference between the grade and the next higher multiple of 5 is less than 3, round to the next higher multiple of 5
If the grade is less than 38, don’t bother as it’s still a failing grade
- Automate the rounding process then round a list of grades and print the results.

## Input Format

## First Line

- integer 
	- n: number of students
	- ![](http://latex.codecogs.com/gif.latex?1%5Cleq%20n%5Cleq%2060)

## Next N lines

- integer 
	- ![](http://latex.codecogs.com/gif.latex?grades_i) : individual grades
	- ![](http://latex.codecogs.com/gif.latex?0%5Cleq%20grades_i%5Cleq%20100)

## Output Format

Print n lines, each with the rounded value of a student’s grade in input order.

## Sample Input 0

4
73
67
38
33

## Sample Output 0

75
67
40
33

## Explanation 0

The first grade, 73 is two below the next higher multiple of 5, so it rounds to 75. 
67 is 3 points less than the next higher multiple of 5 so it doesn’t round. 
38, like 73, rounds up to next higher multiple of 5, or 40 in this case. 
33 is less than 38, so it does not round.