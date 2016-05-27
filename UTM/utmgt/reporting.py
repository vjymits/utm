__author__ = 'sharvija'
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from models import TestSuites, TestCases
from UTM.settings import MEDIA_ROOT
import threading


class ReportTestSuites(threading.Thread):

    def __init__(self, reportFile):
        self.reportName = reportFile
        threading.Thread.__init__(self)

    def run(self):
        self.genrateTableOfTestCases()

    def genrateTableOfTestCases(self):
        print "report: "+self.reportName
        testSuite = TestSuites.objects.get(report=self.reportName)
        print str(testSuite)
        if testSuite is None:
            return
        testCases = TestCases.objects.filter(testSuite=testSuite)
        columns = ['TestCaseId', 'TestCase', 'result', 'attachment']
        name = MEDIA_ROOT+'/'+self.reportName
        doc = SimpleDocTemplate(name, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,
                                bottomMargin=18)
        doc.pagesize = landscape(A4)
        elements = []
        data = [columns]
        for testCase in testCases:
            row =[str(testCase.id), str(testCase.testCase), testCase.result, str(testCase.output)]
            data.append(row)
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
        elements.append(t)
        doc.build(elements)
        return name




