from app.app import App
from app.inputFrame import InputFrame

if __name__ == "__main__":
    app = App()
    InputFrame(app)
    app.mainloop()
