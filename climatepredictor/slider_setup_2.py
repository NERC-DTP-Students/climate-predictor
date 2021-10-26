# https://github.com/MenxLi/tkSliderWidget
# need to add the label for the end of the slider and potentially some filling thing but I think this might fail

from tkinter import *
from tkinter.ttk import *
import numpy as np


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
        self.canv.pack()
        self.canv.bind("<Motion>", self._mouseMotion) #when the mouse is moved
        self.canv.bind("<B1-Motion>", self._moveBar) #when left button is pressed and held down

        self.__addTrack(self.slider_x, self.slider_y, self.canv_W-self.slider_x, self.slider_y)
        for bar in self.bars:
            bar["Ids"] = self.__addBar(bar["Pos"], bar["Idx"])

        #initial percentages
        self.forest_perc = DoubleVar(master,25)
        self.ice_perc = DoubleVar(master,25)
        self.water_perc = DoubleVar(master,25)
        self.desert_perc = DoubleVar(master,25)
        self.canv.create_text(self.canv_W-2*self.slider_x,self.canv_H-0.8*self.slider_y,text='desert',fill='white')

    def getValues(self):
        values = [bar["Value"] for bar in self.bars]
        return values

    def _mouseMotion(self, event):
        x = event.x; y = event.y
        selection = self.__checkSelection(x,y)
        if selection[0]:
            self.canv.config(cursor = "hand2")
            self.selected_idx = selection[1]
        else:
            self.canv.config(cursor = "")
            self.selected_idx = None

    def _moveBar(self, event):
        x = event.x; y = event.y
        if self.selected_idx == None:
            return False
        pos = self.__calcPos(x)
        idx = self.selected_idx
        self.__moveBar(idx,pos)

        # set the values in the entry boxes
        values = self.getValues()
        sorted_values = np.array(sorted(values))
        sorted_list = sorted(values)
        n=0
        pos = np.zeros(3)

            # deals with if the sliders are dragged over each other
        for value in values:
            pos[n] = sorted_list.index(value)
            n = n+1

        percentages = np.concatenate((np.array([sorted_values[0]]), np.diff(sorted_values), np.array([100 - sorted_values[-1]])), axis = 0)

        self.forest_perc.set(np.round(percentages[int(pos[0])],1))
        self.ice_perc.set(np.round(percentages[int(pos[1])],1))
        self.water_perc.set(np.round(percentages[int(pos[2])],1))
        self.desert_perc.set(np.round(percentages[3],1))



    def __addTrack(self, startx, starty, endx, endy):
        id1 = self.canv.create_line(startx, starty, endx, endy, fill = Slider.LINE_COLOR, width = Slider.LINE_WIDTH)
        return id

    def __addBar(self, pos, idx):
        names = ['forest', 'ice', 'water', 'desert']

        """@ pos: position of the bar, ranged from (0,1)"""
        if pos <0 or pos >1:
            raise Exception("Pos error - Pos: "+str(pos))
        R = Slider.BAR_RADIUS
        r = Slider.BAR_RADIUS_INNER
        L = self.canv_W - 2*self.slider_x
        y = self.slider_y
        x = self.slider_x+pos*L
        id_outer = self.canv.create_oval(x-R,y-R,x+R,y+R, fill = Slider.BAR_COLOR_OUTTER, width = 2, outline = "")
        id_inner = self.canv.create_oval(x-r,y-r,x+r,y+r, fill = Slider.BAR_COLOR_INNER, outline = "")
        if self.show_value:
            y_value = y+Slider.BAR_RADIUS+8
            #value = pos*(self.max_val - self.min_val)+self.min_val
            #id_value = self.canv.create_text(x,y_value, text = format(value, Slider.DIGIT_PRECISION))
            id_value = self.canv.create_text(x,y_value,fill='white',text = names[idx])
            return [id_outer, id_inner, id_value]
        else:
            return [id_outer, id_inner]

    def __moveBar(self, idx, pos):
        
        ids = self.bars[idx]["Ids"]
        for id in ids:
            self.canv.delete(id)
        self.bars[idx]["Ids"] = self.__addBar(pos, idx)
        self.bars[idx]["Pos"] = pos
        self.bars[idx]["Value"] = pos*(self.max_val - self.min_val)+self.min_val

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
