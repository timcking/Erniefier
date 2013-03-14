import wx
from wx import xrc
import random
from random import randint
from ErnieDict import ErnieDict

class MyApp(wx.App):

    def OnInit(self):
        self.res = xrc.XmlResource('Erniefier.xrc')
        self.init_frame()
        return(True)

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'frameMain')
        
        # self.favicon = wx.Icon('./ip.ico', wx.BITMAP_TYPE_ICO)
        # self.frame.SetIcon(self.favicon)        

        # Bind Controls
        self.txtErnie = xrc.XRCCTRL(self.frame, 'txtErnie')
        self.txtYou = xrc.XRCCTRL(self.frame, 'txtYou')
        self.btnAnother = xrc.XRCCTRL(self.frame, 'btnAnother')
        self.btnClose = xrc.XRCCTRL(self.frame, 'wxID_EXIT')

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_EXIT'))
        self.frame.Bind(wx.EVT_CLOSE, self.OnExitApp)
        self.btnAnother.Bind(wx.EVT_BUTTON, self.OnBtnAnotherButton, id=xrc.XRCID('btnAnother'))
        
        self.ernieDict = ErnieDict()
        self.getErnie()
        self.frame.Show()

    def getErnie(self):
        erniePhrase = self.ernieDict.getPhrase()
        full = self.getSaying(erniePhrase)
        self.txtErnie.SetValue(full)
    
    def getSaying(self, erniePhrase):
        stmt = self.txtYou.GetValue()
        if stmt.endswith('.'):
            ernie = stmt.rstrip('.') + erniePhrase
        else:
            ernie = stmt + erniePhrase
            
        return ernie
             
    def OnBtnAnotherButton(self, event):
        self.getErnie()
        
    def OnClose(self, evt):
        self.Exit()
        
    def OnExitApp(self, event):
        self.Exit()
        
if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
