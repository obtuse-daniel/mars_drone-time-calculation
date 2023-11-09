# mars_drone-time-calculation
A school portfolio project to calculate the amount of time for a rover to move on Mars' surface.

The program asks for three inputs: the type of rover being used, the distance that the rover needs to traverse, and if there is a dust storm in the path of travel.
There are three types of rovers and they each have a unique set of parameters:

Charlie:
100kW/h battery,
50kW/100km efficiency,
5 kW solar capacity,
5 km/hour average velocity,

Alpha:
130kW/h battery,
40kW/100km efficiency,
8 kW solar capacity,
4 km/hour average velocity,

November:
80kW/h battery,
30kW/100km efficiency,
4 kW solar capacity,
6 km/hour average velocity,

Assumptions:
the rover starts with afull battery charge,
the rover has a consistent speed regardless of terrain,
the battery must charge to 100% each charge,
