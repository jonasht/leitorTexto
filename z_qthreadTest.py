from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QWidget, 
    QTextEdit, QProgressBar, QLabel, QHBoxLayout
)
from PyQt6.QtGui import QFont
from gtts import gTTS
import os
import time
import qt_material as qtm
import funcDefaultUtil as funcUtil

class TextToSpeechWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    status = pyqtSignal(str)
    
    def __init__(self, text, language='pt'):
        super().__init__()
        self.text = text
        self.language = language
    
    def run(self):
        try:
            # Simular preparação (10%)
            self.status.emit('Preparando texto...')
            self.progress.emit(10)
            time.sleep(0.5)
            
            # Conectar ao Google (30%)
            self.status.emit('Conectando ao Google...')
            self.progress.emit(30)
            time.sleep(0.5)
            
            # Gerar áudio (70%)
            self.status.emit('Gerando áudio...')
            self.progress.emit(70)
            tts = gTTS(text=self.text, lang=self.language, slow=False)
            
            # Salvar arquivo (95%)
            self.status.emit('Salvando arquivo...')
            self.progress.emit(95)
            tts.save('output.mp3')
            
            # Finalizado (100%)
            self.status.emit('Concluído!')
            self.progress.emit(100)
            time.sleep(0.5)
            
            self.finished.emit()
            
        except Exception as e:
            self.error.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('gTTS com QThread e Progresso')
        self.setGeometry(100, 100, 500, 450)
        self.worker = None
        
        # Widget central
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        # Título
        self.lb_title = QLabel('Conversor Texto para Fala')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        self.lb_title.setFont(title_font)
        layout.addWidget(self.lb_title)
        
        # Text edit para input
        self.te_text = QTextEdit()
        self.te_text.setPlaceholderText('Digite o texto para converter em fala...')
        self.te_text.setMinimumHeight(150)
        layout.addWidget(self.te_text)
        
        # Label de status
        self.lb_status = QLabel('Pronto para converter')
        self.lb_status.setStyleSheet('color: #666; font-style: italic;')
        layout.addWidget(self.lb_status)
        
        # Barra de progresso
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat('%p%')
        layout.addWidget(self.progress_bar)
        
        # Layout de botões
        button_layout = QHBoxLayout()
        
        # Botão para iniciar
        self.button = QPushButton('Gerar Áudio')
        self.button.clicked.connect(self.start_tts)
        self.button.setMinimumHeight(40)
        button_layout.addWidget(self.button)
        
        
        layout.addLayout(button_layout)
        
        # Label informativo
        self.lb_info = QLabel('💡 O arquivo será salvo como "output.mp3"')
        self.lb_info.setStyleSheet('color: #999; font-size: 10px; margin-top: 10px;')
        layout.addWidget(self.lb_info)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # set texto default em te_text
        self.te_text.setText(funcUtil.TEXTO)
    
    def start_tts(self):
        text = self.te_text.toPlainText().strip()
        
        if not text:
            self.lb_status.setText('⚠️ Digite um texto primeiro!')
            self.lb_status.setStyleSheet('color: #d9534f;')
            return
        
        # Desabilitar interações
        self.button.setEnabled(False)
        self.te_text.setEnabled(False)
        self.progress_bar.setValue(0)
        
        # Criar e iniciar worker
        self.worker = TextToSpeechWorker(text, language='pt')
        self.worker.progress.connect(self.update_progress)
        self.worker.status.connect(self.update_status)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        self.worker.start()
    
    def update_progress(self, value):
        """Atualiza a barra de progresso"""
        self.progress_bar.setValue(value)
    
    def update_status(self, message):
        """Atualiza o label de status"""
        self.lb_status.setText(message)
        self.lb_status.setStyleSheet('color: #5cb85c; font-style: italic;')
    
    def on_finished(self):
        """Chamado quando a conversão termina com sucesso"""
        self.button.setEnabled(True)
        self.te_text.setEnabled(True)
        self.lb_status.setText('✓ Áudio gerado com sucesso!')
        self.lb_status.setStyleSheet('color: #5cb85c; font-weight: bold;')
        
        # Verificar se arquivo existe
        if os.path.exists('output.mp3'):
            size_mb = os.path.getsize('output.mp3') / (1024 * 1024)
            self.lb_status.setText(
                f'✓ Áudio gerado com sucesso! ({size_mb:.2f} MB)'
            )
    
    def on_error(self, error_message):
        """Chamado quando há um erro"""
        self.button.setEnabled(True)
        self.te_text.setEnabled(True)
        self.progress_bar.setValue(0)
        self.lb_status.setText(f'✗ Erro: {error_message}')
        self.lb_status.setStyleSheet('color: #d9534f; font-weight: bold;')
    
    def clear_fields(self):
        """Limpa os campos"""
        self.te_text.clear()
        self.progress_bar.setValue(0)
        self.lb_status.setText('Pronto para converter')
        self.lb_status.setStyleSheet('color: #666; font-style: italic;')


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    qtm.apply_stylesheet(app, theme='dark_lightgreen.xml')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
