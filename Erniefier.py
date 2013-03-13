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
        self.btnAnother = xrc.XRCCTRL(self.frame, 'btnAnother')
        self.btnClose = xrc.XRCCTRL(self.frame, 'wxID_EXIT')

        # Bind Events
        self.frame.Bind(wx.EVT_BUTTON, self.OnClose, id=xrc.XRCID('wxID_EXIT'))
        self.frame.Bind(wx.EVT_CLOSE, self.OnExitApp)
        self.btnAnother.Bind(wx.EVT_BUTTON, self.OnBtnAnotherButton, id=xrc.XRCID('btnAnother'))
        
        self.getErnie()
        self.frame.Show()

    def getErnie(self):
        self.ernieDict = ErnieDict()
        erniePhrase = self.ernieDict.getPhrase()
        
        full = self.getSaying(erniePhrase)
        self.txtErnie.SetLabel(full)
    
    def getSaying(self, erniePhrase):
        user = wx.TextEntryDialog(None, "You would say:", "Ernifier", "Good morning.")
        if user.ShowModal() == wx.ID_OK:
            user.Destroy()
            stmt = user.GetValue()
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
