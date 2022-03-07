# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from tkinter import Canvas
from turtle import right
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    #draw_pine_tree(canvas, 550, 150, 250)
    #draw_pine_tree(canvas, 200, 100, 200)

    draw_ground(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    for x in range(100, 750, 150):
       draw_pine_tree(canvas, x, 150, 150)

    #Clouds
    draw_oval(canvas, 100, 300, 300, 400, fill="floralWhite",
    outline="floralWhite")
    # left, bottom, right, top
    draw_oval(canvas, 150, 375, 250, 425, fill="floralWhite",
    outline="floralWhite")
    draw_oval(canvas, 75, 330, 120, 370, fill="floralWhite",
    outline="floralWhite")
    draw_oval(canvas, 250, 330, 320, 370, fill="floralWhite",
    outline="floralWhite")
    draw_oval(canvas, 100, 340, 215, 415, fill="floralWhite",
    outline="floralWhite")

    #Bird
    #body/head
    draw_oval(canvas, 335, 50, 450, 100, fill="red2",
    outline="red2")
    draw_oval(canvas, 425, 75, 475, 125, fill="red2",
    outline="red2")
    #beak
    draw_polygon(canvas,
    475, 110, 500, 100, 475, 90, fill="gold1",
    outline="gold1")
    #wing
    draw_polygon(canvas,
    425, 75, 365, 145, 356, 75, fill="red2",
    outline="red2")
    draw_oval(canvas, 445, 100, 455, 110, 
    fill="black", outline="black")

    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

#Draw tree
def draw_pine_tree(canvas, center_x, bottom, height):
    #Draw the trunk of the tree
    trunk_width = height / 10
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk,
    trunk_top, fill="tan4", outline="tan4")

    #Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    skirt_center = center_x
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center,
    skirt_top, skirt_right, skirt_bottom, fill="forestGreen", outline = "forestGreen")


#Draw ground
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
    scene_width, scene_height, fill="saddleBrown", outline="saddleBrown")

#Draw sky
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
    scene_width, scene_height, width=0, fill="sky blue")

#Draw clouds
#def draw_clouds(canvas, )

#Grid drawing here, remove after finished with the image
def draw_grid(canvas, width, height, interval):
    # Draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    #Draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

# Call the main function so that
# this program will start executing.
main()