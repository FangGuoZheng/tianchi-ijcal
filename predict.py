# import pickle as pk
#
# if __name__ == "__main__":
#     train = open('../data/train01.pkl', 'rb')
#     train = pk.load(train)
#     # print(train.head(6))
#     train1 = train.groupby(train['shop_id'])
#     train1_grp = train1.size()
#     print(train1_grp.head(6))

from tkinter import *

class Cal(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES,fill = BOTH)
        self.master.title('Calculator By Soulenvy')
        self.master.geometry('400x400')
        self.draw()

    def addButton(self,parent,side,text,command = None):
        b = Button(parent,text = text,command = command)
        b.pack(side = side,expand = YES,fill = BOTH)
        return b

    def addFrame(self,parent,side):
        f = Frame(parent)
        f.pack(side = side,expand = YES,fill = BOTH)
        return f

    def draw(self):
        res = StringVar()
        cc = StringVar()
        e = Entry(self,relief = SUNKEN,textvariable = cc)
        e.pack(side = TOP,expand = YES,fill = BOTH)
        r = Entry(self,relief = SUNKEN,textvariable = res)
        r.pack(side = TOP,expand = YES,fill = BOTH)
        charArray = ("123+","456-","789*","-0./","%()")
        for vx in charArray:
            keyF = self.addFrame(self,TOP)
            for char in vx:
                self.addButton(keyF,LEFT,char,
                               lambda o = cc,s = '%s'%char:self.showCc(o,s))
        self.addButton(keyF,LEFT,'=',lambda o = cc,r = res,s = self:s.cal(o,r))
        keyF = self.addFrame(self,TOP)
        self.addButton(keyF,LEFT,'Clear',
                       lambda o = cc,r = res:(o.set('0'),res.set('0')))
        self.addButton(keyF,LEFT,'Del',
                       lambda o = cc:o.set(o.get()[0:-1]))
        self.addButton(keyF,LEFT,'Demo',None)
        Str = 'By Soulenvy,2013-02-26/Python-V3.2'
        self.addButton(keyF,LEFT,'Help',lambda r = res:r.set(Str))

    def showCc(self,cc,char):
        s = cc.get()
        if s == '0':
            s = ''
        s += char
        cc.set(s)

    def cal(self,cc,r):
        try:
            r.set(eval(cc.get()))
        except Exception:
            r.set("ERROR")

def main():
    Cal().mainloop()

if __name__ == '__main__':
    main()