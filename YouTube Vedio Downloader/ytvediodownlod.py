from tkinter import *
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import threading

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage)
    root.update_idletasks()

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        selected_stream = None

        # Get the selected resolution from the dropdown
        selected_resolution = resolution_var.get()
        if selected_resolution == "Audio Only":
            selected_stream = yt.streams.filter(only_audio=True).first()
        else:
            selected_stream = yt.streams.filter(res=selected_resolution, progressive=True).first()

        if not selected_stream:
            messagebox.showerror("Error", "Selected resolution is not available.")
            return

        save_path = filedialog.askdirectory()
        if not save_path:
            return

        # Reset progress bar
        progress_var.set(0)

        # Start the download in a separate thread
        threading.Thread(target=selected_stream.download, kwargs={'output_path': save_path}).start()
        messagebox.showinfo("Success", f"Downloading '{yt.title}'")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

def fetch_resolutions():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    try:
        yt = YouTube(url)
        resolutions = set()
        for stream in yt.streams.filter(progressive=True):
            resolutions.add(stream.resolution)
        resolutions.add("Audio Only")  # Add audio only option

        resolution_var.set('')
        resolution_menu['menu'].delete(0, 'end')

        for res in sorted(resolutions):
            resolution_menu['menu'].add_command(label=res, command=lambda value=res: resolution_var.set(value))
        resolution_var.set("Select Resolution")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch resolutions: {e}")

# Create the main application window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("400x300")

# Create and place the URL entry widget
url_label = Label(root, text="YouTube Video URL", font=('Arial', 20))
url_label.place(x=70, y=0)
url_entry = Entry(root, width=55, bd=1, relief='solid')
url_entry.place(x=5, y=60, height=30)

# Create and place the Fetch Resolutions button
fetch_button = Button(root, text="Fetch Resolutions", command=fetch_resolutions, bd=1, relief='solid')
fetch_button.place(x=30, y=100)

# Create and place the resolution selection menu
resolution_var = StringVar(root)
resolution_var.set("Select Resolution")
resolution_menu = OptionMenu(root, resolution_var, "Select Resolution")
resolution_menu.place(x=200, y=100)

# Create and place the Download button
download_button = Button(root, text="Download", command=download_video, font=('Arial', 15), bd=1, relief='solid', bg='green', fg='white')
download_button.place(x=150, y=200)

# Create and place the progress bar
progress_var = DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.place(x=50, y=250, width=300, height=30)

# Run the application
root.mainloop()
