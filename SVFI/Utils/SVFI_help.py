# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SVFI_help.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 541)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 600, 492))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\"\n"
                                                  "                                            font-size:12pt; font-weight:600; color:#ffffff;\">快速补帧流程：（鼠标悬浮在选项上可见帮助信息）</span></p><p><span\n"
                                                  "                                            style=\" color:#ffffff;\">0. 请确保本软件在</span><span style=\"\n"
                                                  "                                            font-weight:600; color:#ffffff;\">纯英文、无特殊标点符号及空格的路径</span><span\n"
                                                  "                                            style=\" color:#ffffff;\">下运行</span></p><p><span\n"
                                                  "                                            style=\" color:#ffffff;\">1.\n"
                                                  "                                            选择要补帧的文件。可以选择多个视频文件进行批量补帧，也可以选择包括图片序列的文件夹，后者需要手动填写输入帧率。如果输入的文件有误，</span><span\n"
                                                  "                                            style=\" font-weight:600; color:#ffffff;\">需要重新拖动文件或者点击下方的输入按钮</span></p><p><span\n"
                                                  "                                            style=\" color:#ffffff;\">2. 确认</span><span style=\"\n"
                                                  "                                            font-weight:600; color:#ffffff;\">输入和输出</span><span style=\"\n"
                                                  "                                            color:#ffffff;\">帧率</span></p><p><span style=\"\n"
                                                  "                                            color:#ffffff;\">3. 按“</span><span style=\"\n"
                                                  "                                            font-weight:600; color:#ffffff;\">一键补帧</span><span style=\"\n"
                                                  "                                            color:#ffffff;\">”完成补帧操作，也可以在</span><span style=\"\n"
                                                  "                                            font-size:12pt; font-weight:600; color:#ffffff;\">高级设置</span><span\n"
                                                  "                                            style=\" color:#ffffff;\">界面设置相关参数，并在输出界面点击</span><span\n"
                                                  "                                            style=\" font-weight:600; color:#ffffff;\">开始补帧</span><span\n"
                                                  "                                            style=\" color:#ffffff;\">按钮补帧（A卡补帧需要在高级设置手动设置参数）</span></p><p><span\n"
                                                  "                                            style=\" color:#ffffff;\">4. 在</span><span style=\"\n"
                                                  "                                            font-weight:600; color:#ffffff;\">工具箱</span><span style=\"\n"
                                                  "                                            color:#ffffff;\">一页进行</span><span style=\"\n"
                                                  "                                            font-weight:600; color:#ffffff;\">gif制作</span><span style=\"\n"
                                                  "                                            color:#ffffff;\">、</span><span style=\" font-weight:600;\n"
                                                  "                                            color:#ffffff;\">音视频合并</span><span style=\"\n"
                                                  "                                            color:#ffffff;\">及</span><span style=\" font-weight:600;\n"
                                                  "                                            color:#ffffff;\">已有区块合并（视频合并失败使用）</span></p><p><span\n"
                                                  "                                            style=\" font-weight:600; font-style:italic; color:#ffffff;\">软件最终解释权归SVFI开发团队所有</span></p><p><br/></p></body></html>\n"
                                                  "                                        "))
