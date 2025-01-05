import flet as ft

def main(page: ft.Page):
    page.title = "Flet Sample App"

    def button_clicked(e):
        output_text.value = f"Hello, {input_text.value}!"
        page.update()

    input_text = ft.TextField(label="Enter your name")
    output_text = ft.Text(value="", size=20)
    button = ft.ElevatedButton(text="Greet", on_click=button_clicked)

    page.add(input_text, button, output_text)

ft.app(target=main)