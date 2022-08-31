##############################
#  Importing Dependencies    #
##############################
import os , sys, pyttsx3, datetime, platform, sqlite3
import speech_recognition as sp
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from src.Panel_UI import UI_STC
from PyQt5.QtWebEngineWidgets import QWebEngineView












##################
# STC Root Class #
##################
class Root(QMainWindow):
    def __init__(self):

        #### Init The Ui ####
        QMainWindow.__init__(self)
        self.ui = UI_STC()
        self.ui.setupUi(self)
        self.show()

        #### set info user ####
        self.ui.username.setText(os.getlogin())
        self.ui.profile.setText(str(os.getlogin())[0])

        #### Set Button ####
        self.ui.letsgo.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.select))
        self.ui.ab_dev.clicked.connect(self.abdv)
        self.ui.qiut_btn.clicked.connect(self.quitapp)

        #### Set Back Button And Second page buttons ####
        self.ui.q_app.clicked.connect(self.quitapp)
        self.ui.vcg.clicked.connect(self.vcg_guide)
        self.ui.strt.clicked.connect(self.start_again)

        
    ##########################
    # Mouse Press Event Func #
    ##########################
    def mousePressEvent(self, evt):
        try:
            self.oldPos = evt.globalPos()
        except:
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

    #########################
    # Mouse Move Event Func #
    #########################
    def mouseMoveEvent(self, evt):
        try:
            delta = QPoint(evt.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = evt.globalPos()
        except:
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

    ######################
    # About Dialog Func  #
    ######################
    def abdv(self):
        try:
            dlg = AboutDialog()
            dlg.exec_()
        except:
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

    ###################
    # VCG Guide Func  #
    ###################
    def vcg_guide(self):
        try:
            command = "Voice-Commands-Guide.txt"
            os.system(command)
        except:
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

    #################
    # Quit App Func #
    #################
    def quitapp(self):
        self.close()
        exit()

    #####################
    # Start Method Func #
    #####################
    def start_again(self):
        try:
            instructions()
            WishMe()
            looper = 5

            while looper != 500:
                query = str(take_command())

                    ## Probability Of Commands ##
                if "open notepad" in query:
                    command = "C:\\Windows\\System32\\notepad.exe"
                    os.system(command)
                    
                
                elif "open browser" in query:
                    command = "start https://www.google.com"
                    os.system(command)
                    
                
                elif "clear log" in query:
                    clear_log()
                    speak("Log Cleard Successfuly")
                    
                
                elif "add address" in query:
                    dlg = AddAddress()
                    dlg.exec_()
                    

                elif "add attribute" in query:
                    dlg = AddAttb()
                    dlg.exec_()
                
                    

                elif "add audio" in query:
                    dlg = AddAud()
                    dlg.exec_()
                    

                elif "add br" in query:
                    speak("adding your br tag")
                    finalTag = (f"<br>\n")
                    f = open("index.html", "a")
                    f.write(finalTag)
                    f.close()
                    speak("br added!")
                    


                elif "add button" in query:
                    dlg = AddBtnDg()
                    dlg.exec_()
                    

                elif "add comment" in query:
                    dlg = AddCmDg()
                    dlg.exec_()
                
                    

                elif "add heading" in query:
                    dlg = AddHeadingDg()
                    dlg.exec_()
            
                    

                elif "add text" in query:
                    try:
                        speak("adding your text in a paragraph")
                        query = str(take_command())
                        text = query
                        finalTag = (f'<p>{text}</p>')
                        f = open("index.html", "a")
                        f.write(finalTag)
                        f.close()
                        speak("Text Added")
                        QMessageBox.information(QMessageBox(), "Done!", "Text Added.")
                    except:
                        QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")
                

                elif "add hr" in query:
                    try:
                        speak("adding your hr tag")
                        finalTag = (f"<hr>\n")
                        f = open("index.html", "a")
                        f.write(finalTag)
                        f.close()
                        speak("hr added!")
                        QMessageBox.information(QMessageBox(), "Done!", "Hr Added.")
                    except:
                        QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

                elif "add iframe" in query:
                    dlg = IFrametg()
                    dlg.exec_()
                    
                

                elif "add image" in query:
                    dlg = Addimg()
                    dlg.exec_()
                    

                elif "exit" in query:
                    speak("ending program, thanks for using Me ,Aka ,Jarvis, See You Next Time")
                    looper = 500
                    exit()
                    
                
                elif "time" in query:
                    try:
                        now = datetime.datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        speak(f"Current Time is: {current_time} O'Clock")
                        QMessageBox.information(QMessageBox(), "You Said 'Time'",f"Current Time: {current_time} (Hours,Minutes,Seconds)")
                    except:
                        QMessageBox.warning(QMessageBox(), "Oops! SomeThing Went Wrong.")


                elif "who are you" in query:
                    try:
                        speak("Hello There!, My Name Is Jarvis Im Here To Help You Create Your HTML Document.")
                        QMessageBox.information(QMessageBox(), "You Said 'Who Are You?'", "Hello There!, My Name Is Jarvis Im Here To Help You Create Your HTML Document.")
                    except:
                         QMessageBox.warning(QMessageBox(), "Oops! SomeThing Went Wrong.")
                
                elif "why are you helping me" in query:
                    try:
                        speak("Well, Because I Want To Help You Acheive Your Best, And To make html easy for you!")
                    except:
                        QMessageBox.warning(QMessageBox(), "Oops! SomeThing Went Wrong.")
                    

                elif "how old are you" in query:
                    try:
                        yr_of_birth = 2022
                        m_of_birth = 7
                        d_of_birth = 29
                        cr_yr = datetime.datetime.now().year
                        cr_month = datetime.datetime.now().month
                        cr_day = datetime.datetime.now().day
                        cr_age_yr = cr_yr - yr_of_birth
                        cr_age_month = cr_month - m_of_birth
                        cr_age_day = d_of_birth - cr_day
                        speak(f"Im {cr_age_yr} years, And {cr_age_month} Months ,And {cr_age_day} Days Old.")
                        QMessageBox.information(QMessageBox(), "You Asked For My Age", f"Im {cr_age_yr} years, And {cr_age_month} Months ,And {cr_age_day} Days Old.")
                    except:
                        QMessageBox.warning(QMessageBox(), "Oops! SomeThing Went Wrong.")

                elif "add paragraph" in query:
                    dlg = Addpg()
                    dlg.exec_()

                elif "add video" in query:
                    dlg = AddVideoDg()
                    dlg.exec_()
                

                elif "complete website" in query:
                    try:
                        speak("completing your website")
                        finalTag = (f"</body>\n</html>\n")
                        f = open("index.html", "a")
                        f.write(finalTag)
                        f.close()
                        speak("Website Completed!, Thanks for using Me.")
                        QMessageBox.information(QMessageBox(), "Done!", "Website Completed.")
                    except:
                        QMessageBox.warning(QMessageBox(), "Oops! SomeThing Went Wrong.")
                        

                elif "how are you today" in query:
                    try:
                        speak("Im A Fucking Program ,I Have No Emotions DumbAss")
                        QMessageBox.information(QMessageBox(), "Answer", "Im A Fucking Program I Have No Emotions DumbAss")
                    except:
                        QMessageBox.warning(QMessageBox(), "Oops! SomeThing Went Wrong.")
                    
                
                elif "do you know me" in query:
                    dlg = KnowMe()
                    dlg.exec_()

                else:
                    speak("REQUEST ERROR, SEE THE,'Voice Commands Guide.txt',FILE FOR HELP")
                    QMessageBox.warning(QMessageBox(), "REQUEST ERROR", "SEE THE 'Voice Commands Guide.txt' FILE FOR HELP")
                break
        except:
            # speak("Oops!, something went wrong, try again, or contact support.")
            # QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")
            pass





        


##########################
## About Dev Page Class ##
##########################
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedSize(600, 500)
        self.setWindowTitle("About Creator")

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()


        title = QLabel("Thanks For Using :)")
        font = title.font()
        font.setPointSize(20)
        font.setWeight(20)
        font.setBold(True)
        title.setFont(font)

        lbl_pic = QLabel()
        pixmap = QPixmap('Pics/About.png')
        pixmap = pixmap.scaledToWidth(500)
        lbl_pic.setPixmap(pixmap)
        lbl_pic.setFixedHeight(400)

        layout.addWidget(title)

        layout.addWidget(QLabel("Speach To Code"))
        layout.addWidget(lbl_pic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
###################################
## Necesry Voice Command Classes ##
###################################
## Do You Know Me Command ##
class KnowMe(QDialog):
    def __init__(self, *args, **kwargs):
        super(KnowMe, self).__init__(*args, **kwargs)
        ## Main Window
        self.setFixedSize(443, 297)
        self.setWindowTitle("You Said 'Do You Know Me?'")

        

        self.OKBtn = QtWidgets.QPushButton()
        self.OKBtn.setGeometry(QtCore.QRect(330, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(15)
        self.OKBtn.setFont(font)
        self.OKBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OKBtn.setObjectName("Okbtn")
        self.OKBtn.setText("Submit Answer")

        self.OKBtn.clicked.connect(self.OKBTN)

        layout = QVBoxLayout()

        ## Show Label ##
        self.show_lbl = QtWidgets.QLabel()
        self.show_lbl.setGeometry(QtCore.QRect(20, 30, 191, 31))
        self.show_lbl.setObjectName("show_lbl")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(15)
        self.show_lbl.setFont(font)
        self.show_lbl.setText("Enter Your Code here:")

        ## Text Box ##
        self.txt_box = QtWidgets.QLineEdit()
        self.txt_box.setGeometry(QtCore.QRect(20, 110, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(15)
        self.txt_box.setFont(font)
        self.txt_box.returnPressed.connect(lambda: self.txt_box.setFocus(Qt.ShortcutFocusReason))


        layout.addWidget(self.show_lbl)
        layout.addWidget(self.txt_box)
        layout.addWidget(self.OKBtn)
        self.setLayout(layout)
        

    def OKBTN(self):
        try:
            boss = "pointbreak"
            if self.txt_box.text() in boss:
                speak("yes i know you, you are my creator, thanks for creating me.")
            else:
                speak("You Are A Normal User")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

## Add Video Command ##
class AddVideoDg(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddVideoDg, self).__init__(*args, **kwargs)

        self.setFixedSize(600, 300)
        self.setWindowTitle("You Said 'Add Video'")

        layout = QVBoxLayout()

        ## Head label ##
        self.head_lbl = QtWidgets.QLabel()
        self.head_lbl.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.head_lbl.setText("Enter Video's Info Here:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.head_lbl.setFont(font)
        self.setObjectName("head_lbl")

        ## width label ##
        self.w_lbl = QtWidgets.QLabel()
        self.w_lbl.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.w_lbl.setText("Video's Width:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.w_lbl.setFont(font)
        self.w_lbl.setObjectName("width_lbl")

        ## width text box ##
        self.wd_tbx = QtWidgets.QLineEdit()
        self.wd_tbx.setGeometry(QtCore.QRect(10, 80, 581, 51))
        self.wd_tbx.setValidator(QIntValidator(self))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.wd_tbx.setFont(font)
        self.wd_tbx.setObjectName("wd_tbx")

        ## Height Label ##
        self.hg_lbl = QtWidgets.QLabel()
        self.hg_lbl.setGeometry(QtCore.QRect(10, 160, 91, 31))
        self.hg_lbl.setText("Video's Height:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.hg_lbl.setFont(font)
        self.hg_lbl.setObjectName("hg_lbl")

        ## height text box ##
        self.hg_tbx = QtWidgets.QLineEdit()
        self.hg_tbx.setGeometry(QtCore.QRect(10, 200, 581, 51))
        self.hg_tbx.setValidator(QIntValidator(self))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.hg_tbx.setFont(font)
        self.hg_lbl.setObjectName("hg_tbx")

        ## URL Label ##
        self.url_lbl = QtWidgets.QLabel()
        self.url_lbl.setGeometry(QtCore.QRect(10, 280, 111, 31))
        self.url_lbl.setText("Address / URL:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.url_lbl.setFont(font)
        self.url_lbl.setObjectName("url_lbl")

        ## URL text box ##
        self.url_tbx = QtWidgets.QLineEdit()
        self.url_tbx.setGeometry(QtCore.QRect(10, 320, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.url_tbx.setFont(font)
        self.url_tbx.setObjectName("url_tbx")

        ## Submit Button ## 
        self.subm_btn = QtWidgets.QPushButton()
        self.subm_btn.setGeometry(QtCore.QRect(10, 410, 581, 81))
        self.subm_btn.setText("Submit Info")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.subm_btn.setFont(font)
        self.subm_btn.setObjectName('subm_btn')
        
        ## btn connect ##
        self.subm_btn.clicked.connect(self.submbtn)


        layout.addWidget(self.head_lbl)
        layout.addWidget(self.w_lbl)
        layout.addWidget(self.wd_tbx)
        layout.addWidget(self.hg_lbl)
        layout.addWidget(self.hg_tbx)
        layout.addWidget(self.url_lbl)
        layout.addWidget(self.url_tbx)
        layout.addWidget(self.subm_btn)
        self.setLayout(layout)

        speak("adding your video tag")

    def submbtn(self):
        try:
            width = self.wd_tbx.text()
            height = self.hg_tbx.text()
            url = self.url_tbx.text()
            finalTag = (f"<video width=\"{width}\" height=\"{height}\" controls><source src=\"{url}.mp4\" type=\"video/mp4\"></video>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Video Added")
            QMessageBox.information(QMessageBox(), "Done!", "Video Added")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

## Add Image Command ##
class Addimg(QDialog):
    def __init__(self, *args, **kwargs):
        super(Addimg, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(600, 400)
        self.setWindowTitle("You Said 'Add Image'")

        layout = QVBoxLayout()

        ## Head label ##
        self.head_lbl = QtWidgets.QLabel()
        self.head_lbl.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.head_lbl.setText("Enter Images's Info Here:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.head_lbl.setFont(font)
        self.setObjectName("head_lbl")

        ## img Name Label ##
        self.nameimg = QtWidgets.QLabel()
        self.nameimg.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.nameimg.setText("Image Name:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.nameimg.setFont(font)
        self.setObjectName("nameimg")

        ## img Text box ##
        self.nameimg_tbx = QtWidgets.QLineEdit()
        self.nameimg_tbx.setGeometry(QtCore.QRect(10, 80, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.nameimg_tbx.setFont(font)
        self.nameimg_tbx.setObjectName("nameimg_tbx")

        ## width label ##
        self.w_lbl = QtWidgets.QLabel()
        self.w_lbl.setGeometry(QtCore.QRect(10, 160, 91, 31))
        self.w_lbl.setText("Image Width:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.w_lbl.setFont(font)
        self.w_lbl.setObjectName("width_lbl")

        ## width text box ##
        self.wd_tbx = QtWidgets.QLineEdit()
        self.wd_tbx.setGeometry(QtCore.QRect(10, 200, 581, 51))
        self.wd_tbx.setValidator(QIntValidator(self))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.wd_tbx.setFont(font)
        self.wd_tbx.setObjectName("wd_tbx")

        ## Height Label ##
        self.hg_lbl = QtWidgets.QLabel()
        self.hg_lbl.setGeometry(QtCore.QRect(10, 280, 111, 31))
        self.hg_lbl.setText("Image Height:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.hg_lbl.setFont(font)
        self.hg_lbl.setObjectName("hg_lbl")

        ## height text box ##
        self.hg_tbx = QtWidgets.QLineEdit()
        self.hg_tbx.setGeometry(QtCore.QRect(10, 320, 581, 51))
        self.hg_tbx.setValidator(QIntValidator(self))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.hg_tbx.setFont(font)
        self.hg_lbl.setObjectName("hg_tbx")

        ## URL Label ##
        self.url_lbl = QtWidgets.QLabel()
        self.url_lbl.setGeometry(QtCore.QRect(10, 420, 111, 31))
        self.url_lbl.setText("Address / URL:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.url_lbl.setFont(font)
        self.url_lbl.setObjectName("url_lbl")

        ## URL text box ##
        self.url_tbx = QtWidgets.QLineEdit()
        self.url_tbx.setGeometry(QtCore.QRect(10, 460, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.url_tbx.setFont(font)
        self.url_tbx.setObjectName("url_tbx")

        ## Submit Button ## 
        self.subm_bt = QtWidgets.QPushButton()
        self.subm_bt.setGeometry(QtCore.QRect(10, 540, 581, 81))
        self.subm_bt.setText("Submit Info")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.subm_bt.setFont(font)
        self.subm_bt.setObjectName("subm_bt")


        ## btn connect ##
        self.subm_bt.clicked.connect(self.sbmbtn)


        layout.addWidget(self.head_lbl)
        layout.addWidget(self.nameimg)
        layout.addWidget(self.nameimg_tbx)
        layout.addWidget(self.w_lbl)
        layout.addWidget(self.wd_tbx)
        layout.addWidget(self.hg_lbl)
        layout.addWidget(self.hg_tbx)
        layout.addWidget(self.url_lbl)
        layout.addWidget(self.url_tbx)
        layout.addWidget(self.subm_bt)
        self.setLayout(layout)

        speak("adding your image tag")
    
    def sbmbtn(self):
        try:
            img_name = self.nameimg_tbx.text()
            width = self.wd_tbx.text()
            height = self.hg_tbx.text()
            url = self.url_tbx.text()
            finalTag = (f"<img src=\"{url}\" width=\"{width}px\" height=\"{height}px\" alt=\"{img_name}\">\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("image added!")
            QMessageBox.information(QMessageBox(), "Done!", "Image Tag Added")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")


## Add Paragraph With typing Command ##
class Addpg(QDialog):
    def __init__(self, *args, **kwargs):
        super(Addpg, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(500, 150)

        self.setWindowTitle("You Said 'Add Paragraph'")

        layout = QVBoxLayout()

        ## pg Name Label ##
        self.pg_lbl = QtWidgets.QLabel()
        self.pg_lbl.setGeometry(QtCore.QRect(14, 10, 471, 61))
        self.pg_lbl.setText("Type In What You Want To See In The Paragraph:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(10)
        font.setPointSize(10)
        font.setBold(True)
        self.pg_lbl.setFont(font)
        self.setObjectName("pg_lbl")

        ## pg Text box ##
        self.pg_tbx = QtWidgets.QLineEdit()
        self.pg_tbx.setGeometry(QtCore.QRect(10, 90, 471, 211))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.pg_tbx.setFont(font)
        self.pg_tbx.setObjectName("pg_tbx")

        ## Submit Button ##
        self.subm_pg = QtWidgets.QPushButton()
        self.subm_pg.setGeometry(QtCore.QRect(10, 540, 581, 81))
        self.subm_pg.setText("Submit Info")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.subm_pg.setFont(font)
        self.subm_pg.setObjectName("subm_pg")

        self.subm_pg.clicked.connect(self.sbmpg)


        layout.addWidget(self.pg_lbl)
        layout.addWidget(self.pg_tbx)
        layout.addWidget(self.subm_pg)
        self.setLayout(layout)

        speak("adding your paragraph,\nNo Speech input for paragraph because paragraphs can be too long to speak")

    ## A little Problem Here to Fix :(
    def sbmpg(self):
        try:
            content = self.pg_tbx.text()
            finalTag = (f"<p>{content}</p>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("paragraph added!")
            QMessageBox.information(QMessageBox(), "Done!", "Paragraph Added")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")
        
## Add Frame Command ##
class IFrametg(QDialog):
    def __init__(self, *args, **kwargs):
        super(IFrametg, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(600, 300)
        self.setWindowTitle("You Said 'Add Frame'")

        layout = QVBoxLayout()

        ## Head label ##
        self.head_lbl = QtWidgets.QLabel()
        self.head_lbl.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.head_lbl.setText("Enter Frame's Info Here:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.head_lbl.setFont(font)
        self.setObjectName("head_lbl")

        ## width label ##
        self.w_lbl = QtWidgets.QLabel()
        self.w_lbl.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.w_lbl.setText("Enter Width of your ifame in pixels:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.w_lbl.setFont(font)
        self.w_lbl.setObjectName("width_lbl")

        ## width text box ##
        self.wd_tbx = QtWidgets.QLineEdit()
        self.wd_tbx.setGeometry(QtCore.QRect(10, 80, 581, 51))
        self.wd_tbx.setValidator(QIntValidator(self))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.wd_tbx.setFont(font)
        self.wd_tbx.setObjectName("wd_tbx")

        ## Height Label ##
        self.hg_lbl = QtWidgets.QLabel()
        self.hg_lbl.setGeometry(QtCore.QRect(10, 160, 91, 31))
        self.hg_lbl.setText("Enter height of your ifame in pixels:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.hg_lbl.setFont(font)
        self.hg_lbl.setObjectName("hg_lbl")

        ## height text box ##
        self.hg_tbx = QtWidgets.QLineEdit()
        self.hg_tbx.setGeometry(QtCore.QRect(10, 200, 581, 51))
        self.hg_tbx.setValidator(QIntValidator(self))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.hg_tbx.setFont(font)
        self.hg_lbl.setObjectName("hg_tbx")

        ## URL Label ##
        self.url_lbl = QtWidgets.QLabel()
        self.url_lbl.setGeometry(QtCore.QRect(10, 280, 111, 31))
        self.url_lbl.setText("paste/enter url for iframe:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.url_lbl.setFont(font)
        self.url_lbl.setObjectName("url_lbl")

        ## URL text box ##
        self.url_tbx = QtWidgets.QLineEdit()
        self.url_tbx.setGeometry(QtCore.QRect(10, 320, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.url_tbx.setFont(font)
        self.url_tbx.setObjectName("url_tbx")

        ## Submit Button ## 
        self.subm_btn = QtWidgets.QPushButton()
        self.subm_btn.setGeometry(QtCore.QRect(10, 410, 581, 81))
        self.subm_btn.setText("Submit Info")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.subm_btn.setFont(font)
        self.subm_btn.setObjectName('subm_btn')
        
        ## btn connect ##
        self.subm_btn.clicked.connect(self.sbbtn)


        layout.addWidget(self.head_lbl)
        layout.addWidget(self.w_lbl)
        layout.addWidget(self.wd_tbx)
        layout.addWidget(self.hg_lbl)
        layout.addWidget(self.hg_tbx)
        layout.addWidget(self.url_lbl)
        layout.addWidget(self.url_tbx)
        layout.addWidget(self.subm_btn)
        self.setLayout(layout)
        
        speak("Adding your iframe tag")

    def sbbtn(self):
        try:
            width = self.wd_tbx.text()
            height = self.hg_tbx.text()
            url = self.url_tbx.text()
            finalTag = (f"<iframe src=\"{url}\" width=\"{width}px\" height=\"{height}px\"></iframe>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("iframe added!")
            QMessageBox.information(QMessageBox(), "Done!", "Iframe Tag Added")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

class AddHeadingDg(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddHeadingDg, self).__init__(*args, **kwargs)

        self.setFixedSize(600, 300)
        self.setWindowTitle("You Said 'Add Frame'")

        layout = QVBoxLayout()

        ## Head Tag size Label ##
        self.head_size_lbl = QtWidgets.QLabel()
        self.head_size_lbl.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.head_size_lbl.setText("Enter The Size Of Heading Tag:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setWeight(10)
        font.setPointSize(10)
        self.head_size_lbl.setFont(font)
        self.head_size_lbl.setObjectName("HeadTaglbl")

        ## Head Tag size Text Box ##
        self.head_tbx = QtWidgets.QLineEdit()
        self.head_tbx.setGeometry(QtCore.QRect(10, 80, 581, 91))
        self.head_tbx.setPlaceholderText("1,2,3,... Number Only")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(10)
        font.setPointSize(10)
        font.setBold(True)
        self.head_tbx.setFont(font)
        self.head_tbx.setObjectName("headtagtbx")
        self.head_tbx.setValidator(QIntValidator())
        
        ## head tag content lbl ##
        self.head_cont = QtWidgets.QLabel()
        self.head_cont.setGeometry(QtCore.QRect(10, 200, 131, 41))
        self.head_cont.setText("Enter The Content Of Heading:")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setWeight(10)
        font.setPointSize(10)
        self.head_cont.setFont(font)
        self.head_cont.setObjectName("headcont")

        ## head tag cont tbx ##
        self.head_cont_tbx = QtWidgets.QLineEdit()
        self.head_cont_tbx.setGeometry(QtCore.QRect(10, 250, 581, 151))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(10)
        font.setPointSize(10)
        font.setBold(True)
        self.head_cont_tbx.setFont(font)
        self.head_cont_tbx.setObjectName("headtagtbx")

        ## Submit Button ## 
        self.submbtn = QtWidgets.QPushButton()
        self.submbtn.setGeometry(QtCore.QRect(10, 410, 581, 81))
        self.submbtn.setText("Submit Info")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.submbtn.setFont(font)
        self.submbtn.setObjectName('submbtn')

        ## Connect btn To Func ##
        self.submbtn.clicked.connect(self.sbtn)


        layout.addWidget(self.head_size_lbl)
        layout.addWidget(self.head_tbx)
        layout.addWidget(self.head_cont)
        layout.addWidget(self.head_cont_tbx)
        layout.addWidget(self.submbtn)
        self.setLayout(layout)
        

        speak("adding your heading, Tell me your heading Size")

    def sbtn(self):
        try:
            sizeOfHeadingTag = self.head_tbx.text()
            contentofheading = self.head_cont_tbx.text()
            finalTag = (f"<h{sizeOfHeadingTag}>{contentofheading}</h{sizeOfHeadingTag}>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Heading added!")
            QMessageBox.information(QMessageBox(), "Done!", "Heading Tag Added!")
        except:
            speak("Oops!, Something Went Wrong Please Try again.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, Something Went Wrong Please Try again.")


## Add comment Command ##
class AddCmDg(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddCmDg, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(600, 200)
        self.setWindowTitle("You Said 'Add Comment'")

        layout = QVBoxLayout()

        ## Label ##
        self.mlbl = QtWidgets.QLabel()
        self.mlbl.setGeometry(QtCore.QRect(10, 10, 151, 41))
        self.mlbl.setObjectName("mlbl")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(10)
        self.mlbl.setFont(font)
        self.mlbl.setText("Enter Your Comment Here:")

        ## text box ##
        self.tbx = QtWidgets.QLineEdit()
        self.tbx.setGeometry(QtCore.QRect(10, 70, 421, 101))
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setWeight(15)
        font.setPointSize(12)
        font.setBold(True)
        self.tbx.setFont(font)
        self.tbx.setObjectName("tbx")

        ## btn ##
        self.btn = QtWidgets.QPushButton()
        self.btn.setGeometry(QtCore.QRect(10, 180, 421, 91))
        self.btn.setText("Submit")
        font = QtGui.QFont()
        font.setFamily("Word Black")
        font.setBold(True)
        font.setWeight(10)
        font.setPointSize(10)
        self.btn.setFont(font)

        ## Connect btn ##
        self.btn.clicked.connect(self.mbtn)

        layout.addWidget(self.mlbl)
        layout.addWidget(self.tbx)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        
        
        speak("adding your comment...")
        
    def mbtn(self):
        try:
            comment = self.tbx.text()
            finalTag = (f"<!--{comment}-->\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Comment added!")
            QMessageBox.information(QMessageBox(), "Done!", "Comment Added.")
        except:
            speak("Oops!, Something Went Wrong Please Try again.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, Something Went Wrong Please Try again.")





## Add Button Class ##
class AddBtnDg(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddBtnDg, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(600, 200)
        self.setWindowTitle("You Said 'Add Button'")

        ## Main Label ##
        self.mlbl = QtWidgets.QLabel()
        self.mlbl.setText("Type In The Name Of Your button:")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.mlbl.setFont(font)
        self.setObjectName("mlbl")

        ## Main Text Box ##
        self.m_tbx = QtWidgets.QLineEdit()
        self.m_tbx.setPlaceholderText("Name of Your Button Here.")
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.m_tbx.setFont(font)
        self.m_tbx.setObjectName("m_tbx")

        ## Button For Submiting ##
        self.sbtn = QtWidgets.QPushButton()
        self.sbtn.setText("Submit Info")
        self.sbtn.setObjectName("sbtn")
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.sbtn.setFont(font)

        layout = QVBoxLayout()

        ## Btn connect ##
        self.sbtn.clicked.connect(self.sbtn_m)

        layout.addWidget(self.mlbl)
        layout.addWidget(self.m_tbx)
        layout.addWidget(self.sbtn)
        self.setLayout(layout)

        speak("adding your Button")
    
    def sbtn_m(self):
        try:
            buttonName = self.m_tbx.text()
            finalTag = (f'<button type="button">{buttonName}</button>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Button Added!")
            QMessageBox.information(QMessageBox(), "Done!", "Attribute/URL added!")
        except:
            speak("Oops!, Something Went Wrong Please Try again.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, Something Went Wrong Please Try again.")

## Add Audio Command ##
class AddAud(QDialog):
    def __init__(self, parent=None,*args, **kwargs):
        super(AddAud, self).__init__(parent ,*args, **kwargs)

        ## Main Wndow ##
        self.setFixedSize(600, 200)
        self.setWindowTitle("You said 'Add Audio'")

        layout = QVBoxLayout()

        ## Label ##
        self.milbl = QtWidgets.QLabel()
        self.milbl.setText("Browse / Paste Audio Path Here:")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.milbl.setFont(font)
        self.setObjectName("milbl")

        ## Tbx ##
        self.TBX = QtWidgets.QLineEdit()
        self.TBX.setPlaceholderText("your Audio Path Here.")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.TBX.setFont(font)
        self.setObjectName("TBX")

        ## Open File (Browse File) Button ##
        self.o_f = QtWidgets.QPushButton()
        self.o_f.setText("Browse Audio")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.o_f.setFont(font)
        self.setObjectName("o_f")

        ## S Btn ##
        self.submit = QtWidgets.QPushButton()
        self.submit.setText("Submit")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(10)
        font.setBold(True)
        self.submit.setFont(font)
        self.setObjectName("submit")

        ## S Btn Connect ##
        self.submit.clicked.connect(self.accSub)

        ## Connect Browse Audio Btn ##
        self.o_f.clicked.connect(self.op_File)

        layout.addWidget(self.milbl)
        layout.addWidget(self.TBX)
        layout.addWidget(self.o_f)
        layout.addWidget(self.submit)
        self.setLayout(layout)

        speak("Adding Your Audio")
    
    def accSub(self):
        try:
            audio_path = self.TBX.text()
            finalTag = (f'<audio controls autoplay><source src="{audio_path}" type="audio/mpeg"></audio>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Audio Added!")
            QMessageBox.information(QMessageBox(), "Done!", "Audio Added")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

    def op_File(self):
        try:
            path = QFileDialog.getOpenFileName(self, "Browse For Audio", "", "Audio Files(*.mp3)")
            if path != ('', ''):
                self.TBX.setText(path[0])
        
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")


## Add Attribute Command ##
class AddAttb(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddAttb, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(600, 300)
        self.setWindowTitle("You Said 'Add Attribute'")

        ## Page Layout ##
        layout = QVBoxLayout()

        ## Page Buttons And Text Boxes And Labels ##
        ## First Label ##
        self.flbl = QtWidgets.QLabel()
        self.flbl.setText("Type Your URL Address Here:")
        self.setObjectName("flbl")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.flbl.setFont(font)

        ## First tbx ##
        self.ftbx = QtWidgets.QLineEdit()
        self.ftbx.setObjectName("ftbx")
        self.ftbx.setPlaceholderText("Your URL Address Here")
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.ftbx.setFont(font)

        ## Second Label ##
        self.slbl = QtWidgets.QLabel()
        self.slbl.setText("Enter The Title Of Your URL Here:")
        self.setObjectName("slbl")
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.slbl.setFont(font)

        ## Second Tbx ##
        self.stbx = QtWidgets.QLineEdit()
        self.stbx.setObjectName("stbx")
        self.stbx.setPlaceholderText("The Title Of Your URL Here")
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.stbx.setFont(font)

        ## The Submit Button ##
        self.Sbtn = QtWidgets.QPushButton()
        self.Sbtn.setObjectName("Sbtn")
        self.Sbtn.setText("Submit Info")
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.Sbtn.setFont(font)

        ## Btn Connect ##
        self.Sbtn.clicked.connect(self.sinfo)

        layout.addWidget(self.flbl)
        layout.addWidget(self.ftbx)
        layout.addWidget(self.slbl)
        layout.addWidget(self.stbx)
        layout.addWidget(self.Sbtn)
        self.setLayout(layout)

        speak("Adding Your Attribute")
    def sinfo(self):
        try:
            URL = self.ftbx.text()
            URLName = self.stbx.text()
            finalTag = (f'<a href="{URL}">{URLName}</a>')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Attribute or URL Added!")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

## Add Address Command ##
class AddAddress(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddAddress, self).__init__(*args, **kwargs)

        ## Main Window ##
        self.setFixedSize(600, 150)
        self.setWindowTitle("You Said 'Add Address'")

        ## Page layout ##
        layout = QVBoxLayout()



        ## page Labels , Tbxs and btns ##

        ## The Label ##
        self.frstlb = QtWidgets.QLabel()
        self.frstlb.setText("Please Type Your Address Here:")
        self.setObjectName("frstlb")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.frstlb.setFont(font)

        ## Tbx ##
        self.frsttbx = QtWidgets.QLineEdit()
        self.frsttbx.setObjectName("frsttbx")
        self.frsttbx.setPlaceholderText("Your Address Here")
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.frsttbx.setFont(font)

        ## Btn ##
        self.SPBTN = QtWidgets.QPushButton()
        self.SPBTN.setObjectName("SPBTN")
        self.SPBTN.setText("Submit Info")
        font.setBold(True)
        font.setPointSize(12)
        font.setFamily("Word Black")
        font.setWeight(10)
        self.SPBTN.setFont(font)

        ## Btn Connect ##
        self.SPBTN.clicked.connect(self.spbtn)

        layout.addWidget(self.frstlb)
        layout.addWidget(self.frsttbx)
        layout.addWidget(self.SPBTN)
        self.setLayout(layout)
        

        speak("Adding Your Address, Tell Me Your Address")
    
    def spbtn(self):
        try:
            address = self.frsttbx.text()
            finalTag = (f"<address>{address}</address>")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            speak("Address Added!")
        except:
            speak("Oops!, something went wrong, try again, or contact support.")
            QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")



##### User Information Database #####
conn2 = sqlite3.connect('usin.db')
c2 = conn2.cursor()
c2.execute('''CREATE TABLE IF NOT EXISTS level(level text)''')
conn2.commit()
### Status Of Pages (The Starter Or Other Pages)
status_pages = False

### Restircting To Only Run In Windows ###
if platform.system() == "Windows":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    userSaid = "hello world"

else:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 160)
    userSaid = "hello world"


### Wishing Function ###
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        

    else:
        speak("Good Evening")



def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except:
        QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")
        endl()


## Listening Function ##
def take_command(wtr=0):
    r = sp.Recognizer()
    r.pause_threshold = 1
    r.operation_timeout = 5
    with sp.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source, phrase_time_limit=5)

        try:
            speak("Recognizing...")
            heard = r.recognize_google(audio)
            return heard.lower()

        except sp.UnknownValueError:
            speak("I Didn't Understood What You Said...")
            QMessageBox.warning(QMessageBox(), "Error", "You said something that is beyond my understanding or maybe you didn't say anything.")
        engine.runAndWait()
        return 0



## Instruction Function ##
def instructions():
    speak("Hello There, Welcome.")



## ScilenceChecker Function Takes input and removes scilence ##
def scilenceChecker():
    userSaid = take_command().lower()
    if userSaid == "":
        userSaid = "nothing"
    elif userSaid == " ":
        userSaid = "nothing"
    else:
        userSaid = take_command().lower()


def clear_log():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("Clear")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
###########################################################################################
#                                                                                         #
#        |          ||          _________                       _____      ___________    #
#        |         |  |        |         |   \              /     |       |               #
#        |        |    |       |         |    \            /      |       |               #
#        |       |      |      |_________|     \          /       |       |               #
#        |      |        |     |\               \        /        |       |___________    #
#        |     |__________|    | \               \      /         |                   |   #
# |      |    |            |   |  \               \    /          |                   |   #
# |      |   |              |  |   \               \  /           |                   |   #
# |______|  |                | |    \               \/          __|__     ____________|   #
#                                                                                         #
###########################################################################################
###########################
# AI COMPANION UI Edition #
###########################