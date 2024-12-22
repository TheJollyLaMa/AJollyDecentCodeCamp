import os
import requests
import pygame
import audioop
from pydub import AudioSegment
import tempfile
from bs4 import BeautifulSoup
import threading


def fetch_song_list(ipfs_url):
    try:
        print(f"Fetching file list from IPFS directory: {ipfs_url}")
        response = requests.get(ipfs_url)
        response.raise_for_status()
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        all_files = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(('.m4a', '.mp3', '.wav', '.ogg'))]

        unique_files = [file for file in all_files if "?filename=" not in file]

        if not unique_files:
            print("No audio files found in the IPFS directory.")
            return []

        print("\nAvailable Songs:")
        for i, file in enumerate(unique_files, start=1):
            file_name = os.path.basename(file).replace('%20', ' ')
            print(f"{i}. {file_name}")

        return unique_files

    except requests.exceptions.RequestException as e:
        print(f"Error accessing IPFS directory: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def play_song(ipfs_url, file_url, file_name):
    try:
        print(f"\nFetching and playing: {file_name.replace('%20', ' ')}")

        if not file_url.startswith("http"):
            file_url = os.path.join(ipfs_url, file_url.lstrip("/"))

        audio_data = requests.get(file_url)
        audio_data.raise_for_status()

        file_ext = os.path.splitext(file_url)[1].lower()
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=file_ext)
        temp_file.write(audio_data.content)
        temp_file.close()

        if file_ext in ['.m4a']:
            audio = AudioSegment.from_file(temp_file.name, format="m4a")
            temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            audio.export(temp_wav.name, format="wav")
            os.remove(temp_file.name)
            temp_file.name = temp_wav.name

        pygame.mixer.music.load(temp_file.name)
        pygame.mixer.music.play()

        return temp_file.name

    except requests.exceptions.RequestException as e:
        print(f"Error fetching file '{file_name}': {e}")
    except pygame.error as e:
        print(f"Error playing file '{file_name}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred with file '{file_name}': {e}")


def play_all_songs(ipfs_url, songs):
    stop_event = threading.Event()
    paused_event = threading.Event()

    def playback_control():
        while not stop_event.is_set():
            print("\nPlay-All Controls:")
            print("1. Pause")
            print("2. Resume")
            print("3. Stop")
            try:
                control = int(input("\nEnter your choice: "))
                if control == 1:
                    if not paused_event.is_set():
                        pygame.mixer.music.pause()
                        paused_event.set()
                        print("Playback paused.")
                elif control == 2:
                    if paused_event.is_set():
                        pygame.mixer.music.unpause()
                        paused_event.clear()
                        print("Playback resumed.")
                elif control == 3:
                    stop_event.set()
                    pygame.mixer.music.stop()
                    print("Stopping playback...")
            except ValueError:
                print("Invalid input. Please enter a number.")

    control_thread = threading.Thread(target=playback_control)
    control_thread.start()

    for file_url in songs:
        if stop_event.is_set():
            break
        file_name = os.path.basename(file_url).replace('%20', ' ')
        temp_file = play_song(ipfs_url, file_url, file_name)
        if temp_file:
            while pygame.mixer.music.get_busy():
                if stop_event.is_set():
                    break
                if paused_event.is_set():
                    pygame.time.Clock().tick(10)  # Avoid busy-waiting during pause
                else:
                    pygame.time.Clock().tick(10)  # Check every 100ms for playback
            os.remove(temp_file)

    stop_event.set()
    control_thread.join()
    print("Finished playing all songs.")


def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error initializing audio system: {e}")
        return

    ipfs_directory_url = "https://bafybeibokvlz3aqh2ziuejpbkxrheqlg55zhfcb7rfjafdbx42jm4vor7u.ipfs.w3s.link/"
    songs = fetch_song_list(ipfs_directory_url)
    if not songs:
        return

    current_song = None

    while True:
        print("\nControls:")
        print("1. Play a song")
        print("2. Play all songs")
        print("3. Pause")
        print("4. Resume")
        print("5. Stop")
        print("6. Show song list")
        print("7. Change playlist")
        print("8. Exit")

        try:
            choice = int(input("\nGive me Your dAMn your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            try:
                song_choice = int(input(f"Enter the song number (1-{len(songs)}): "))
                if 1 <= song_choice <= len(songs):
                    if current_song:
                        pygame.mixer.music.stop()
                        os.remove(current_song)
                    file_url = songs[song_choice - 1]
                    file_name = os.path.basename(file_url).replace('%20', ' ')
                    current_song = play_song(ipfs_directory_url, file_url, file_name)
                else:
                    print("Invalid song number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == 2:
            if current_song:
                pygame.mixer.music.stop()
                os.remove(current_song)
                current_song = None
            play_all_songs(ipfs_directory_url, songs)
        elif choice == 3:
            pygame.mixer.music.pause()
            print("Song paused.")
        elif choice == 4:
            pygame.mixer.music.unpause()
            print("Song resumed.")
        elif choice == 5:
            pygame.mixer.music.stop()
            if current_song:
                os.remove(current_song)
                current_song = None
            print("Song stopped.")
        elif choice == 6:
            fetch_song_list(ipfs_directory_url)
        elif choice == 7:
            new_url = input("Enter the new IPFS directory URL: ").strip()
            songs = fetch_song_list(new_url)
            if songs:
                ipfs_directory_url = new_url
                if current_song:
                    pygame.mixer.music.stop()
                    os.remove(current_song)
                    current_song = None
        elif choice == 8:
            print("Exiting...")
            if current_song:
                os.remove(current_song)
            pygame.mixer.quit()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()