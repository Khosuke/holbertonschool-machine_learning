# Project: Plotting

## Task 0. Line Graph
plot y as a line graph

_y should be plotted as a solid red line
The x-axis should range from 0 to 10_

- File: [0-line.py](0-line.py)

## Task 1. Scatter

plot x ↦ y as a scatter plot

_The x-axis should be labeled Height (in)
The y-axis should be labeled Weight (lbs)
The title should be Men's Height vs Weight
The data should be plotted as magenta points_

- File: [1-scatter.py](1-scatter.py)

## Task 2. Change of scale

plot x ↦ y as a line graph

_The x-axis should be labeled Time (years)
The y-axis should be labeled Fraction Remaining
The title should be Exponential Decay of C-14
The y-axis should be logarithmically scaled
The x-axis should range from 0 to 28650_

- File: [2-change_scale.py](2-change_scale.py)

## Task 3. Two is better than one

plot x ↦ y1 and x ↦ y2 as line graphs

_The x-axis should be labeled Time (years)
The y-axis should be labeled Fraction Remaining
The title should be Exponential Decay of Radioactive Elements
The x-axis should range from 0 to 20,000
The y-axis should range from 0 to 1
x ↦ y1 should be plotted with a dashed red line
x ↦ y2 should be plotted with a solid green line
A legend labeling x ↦ y1 as C-14 and x ↦ y2 as Ra-226 should be placed in the upper right hand corner of the plot_

- File: [3-two.py](3-two.py)

## Task 4. Frequency

plot a histogram of student scores for a project

_The x-axis should be labeled Grades
The y-axis should be labeled Number of Students
The x-axis should have bins every 10 units
The title should be Project A
The bars should be outlined in black_

- File: [4-frequency.py](4-frequency.py)

## Task 5. All in One

plot all 5 previous graphs in one figure

_All axis labels and plot titles should have a font size of x-small (to fit nicely in one figure)
The plots should make a 3 x 2 grid
The last plot should take up two column widths (see below)
The title of the figure should be All in One_

- File: [5-all_in_one.py](5-all_in_one.py)

## Task 6. Stacking Bars

plot a stacked bar graph

```
- fruit is a matrix representing the number of fruit various people possess
    - The columns of fruit represent the number of fruit Farrah, Fred, and Felicia have, respectively
    - The rows of fruit represent the number of apples, bananas, oranges, and peaches, respectively
- The bars should represent the number of fruit each person possesses:
    - The bars should be grouped by person, i.e, the horizontal axis should have one labeled tick per person
    - Each fruit should be represented by a specific color:
        - apples = red
        - bananas = yellow
        - oranges = orange (#ff8000)
        - peaches = peach (#ffe5b4)
        - A legend should be used to indicate which fruit is represented by each color
    - The bars should be stacked in the same order as the rows of fruit, from bottom to top
    - The bars should have a width of 0.5
- The y-axis should be labeled Quantity of Fruit
- The y-axis should range from 0 to 80 with ticks every 10 units
- The title should be Number of Fruit per Person
```

- File: [6-bars.py](6-bars.py)
