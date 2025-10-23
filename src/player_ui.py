#!/usr/bin/env python3
"""
SnakeMediaPlayer - User Interface Module
Developer: Er. Sangam Krishna
GitHub: @SnakeEye-sudo
"""
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel, QFileDialog, QListWidget
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from media_player import MediaPlayer
import os

class MediaPlayerUI(QMainWindow):
    """
    Main UI class for SnakeMediaPlayer with SnakeEye theme.
    """
    
    def __init__(self):
        super().__init__()
        self.media_player = MediaPlayer()
        self.playlist = []
        self.current_index = -1
        self.init_ui()
        self.setup_connections()
        
    def init_ui(self):
        """
        Initialize the user interface components.
        """
        self.setWindowTitle("🐍 SnakeMediaPlayer")
        self.setGeometry(100, 100, 800, 600)
        
        # Set window icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'icons', 'generated-image.jpg')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Apply SnakeEye theme (dark green/black theme)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0a0a;
            }
            QPushButton {
                background-color: #1a4d2e;
                color: #00ff00;
                border: 2px solid #00aa00;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2a5d3e;
                border: 2px solid #00ff00;
            }
            QPushButton:pressed {
                background-color: #0a3d1e;
            }
            QLabel {
                color: #00ff00;
                font-size: 14px;
            }
            QSlider::groove:horizontal {
                background: #1a4d2e;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #00ff00;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QListWidget {
                background-color: #0a0a0a;
                color: #00ff00;
                border: 2px solid #1a4d2e;
            }
        """)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Title label
        title_label = QLabel("🐍 SnakeMediaPlayer 🎵")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px;")
        main_layout.addWidget(title_label)
        
        # Current file label
        self.current_file_label = QLabel("No file loaded")
        self.current_file_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.current_file_label)
        
        # Progress slider
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setRange(0, 100)
        main_layout.addWidget(self.progress_slider)
        
        # Time labels
        time_layout = QHBoxLayout()
        self.time_label = QLabel("00:00")
        self.duration_label = QLabel("00:00")
        time_layout.addWidget(self.time_label)
        time_layout.addStretch()
        time_layout.addWidget(self.duration_label)
        main_layout.addLayout(time_layout)
        
        # Control buttons
        controls_layout = QHBoxLayout()
        
        self.open_button = QPushButton("📂 Open File")
        self.play_button = QPushButton("▶️ Play")
        self.pause_button = QPushButton("⏸️ Pause")
        self.stop_button = QPushButton("⏹️ Stop")
        self.prev_button = QPushButton("⏮ Previous")
        self.next_button = QPushButton("⏭ Next")
        
        controls_layout.addWidget(self.prev_button)
        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.pause_button)
        controls_layout.addWidget(self.stop_button)
        controls_layout.addWidget(self.next_button)
        controls_layout.addWidget(self.open_button)
        
        main_layout.addLayout(controls_layout)
        
        # Volume control
        volume_layout = QHBoxLayout()
        volume_label = QLabel("🔊 Volume:")
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(70)
        volume_layout.addWidget(volume_label)
        volume_layout.addWidget(self.volume_slider)
        main_layout.addLayout(volume_layout)
        
        # Playlist
        playlist_label = QLabel("📝 Playlist")
        main_layout.addWidget(playlist_label)
        self.playlist_widget = QListWidget()
        main_layout.addWidget(self.playlist_widget)
        
        # Credits
        credits_label = QLabel("Created by: Er. Sangam Krishna (@SnakeEye-sudo)")
        credits_label.setAlignment(Qt.AlignCenter)
        credits_label.setStyleSheet("font-size: 10px; padding: 10px;")
        main_layout.addWidget(credits_label)
        
    def setup_connections(self):
        """
        Setup signal-slot connections for UI elements.
        """
        self.open_button.clicked.connect(self.open_file)
        self.play_button.clicked.connect(self.play_media)
        self.pause_button.clicked.connect(self.pause_media)
        self.stop_button.clicked.connect(self.stop_media)
        self.prev_button.clicked.connect(self.previous_track)
        self.next_button.clicked.connect(self.next_track)
        self.volume_slider.valueChanged.connect(self.change_volume)
        self.progress_slider.sliderMoved.connect(self.seek_media)
        self.playlist_widget.itemDoubleClicked.connect(self.play_from_playlist)
        
    def open_file(self):
        """
        Open file dialog to select media files.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Media File",
            "",
            "Media Files (*.mp3 *.mp4 *.avi *.mkv *.wav *.flac);;All Files (*.*)"
        )
        
        if file_path:
            self.add_to_playlist(file_path)
            self.current_index = len(self.playlist) - 1
            self.load_media(file_path)
            
    def add_to_playlist(self, file_path):
        """
        Add a file to the playlist.
        """
        if file_path not in self.playlist:
            self.playlist.append(file_path)
            filename = os.path.basename(file_path)
            self.playlist_widget.addItem(filename)
            
    def load_media(self, file_path):
        """
        Load a media file.
        """
        self.media_player.load(file_path)
        filename = os.path.basename(file_path)
        self.current_file_label.setText(f"Loaded: {filename}")
        
    def play_media(self):
        """
        Play the current media.
        """
        self.media_player.play()
        self.current_file_label.setText(f"Playing: {self.get_current_filename()}")
        
    def pause_media(self):
        """
        Pause the current media.
        """
        self.media_player.pause()
        self.current_file_label.setText(f"Paused: {self.get_current_filename()}")
        
    def stop_media(self):
        """
        Stop the current media.
        """
        self.media_player.stop()
        self.current_file_label.setText(f"Stopped: {self.get_current_filename()}")
        
    def previous_track(self):
        """
        Play the previous track in the playlist.
        """
        if self.current_index > 0:
            self.current_index -= 1
            self.load_media(self.playlist[self.current_index])
            self.play_media()
            
    def next_track(self):
        """
        Play the next track in the playlist.
        """
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.load_media(self.playlist[self.current_index])
            self.play_media()
            
    def change_volume(self, value):
        """
        Change the volume level.
        """
        self.media_player.set_volume(value)
        
    def seek_media(self, position):
        """
        Seek to a specific position in the media.
        """
        self.media_player.seek(position)
        
    def play_from_playlist(self, item):
        """
        Play a selected item from the playlist.
        """
        index = self.playlist_widget.row(item)
        self.current_index = index
        self.load_media(self.playlist[index])
        self.play_media()
        
    def get_current_filename(self):
        """
        Get the current file name.
        """
        if 0 <= self.current_index < len(self.playlist):
            return os.path.basename(self.playlist[self.current_index])
        return "No file"
