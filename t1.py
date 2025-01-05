import flet as ft
import flet.canvas as cv
from flet_canvas2img import canvas2img

class State:
    x: float
    y: float

state = State()

def main(page: ft.Page):
    page.title = "Flet Brush"

    def pan_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: ft.DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    cp = cv.Canvas(
        [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.Colors.CYAN_50, ft.Colors.GREY]
                    )
                )
            ),
        ],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    def save_to_img(e):
        canvas2img(cp.shapes)

    def clear_canvas(e):
        cp.shapes = [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.Colors.CYAN_50, ft.Colors.GREY]
                    )
                )
            ),
        ]
        cp.update()

    page_col = ft.Column(
        [
            ft.Row(
                [
                    ft.ElevatedButton("Save", color='green', on_click=save_to_img),
                    ft.ElevatedButton("Clear", color='red', on_click=clear_canvas),
                ],
            ),

            ft.Container(
                cp,
                border_radius=5,
                width=float("inf"),
                expand=True,
            ),
        ],
        # vertical_alignment="center",
        horizontal_alignment="center",
        expand=True,
    )

    page.add(page_col)


ft.app(main)