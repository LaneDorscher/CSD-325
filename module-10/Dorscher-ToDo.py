"""
Author: Lane Dorscher
Date: 08/13/2026
Course: CSD-325
Assignment: 10.2
Description: ToDo list program allows user to add and delete tasks.
"""
import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):

    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            tasks = []

        self.tasks = tasks

        # Window settings
        self.title("Dorscher-ToDo")
        self.geometry("300x400")

        # File menu
        self.menu_bar = tk.Menu(self)

        self.file_menu = tk.Menu(
            self.menu_bar,
            tearoff=0
        )

        self.file_menu.add_command(
            label="Exit",
            command=self.destroy
        )

        self.menu_bar.add_cascade(
            label="File",
            menu=self.file_menu
        )

        self.config(menu=self.menu_bar)

        # Color schemes for tasks
        self.colour_schemes = [
            {
                "bg": "lightgreen",
                "fg": "black"
            },
            {
                "bg": "darkgreen",
                "fg": "white"
            }
        ]

        # Scrollable task area
        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(
            self.tasks_canvas
        )

        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.tasks_canvas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1
        )

        self.scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        # Instruction label
        todo1 = tk.Label(
            self.tasks_frame,
            text="Add items below.\nRight-click a task to delete it.",
            bg="darkgrey",
            fg="white",
            pady=10
        )

        todo1.pack(
            side=tk.TOP,
            fill=tk.X
        )

        # Text box for adding tasks
        self.task_create = tk.Text(
            self.text_frame,
            height=3,
            bg="white",
            fg="black"
        )

        self.task_create.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.text_frame.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.task_create.focus_set()

        # Event bindings
        self.bind(
            "<Return>",
            self.add_task
        )

        self.bind(
            "<Configure>",
            self.on_frame_configure
        )

        self.bind_all(
            "<MouseWheel>",
            self.mouse_scroll
        )

        self.bind_all(
            "<Button-4>",
            self.mouse_scroll
        )

        self.bind_all(
            "<Button-5>",
            self.mouse_scroll
        )

        self.tasks_canvas.bind(
            "<Configure>",
            self.task_width
        )

    def add_task(self, event=None):
        task_text = self.task_create.get(
            1.0,
            tk.END
        ).strip()

        if len(task_text) > 0:
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10
            )

            self.set_task_colour(
                len(self.tasks),
                new_task
            )

            # Right-click deletes task
            new_task.bind(
                "<Button-3>",
                self.remove_task
            )

            new_task.pack(
                side=tk.TOP,
                fill=tk.X
            )

            self.tasks.append(new_task)

        self.task_create.delete(
            1.0,
            tk.END
        )

    def remove_task(self, event):
        task = event.widget

        if msg.askyesno(
            "Really Delete?",
            "Delete " + task.cget("text") + "?"
        ):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(
                index,
                task
            )

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(
            position,
            2
        )

        my_scheme_choice = self.colour_schemes[
            task_style_choice
        ]

        task.configure(
            bg=my_scheme_choice["bg"],
            fg=my_scheme_choice["fg"]
        )

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    def task_width(self, event):
        canvas_width = event.width

        self.tasks_canvas.itemconfig(
            self.canvas_frame,
            width=canvas_width
        )

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(
                move,
                "units"
            )


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()