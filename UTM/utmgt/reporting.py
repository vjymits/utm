__author__ = 'sharvija'
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import cm, inch
from reportlab.lib.colors import Color, PCMYKColor
from models import TestSuites, TestCases
from UTM.settings import MEDIA_ROOT
import threading
import time, datetime



class ReportTestSuites(threading.Thread):

    def __init__(self, reportFile):
        self.reportName = reportFile
        threading.Thread.__init__(self)

    def run(self):
        self.generateTableOfTestCases()

    def generateTableOfTestCases(self):
        print "report: "+self.reportName
        testSuite = TestSuites.objects.get(report=self.reportName)
        print str(testSuite)
        if testSuite is None:
            return
        testCases = TestCases.objects.filter(testSuite=testSuite)
        columns = ['TestCaseId', 'TestCase', 'Result', 'Attachment']
        name = MEDIA_ROOT+'/'+self.reportName
        doc = SimpleDocTemplate(name, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,
                                bottomMargin=18)
        doc.pagesize = landscape(A4)
        elements = []
        data = [columns]
        #pie_data={'passed': 0,'retest': 0, 'blocked':0 , 'failed':0 , 'untested':0 , 'retest':0}
        pie_data={}
        for testCase in testCases:
            row =[str(testCase.id), str(testCase.testCase), testCase.result,str(testCase.output)]
            data.append(row)
            pie_data[testCase.result]= pie_data.get(testCase.result, 0)+1
        style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])
        #Configure style and word wrap
        s = getSampleStyleSheet()
        s = s["BodyText"]
        s.wordWrap = 'CJK'
        data2 = [[Paragraph(cell, s) for cell in row] for row in data]
        t=Table(data2)
        t.setStyle(style)
        #Send the data and build the file
        drw= self.Pie(pie_data)
        elements.append(drw)

        elements.append(Spacer(1, 48))
        elements.append(t)
        doc.build(elements)
        return name



    class Pie(_DrawingEditorMixin,Drawing):
        def __init__(self, pie_data, width=400,height=200):
            apply(Drawing.__init__,(self,width,height))
            self._add(self,Pie(),name='chart',validate=None,desc=None)
            self.chart.x                    = 20
            self.chart.y                    = (self.height-self.chart.height)/2
            self.chart.slices.strokeWidth   = 1
            self.chart.slices.popout        = 1
            self.chart.direction            = 'clockwise'
            self.chart.width                = self.chart.height
            self.chart.startAngle           = 90
            self.chart.slices[0].popout     = 10
            self._add(self,Legend(),name='legend',validate=None,desc=None)
            self.legend.x                   = width - 20
            self.legend.y                   = 0
            self.legend.boxAnchor           = 'se'
            self.legend.subCols[1].align    = 'right'
            # these data can be read from external sources
            data=[]
            categories=[]
            for d in pie_data.keys():
                categories.append(d)
                data.append(pie_data.get(d, 0))
            #data                = (9, 7, 6, 4, 2.5, 1.0)
            #categories          = ('A','B','C','D','E','F',)

            colors              = [PCMYKColor(0,1,550,x) for x in (1030,2080,3060,440,4520,2225)]
            self.chart.data     = data
            self.chart.labels   = map(str, self.chart.data)
            self.legend.colorNamePairs = zip(colors, categories)
            for i, color in enumerate(colors): self.chart.slices[i].fillColor  = color




