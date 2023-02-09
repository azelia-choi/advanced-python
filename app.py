import os

from dash import Dash, dcc, html

from callbacks import get_callbacks
from utils import MBTI

app = Dash(__name__)


def user_controls():
    return html.Div(
        [
            html.Div(
                [
                    html.Label("이름"),
                    dcc.Input(placeholder="아무개", type="text", id="name-input"),
                    html.Label("나이"),
                    dcc.Input(placeholder="20", type="number", id="age-input"),
                    html.Label("MBTI"),
                    dcc.Dropdown(options=MBTI, id="mbti-input"),
                    html.Label("아바타 재생성"),
                    html.Button("재생성", id="avatar-button", style={"font-size": "16px"}),
                ],
                className="row",
            ),
        ],
        className="three columns div-user-controls",
    )

def profile():
    return html.Div(
        [
            html.Div([
                html.H2("Profile", styles = {"font-size":"36px"}),
                html.Div([
                    html.H2("name"),
                    html.H2("age")
                ]),
                html.Img()
            ]),
            dcc.Graph()
            
        ],
        className="nine columns bg-grey",
        style={
            "display": "flex",
            "flex-direction": "column",
            "flex-grow": 1,
        },
    )


app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                user_controls(),
                profile(),
            ],
        )
    ]
)

get_callbacks(app)

# Remove all svg files is assets folder
for file in os.listdir("assets"):
    if file.endswith(".svg"):
        os.remove(os.path.join("assets", file))


if __name__ == "__main__":
    app.run_server(debug=True)
