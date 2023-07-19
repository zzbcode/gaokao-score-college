import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口图标
        self.setWindowIcon(QIcon('favicon.ico'))
        
        # 创建界面元素
        self.score_label = QLabel('请输入分数：')
        self.score_input = QLineEdit()
        self.result_label = QLabel('查询结果：')
        self.result_output = QLabel()
        self.search_button = QPushButton('查询')

        # 设置界面布局
        layout = QVBoxLayout()
        layout.addWidget(self.score_label)
        layout.addWidget(self.score_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        self.setLayout(layout)

        # 绑定按钮点击事件
        self.search_button.clicked.connect(self.search)

    def search(self):
        # 读取CSV文件
        df = pd.read_csv('理工.csv')

        # 过滤数据
        score = float(self.score_input.text())
        filtered_df = df[df['最低分'] >= score]
        # filtered_df = df[df['最低分'].astype(int) >= int(score)]


        # 显示结果
        result = '\n'.join(filtered_df['院校名称'].tolist())
        self.result_output.setText(result)

if __name__ == '__main__':
    # 创建应用程序和主窗口
    app = QApplication(sys.argv)
    window = MainWindow()

    # 显示主窗口
    window.show()

    # 运行应用程序
    sys.exit(app.exec_())