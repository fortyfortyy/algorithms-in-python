"""
It's photo day at the local school, and you're the photographer assigned to take class photos. The class that you will be
photographing has an even number of students, and all these students are wearing ted or blue shirts. In fact, exactly
half of the class is wearing red shirts, and the other half is wearing blue shirts. You're responsible for arranging
the studens in two rows before taking the photo. Each row should contain the same number of the studens and should adhere
to the following guideliness:

    - All students wearing red shirts must be in the same row.
    - All students wearing blue shirts must be in the same row.
    - Each student in the back row must be strictly taller than the student directly in front of them in the front row.

You're given two input arrays: one containg the heights of all the students with red shirts and another one containing
the heights of all the students with blue shirts. These arrays will always have the same lenght and positive integers.


Sample Input:                         |         Sample Output:
red_shirt_heights = [5, 8, 1, 3, 4]   |            true     # place all students with blue shirts in the back row
blue_shirt_heights = [6, 9, 2, 4, 5]  |
"""

# O(nlog(n)) time | O(1) space - where n is the number of students
def class_photos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    behind = "blue" if blueShirtHeights[0] > redShirtHeights[0] else "red"
    for idx in range(len(redShirtHeights)):
        red = redShirtHeights[idx]
        blue = blueShirtHeights[idx]
        if behind == "blue":
            if red >= blue:
                return False
        else:
            if red <= blue:
                return False

    return True


red_shirt_heights = [5, 8, 1, 3, 4]
blue_shirt_heights = [6, 9, 2, 4, 5]
print(class_photos(red_shirt_heights, blue_shirt_heights))