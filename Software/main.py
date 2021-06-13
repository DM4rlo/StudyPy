import sys 
import os
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
'''Author Dharmarlou Bowen'''

# Track if Guest or User is in use
x = 0  

# Contains QSS for button hovering adaptation
qss = ("QPushButton:!pressed {color : #FF6600;}"
       "QPushButton:!pressed {background-color : #003366;}"
       "QPushButton:!pressed {border-top-left-radius :20px;}"
       "QPushButton:!pressed {border-top-right-radius : 20px;}" 
       "QPushButton:!pressed {border-bottom-left-radius : 20px;}" 
       "QPushButton:!pressed {border-bottom-right-radius : 20px;}"
       "QPushButton:hover {background-color : #FF6600;}"
       "QPushButton:hover {color : #003366;}")

# StartPage Window - Done
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('startpage.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnStart.clicked.connect(self.contin)
        self.UiComponents()
        
    def UiComponents(self):
        self.btnStart.setStyleSheet(qss)
        
    def contin(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    
# Introduction Page - Done
class Intro_Page(QDialog):
    def __init__(self):
        super(Intro_Page, self).__init__()
        loadUi('intro.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnContin.clicked.connect(self.continu)
        self.UiComponents()

    def UiComponents(self):
        self.btnContin.setStyleSheet(qss)
    
    def continu(self):
       widget.setCurrentIndex(widget.currentIndex()+1) 

# User Option Menu Page - Done
class UserOp(QDialog):
    def __init__(self):
        super(UserOp, self).__init__()
        loadUi('useropt.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnGuest.clicked.connect(self.guestdemo)
        self.btnSignin.clicked.connect(self.signin)
        self.btnSignup.clicked.connect(self.signup)
        self.UiComponents()
        
        
    def UiComponents(self):
        self.btnGuest.setStyleSheet(qss)
        self.btnSignin.setStyleSheet(qss)
        self.btnSignup.setStyleSheet(qss)

    def guestdemo(self):
        global x
        x = 0
        widget.setCurrentIndex(3)
        
    def signin(self):
        widget.setCurrentIndex(4)
        
    def signup(self):
        widget.setCurrentIndex(6)


# Sign in Page - Done
class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi('login.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnLogin.clicked.connect(self.login)
        self.btnFgt.clicked.connect(self.fgtdt)
        self.btnR.clicked.connect(self.rtn)
        self.txtpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.UiComponents()

    def UiComponents(self):
        self.btnLogin.setStyleSheet(qss)
        self.btnFgt.setStyleSheet(qss)
        self.btnR.setStyleSheet(qss)
        
    def login(self):
        if self.txtusr.text() == "":
            self.txtusr.setText("Must input a username!")
        else:
            global x, cusr
            x += 1
            cusr = self.txtusr.text()
            path = 'usr_accs/'+self.txtusr.text()+".txt"
            isfile = os.path.isfile(path)
            
            
            if isfile == True:
                lines = []
                with open(path , 'r') as f:
                    lines = f.readlines()
                
                pwd = lines[1]
                
                if pwd == self.txtpwd.text():
                    widget.setCurrentIndex(3)
                else:
                    self.txtusr.setText("Please check your inputs are accurate!")
            else:
                self.txtusr.setText("User could not be found!")
        
    
    def fgtdt(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def rtn(self):
        widget.setCurrentIndex(2)
        

# Forgotten Details Page - Done
class FgtDetails(QDialog):
    def __init__(self):
        super(FgtDetails, self).__init__()
        loadUi('forgotDt.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnReturn.clicked.connect(self.rtn)
        self.UiComponents()
        
    def UiComponents(self):
        self.btnReturn.setStyleSheet(qss)
        
    def rtn(self):
        widget.setCurrentIndex(2)

# Create Account Page - Here
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi('createacc.ui', self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnSignup.clicked.connect(self.sgup)
        self.btnR.clicked.connect(self.rtn)
        self.txtpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtRpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.UiComponents()    

    def UiComponents(self):
        self.btnSignup.setStyleSheet(qss)
        self.btnR.setStyleSheet(qss)
    
    def sgup(self):
        # Line Edit Inputs
        usr  = self.txtUn.text()
        pwd  = self.txtpwd.text()
        pwdR = self.txtRpwd.text()
        
        # If usr txt field empty
        if usr == "":
            self.txtusr.setText("Must input a username!")
        # checks if username already exists
        else:
            path = 'usr_accs/'+self.txtUn.text()+".txt"
            isfile = os.path.isfile(path)
    
            if isfile == False:
                if pwd == pwdR:
        
                    # create user file
                    file  = open(path,"w") 
                    file.write(usr+"\n")
                    file.write(pwd)
                    file.close()
                    
                    # create user stats file
                    file  = open("usr_sts/"+self.txtUn.text()+".txt","w") 
                    for i in range(14):
                        file.write('0%\n')
                    file.close()
                    
                    # Clear all text boxes
                    self.txtUn.setText("")
                    self.txtpwd.setText("")
                    self.txtRpwd.setText("")
                    
                    # resets pwd mismatch lbl
                    self.lblpwd.setStyleSheet("color: rgb(170, 0, 0, 0%);")
                    
                    # Take user to account verification
                    widget.setCurrentIndex(widget.currentIndex()+1)
                else:
                    # pwd dont match
                    pwd.setText() 
                    pwdR.setText()
                    # mks error msg visible
                    self.lblpwd.setStyleSheet("color: rgb(170, 0, 0, 100%);")
            else:
                self.txtUn.setText("Username already exists!")
        
    # takes users back to main menu
    def rtn(self):
        widget.setCurrentIndex(2)
    
# Create Account Verification Page - Done
class CrtAccV(QDialog):
    def __init__(self):
        super(CrtAccV, self).__init__()
        loadUi('crtaccVerf.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnR.clicked.connect(self.rtn)
        self.UiComponents()

    def UiComponents(self):
        self.btnR.setStyleSheet(qss)

    # takes users back to main menu
    def rtn(self):
        widget.setCurrentIndex(2)


# Main Menu Window Page    
class MMenu(QDialog):
    def __init__(self):
        super(MMenu, self).__init__()
        loadUi('mainMenu.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnAlgo.clicked.connect(self.algo)
        self.btnNetF.clicked.connect(self.netf)
        self.btnStats.clicked.connect(self.mstats)
        self.btnRtn.clicked.connect(self.rtn)
        global crtQ, cq 
        crtQ = 0 ; cq = 0
        self.UiComponents() 
        
        
    def UiComponents(self):
        self.btnRtn.setStyleSheet(qss)
        self.btnAlgo.setStyleSheet(qss)
        self.btnNetF.setStyleSheet(qss)
        self.btnStats.setStyleSheet(qss)
        
    def algo(self):
        widget.setCurrentIndex(8)
        
    def netf(self):
        widget.setCurrentIndex(9)
    
    def mstats(self):
        if x == 0:
            # go to gstats
            widget.setCurrentIndex(10)
        else:
            # go to ustats
            widget.setCurrentIndex(11)
        
    def rtn(self):
        widget.setCurrentIndex(2)
        
        
# Guest Stats - Done
class Gstats(QDialog):
    def __init__(self):
        super(Gstats, self).__init__()
        loadUi('guestStats.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnReturn.clicked.connect(self.bmenu)
        self.UiComponents()

    def UiComponents(self):
        self.btnReturn.setStyleSheet(qss)
        
    def bmenu(self):
        # Return to main menu
        widget.setCurrentIndex(3)
    
        

# User Stats - Done
class Ustats(QDialog):
    def __init__(self):
        super(Ustats, self).__init__()
        loadUi('userStats.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnReturn.clicked.connect(self.bmenu)
        self.btnLoad.clicked.connect(self.ld)
        self.UiComponents()
        
              
            
            
        
        
    def UiComponents(self):
        self.btnReturn.setStyleSheet(qss)
        self.btnLoad.setStyleSheet(qss)
                
    def ld(self):
        path = 'usr_sts/'+cusr+'.txt'
        with open(path , 'r') as f:
            lines = f.readlines()
    
        # DSA
        self.lblDtypes.setText(lines[0])
        self.lblMM.setText(lines[1])
        self.lblTG.setText(lines[2])
        self.lblRC.setText(lines[3])
        self.lblAlgoP.setText(lines[4])
        self.lblSrcAlgo.setText(lines[5])
        self.lblSrtAlgo.setText(lines[6])
        self.lblEC.setText(lines[7])
        # NetF
        self.lblNC.setText(lines[8])
        self.lblPM.setText(lines[9])
        self.lblOsi.setText(lines[10])
        self.lblSF.setText(lines[11])
        
        
         
    def bmenu(self):
        # Return to main menu
        widget.setCurrentIndex(3)
        

####################################################################


# DSA Menu Page - Done
class DSA_M(QDialog):
    def __init__(self):
        super(DSA_M, self).__init__()
        loadUi('dsaMenu.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnRtn.clicked.connect(self.bmenu)
        self.btnds.clicked.connect(self.dsw)
        self.btnalgo.clicked.connect(self.algow)
        self.UiComponents()
        
    def UiComponents(self):
        self.btnRtn.setStyleSheet(qss)
        self.btnds.setStyleSheet(qss)
        self.btnalgo.setStyleSheet(qss)
        
    def dsw(self):
        global c ; c = "ds"
        widget.setCurrentIndex(12)
    
    def algow(self):
        global c ; c = "algo"
        widget.setCurrentIndex(13)
    
    def bmenu(self):
        # Return to main menu
        widget.setCurrentIndex(3)



# DS Sub Menu Page 
class DS_M(QDialog):
    def __init__(self):
        super(DS_M, self).__init__()
        loadUi('dsMenu.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnRtn.clicked.connect(self.bmenu)
        self.btndt.clicked.connect(self.Qzdt)
        self.btnmm.clicked.connect(self.Qzmm)
        self.btntg.clicked.connect(self.Qztg)
        self.btnrec.clicked.connect(self.Qzrec)
        self.UiComponents()
        
    def UiComponents(self):
        self.btnRtn.setStyleSheet(qss)
        self.btndt.setStyleSheet(qss)
        self.btnmm.setStyleSheet(qss)
        self.btntg.setStyleSheet(qss)
        self.btnrec.setStyleSheet(qss)
        
        
    def Qzdt(self):
        # take to quiz intro
        global QC, SC 
        QC = "DS" ; SC = "DT"
        widget.setCurrentIndex(14)
    
    def Qzmm(self):
        global QC, SC
        QC = "DS" ; SC = "MM" 
        widget.setCurrentIndex(14)
    
    def Qztg(self):
        global QC, SC 
        QC = "DS" ; SC = "TG" 
        widget.setCurrentIndex(14)
    
    def Qzrec(self):
        global QC, SC 
        QC = "DS" ; SC = "REC"
        widget.setCurrentIndex(14)
    
    def bmenu(self):
        # Return to main menu
        widget.setCurrentIndex(3)



# Algorithm Menu Page
class Algo_M(QDialog):
    def __init__(self):
        super(Algo_M, self).__init__()
        loadUi('algoMenu.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnRtn.clicked.connect(self.bmenu)
        self.btnalp.clicked.connect(self.QzAlgoP)
        self.btnSrc.clicked.connect(self.QzSrc)
        self.btnSrt.clicked.connect(self.QzSrt)
        self.btnEF.clicked.connect(self.QzEF)
        self.UiComponents()
        

    def UiComponents(self):
        self.btnRtn.setStyleSheet(qss)
        self.btnalp.setStyleSheet(qss)
        self.btnSrc.setStyleSheet(qss)
        self.btnSrt.setStyleSheet(qss)
        self.btnEF.setStyleSheet(qss)
        
    # Take to quiz funcs
    def QzAlgoP(self):
        global QC, SC 
        QC = "Algo" ; SC = "AP"
        widget.setCurrentIndex(14)
        
    def QzSrc(self):
        global QC, SC 
        QC = "Algo" ; SC = "SrA"
        widget.setCurrentIndex(14)
    
    def QzSrt(self):
        global QC, SC 
        QC = "Algo" ; SC = "StA"
        widget.setCurrentIndex(14)
    
    def QzEF(self):
        global QC, SC 
        QC = "Algo" ; SC = "EF"
        widget.setCurrentIndex(14)
    
    
    def bmenu(self):
        # Return to main menu
        widget.setCurrentIndex(3)







##############################################################################




# Network Fundamentals Menu Page
class NetF_M(QDialog):
    def __init__(self):
        super(NetF_M, self).__init__()
        loadUi('netFMenu.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnRtn.clicked.connect(self.bmenu)
        self.btnnc.clicked.connect(self.Qznc)
        self.btnpm.clicked.connect(self.Qzpm)
        self.btnosi.clicked.connect(self.Qzosi)
        self.btnsf.clicked.connect(self.Qzsf)
        self.UiComponents()
        global c ; c = "net"
        

    def UiComponents(self):
        self.btnRtn.setStyleSheet(qss) 
        self.btnnc.setStyleSheet(qss)
        self.btnpm.setStyleSheet(qss)
        self.btnosi.setStyleSheet(qss)
        self.btnsf.setStyleSheet(qss)
    
    def Qznc(self):
        global QC, SC 
        QC = "NetF" ; SC = "NC"
        widget.setCurrentIndex(14)
    
    def Qzpm(self):
        global QC, SC 
        QC = "NetF" ; SC = "PM"
        widget.setCurrentIndex(14)
    
    def Qzosi(self):
        global QC, SC 
        QC = "NetF" ; SC = "OSI"
        widget.setCurrentIndex(14)
    
    def Qzsf(self):
        global QC, SC 
        QC = "NetF" ; SC = "SF"
        widget.setCurrentIndex(14)
    
    def bmenu(self):
        # Return to main menu
        widget.setCurrentIndex(3)
 
#################################################################################################################
# Quiz Pages
     
class QPage(QDialog):
    def __init__(self):
        super(QPage, self).__init__()
        loadUi('QuizPage.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnRtn.clicked.connect(self.bmenu)
        self.btnNQ.clicked.connect(self.nxtQ)
        self.btnPQ.clicked.connect(self.prvQ)
        self.UiComponents()
        
        
        global crtQ, SC, total, zx
        if crtQ == 0:
            self.btnPQ.setEnabled(False)
            self.btnNQ.setText("Load Questions")
        if crtQ == 1:
            self.btnPQ.setEnabled(False)
            self.btnNQ.setText("Next Question")
        
        total = 0
        zx = -1
    
    def nxtQ(self):
        
        global crtQ, total, buffer, zx
        crtQ += 1
        zx += 1
        buffer = 0
        # Enables the Previous Question Button
        if crtQ == 2:
            self.btnPQ.setEnabled(True)
        
        
        if crtQ == 6:
            self.btnNQ.setText("Finish Quiz")
        else:
            if crtQ < 6 and crtQ > 0:
                self.btnNQ.setText("Next Question")
            else:
                self.btnNQ.setText("Load Questions")
       
        if zx == 0:
            pass
        else:
            if zx == 7:
                pass
            else:
                ph = 'Quiz_Pages/'+QC+'/Questions'+SC+'/ans'+str(zx)+'.txt'
                with open(ph , 'r') as f:
                    lines = f.readlines()
            
                a1, a2 = lines[0], lines[1]
        
                # Check if any of the inputs were correct and then reset them
                if self.cb1.isChecked():
                    if self.cb1.text() == a1:
                        buffer += 1
                    if self.cb1.text() == a2:
                        buffer += 1
                            
                if self.cb2.isChecked():
                    if self.cb2.text() == a1:
                        buffer += 1
                    if self.cb2.text() == a2:
                        buffer += 1  
                
                if self.cb3.isChecked():
                    if self.cb3.text() == a1:
                        buffer += 1
                    if self.cb3.text() == a2:
                        buffer += 1
                
                if self.cb4.isChecked():
                    if self.cb4.text() == a1:
                        buffer += 1
                    if self.cb4.text() == a2:
                        buffer += 1
                        
                if self.cb5.isChecked():
                    if self.cb5.text() == a1:
                        buffer += 1
                    if self.cb5.text() == a2:
                        buffer += 1
                        
                
                if self.cb6.isChecked():
                    if self.cb6.text() == a1:
                        buffer += 1
                    if self.cb6.text() == a2:
                        buffer += 1
                        
                
                # Keeps track or right and wrong answers to questions
                if buffer == 0:
                    file  = open("QPerformance.txt","a") 
                    file.write("You got Question "+str(zx)+" wrong!\n")
                    file.close()
                
                if buffer == 1:
                    file  = open("QPerformance.txt","a") 
                    file.write("You got Question "+str(zx)+" half correct!\n")
                    file.close()
                
                if buffer == 2:
                    file  = open("QPerformance.txt","a") 
                    file.write("You got Question "+str(zx)+" completely correct!\n")
                    file.close()

                total += buffer
                buffer = 0
            
        if crtQ == 7:
            # goes to Quiz completion page
            crtQ = 0
            buffer = 0 
            zx = -1
            self.btnPQ.setEnabled(False)
            self.txtQs.setText("")
            self.btnNQ.setText("Load Questions") 
            self.cb1.setChecked(False)
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)
            self.cb5.setChecked(False)
            self.cb6.setChecked(False)
        
            self.cb1.setText("")
            self.cb2.setText("")
            self.cb3.setText("")
            self.cb4.setText("")
            self.cb5.setText("")
            self.cb6.setText("")
            widget.setCurrentIndex(15)
        else:
            # Clears checkboxes for next question
            self.cb1.setChecked(False)
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)
            self.cb5.setChecked(False)
            self.cb6.setChecked(False)
            
            # Sets Quiz Question
            path = "Quiz_Pages/"+QC+"/Questions"+SC+"/Q"+str(crtQ)+".txt"
            with open(path , 'r') as f:
                lines = f.readlines()    
                self.txtQs.setText(lines[0])
                self.txtQs.setStyleSheet("background-color: rgb(237, 237, 237); font: 18pt;")
                
            # Sets Checkboxes
            path = "Quiz_Pages/"+QC+"/Questions"+SC+"/Q"+str(crtQ)+"_cbs.txt"
            with open(path , 'r') as f:
                lines = f.readlines()
                    
            self.cb1.setText(lines[0])
            self.cb1.setStyleSheet("background-color: transparent; font: 16pt;")
            
            self.cb2.setText(lines[1])
            self.cb2.setStyleSheet("background-color: transparent; font: 16pt;")
            
            self.cb3.setText(lines[2])
            self.cb3.setStyleSheet("background-color: transparent; font: 16pt;")
            
            self.cb4.setText(lines[3])
            self.cb4.setStyleSheet("background-color: transparent; font: 16pt;")
            
            self.cb5.setText(lines[4])
            self.cb5.setStyleSheet("background-color: transparent; font: 16pt;")
            
            self.cb6.setText(lines[5])
            self.cb6.setStyleSheet("background-color: transparent; font: 16pt;")             
            
        
        
    
    def prvQ(self):
        global crtQ, total, buffer, zx 
        crtQ -= 1
        zx -= 1
        total -= buffer
        
        with open("QPerformance.txt" , 'r') as f:
            lines = f.readlines() 

        lines.pop() # removes last amendment
        
        file  = open("QPerformance.txt","w") 
        for i in lines:    
            file.write(i)
        file.close()
        
        
        if crtQ < 2:
            self.btnPQ.setEnabled(False)
        if crtQ >= 1:
            
            # Sets Quiz Question
            path = "Quiz_Pages/"+QC+"/Questions"+SC+"/Q"+str(crtQ)+".txt"
            with open(path , 'r') as f:
                lines = f.readlines()    
                self.txtQs.setText(lines[0])
                self.txtQs.setStyleSheet("background-color: rgb(237, 237, 237); font: 18pt;")
                
                # Sets Checkboxes
                path = "Quiz_Pages/"+QC+"/Questions"+SC+"/Q"+str(crtQ)+"_cbs.txt"
                with open(path , 'r') as f:
                    lines = f.readlines()
                    
                    self.cb1.setText(lines[0])
                    self.cb1.setStyleSheet("background-color: transparent; font: 16pt;")
                    
                    self.cb2.setText(lines[1])
                    self.cb2.setStyleSheet("background-color: transparent; font: 16pt;")
                    
                    self.cb3.setText(lines[2])
                    self.cb3.setStyleSheet("background-color: transparent; font: 16pt;")
                    
                    self.cb4.setText(lines[3])
                    self.cb4.setStyleSheet("background-color: transparent; font: 16pt;")
                    
                    self.cb5.setText(lines[4])
                    self.cb5.setStyleSheet("background-color: transparent; font: 16pt;")
                    
                    self.cb6.setText(lines[5])
                    self.cb6.setStyleSheet("background-color: transparent; font: 16pt;")
        
        
    def UiComponents(self):
        self.btnRtn.setStyleSheet(qss)
        self.btnNQ.setStyleSheet(qss)
        self.btnPQ.setStyleSheet(qss)
        
    def bmenu(self):
        global crtQ
        crtQ = 0
        self.txtQs.setText("")
        self.btnNQ.setText("Load Questions") 
        self.cb1.setChecked(False)
        self.cb2.setChecked(False)
        self.cb3.setChecked(False)
        self.cb4.setChecked(False)
        self.cb5.setChecked(False)
        self.cb6.setChecked(False)
        
        self.cb1.setText("")
        self.cb2.setText("")
        self.cb3.setText("")
        self.cb4.setText("")
        self.cb5.setText("")
        self.cb6.setText("")
        
        if c == "ds":
            widget.setCurrentIndex(12)
            
        elif c == "algo":
            widget.setCurrentIndex(13)
           
        elif c == "net":
            widget.setCurrentIndex(9)
 
 
    
 
class FshQ(QDialog):
    def __init__(self):
        super(FshQ, self).__init__()
        loadUi('QuizFinish.ui',self)
        lbl = self.lbl_logo
        lbl.setStyleSheet("border-image: url(logo.png)")
        self.btnR.clicked.connect(self.bmenu)
        self.btnScr.clicked.connect(self.score)
        self.UiComponents()    
        
        
    def UiComponents(self):
        self.btnR.setStyleSheet(qss)
        self.btnScr.setStyleSheet(qss)
        
        
    def score(self):
    
        # Prints Questions User got wrong to screen
        with open("QPerformance.txt" , 'r') as f:
            lines = f.readlines()  
        # Display Question Performance
        self.lbl1.setText(lines[0])
        self.lbl2.setText(lines[1])
        self.lbl3.setText(lines[2])
        self.lbl4.setText(lines[3])
        self.lbl5.setText(lines[4])
        self.lbl6.setText(lines[5])
        
        # shows score
        global total
        total = (total / 12)*100
        
        # Add Stats for users only
        if x == 1:
            tt = (f'{total:.0f}'+"%"+" was score from last attempt.\n")
            path = 'usr_sts/'+cusr+'.txt'
            with open(path , 'r') as f:
                lines = f.readlines()
            # Data Structures
            if SC == "DT":
                lines[0] = tt
            if SC == "MM":
                lines[1] = tt
            if SC == "TG":
                lines[2] = tt
            if SC == "REC":
                lines[3] = tt
            
            # Algorithms
            if SC == "AP":
                lines[4] = tt
            if SC == "SrA":
                lines[5] = tt
            if SC == "StA":
                lines[6] = tt
            if SC == "EF":
                lines[7] = tt
            
            # Network Fundamentals
            if SC == "NC":
                lines[8] = tt
            if SC == "PM":
                lines[9] = tt
            if SC == "OSI":
                lines[10] = tt
            if SC == "SF":
                lines[11] = tt
            
                
            file  = open(path,"w") 
            for i in lines:
                file.write(i)
            file.close()
            
            
        

        self.lblScr.setText(f'{total:.0f}'+"%")
        
        
        self.btnScr.setEnabled(False)
        
        file  = open("QPerformance.txt","w") 
        file.write("")
        file.close()
        
    
    def bmenu(self):
    
        file  = open("QPerformance.txt","w") 
        file.write("")
        file.close()
        
        self.btnScr.setEnabled(True)
        
        self.lblScr.setText("???")
        self.lbl1.setText("???")
        self.lbl2.setText("???")
        self.lbl3.setText("???")
        self.lbl4.setText("???")
        self.lbl5.setText("???")
        self.lbl6.setText("???")
        
        # Resets Quiz variables
        global cq, crtQ, total, c
        cq = 0 ; crtQ = 0 ; total = 0 
        
        if c == "ds":
            widget.setCurrentIndex(12)
            
        elif c == "algo":
            widget.setCurrentIndex(13)
           
        elif c == "net":
            widget.setCurrentIndex(9)
 
    
    
    
app = QApplication(sys.argv)

# Stack Initialisation
widget = QtWidgets.QStackedWidget()

# Page
mainwindow = MainWindow()
itrp       = Intro_Page()
usrop      = UserOp()
mm         = MMenu()
sn         = SignIn()
fgt        = FgtDetails()
crtacc     = CreateAcc()
cv         = CrtAccV()

# Main Menu Initialisations
dsa        = DSA_M()   
nf         = NetF_M()  
gs         = Gstats()
us         = Ustats()

# DSA Menu
ds = DS_M()
al = Algo_M()

# Quiz Pages
qp = QPage()
fq = FshQ()

   
# Pages added to stack 
widget.addWidget(mainwindow) # 0
widget.addWidget(itrp)       # 1
widget.addWidget(usrop)      # 2

# Main Menu Page
widget.addWidget(mm)         # 3

# Sign In Pages
widget.addWidget(sn)         # 4
widget.addWidget(fgt)        # 5

# Create Account Pages
widget.addWidget(crtacc)     # 6
widget.addWidget(cv)         # 7

# Main Menu Pages
widget.addWidget(dsa)        # 8 
widget.addWidget(nf)         # 9
widget.addWidget(gs)         # 10
widget.addWidget(us)         # 11

# DSA Menu Pages
widget.addWidget(ds)         # 12
widget.addWidget(al)         # 13

# Quiz Pages
widget.addWidget(qp)         # 14
widget.addWidget(fq)         # 15
widget.show()
app.exec()   