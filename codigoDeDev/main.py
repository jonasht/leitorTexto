from PyQt6.QtGui import QKeyEvent, QFont
from PyQt6.QtWidgets import (QApplication, QWidget, 
                             QHBoxLayout, QVBoxLayout, QGridLayout, QFrame,
                             QTextEdit, QPushButton, QLabel, QLineEdit, QComboBox, QProgressBar)

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl, Qt, QThread, pyqtSignal
import time
from gtts import gTTS
import sys
import func
from qt_material import apply_stylesheet
import funcDefaultUtil as funcUtil
from datetime import datetime



class W_main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.gen_audio = None
        self.fileName = ''
        self.var_langText = 'Português (Brasil)'


        lay_main = QVBoxLayout()
        lay_fr = QVBoxLayout()
        fr = QFrame()

        fr.setLayout(lay_fr)
        self.layout_top = QHBoxLayout() # in: layout_topLeft e LayoutRight
        # combox idioma ======================================
        self.layout_topLeft = QHBoxLayout()
        self.lb_idioma = QLabel('Idioma:')
        self.cob_lang = QComboBox()

        self.cob_lang.addItems(func.get_audioLangs_keys())
        self.cob_lang.setCurrentIndex(0)
        
        self.layout_topLeft.addWidget(self.lb_idioma)
        self.layout_topLeft.addWidget(self.cob_lang)
        self.layout_top.addLayout(self.layout_topLeft)
        self.layout_topLeft.addStretch()
        self.cob_lang.currentIndexChanged.connect(self.event_changeTextLang)
        

        
        
        # parte de texto em cima ==========================================
        self.lb_titulo = QLabel('Texto:')
        self.te_text = QTextEdit()
        

        lay_fr.addLayout(self.layout_top)
        lay_fr.addWidget(self.lb_titulo)
        lay_fr.addWidget(self.te_text)
        
        # botoes gerar audio, play =================================
        self.lay_bts = QHBoxLayout()
        self.bt_gerarAudio = QPushButton('Gerar Audio')
        self.bt_play = QPushButton('Play')
        self.lay_bts.addWidget(self.bt_play)
        self.lay_bts.addWidget(self.bt_gerarAudio)
        lay_fr.addLayout(self.lay_bts)
        
        # botao APAGAR TUDO ============================
        self.bt_dellAll = QPushButton('Apagar Tudo')
        
        lay_fr.addWidget(self.bt_dellAll)
        
        # salvar como
        self.layout_save = QHBoxLayout()
        self.lb_save = QLabel('salvar como:')
        self.le_save = QLineEdit()
        self.layout_save.addWidget(self.lb_save)
        self.layout_save.addWidget(self.le_save)
        lay_fr.addLayout(self.layout_save)

        
        lay_main.addWidget(fr)
        self.setLayout(lay_main)
        
        # player ================================================
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # event buttons ===========================================
        self.bt_gerarAudio.clicked.connect(self.event_btGerarAudio)
        self.bt_play.clicked.connect(self.event_btPlayAudio)
        self.bt_dellAll.clicked.connect(self.event_btDelAll)

        self.set_styleUI()
        self.set_default()
        
    def get_fileName(self):
        
        var_le_save = self.le_save.text()
        if var_le_save:
            fileName = var_le_save
        else:
            agora = datetime.now()

            data = agora.strftime("%d%m%Y")
            hora = agora.strftime("%H%M%S")
            lang = func.get_audioLangs()[self.var_langText]
        
            fileName = 'l'+lang.title()+'_D'+data+'H'+hora
            
        fileName = fileName + '.mp3'
        
        return fileName
        
        
        
    def set_default(self):
        # texto = funcUtil.TEXTO
        # self.te_text.setText(texto)
        self.le_save.setPlaceholderText('Lang_Data_Hara')
        
        self.bt_play.setEnabled(False)


    def event_changeTextLang(self):
        text = self.cob_lang.currentText()
        print(f'lingua de texto:{text}')

        self.var_langText = text
        

    def set_styleUI(self):
        # font ==========================
        fontsize14 = 'font-size: 14pt;'
        fontsize16 = 'font-size: 16pt;'
        fontsize20 = 'font-size: 20pt;'
        fontweight = 'font-weight: bold;'
        
        self.lb_titulo.setStyleSheet('font-size: 14pt;')
        self.cob_lang.setStyleSheet(fontsize14+fontweight)
        self.te_text.setStyleSheet(fontsize14)
        
        # ===========================================
        CENTER = Qt.AlignmentFlag.AlignCenter
        RIGHT = Qt.AlignmentFlag.AlignRight
        LEFT = Qt.AlignmentFlag.AlignLeft
        VCENTER = Qt.AlignmentFlag.AlignVCenter
        RIGHTVCENTER = RIGHT|VCENTER
        LEFTTVCENTER = LEFT|VCENTER

        self.lb_titulo.setAlignment(LEFT)
        self.lb_idioma.setAlignment(LEFTTVCENTER)
        self.cob_lang.setFixedWidth(320)




    def keyPressEvent(self, a0) -> None:
        if a0.key() == Qt.Key.Key_Escape: #type:ignore
            self.close()

    def event_btDelAll(self):
        self.te_text.setText('')
        
    def event_btGerarAudio(self):
        text = self.te_text.toPlainText()
        self.fileName = self.get_fileName()
        lang = func.get_audioLangs()[self.var_langText]
        func.read_audio(text, lang, self.fileName)
        
        # ativa botao play
        self.bt_play.setEnabled(True)

    
    def event_btPlayAudio(self):
        self.player.setSource(QUrl.fromLocalFile('./'+ self.fileName))
        self.audio_output.setVolume(1.0)
        self.player.play()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_main()

    apply_stylesheet(app, theme='dark_lightgreen.xml')
    
    window.setWindowTitle('LeitorDeTexto')
    window.setGeometry(800, 800, 1500, 1000)
    window.show()

    sys.exit(app.exec())
    