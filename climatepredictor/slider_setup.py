
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
        for value in self.init_lis:
            pos = (value-min_val)/(max_val-min_val) #sets the position of the bar based on the initial values given
            ids = []
            bar = {"Pos":pos, "Ids":ids, "Value":value} # current value is set to the initial value
            self.bars.append(bar)


        self.canv = Canvas(self, height = self.canv_H, width = self.canv_W)
        self.canv.pack()
        self.canv.bind("<Motion>", self._mouseMotion) #when the mouse is moved
        self.canv.bind("<B1-Motion>", self._moveBar) #when left button is pressed and held down

        self.__addTrack(self.slider_x, self.slider_y, self.canv_W-self.slider_x, self.slider_y)
        for bar in self.bars:
            bar["Ids"] = self.__addBar(bar["Pos"])


    def getValues(self):
        values = [bar["Value"] for bar in self.bars]
        #return sorted(values)
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

        values = slider.getValues()
        sorted_values = np.array(sorted(values))
        n=0
        pos = np.zeros(3)

        for value in sorted_values:
            pos[n] = values.index(value)
            n=n+1
            #pos[n] = np.where(value = sorted_values)

        percentages = np.concatenate((np.array([sorted_values[0]]), np.diff(sorted_values), np.array([100 - sorted_values[-1]])), axis = 0)
        print(percentages)
        print(pos)

        forest_perc.set(percentages[0])
        ice_perc.set(percentages[1])
        water_perc.set(percentages[2])
        desert_perc.set(percentages[3])



        forest_perc.set(percentages[0])
        ice_perc.set(percentages[1])
        water_perc.set(percentages[2])
        desert_perc.set(percentages[3])


        #print(values[1])

        #print(slider.getValues())
        #for value in slider.getValues():
        #    print(value)

        #entry_test.set(slider.getValues())



    def __addTrack(self, startx, starty, endx, endy):
        id1 = self.canv.create_line(startx, starty, endx, endy, fill = Slider.LINE_COLOR, width = Slider.LINE_WIDTH)
        return id

    def __addBar(self, pos):
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
            value = pos*(self.max_val - self.min_val)+self.min_val
            id_value = self.canv.create_text(x,y_value, text = format(value, Slider.DIGIT_PRECISION))
            return [id_outer, id_inner, id_value]
        else:
            return [id_outer, id_inner]

    def __moveBar(self, idx, pos):
        ids = self.bars[idx]["Ids"]
        for id in ids:
            self.canv.delete(id)
        self.bars[idx]["Ids"] = self.__addBar(pos)
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

    def __getValue(self, idx):
        """#######Not used function#####"""
        bar = self.bars[idx]
        ids = bar["Ids"]
        x = self.canv.coords(ids[0])[0] + Slider.BAR_RADIUS
        pos = self.__calcPos(x)
        return pos*(self.max_val - self.min_val)+self.min_val

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

slider = Slider(root, width = 400, height = 60, min_val = 0, max_val = 100, init_lis = [20,50,75], show_value = True)
slider.pack()

#initial percentages
forest_perc = DoubleVar(root, 10)
ice_perc = DoubleVar(root, 10)
water_perc = DoubleVar(root, 10)
desert_perc = DoubleVar(root, 10)


forest_value = Entry(textvariable=forest_perc)
ice_value = Entry(textvariable=ice_perc)
water_value = Entry(textvariable=water_perc)
desert_value = Entry(textvariable=desert_perc)

forest_value.pack()
ice_value.pack()
water_value.pack()
desert_value.pack()

root.title("Slider Widget")
root.mainloop()

print(slider.getValues())