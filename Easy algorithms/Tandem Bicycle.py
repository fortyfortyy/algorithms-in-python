"""
A tandem bicycle is a bicycle that's operated by two people: Perosn A and Perosn B. Both poeple pedal the bicycle,
but the perosn that pedals faster dictates the speed of the bicycle. So if Perosn A pedals at a speed of 5, and Perosn B
pedals at a speed of 4, the tandem bicycle moves at a speed of 5 (i.e tandem_speed = max(speedA, speedB)).

Function has to return the maximum possible total speed or the minimum possible total speed of all of the tandem
bicycles being ridden based on an input parameter, fastest. If fastest = true, function should return the maximum possible
total speed; otherwise it should return the minimum total speed.

"Total speed" is defined as the sum of the sppeds of all the tandem bicycles being ridden. For example, if there are
4 riders (2 red-shirt and 2 blue-shirt riders) who have speed of 1, 3, 4, 5, and if they're paired on tandem bicycles
as follows: [1, 4], [5, 3], then the toal speed of these tandem bicycles is 4 + 5 = 9

Sample input:                            |       Sample Output:
red_shirt_speeds = [5, 5, 3, 9, 2]       |       32
blue_shirt_speeds = [3, 6, 7, 2, 1]      |
fastest = True                           |
"""

# O(nlog(n)) time | O(1) space - where n is the number of tandem bicycles
def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    total = 0
    if fastest:
        red_shirt_speeds.sort(reverse=True)
        blue_shirt_speeds.sort()
    else:
        red_shirt_speeds.sort()
        blue_shirt_speeds.sort()

    for e in range(len(red_shirt_speeds)):
        total += max(red_shirt_speeds[e], blue_shirt_speeds[e])

    return total


red_shirt_speeds = [5, 5, 3, 9, 2]
blue_shirt_speeds = [3, 6, 7, 2, 1]
fastest = True
print(tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest))