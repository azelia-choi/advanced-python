import plotly.express as px
from dash.dependencies import Input, Output
from plotly import graph_objects as go

from utils import MBTI, random_avatar


def get_callbacks(app):
    @app.callback(
        Output("avatar", "src"),
        Input("avatar-button", "n_clicks"),
    )
    def update_avatar(clicks):
        return random_avatar()

    @app.callback(
        Output("pie-chart", "figure"),
        Input("mbti-input", "value"),
    )
    def update_pie_chart(mbti):
        color = px.colors.diverging.RdBu
        if mbti:
            color = ["rgb(178,24,43)" if mbti == m else "#323130" for m in MBTI]

        pie_chart = go.Figure(
            [
                go.Pie(
                    values=[1] * 16,
                    labels=MBTI,
                    hole=0.6,
                    textinfo="label",
                    marker=dict(colors=color),
                    hoverinfo="label",
                    textfont=dict(size=20),
                )
            ]
        )

        pie_chart.update_layout(
            margin=dict(t=0, l=0, r=0, b=0),
            paper_bgcolor="#323130",
            plot_bgcolor="#323130",
            showlegend=False,
        )
        return pie_chart

    @app.callback(
        Output("name", "children"),
        Input("name-input", "value"),
    )
    def update_name(name):
        return f"이름: {name}" if name else "이름: "

    @app.callback(
        Output("age", "children"),
        Input("age-input", "value"),
    )
    def update_age(age):
        return f"나이: {age}" if age else "나이: "

    @app.callback(
        Output("mbti-input", "value"),
        Input("pie-chart", "clickData"),
    )
    def update_mbti_input_from_pie_chart(mbti):
        if mbti:
            return mbti["points"][0]["label"]
        return None
