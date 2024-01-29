import flet as ft
#TODO переписать все нахрен

def main(page: ft.Page):
    page.window_bgcolor = 'images/img.png'
    page.bgcolor = ft.colors.BLACK

    page.title = "Счетчик бойцов"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="center", text_size=50, width=100, color='red')

    page.title = "Счетчик очков"
    page.vertical_alignment = ft.MainAxisAlignment.NONE

    txt_number2 = ft.TextField(value="0", text_align="center", text_size=50, width=100, color='blue')

    def minus_click_1(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click_1(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.Icon(name=ft.icons.MAN_2, color=ft.colors.RED, size=30),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_1, icon_color='red'),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_1, icon_color="red"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    def minus_click_2(e):
        txt_number2.value = str(int(txt_number2.value) - 1)
        page.update()

    def plus_click_2(e):
        txt_number2.value = str(int(txt_number2.value) + 1)
        page.update()


    page.add(
        ft.Row(
            [
                ft.Icon(name=ft.icons.MAN_2, color=ft.colors.BLUE, size=30),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_2, icon_color='blue'),
                txt_number2,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_2, icon_color='blue')

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
