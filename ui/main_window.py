# ui/main_window.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from logic.converter import convert_multiple
from .style import apply_styles


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NCM 转换器")
        self.setFixedSize(600, 360)
        self.setAcceptDrops(True)

        apply_styles(self)  # 应用样式

        self.selected_files = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        title = QLabel("🎧 NCM 批量转换器")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.status_label = QLabel("拖拽文件进来或点击下方按钮选择文件")
        self.status_label.setStyleSheet("color: #444; font-size: 14px;")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        btn_layout = QHBoxLayout()
        self.select_btn = QPushButton("选择文件")
        self.select_btn.clicked.connect(self.select_files)

        self.convert_btn = QPushButton("开始转换")
        self.convert_btn.setEnabled(False)
        self.convert_btn.clicked.connect(self.convert_files)

        btn_layout.addWidget(self.select_btn)
        btn_layout.addWidget(self.convert_btn)
        layout.addLayout(btn_layout)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "选择 NCM 文件", "", "NCM 文件 (*.ncm)"
        )
        if files:
            self.selected_files = files
            self.status_label.setText(f"已选择 {len(files)} 个文件")
            self.convert_btn.setEnabled(True)
        else:
            self.status_label.setText("未选择文件")
            self.convert_btn.setEnabled(False)

    def convert_files(self):
        if self.selected_files:
            results = convert_multiple(self.selected_files)
            result_text = "\n".join(results)
            QMessageBox.information(self, "转换完成", result_text)
        else:
            QMessageBox.warning(self, "提示", "请先选择文件")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        ncm_files = [f for f in files if f.lower().endswith(".ncm")]
        if ncm_files:
            self.selected_files = ncm_files
            self.status_label.setText(f"拖拽添加了 {len(ncm_files)} 个文件")
            self.convert_btn.setEnabled(True)
        else:
            QMessageBox.warning(self, "提示", "请拖入 .ncm 文件")
