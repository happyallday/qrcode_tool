import sys
import os
import tempfile
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QFileDialog, QMessageBox, QGroupBox)
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QColorDialog
from PIL import Image
import qrcode
from pyzbar.pyzbar import decode


class QRCodeTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("二维码工具")
        self.setMinimumSize(800, 500)
        self.current_qr_image = None
        self.fore_color = (0, 0, 0)
        self.back_color = (255, 255, 255)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        main_layout.addWidget(self.create_generate_group())
        main_layout.addWidget(self.create_decode_group())

    def create_generate_group(self):
        group = QGroupBox("生成二维码")
        layout = QVBoxLayout()
        group.setLayout(layout)

        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText("请输入内容...")
        self.input_edit.returnPressed.connect(self.generate_qrcode)
        layout.addWidget(QLabel("输入内容:"))
        layout.addWidget(self.input_edit)

        self.generate_btn = QPushButton("生成二维码")
        self.generate_btn.clicked.connect(self.generate_qrcode)
        layout.addWidget(self.generate_btn)

        color_layout = QHBoxLayout()
        self.fore_color_btn = QPushButton("前景色")
        self.fore_color_btn.setStyleSheet("background-color: black; color: white;")
        self.fore_color_btn.clicked.connect(self.select_fore_color)
        self.back_color_btn = QPushButton("背景色")
        self.back_color_btn.setStyleSheet("background-color: white; border: 1px solid #ccc;")
        self.back_color_btn.clicked.connect(self.select_back_color)
        color_layout.addWidget(self.fore_color_btn)
        color_layout.addWidget(self.back_color_btn)
        color_layout.addStretch()
        layout.addLayout(color_layout)

        self.qr_label = QLabel()
        self.qr_label.setMinimumSize(250, 250)
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setStyleSheet("border: 1px solid #ccc; background: white;")
        layout.addWidget(self.qr_label)

        self.save_btn = QPushButton("保存二维码")
        self.save_btn.clicked.connect(self.save_qrcode)
        self.save_btn.setEnabled(False)
        layout.addWidget(self.save_btn)

        layout.addStretch()
        return group

    def create_decode_group(self):
        group = QGroupBox("解析二维码")
        layout = QVBoxLayout()
        group.setLayout(layout)

        self.upload_btn = QPushButton("上传图片")
        self.upload_btn.clicked.connect(self.upload_image)
        layout.addWidget(self.upload_btn)

        self.image_label = QLabel()
        self.image_label.setMinimumSize(250, 250)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid #ccc; background: white;")
        layout.addWidget(self.image_label)

        layout.addWidget(QLabel("解析结果:"))
        self.result_edit = QTextEdit()
        self.result_edit.setReadOnly(True)
        self.result_edit.setMaximumHeight(100)
        layout.addWidget(self.result_edit)

        return group

    def generate_qrcode(self):
        content = self.input_edit.text().strip()
        if not content:
            QMessageBox.warning(self, "提示", "请输入内容")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fore_color, back_color=self.back_color)
        self.current_qr_image = img

        img_pil = img.resize((250, 250))
        temp_path = os.path.join(tempfile.gettempdir(), "temp_qr.png")
        img_pil.save(temp_path)
        
        pixmap = QPixmap(temp_path)
        self.qr_label.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.save_btn.setEnabled(True)

    def select_fore_color(self):
        color = QColorDialog.getColor(QColor(*self.fore_color), self, "选择前景色")
        if color.isValid():
            self.fore_color = (color.red(), color.green(), color.blue())
            self.fore_color_btn.setStyleSheet(f"background-color: {color.name()}; color: {'white' if sum(self.fore_color) < 384 else 'black'};")

    def select_back_color(self):
        color = QColorDialog.getColor(QColor(*self.back_color), self, "选择背景色")
        if color.isValid():
            self.back_color = (color.red(), color.green(), color.blue())
            self.back_color_btn.setStyleSheet(f"background-color: {color.name()}; color: {'white' if sum(self.back_color) < 384 else 'black'};")

    def save_qrcode(self):
        if self.current_qr_image is None:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "保存二维码", "", "PNG Image (*.png)"
        )
        if file_path:
            self.current_qr_image.save(file_path)
            QMessageBox.information(self, "成功", "二维码已保存")

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择图片", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if not file_path:
            return

        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        try:
            img = Image.open(file_path)
            decoded = decode(img)
            if decoded:
                results = [d.data.decode('utf-8') for d in decoded]
                self.result_edit.setText("\n".join(results))
            else:
                self.result_edit.setText("未检测到二维码")
        except Exception as e:
            self.result_edit.setText(f"解析失败: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeTool()
    window.show()
    sys.exit(app.exec_())
