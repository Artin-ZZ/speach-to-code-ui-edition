##########################
# Importing Dependencies #
##########################
from PyQt5 import QtCore, QtGui, QtWidgets









#################
# Main UI Class #
#################
class UI_STC(object):
    def setupUi(self, stc):

        ## Main Window/Frame ##
        stc.setObjectName("stc")
        stc.setFixedSize(1079, 715)
        self.centralwidget = QtWidgets.QWidget(stc)
        self.centralwidget.setObjectName("centralwidget")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.pages.setObjectName("pages")
        self.start = QtWidgets.QWidget()
        self.start.setStyleSheet("border-radius: 1px")
        self.start.setObjectName("start")
        self.back_start = QtWidgets.QLabel(self.start)
        self.back_start.setGeometry(QtCore.QRect(0, -10, 1081, 731))
        self.back_start.setText("")
        self.back_start.setPixmap(QtGui.QPixmap("Pics/back_start.jpg"))
        self.back_start.setObjectName("back_start")
        self.sp_to_code = QtWidgets.QLabel(self.start)
        self.sp_to_code.setGeometry(QtCore.QRect(360, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("word [    ]")
        font.setPointSize(16)
        self.sp_to_code.setFont(font)
        self.sp_to_code.setStyleSheet("color: rgb(255, 255, 255);")
        self.sp_to_code.setAlignment(QtCore.Qt.AlignCenter)
        self.sp_to_code.setObjectName("Sp_to_code")

        ## About Developer Bttn ##
        self.ab_dev = QtWidgets.QPushButton(self.start)
        self.ab_dev.setGeometry(QtCore.QRect(0, 0, 251, 51))
        font.setFamily("Word Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ab_dev.setFont(font)
        self.ab_dev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ab_dev.setStyleSheet("QPushButton {\n""background-color: rgb(196, 93, 255);\n""border-radius: 20px;\n""color: rgb(31, 12, 47);\n""}\n""QPushButton:hover {\n""background-color: rgb(95, 0, 143);\n""color: rgb(181, 83, 255);\n""}")
        self.ab_dev.setObjectName("About Developer")

        ## Quit Button ##
        self.qiut_btn = QtWidgets.QPushButton(self.start)
        self.qiut_btn.setGeometry(QtCore.QRect(500, 550, 250, 40))
        font.setFamily("Word Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.qiut_btn.setFont(font)
        self.qiut_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.qiut_btn.setStyleSheet("QPushButton {\n""background-color: rgb(0, 196, 255);\n""border-radius: 20px;\n""color: rgb(255, 255, 255);\n""}\n""QPushButton:hover {\n""background-color: rgb(2, 65, 255);\n""color: rgb(0, 0, 0);\n""}")
        self.qiut_btn.setObjectName("Quit App")

        ## Let's Go / Start Button ##
        self.letsgo = QtWidgets.QPushButton(self.start)
        self.letsgo.setGeometry(QtCore.QRect(429, 467, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.letsgo.setFont(font)
        self.letsgo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letsgo.setStyleSheet("QPushButton {\n""color: rgb(255, 255, 255);\n""}\n""QPushButton:hover {\n""\n""color: rgb(55, 26, 70);\n""}")
        self.letsgo.setObjectName("letsgo")

        ## Label For Start Page Title Pic ##
        self.label = QtWidgets.QLabel(self.start)
        self.label.setGeometry(QtCore.QRect(0, 250, 731, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pics/logo.png"))
        self.label.setObjectName("label")
        self.pages.addWidget(self.start)

        ## Rest Of The Ui Props ##
        self.select = QtWidgets.QWidget()
        self.select.setStyleSheet("border-radius: 1px;")
        self.select.setObjectName("select")
        self.back_select = QtWidgets.QLabel(self.select)
        self.back_select.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.back_select.setText("")
        self.back_select.setPixmap(QtGui.QPixmap("Pics/select.jpg"))
        self.back_select.setObjectName("back_select")

        ## Label Pic Number Two ##
        self.label_3 = QtWidgets.QLabel(self.select)
        self.label_3.setGeometry(QtCore.QRect(330, 380, 381, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Pics/Astronautـselect.png"))
        self.label_3.setObjectName("label_3")

        ## Text Label In page 2 ##
        self.welc_screen_lbl = QtWidgets.QLabel(self.select)
        self.welc_screen_lbl.setGeometry(QtCore.QRect(10, 110, 781, 221))
        self.welc_screen_lbl.setText("")
        self.welc_screen_lbl.setObjectName("label_welc_screen")
        self.welc_screen_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Word Blasck")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(30)
        self.welc_screen_lbl.setFont(font)

        ## Updating Label ##
        self.updt_lbl = QtWidgets.QLineEdit(self.select)
        self.updt_lbl.setGeometry(QtCore.QRect(40, 330, 991, 91))
        self.updt_lbl.setReadOnly(True)
        self.updt_lbl.setObjectName("update_lbl")
        self.updt_lbl.setStyleSheet("background-image : url(Pics/question.jpg);""color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(30)
        self.updt_lbl.setFont(font)

        ## Profile And UserName For Showing In The App ##
        self.username = QtWidgets.QLabel(self.select)
        self.username.setGeometry(QtCore.QRect(100, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Cocogoose [pyrs]")
        font.setPointSize(14)
        font.setItalic(False)
        self.username.setFont(font)
        self.username.setStyleSheet("color: rgb(249, 249, 249);")
        self.username.setObjectName("username")
        self.profile = QtWidgets.QLabel(self.select)
        self.profile.setGeometry(QtCore.QRect(30, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Cocogoose [pyrs]")
        font.setPointSize(16)
        font.setItalic(False)
        self.profile.setFont(font)
        self.profile.setStyleSheet("background-color: rgb(226, 178, 255, 200);\n""border-radius: 25px;\n""color: rgb(44, 18, 66);")
        self.profile.setAlignment(QtCore.Qt.AlignCenter)
        self.profile.setObjectName("profile")
        self.pages.addWidget(self.select)
        ## Frame 1 ##
        self.frame = QtWidgets.QFrame()
        self.frame.setGeometry(QtCore.QRect(240, 110, 631, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n""border-radius: 30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        ## Frame 2 ##
        self.frame_2 = QtWidgets.QFrame()
        self.frame_2.setGeometry(QtCore.QRect(280, 80, 511, 311))
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255,);\n""border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        ## Go Back Button ##
        self.q_app = QtWidgets.QPushButton(self.select)
        self.q_app.setGeometry(QtCore.QRect(80, 501, 301, 71))
        font.setFamily("Word Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.q_app.setFont(font)
        self.q_app.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.q_app.setStyleSheet("QPushButton {\n""background-color: rgb(196, 93, 255);\n""border-radius: 20px;\n""color: rgb(31, 12, 47);\n""}\n""QPushButton:hover {\n""background-color: rgb(95, 0, 143);\n""color: rgb(181, 83, 255);\n""}")
        self.q_app.setObjectName("Go Back")

        ## Start Button ##
        self.strt = QtWidgets.QPushButton(self.select)
        self.strt.setGeometry(QtCore.QRect(740, 520, 300, 51))
        font.setFamily("Word Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.strt.setFont(font)
        self.strt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.strt.setStyleSheet("QPushButton {\n""background-color: rgb(196, 93, 255);\n""border-radius: 20px;\n""color: rgb(31, 12, 47);\n""}\n""QPushButton:hover {\n""background-color: rgb(95, 0, 143);\n""color: rgb(181, 83, 255);\n""}")
        self.strt.setObjectName("Start_sc Btn")


        ## Voice Commands Guide Button ##
        self.vcg = QtWidgets.QPushButton(self.select)
        self.vcg.setGeometry(QtCore.QRect(770, 10, 301, 81))
        font.setFamily("Word Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vcg.setFont(font)
        self.vcg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vcg.setStyleSheet("QPushButton {\n""background-color: rgb(196, 93, 255);\n""border-radius: 20px;\n""color: rgb(31, 12, 47);\n""}\n""QPushButton:hover {\n""background-color: rgb(95, 0, 143);\n""color: rgb(181, 83, 255);\n""}")
        self.vcg.setObjectName("Go Back")

        stc.setCentralWidget(self.centralwidget)

        self.retranslateUi(stc)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(stc)

    def retranslateUi(self, stc):
        _translate = QtCore.QCoreApplication.translate
        stc.setWindowTitle(_translate("stc", "Speach To Code HTML Edition V-4.1.0"))
        self.sp_to_code.setText(_translate("stc", "Version 4.1.0"))
        self.qiut_btn.setText(_translate("stc", "Exit App"))
        self.letsgo.setText(_translate("stc", "Let's Go"))
        self.ab_dev.setText(_translate("stc", "About Developer"))
        self.username.setText(_translate("stc", "username"))
        self.profile.setText(_translate("stc", "u"))
        self.vcg.setText(_translate("stc", "Voice Commands Guide"))
        self.q_app.setText(_translate("stc", "Quit App"))
        self.updt_lbl.setText(_translate("stc", ""))
        self.strt.setText(_translate("stc", "Start / continue"))
        self.welc_screen_lbl.setText(_translate("stc", """
        ----------------------------------------------------------------------------------------------------------			
		   ***
		  **/**
		 **/||**	| J A R V I S - SPEACH To Code  <HTML EDITION>
		 **||/**	| ----------------------------------------------------------------
		  **/**	| By A R T I N   Z A F A R I
 		   ***
        ----------------------------------------------------------------------------------------------------------"""))