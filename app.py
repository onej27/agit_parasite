import tkinter as tk
import main
import asyncio
import threading

# Create the main window with width 500 height 300
root = tk.Tk()
root.geometry("500x100")

# Label with "Enter URL"
label = tk.Label(root, text="Enter URL")
label.pack()

# Add single line textfield with 100% of widdow width
entry = tk.Entry(root, width=500)

entry.pack()

# Add Button Start
button = tk.Button(root, text="Start")
button.pack()

# Progress label
progressLabel = tk.Label(root, text="")
progressLabel.pack()

# Define an async function that will call main.download_novel
async def download_novel_async(url, progress_callback):
    await main.download_novel(url, progress_callback=progress_callback)
    button.pack()
    progressLabel.config(text="완료")
    return "Task completed"

# Print text enter when start is pressed
def handleStartButton():
    url = entry.get()

    def update_progress(progress):
        progressLabel.config(text=f"다운로드중: {progress}")

    # Run the asyncio event loop in a new thread
    threading.Thread(target=asyncio.run, args=(download_novel_async(url, update_progress),)).start()
    
    #Hide button while download in progress
    button.pack_forget()


# Bind the button to the handleStartButton function
button.config(command=handleStartButton)

# Start the event loop
root.mainloop()