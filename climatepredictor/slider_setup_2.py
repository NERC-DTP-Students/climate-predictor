# https://github.com/MenxLi/tkSliderWidget
# need to add the label for the end of the slider and potentially some filling thing but I think this might fail

from tkinter import *
from tkinter.ttk import *
import numpy as np
import functools

class Slider(Frame):
    LINE_COLOR = "#476b6b"
    LINE_WIDTH = 3
    BAR_COLOR_INNER = "#5c8a8a"
    BAR_COLOR_OUTTER = "#c2d6d6"
    BAR_RADIUS = 10
    BAR_RADIUS_INNER = BAR_RADIUS-5
    DIGIT_PRECISION = '.1f' # for showing in the canvas

    # the aesthetics
    def __init__(self, master, width = 400, height = 80, min_val = 0, max_val = 1, init_lis = None, show_value = True):
        Frame.__init__(self, master, height = height, width = width)
        self.master = master
        if init_lis == None:
            init_lis = [min_val]
        self.init_lis = init_lis
        self.max_val = max_val
        self.min_val = min_val
        self.show_value = show_value
        self.H = height
        self.W = width
        self.canv_H = self.H
        self.canv_W = self.W
        if not show_value:
            self.slider_y = self.canv_H/2 # y pos of the slider
        else:
            self.slider_y = self.canv_H*2/5
        self.slider_x = Slider.BAR_RADIUS # x pos of the slider (left side)

        self.bars = []
        self.selected_idx = None # current selection bar index
        
        i=0

        for value in self.init_lis:
            pos = (value-min_val)/(max_val-min_val) #sets the position of the bar based on the initial values given
            ids = []
            bar = {"Pos":pos, "Ids":ids, "Value":value, "Idx": i} # current value is set to the initial value
            self.bars.append(bar)
            i = i+1

        self.canv = Canvas(self, height = self.canv_H, width = self.canv_W)
        self.canv.create_text(self.canv_W-2*self.slider_x, self.canv_H-0.8*self.slider_y, text = "desert")
        
        self.canv.pack()
        self.canv.bind("<Motion>", self._mouseMotion) #when the mouse is moved
        self.canv.bind("<B1-Motion>", self._moveBar) #when left button is pressed and held down

        # add the slider line
        self.__addTrack(self.slider_x, self.slider_y, self.canv_W-self.slider_x, self.slider_y)
        
        # add each slider with position and index
        for bar in self.bars:
            #bar["Ids"] = self.__addBar(bar["Pos"], bar["Idx"])
            bar["Ids"] = self.addBar(bar["Pos"], bar["Idx"])
        print(self.bars)


    def getValues(self):
        """gets the values for each marker in the slider"""
        values = [bar["Value"] for bar in self.bars]
        return values

    def _mouseMotion(self, event):
        """passes the x coordinate of the mouse and the y coordinate of the mouse.
        If the mouse is inside a slider will change the cursor to a hand"""
        x = event.x; y = event.y
        selection = self.__checkSelection(x,y)
        if selection[0]: #if a slider is selected
            self.canv.config(cursor = "hand2") #change cursor to hand
            self.selected_idx = selection[1] #retrieve the index of the selected slider
        else:
            self.canv.config(cursor = "")
            self.selected_idx = None

    def _moveBar(self, event):
        x = event.x; y = event.y
        if self.selected_idx == None:
            return False
        pos = self.__calcPos(x)
        idx = self.selected_idx
        self.moveBar(idx,pos)
        #self.__moveBar(idx,pos)

        # set the values in the entry boxes
        values = slider.getValues()
        sorted_values = np.array(sorted(values))
        sorted_list = sorted(values)
        n=0
        pos = np.zeros(3)

            # deals with if the sliders are dragged over each other
        for value in values:
            pos[n] = sorted_list.index(value)
            n = n+1

        percentages = np.concatenate((np.array([sorted_values[0]]), np.diff(sorted_values), np.array([100 - sorted_values[-1]])), axis = 0)

        forest_perc.set(percentages[int(pos[0])])
        ice_perc.set(percentages[int(pos[1])])
        water_perc.set(percentages[int(pos[2])])
        desert_perc.set(percentages[3])



    def __addTrack(self, startx, starty, endx, endy):
        # add initial slider line
        id1 = self.canv.create_line(startx, starty, endx, endy, fill = Slider.LINE_COLOR, width = Slider.LINE_WIDTH)

        #add desert text and oval
        R = Slider.BAR_RADIUS
        r = Slider.BAR_RADIUS_INNER
        y = endy
        x = endx

        self.canv.create_text(self.canv_W-2*self.slider_x, self.canv_H-0.8*self.slider_y, text = "desert")
        self.canv.create_oval(x-R,y-R,x+R,y+R, fill = Slider.BAR_COLOR_OUTTER, width = 2, outline = "")
        self.canv.create_oval(x-r,y-r,x+r,y+r, fill = Slider.BAR_COLOR_INNER, outline = "")

        return id

    #def __addBar(self, pos, idx):
    def addBar(self, pos, idx):
        names = ['forest', 'ice', 'water', 'desert']
        colour = ['green', 'white', 'blue', 'yellow']

        """@ pos: position of the bar, ranged from (0,1).
        Wil create the actual slider objects"""
        if pos <0 or pos >1:
            raise Exception("Pos error - Pos: "+str(pos))
        R = Slider.BAR_RADIUS
        r = Slider.BAR_RADIUS_INNER
        L = self.canv_W - 2*self.slider_x
        y = self.slider_y
        x = self.slider_x+pos*L
        id_outer = self.canv.create_oval(x-R,y-R,x+R,y+R, fill = Slider.BAR_COLOR_OUTTER, width = 2, outline = "")
        id_inner = self.canv.create_oval(x-r,y-r,x+r,y+r, fill = Slider.BAR_COLOR_INNER, outline = "")

        L = 1
        self.canv.create_line(x-L, y-2*R, x+L, y-2*R, fill = colour[idx], width = Slider.LINE_WIDTH)

        if self.show_value:
            y_value = y+Slider.BAR_RADIUS+8
            #value = pos*(self.max_val - self.min_val)+self.min_val
            #id_value = self.canv.create_text(x,y_value, text = format(value, Slider.DIGIT_PRECISION))
            id_value = self.canv.create_text(x,y_value, text = names[idx])
            return [id_outer, id_inner, id_value]
        else:
            return [id_outer, id_inner]

    #def __moveBar(self, idx, pos):
    def moveBar(self, idx, posit, entry = False):

        if entry and idx>0:
            c_value = self.bars[idx-1]
    
            pos = (c_value["Value"]+posit*100)/100
            #pos = c_value["Value"]+pos
            #print(pos)
            #for bar in self.bars:
            #    print(bar["Value"])
        else:
            pos = posit



        """slider will be moved"""
        ids = self.bars[idx]["Ids"]
        for id in ids:
            self.canv.delete(id) #deletes old slider nmarker
        #self.bars[idx]["Ids"] = self.__addBar(pos, idx)
        self.bars[idx]["Ids"] = self.addBar(pos, idx)
        self.bars[idx]["Pos"] = pos #sets new position
        self.bars[idx]["Value"] = pos*(self.max_val - self.min_val)+self.min_val #sets new value

    def __calcPos(self, x):
        """calculate position from x coordinate"""
        pos = (x - self.slider_x)/(self.canv_W-2*self.slider_x)
        if pos<0:
            return 0
        elif pos>1:
            return 1
        else:
            return pos

    def __checkSelection(self, x, y):
        """
        To check if the position is inside the bounding rectangle of a Bar
        Return [True, bar_index] or [False, None]
        """
        for idx in range(len(self.bars)):
            id = self.bars[idx]["Ids"][0]
            bbox = self.canv.bbox(id)
            if bbox[0] < x and bbox[2] > x and bbox[1] < y and bbox[3] > y:
                return [True, idx]
        return [False, None]

