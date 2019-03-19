# Trig Graph Simulator
This is a basic simulation of how a trigonometric graph (sin, cos, or tan) is created from a unit circle. Coded in Python 3.6 with the Pygame library.

Project done for Mr. Sharick's 2nd period APCSP class (2018-2019). 

# General Info 
Use the big sin, cos, tan buttons to change the graph. Each graph has its own set of attributes and do not share any inputs with each other. 

To change attributes, click on an input box, type an integer*, and press enter. If legal your new value will be shown. If illegal the input will be ignored. 

Use the pause and play buttons to pause and play the movement of the graph. Can be useful for understanding the horizontal shift, because when moving the initial horizontal shift is meaningless. 



*must be an integer because the Pygame methods I used only take in integers as inputs. Also because I used the int() method. 

# Bugs
-If you enter in a negative amplitude the program crashes because a negative radius isn't allowed. This would be easily fixed by creating an exception and catching the error but I'm too lazy.

-If you set the amplitude higher than what is shown on the screen the dot does not go fully around the circle. This is because the way I wrote the dot to go around the circle was super jank and involved using Pythagorean's theorem to calculate the necessary x values from the calculated y values and the given radius. Because of this the dot would initally only rotate from pi/2 to -pi/2. To fix this I checked whether the dot was on the highest pixel point and setting the x-coordinates to be negative if it reached that point. It generally works besides a frame skip when the dot is at the highest point if you look closely, but I'm not sure how to fix this bug. There was probably a better way to do what I wanted anyway. 

-the tan graph has a line drawn in place of the asymptote. Not a huge deal but it's impossible to remove without fundamentally changing how the graph is drawn because the draw.lines() function has to connect every piece of the graph in one continous stroke. 

-Also, not really a bug, but if you enter an illegal input it just ignores it without any message. What was supposed to happen was a message pops up notifying it's an illegal input but the surface of is redrawn after each input is entered and it seemed more trouble than its worth. 

# Other Things
This is mainly code specific stuff.

-You can change the INCREMENT variable in variables.py to change the number of pixels that equal 1 unit. 

-THEORETICALLY, you can change the HEIGHT and WIDTH variables in variables.py. However, I am an idiot and probably hardcoded the numbers somewhere, so it might not work. I did my best to diligently avoid it but there's probably a hardcoded number somewhere. 

-You can change the colors of the buttons to anything you want in variables.py. The "ON" ones are for when the button is pressed down.

-Pretty sure the DEGREE variable is unused lol.
