import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QListWidget, QLabel, QProgressBar, QMessageBox
from PySide6.QtCore import Qt

from data_merge import merge_files_in_directory


class DataManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('c-med alpha Data Management')
        
        # main layout
        main_layout = QVBoxLayout()
        
        # add ListView for file list
        self.file_list = QListWidget(self)
        
        # path box layout setting
        path_box_layout = QHBoxLayout()
        
        # add path label
        self.path_label = QLabel('No folder selected', self)
        self.path_label.setFixedSize(300, 30) # Fix label size
        self.path_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.path_label.setWordWrap(False)
        self.path_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.path_label.setStyleSheet("QLabel { background-color : lightgrey; }")
        path_box_layout.addWidget(self.path_label)
        
        # add path search button
        self.path_button = QPushButton('Search', self)
        self.path_button.setFixedSize(100, 30)
        self.path_button.clicked.connect(self.select_folder)
        path_box_layout.addWidget(self.path_button)
        
        # bottom layout setting
        bottom_layout = QHBoxLayout()
        
        # add start button
        self.start_button = QPushButton('Start', self)
        self.start_button.setFixedSize(100, 30)
        self.start_button.clicked.connect(self.start_merge_data)
        bottom_layout.addWidget(self.start_button)
        
        # add reset button
        self.reset_button = QPushButton('Reset', self)
        self.reset_button.setFixedSize(100, 30)
        self.reset_button.clicked.connect(self.reset_app)
        bottom_layout.addWidget(self.reset_button)
        
        # add progress bar
        #! progress bar는 파일 합치는 코드에서 업데이트 진행
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        
        # layout stack
        main_layout.addWidget(self.file_list)
        main_layout.addLayout(path_box_layout)
        main_layout.addLayout(bottom_layout)
        main_layout.addWidget(self.progress_bar)
        
        # main layout setting
        self.setLayout(main_layout)
        self.resize(400, 400)
        
        
    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            elided_text = self.fontMetrics().elidedText(folder_path, Qt.TextElideMode.ElideRight, self.path_label.width())
            self.path_label.setText(elided_text)
            self.list_files(folder_path)
    
    def list_files(self, folder_path):
        self.file_list.clear()
        files = os.listdir(folder_path)
        for file in files:
            self.file_list.addItem(file)
    
    '''
    # TODO: data_merge_start function 완성하기
    '''
    def start_merge_data(self):
        directory_path = self.path_label.text()
        if not os.path.isdir(directory_path):
            self.show_error_message("파일 경로가 잘못되었습니다.")
            return
        merge_files_in_directory
    
    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle('Error')
        msg_box.exec()
    
    def reset_app(self):
        self.path_label.setText("No folder selected")
        self.file_list.clear()