root = Tk()


#initial percentages
forest_perc = DoubleVar(root, 25)
ice_perc = DoubleVar(root, 25)
water_perc = DoubleVar(root, 25)
desert_perc = DoubleVar(root, 25)

# initial positions on the slider (calculated from initial percentages)
init_positions = [ice_perc.get(), forest_perc.get()+ice_perc.get(), forest_perc.get()+ice_perc.get()+water_perc.get()]

# create the slider
slider = Slider(root, width = 400, height = 60, min_val = 0, max_val = 100, init_lis = init_positions, show_value = True)
slider.pack()

# Entry boxes for the different values
forest_value = Entry(textvariable=forest_perc)
ice_value = Entry(textvariable=ice_perc)
water_value = Entry(textvariable=water_perc)
desert_value = Entry(textvariable=desert_perc)

forest_value.pack()
ice_value.pack()
water_value.pack()
desert_value.pack()

#added this but it belongs to the entry class and I want it to belong to the slider class
def type_albedo(idx, pos):
    print(type(pos))
    print(pos)
    #idx = int(idx)
    #print(type(idx))
    #slider.moveBar(pos=pos, idx=0)
    return


def test(self, param):
    print(param)
    return

def check_total():
    current_tot = forest_perc.get() + ice_perc.get() + water_perc.get()
    print(current_tot)
    if current_tot > 100:
        print("Current total greater than 100% please reduce some of your values")
    else:
        desert_perc.set(100-current_tot)
    return

def forest_change(event):
        # add function to deal with errors if the box is empty
        try:
            f_pos = forest_perc.get()
        except TclError:
            f_pos = 0
        slider.moveBar(posit = f_pos/100, idx = 0, entry=True)
        check_total()
        return

def ice_change(event):
        # add function to deal with errors if the box is empty
        try:
            ice_pos = ice_perc.get()
        except TclError:
            ice_pos = 0
        slider.moveBar(posit = ice_pos/100, idx = 1, entry=True)
        check_total()
        return

def water_change(event):
        # add function to deal with errors if the box is empty
        try:
            water_pos = water_perc.get()
        except TclError:
            water_pos = 0
        slider.moveBar(posit = water_pos/100, idx = 2, entry=True)
        check_total()
        return

def desert_change(event):
        desert_pos = desert_perc.get()
        slider.moveBar(posit = desert_pos/100, idx = 3, entry=True)
        return

#data = {'h':'t'}

forest_value.bind('<KeyRelease>', forest_change)
ice_value.bind('<KeyRelease>', ice_change)
water_value.bind('<KeyRelease>', water_change)
desert_value.bind('<KeyRelease>', desert_change)

#forest_value.bind('<KeyRelease>', functools.partial(test, param = forest_perc.get()))


root.title("Slider Widget")
root.mainloop()