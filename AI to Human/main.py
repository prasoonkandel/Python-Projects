# This converts ai written text human form
# This has neat and clean dark UI you'll love it.
import tkinter as tk
import requests
from tkinter import messagebox

root = tk.Tk()
root.title("AI to Human Text Converter")
root.geometry("900x550")
root.minsize(900, 550)
root.configure(bg="#121212")

label_style = {
    "font": ("Montserrat", 18, "bold"),
    "bg": "#121212",
    "fg": "#e0e0e0"
}

text_style = {
    "font": ("Montserrat", 14),
    "bg": "#1e1e1e",
    "fg": "#fafafa",
    "insertbackground": "#ffffff",
    "relief": "flat",
    "wrap": "word",
    "borderwidth": 0,
    "padx": 10,
    "pady": 10
}

tk.Label(root, text="AI Text", **label_style).grid(row=0,
                                                   column=0, sticky="nsew", pady=(10, 0))
tk.Label(root, text="Human Text", **label_style).grid(row=0,
                                                      column=1, sticky="nsew", pady=(10, 0))

ai_text = tk.Text(root, **text_style)
ai_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

human_text = tk.Text(root, **text_style)
human_text.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
human_text.insert(1.0, "Your result will appear here")

style_var = tk.StringVar(root)
style_var.set("Formal")

style_dropdown = tk.OptionMenu(root, style_var, "Formal", "Academic", "Casual")
style_dropdown.config(
    font=("Montserrat", 14, "bold"),
    bg="#303030",
    fg="white",
    activebackground="#505050",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    highlightthickness=0
)
style_dropdown.grid(row=2, column=0, columnspan=2, pady=(0, 10))


def humanize_text():
    input_text = ai_text.get("1.0", tk.END).strip()
    selected_style = style_var.get().lower()

    if input_text == "":
        messagebox.showwarning(
            "Missing Text", "Please enter your AI-generated text.")
        return

    if len(input_text) <= 200:
        messagebox.showwarning(
            "Too Short", "Please enter more than 200 characters.")
        return

    API_URL = "https://chatgpt-42.p.rapidapi.com/aitohuman"
    payload = {
        "text": input_text,
        "prompt": f"Rewrite this text in a {selected_style} and human-like tone."
    }
    headers = {

        # I used rapid free version u can also use it to get your own api key
        "x-rapidAPI-Key": "[Your api key]",  # paste here
        "x-rapidAPI-Host": "https://chatgpt-42.p.rapidapi.com/aitohuman",
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    try:

        response.raise_for_status()
        res_data = response.json()
        print("API Response:", res_data)

        if res_data.get("status") and res_data.get("result"):
            output = res_data["result"][0]
            human_text.delete("1.0", tk.END)
            human_text.insert("1.0", output)
        else:
            human_text.delete("1.0", tk.END)
            human_text.insert(
                "1.0", "❌ No result returned. Try a different style or longer input.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request failed: {e}")


humanize_button = tk.Button(
    root,
    text="🔁 Humanize",
    command=humanize_text,
    font=("Montserrat", 18, "bold"),
    bg="#0e9f30",
    fg="white",
    activebackground="#0b7a25",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)
humanize_button.grid(row=3, column=0, columnspan=2,
                     sticky="nsew", padx=20, pady=(0, 15))

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
