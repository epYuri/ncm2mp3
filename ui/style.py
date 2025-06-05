# ui/style.py
def apply_styles(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #fafafa;
            font-family: 'Arial';
            font-size: 14px;
        }
        QPushButton {
            background-color: #ffffff;
            border: 1px solid #ccc;
            padding: 10px 20px;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #f0f0f0;
            border-color: #aaa;
        }
        QPushButton:disabled {
            background-color: #eee;
            color: #999;
            border-color: #ddd;
        }
    """)
