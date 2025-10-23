#!/usr/bin/env python3
"""
SnakeMediaPlayer - Media Player Backend Module
Developer: Er. Sangam Krishna
GitHub: @SnakeEye-sudo
"""

import pygame
import os

class MediaPlayer:
    """
    Backend media player class using pygame for playback.
    Handles loading, playing, pausing, and controlling media files.
    """
    
    def __init__(self):
        """
        Initialize the media player.
        """
        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        
        self.current_file = None
        self.is_playing = False
        self.is_paused = False
        self.volume = 0.7  # Default volume (0.0 to 1.0)
        self.position = 0
        
        print("🎵 Media Player initialized")
        
    def load(self, file_path):
        """
        Load a media file.
        
        Args:
            file_path (str): Path to the media file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            if not os.path.exists(file_path):
                print(f"Error: File not found - {file_path}")
                return False
                
            # Stop any currently playing media
            self.stop()
            
            # Load the new file
            pygame.mixer.music.load(file_path)
            self.current_file = file_path
            
            # Set volume
            pygame.mixer.music.set_volume(self.volume)
            
            print(f"✓ Loaded: {os.path.basename(file_path)}")
            return True
            
        except pygame.error as e:
            print(f"Error loading file: {e}")
            return False
            
    def play(self):
        """
        Play the currently loaded media.
        """
        if self.current_file is None:
            print("No file loaded")
            return
            
        if self.is_paused:
            # Unpause if paused
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            # Start playing from beginning
            pygame.mixer.music.play()
            
        self.is_playing = True
        print(f"▶️ Playing: {os.path.basename(self.current_file)}")
        
    def pause(self):
        """
        Pause the currently playing media.
        """
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.is_playing = False
            print("⏸️ Paused")
        else:
            print("Nothing to pause")
            
    def stop(self):
        """
        Stop the currently playing media.
        """
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.position = 0
        print("⏹️ Stopped")
        
    def set_volume(self, volume):
        """
        Set the playback volume.
        
        Args:
            volume (int): Volume level (0-100)
        """
        # Convert from 0-100 to 0.0-1.0
        self.volume = volume / 100.0
        pygame.mixer.music.set_volume(self.volume)
        print(f"🔊 Volume: {volume}%")
        
    def seek(self, position):
        """
        Seek to a specific position in the media.
        
        Args:
            position (int): Position in seconds
        """
        try:
            # Note: pygame.mixer.music.set_pos() works differently for different formats
            # This is a simplified implementation
            pygame.mixer.music.set_pos(position)
            self.position = position
            print(f"⏭ Seeking to: {position}s")
        except Exception as e:
            print(f"Seek error: {e}")
            
    def get_volume(self):
        """
        Get the current volume level.
        
        Returns:
            float: Volume level (0.0 to 1.0)
        """
        return self.volume
        
    def is_busy(self):
        """
        Check if the player is currently playing.
        
        Returns:
            bool: True if playing, False otherwise
        """
        return pygame.mixer.music.get_busy()
        
    def get_current_file(self):
        """
        Get the current file path.
        
        Returns:
            str: Current file path or None
        """
        return self.current_file
        
    def cleanup(self):
        """
        Cleanup resources when closing the player.
        """
        self.stop()
        pygame.mixer.quit()
        print("👋 Media Player closed")
        
    def __del__(self):
        """
        Destructor to ensure cleanup.
        """
        try:
            self.cleanup()
        except:
            pass


# Example usage for testing
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🐍 SnakeMediaPlayer - Media Player Module Test")
    print("Developed by: Er. Sangam Krishna")
    print("GitHub: @SnakeEye-sudo")
    print("="*50 + "\n")
    
    # Create player instance
    player = MediaPlayer()
    
    # Test basic functionality
    print("\nMedia Player backend is ready!")
    print("Use this module with player_ui.py for full functionality.\n")
