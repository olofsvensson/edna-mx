'''
Created on May 9, 2016

@author: svensson
'''

import os
import sys
import html
import PIL.Image
import json
import time
import base64
import tempfile

import markupv1_10

# Report version
REPORT_VERSION = 1.0

class WorkflowStepReport(object):

    def __init__(self, stepType, stepTitle=""):
        self.imageList = None
        self.dictReport = {}
        self.dictReport["version"] = REPORT_VERSION
        self.dictReport["type"] = stepType
        self.dictReport["title"] = stepTitle
        self.dictReport["items"] = []

    def setTitle(self, stepTitle):
        self.dictReport["title"] = stepTitle


    def addInfo(self, infoText):
        self.dictReport["items"].append({"type": "info",
                                         "value": infoText})

    def addWarning(self, infoText):
        self.dictReport["items"].append({"type": "warning",
                                         "value": infoText})

    def startImageList(self):
        self.imageList = {}
        self.imageList["type"] = "images"
        self.imageList["items"] = []

    def endImageList(self):
        self.dictReport["items"].append(self.imageList)
        self.imageList = None

    def __createImageItem(self, pathToImage, imageTitle, pathToThumbnailImage=None,
                          thumbnailHeight=None, thumbnailWidth=None):
        item = {}
        item["type"] = "image"
        item["suffix"] = pathToImage.split(".")[-1]
        item["title"] = imageTitle
        im = PIL.Image.open(pathToImage)
        item["xsize"] = im.size[0]
        item["ysize"] = im.size[1]
        item["value"] = base64.b64encode(open(pathToImage, "rb").read()).decode("utf-8")
        if pathToThumbnailImage is None:
            if thumbnailHeight is not None and thumbnailWidth is not None:
                item["thumbnailSuffix"] = pathToImage.split(".")[-1]
                item["thumbnailXsize"] = thumbnailHeight
                item["thumbnailYsize"] = thumbnailWidth
                item["thumbnailValue"] = base64.b64encode(open(pathToImage, "rb").read()).decode("utf-8")
        else:
            item["thumbnailSuffix"] = pathToThumbnailImage.split(".")[-1]
            thumbnailIm = PIL.Image.open(pathToThumbnailImage)
            item["thumbnailXsize"] = thumbnailIm.size[0]
            item["thumbnailYsize"] = thumbnailIm.size[1]
            item["thumbnailValue"] = base64.b64encode(open(pathToThumbnailImage, "rb").read()).decode("utf-8")
        return item

    def addImage(self, pathToImage, imageTitle="", pathToThumbnailImage=None, thumbnailHeight=None, thumbnailWidth=None):
        if self.imageList is None:
            self.dictReport["items"].append(self.__createImageItem(pathToImage, imageTitle,
                                                                   pathToThumbnailImage, thumbnailHeight, thumbnailWidth))
        else:
            self.imageList["items"].append(self.__createImageItem(pathToImage, imageTitle,
                                                                  pathToThumbnailImage, thumbnailHeight, thumbnailWidth))

    def addTable(self, title, columns, data, orientation="horizontal"):
        item = {}
        item["type"] = "table"
        item["title"] = title
        item["columns"] = columns
        item["data"] = data
        item["orientation"] = orientation
        self.dictReport["items"].append(item)


    def addLogFile(self, title, linkText, pathToLogFile):
        item = {}
        item["type"] = "logFile"
        item["title"] = title
        item["linkText"] = linkText
        item["logText"] = open(pathToLogFile, 'rb').read().decode('ISO-8859-1')
        self.dictReport["items"].append(item)


    def renderJson(self, pathToJsonDir):
        pathToJsonFile = os.path.join(pathToJsonDir, "report.json")
        open(pathToJsonFile, "w").write(json.dumps(self.dictReport, indent=4))
        return pathToJsonFile

    def renderHtml(self, pathToHtmlDir, nameOfIndexFile="index.html"):
        page = markupv1_10.page(mode='loose_html')
        page.init(title=self.dictReport["title"],
                        footer="Generated on %s" % time.asctime())
        page.div(align_="LEFT")
        page.h1()
        page.strong(self.dictReport["title"])
        page.h1.close()
        page.div.close()
        for item in self.dictReport["items"]:
            if item["type"] == "info":
                page.p(item["value"])
            if item["type"] == "warning":
                page.font(_color="red", size="+1")
                page.p()
                page.strong(item["value"])
                page.p.close()
                page.font.close()
            elif item["type"] == "image":
                self.__renderImage(page, item, pathToHtmlDir)
                page.br()
                page.p(item["title"])
            elif item["type"] == "images":
                page.table()
                page.tr(align_="CENTER")
                for item in item["items"]:
                    page.td()
                    page.table()
                    page.tr()
                    page.td()
                    self.__renderImage(page, item, pathToHtmlDir)
                    page.td.close()
                    page.tr.close()
                    page.tr(align_="CENTER")
                    page.td(item["title"])
                    page.tr.close()
                    page.table.close()
                    page.td.close()
                page.tr.close()
                page.table.close()
                page.br()
            elif item["type"] == "table":
                page.h3()
                page.strong(item["title"])
                page.h3.close()
                page.table(border_="1",
                           cellpadding_="2")
                if "orientation" in item and item["orientation"] == "vertical":
                    for index1 in range(len(item["columns"])):
                        page.tr(align_="CENTER")
                        page.th(item["columns"][index1].replace("\n", "<br>"), bgcolor_="#F0F0FF", align_="LEFT")
                        for index2 in range(len(item["data"])):
                            page.th(str(item["data"][index2][index1]).replace("\n", "<br>"), bgcolor_="#FFFFA0")
                        page.tr.close()
                else:
                    page.tr(align_="CENTER", bgcolor_="#F0F0FF")
                    for column in item["columns"]:
                        page.th(column.replace("\n", "<br>"))
                    page.tr.close()
                    for listRow in item["data"]:
                        page.tr(align_="CENTER", bgcolor_="#FFFFA0")
                        for cell in listRow:
                            page.th(str(cell).replace("\n", "<br>"))
                        page.tr.close()
                page.table.close()
            elif item["type"] == "logFile":
                fd, pathToLogHtml = tempfile.mkstemp(suffix=".html",
                                                     prefix=item["title"].replace(" ", "_") + "_",
                                                     dir=pathToHtmlDir)
                os.close(fd)
                pageLogHtml = markupv1_10.page()
                pageLogHtml.h1(item["title"])
                pageLogHtml.pre(html.escape(item["logText"]))
                open(pathToLogHtml, "w").write(str(pageLogHtml))
                os.chmod(pathToLogHtml, 0o644)
                page.p()
                page.a(item["linkText"], href_=os.path.basename(pathToLogHtml))
                page.p.close()
        html = str(page)
        pagePath = os.path.join(pathToHtmlDir, nameOfIndexFile)
        filePage = open(pagePath, "w")
        filePage.write(html)
        filePage.close()
        return pagePath

    def __renderImage(self, page, item, pathToHtmlDir):
        imageName = item["title"].replace(" ", "_")
        pathToImage = os.path.join(pathToHtmlDir, "{0}.{1}".format(imageName, item["suffix"]))
        if os.path.exists(pathToImage):
            fd, pathToImage = tempfile.mkstemp(suffix="." + item["suffix"],
                                               prefix=imageName + "_",
                                               dir=pathToHtmlDir)
            os.close(fd)
        open(pathToImage, "w").write(base64.b64decode(item["value"]))
        os.chmod(pathToImage, 0o644)
        if "thumbnailValue" in item:
            thumbnailImageName = imageName + "_thumbnail"
            pathToThumbnailImage = os.path.join(pathToHtmlDir, "{0}.{1}".format(thumbnailImageName, item["suffix"]))
            if os.path.exists(pathToThumbnailImage):
                pathToThumbnailImage = tempfile.mkstemp(suffix="." + item["suffix"],
                                                        prefix=thumbnailImageName + "_",
                                                        dir=pathToHtmlDir)[1]
            open(pathToThumbnailImage, "w").write(base64.b64decode(item["value"]))
            os.chmod(pathToThumbnailImage, 0o644)
            pageReferenceImage = markupv1_10.page(mode='loose_html')
            pageReferenceImage.init(title=imageName, footer="Generated on %s" % time.asctime())
            pageReferenceImage.h1(imageName)
            pageReferenceImage.br()
            pageReferenceImage.img(src=os.path.basename(pathToImage),
                                   title=imageName,
                                   width=item["xsize"], height=item["ysize"])
            pageReferenceImage.br()
            pathPageReferenceImage = os.path.join(pathToHtmlDir, "{0}.html".format(imageName))
            filePage = open(pathPageReferenceImage, "w")
            filePage.write(str(pageReferenceImage))
            filePage.close()
            page.a(href=os.path.basename(pathPageReferenceImage))
            page.img(src=os.path.basename(pathToThumbnailImage),
                     title=imageName, width=item["thumbnailXsize"], height=item["thumbnailYsize"])
            page.a.close()
        else:
            page.img(src=os.path.basename(pathToImage),
                     title=item["title"],
                     width=item["xsize"],
                     height=item["ysize"])
