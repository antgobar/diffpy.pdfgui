#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4.1 on Mon Nov 27 10:41:56 2006

import wx
import re, sys, os.path
from pdfpanel import PDFPanel
from tooltips import dopingseriespanel as toolTips
from diffpy.pdfgui.control.pdfguimacros import makeDopingSeries
from wxExtensions.listctrls import AutoWidthListCtrl
from wxExtensions.validators import TextValidator, ALPHA_ONLY

class DopingSeriesPanel(wx.Panel,PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: DopingSeriesPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.instructionsLabel = wx.StaticText(self, -1, "Select a fit from the tree on the left then add datasets and assign\ndoping elements and values below. If you have not set up a fit to be\nthe template for the series, hit cancel and rerun this macro once a\nfit has been created.")
        self.labelBaseElement = wx.StaticText(self, -1, "Base element")
        self.textCtrlBaseElement = wx.TextCtrl(self, -1, "")
        self.labelDopant = wx.StaticText(self, -1, "Dopant")
        self.textCtrlDopant = wx.TextCtrl(self, -1, "")
        self.listCtrlFiles = AutoWidthListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_EDIT_LABELS|wx.SUNKEN_BORDER)
        self.buttonUp = wx.BitmapButton(self, -1, wx.NullBitmap)
        self.buttonDown = wx.BitmapButton(self, -1, wx.NullBitmap)
        self.buttonAdd = wx.Button(self, wx.ID_ADD, "Add")
        self.buttonDelete = wx.Button(self, wx.ID_DELETE, "Delete")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.goButton = wx.Button(self, wx.ID_OK, "OK")
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_COL_CLICK, self.onColClick, self.listCtrlFiles)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.onEndLabelEdit, self.listCtrlFiles)
        self.Bind(wx.EVT_BUTTON, self.onUp, self.buttonUp)
        self.Bind(wx.EVT_BUTTON, self.onDown, self.buttonDown)
        self.Bind(wx.EVT_BUTTON, self.onAdd, id=wx.ID_ADD)
        self.Bind(wx.EVT_BUTTON, self.onDelete, id=wx.ID_DELETE)
        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: DopingSeriesPanel.__set_properties
        self.instructionsLabel.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.buttonUp.SetSize(self.buttonUp.GetBestSize())
        self.buttonDown.SetSize(self.buttonDown.GetBestSize())
        # end wxGlade
        self.setToolTips(toolTips)

    def __do_layout(self):
        # begin wxGlade: DopingSeriesPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(1, 2, 10, 10)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.instructionsLabel, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        sizer_6.Add(self.labelBaseElement, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_6.Add(self.textCtrlBaseElement, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_6.Add(self.labelDopant, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_6.Add(self.textCtrlDopant, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_4.Add(self.listCtrlFiles, 1, wx.ALL|wx.EXPAND, 5)
        sizer_5.Add((0, 0), 1, wx.ADJUST_MINSIZE, 0)
        sizer_5.Add(self.buttonUp, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_5.Add(self.buttonDown, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_5.Add((0, 0), 1, wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.buttonAdd, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.buttonDelete, 0, wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.ALL, 5)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_3.Add((20, 20), 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.goButton, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.cancelButton, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

    def __customProperties(self):
        """Set the custom properties."""
        self.fit = None
        self.reverse = False # Reverse the sort?
        self.fullpath = '.'
        self.datasets = [] # Contains (doping, filename) tuples
                           # doping comes first for easy sorting

        self.listCtrlFiles.InsertColumn(0, "Doping")
        self.listCtrlFiles.InsertColumn(1, "Data Set")
        self.listCtrlFiles.SetColumnWidth(0,-2)

        # Set the validators
        self.textCtrlBaseElement.SetValidator(TextValidator(ALPHA_ONLY))
        self.textCtrlDopant.SetValidator(TextValidator(ALPHA_ONLY))
        return

    def onColClick(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Sort by doping."""
        self.datasets.sort()
        if self.reverse:
            self.datasets.reverse()
        self.reverse = not self.reverse
        self.fillList()
        return

    def onEndLabelEdit(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Update the doping in the datasets."""
        index = event.GetIndex()
        text = event.GetText()
        doping = 0.0
        try:
            doping = float(text)
        except ValueError:
            event.Veto()
            return
        if doping < 0 or doping > 1:
            event.Veto()
            return
        # update the internal information
        self.datasets[index][0] = doping
        self.reverse = False
        return

    def onUp(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Move an item in the list up."""
        index = self.listCtrlFiles.GetFirstSelected()
        if index > 0:
            temp = self.datasets[index]
            self.datasets[index] = self.datasets[index-1]
            self.datasets[index-1] = temp
            self.fillList()
            self.listCtrlFiles.Select(index-1)
        return

    def onDown(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Move an item in the list down."""
        index = self.listCtrlFiles.GetFirstSelected()
        if index > -1 and index != len(self.datasets)-1:
            temp = self.datasets[index]
            self.datasets[index] = self.datasets[index+1]
            self.datasets[index+1] = temp
            self.fillList()
            self.listCtrlFiles.Select(index+1)
        return

    def onAdd(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Append files to the list."""
        dir, filename = os.path.split(self.fullpath)
        if not dir: dir = os.path.abspath('.')

        matchstring = "PDF data files (*.gr)|*.gr|PDF fit files (*.fgr)|*.fgr|PDF fit files (*.fit)|*.fit|PDF calculation files (*.cgr)|*.cgr|PDF calculation files (*.calc)|*.calc|All Files|*"
        d = wx.FileDialog(None, "Choose files", dir, "", matchstring,
                wx.OPEN|wx.FILE_MUST_EXIST|wx.MULTIPLE)
        paths = []
        if d.ShowModal() == wx.ID_OK:
            paths = d.GetPaths()
            d.Destroy()

        # Assign the doping. Default to 0.0
        newdatasets = []
        for path in paths:
            self.fullpath = path

            # Look for the doping in the filename
            doping = 0.0
            rx = {'f' : r'(?:\d+(?:\.\d*)?|\d*\.\d+)' }
            # Search for x123, X123, doping123, Doping123.
            # Is there a better regexp? Probably...
            regexp = r"(?:X|x|Doping|doping)(%(f)s)" % rx
            res = re.search(regexp, os.path.basename(path))
            if res:
                doping = float(res.groups()[0])
            else:
                # Look in the file
                infile = file(path,'r')
                datastring = infile.read()
                infile.close()
                # Look for it first in the file
                res = re.search(r'^#+ start data\s*(?:#.*\s+)*', datastring, re.M)
                # start_data is position where the first data line starts
                if res:
                    start_data = res.end()
                else:
                    res = re.search(r'^[^#]', datastring, re.M)
                    if res:
                        start_data = res.start()
                    else:
                        start_data = 0
                header = datastring[:start_data]
                # parse header to get doping
                regexp = r"\b(?:x|doping)\ *=\ *(%(f)s)\b" % rx
                res = re.search(regexp, header)
                if res:
                    doping = float(res.groups()[0])
            # Add the new path
            if doping < 0: doping = 0.0
            newdatasets.append([doping, path])

        self.datasets.extend(newdatasets)
        self.fillList()
        return

    def onDelete(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Delete selected files from the list."""
        idxlist = []
        item = self.listCtrlFiles.GetFirstSelected()
        while item != -1:
            idxlist.append(item)
            item = self.listCtrlFiles.GetNextSelected(item)

        idxlist.reverse()
        for item in idxlist:
            del self.datasets[item]
        self.fillList()
        return

    def onOK(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Let's go!"""
        dvals = [tp[0] for tp in self.datasets]
        paths = [tp[1] for tp in self.datasets]
        base = self.textCtrlBaseElement.GetValue()
        dopant = self.textCtrlDopant.GetValue()
        # Value checks will take place in makeDopingSeries
        org = makeDopingSeries(self.mainFrame.control, self.fit, base, dopant,
                paths, dvals)
        self.treeCtrlMain.ExtendProjectTree(org, clear=False)
        self.mainFrame.needsSave()
        self.onCancel(event)
        return

    def onCancel(self, event): # wxGlade: DopingSeriesPanel.<event_handler>
        """Let's go, but not actually do anything."""
        self.mainFrame.setMode("fitting")
        self.treeCtrlMain.UnselectAll()
        self.mainFrame.switchRightPanel("blank")
        return

    ## Utility functions
    def checkConfiguration(self):
        """Verify that the dopant and base are elements.
        
        More detailed checking is done in the control method.
        """
        from diffpy.pdffit2 import is_element
        base = self.textCtrlBaseElement.GetValue()
        dopant = self.textCtrlDopant.GetValue()
        # Make sure that the base and dopant are actual elements
        base = base.title()
        dopant = dopant.title()
        if not is_element(base):
            raise ControlValueError("'%s' is not an element!"%base)
        if not is_element(dopant):
            raise ControlValueError("'%s' is not an element!"%dopant)
        return

    def fillList(self):
        """Fill the list with the datasets."""
        self.listCtrlFiles.DeleteAllItems()
        names = [pair[1] for pair in self.datasets]
        cp = os.path.commonprefix(names)
        lcp = len(cp)
        for doping, filename in self.datasets:
            shortname = ".../" + filename[lcp:]
            index = self.listCtrlFiles.InsertStringItem(sys.maxint, str(doping))
            self.listCtrlFiles.SetStringItem(index, 1, shortname)
        return

    ## Needed by mainframe
    def onTreeSelChanged(self, event):
        """Set the current fit when the tree selection changes."""
        selections = self.treeCtrlMain.GetSelections()
        self.fit = None
        if len(selections) == 1:
            node = selections[0]
            nodetype = self.treeCtrlMain.GetNodeType(node)
            if nodetype == 'fit':
                self.fit = self.treeCtrlMain.GetControlData(node)
        self.refresh()
        return

    ## Required by PDFPanel
    def refresh(self):
        """Block out OK button if there is no fit.

        This also blocks OK if the fit has no datasets or structures.
        """
        # We can't rely on Veto to block unwanted tree selections on windows.
        # So, we have to check for errors here.
        node = None
        nodetype = None
        selections = self.treeCtrlMain.GetSelections()
        if selections: 
            node = selections[0]
            nodetype = self.treeCtrlMain.GetNodeType(node)

        if node and nodetype == "fit" \
                and self.fit and self.fit.hasDataSets() \
                and self.fit.hasStructures():
            self.goButton.Enable()
        else:
            self.goButton.Enable(False)
        return

# end of class DopingSeriesPanel

__id__ = "$Id$"
