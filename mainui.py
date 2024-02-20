from PyQt5.QtWidgets import QMainWindow, QSplitter, QTextBrowser, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import ChatGPT
import markdown

initial_text = "Your code here..."
message_here = "Your messages here..."
enter_here = "Enter your request here..."
Submit = "Submit"
window_Input = "UI Recreation with Input"

class CustomUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 创建主拆分器
        main_splitter = QSplitter(Qt.Horizontal, self)
        
        # 在右侧创建消息和输入显示
        message_input_display = QWidget(main_splitter)
        message_input_layout = QVBoxLayout(message_input_display)
        
        # 消息显示部分
        message_display_label = QLabel(message_here)
        message_display_label.setFont(QFont('Arial', 12))
        message_input_layout.addWidget(message_display_label)
        
        # 输入部分
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText(enter_here)
        input_layout.addWidget(self.input_box)
        
        submit_button = QPushButton(Submit)
        submit_button.clicked.connect(self.onSubmit)
        input_layout.addWidget(submit_button)
        
        message_input_layout.addLayout(input_layout)
        
        # 设置主布局
        self.setCentralWidget(main_splitter)
        
        # 设置窗口标题和初始大小
        self.setWindowTitle(window_Input)
        self.setGeometry(100, 100, 1200, 600)
        # 左侧的代码编辑器，替换为用于Markdown的QTextBrowser
        self.code_display = QTextBrowser(main_splitter)
        self.code_display.setFont(QFont('Consolas', 10))
        self.setMarkdown(initial_text)

    def setMarkdown(self, md_text):
        # 将Markdown转换为HTML并在QTextBrowser中进行设置
        html_text = markdown.markdown(md_text)
        self.code_display.setHtml(html_text)    
    
    def onSubmit(self):
        # 处理输入的提交
        request_text = self.input_box.text()
        if request_text != "":
            # 在这里，您应该替换为对ChatGPT的实际调用和响应处理
            print(request_text)
            response_html = markdown.markdown(ChatGPT.sendMessageChatGPT(request_text))
            self.code_display.setHtml(response_html)  # 使用setHtml显示HTML
            self.input_box.setText("")  # 提交后清除输入框
