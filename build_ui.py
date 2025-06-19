import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class UiFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".ui"):
            ui_file = Path(event.src_path)
            py_file = ui_file.with_name(f"ui_{ui_file.stem}.py")
            print(f"Detected change: {ui_file}, rebuilding → {py_file}")

            result = subprocess.run([
                ".venv\\Scripts\\pyside6-uic.exe",
                str(ui_file),
                "-o",
                str(py_file)
            ])

            if result.returncode == 0:
                print(f"✅ Successfully rebuilt {py_file}")
            else:
                print(f"❌ Failed to rebuild {py_file}")
    def on_created(self, event):
        self.on_modified(event)

if __name__ == "__main__":
    path_to_watch = Path("app").resolve()
    print(f"👀 Watching {path_to_watch} for .ui changes...")

    event_handler = UiFileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(path_to_watch), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
