import flet as ft

def main(page: ft.Page):

    # タイトル
    page.title = 'パスワード生成'
    title = ft.Text("パスワード生成", size=40)

    # 文字種類選択
    uppercase_alphabet = ft.Checkbox(label="英大文字")
    lowercase_alphabet = ft.Checkbox(label="英小文字")
    number = ft.Checkbox(label="数字")
    symbol = ft.Checkbox(label="記号")
    charset = ft.Row(
        [uppercase_alphabet, lowercase_alphabet, number, symbol],
    )

    # パスワードの表示エリア
    password_area = ft.TextField(read_only=True, label="パスワード")

    # パスワードの長さを決めるスライダー
    password_length = ft.Slider(min=8, max=64, value=8)
    length_text = ft.Text(value=str(int(password_length.value)))  # 初期値を設定
    length_row = ft.Row(
        [ft.Text("パスワードの長さ"), password_length, length_text],
    )

    # パスワードの強さ表示
    strength_container = ft.Container(bgcolor=ft.colors.GREEN, width=100, height=20)
    strength_label = ft.Text(value="強い")
    strength_row = ft.Row([strength_container, strength_label])
    estimated_time_label = ft.Text()

    # パスワード生成ボタン
    generate_button = ft.ElevatedButton(text="生成")

    # スライダーの実装
    def slider_changed(e):
        length_text.value = str(int(e.control.value))
        page.update() # 画面を更新して変更を反映

    password_length.on_change = slider_changed # イベントハンドラを登録

    # レイアウト
    page.add(
        title,
        charset,
        password_area,
        length_row,
        strength_row,
        estimated_time_label,
        generate_button,
        
    )

ft.app(target=main)