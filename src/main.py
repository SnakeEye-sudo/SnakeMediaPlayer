#!/usr/bin/env python3
"""
SnakeMediaPlayer - Main Entry Point
Developer: Er. Sangam Krishna
GitHub: @SnakeEye-sudo
"""
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from player_ui import MediaPlayerUI

def main():
    """
    Main function to initialize and run the media player application.
    """
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("SnakeMediaPlayer")
    app.setOrganizationName("SnakeEye")
    app.setApplicationVersion("1.0.0")
    
    # Set application icon
    icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'icons', 'generated-image.jpg')
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    # Create and show the main window
    player = MediaPlayerUI()
    player.show()
    
    # Execute the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🐍 SnakeMediaPlayer v1.0.0 🎵")
    print("Developed by: Er. Sangam Krishna")
    print("GitHub: @SnakeEye-sudo")
    print("="*50 + "\n")
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {e}")
        sys.exit(1)
