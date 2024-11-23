from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QHBoxLayout
)
import yt_dlp

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_directory = "."  # Initial directory for saving downloads
        self.initUI()

    def initUI(self):
        # Set window properties and layout
        self.setWindowTitle("YouTube Link and Directory Selector")
        self.setGeometry(100, 100, 400, 180)

        layout = QVBoxLayout()
        self.directory_layout = QHBoxLayout()

        # Setup directory selection label and button
        self.directory_label = QLabel("No directory selected", self)
        self.directory_layout.addWidget(self.directory_label)
        self.select_directory_btn = QPushButton("Select", self)
        self.select_directory_btn.setFixedSize(70, 30)
        self.select_directory_btn.clicked.connect(self.showDirectoryDialog)
        self.directory_layout.addWidget(self.select_directory_btn)

        layout.addLayout(self.directory_layout)
        self.setLayout(layout)

        # Setup input field for YouTube link
        self.youtube_link_label = QLabel("Enter YouTube Link:", self)
        layout.addWidget(self.youtube_link_label)
        self.youtube_link_input = QLineEdit(self)
        layout.addWidget(self.youtube_link_input)

        # Setup download button
        self.submit_button = QPushButton("DOWNLOAD", self)
        self.submit_button.clicked.connect(self.submitLink)
        layout.addWidget(self.submit_button)

    def submitLink(self):
        link = self.youtube_link_input.text()
        # Handle download if directory is selected
        if self.selected_directory:
            try:
                ydl_opts = {
                    "format": "bestvideo+bestaudio/best",
                    "outtmpl": f"{self.selected_directory}/%(title)s.%(ext)s",
                    "noplaylist": True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                self.youtube_link_label.setText("Download Complete.")
            except Exception as e:
                self.youtube_link_label.setText(f"Failed to download: {str(e)}")
                print(f"Error: {str(e)}")
        else:
            self.youtube_link_label.setText("Please select a directory first.")

    def showDirectoryDialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        # Update UI with selected directory
        if directory:
            self.directory_label.setText(f"Selected Directory: {directory}")
            self.selected_directory = directory

if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    ex.show()
    app.exec_()
