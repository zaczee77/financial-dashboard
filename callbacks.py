import random
from dash import Input, Output, html

def register_callbacks(app):
    # Callback for Quantitative Analysis graph
    @app.callback(
        Output('quant-analysis-graph', 'figure'),
        Input('interval-component', 'n_intervals')
    )
    def update_quant_analysis(n):
        return {
            'data': [{'x': list(range(10)), 'y': [random.randint(0, 100) for _ in range(10)]}],
            'layout': {'title': 'Quantitative Analysis'}
        }

    # Callback for Real-time News feed
    @app.callback(
        Output('news-feed', 'children'),
        Input('interval-component', 'n_intervals')
    )
    def update_news_feed(n):
        return [
            html.P(f"News article {i}: Some interesting headline {random.randint(1, 100)}")
            for i in range(5)
        ]

    # Callback for Stock Calculator
    @app.callback(
        [Output('calculation-result', 'children'),
         Output('hold-sell-decision', 'children')],
        [Input('calculate-button', 'n_clicks')],
        [Input('stock-input', 'value'), Input('quantity-input', 'value')]
    )
    def calculate_stock_value(n_clicks, stock, quantity):
        if stock and quantity:
            stock_price = random.uniform(100, 500)
            total_value = stock_price * quantity
            decision = "Hold" if random.choice([True, False]) else "Sell"
            return f'Total Value of {stock}: ${total_value:.2f}', decision
        return "Enter stock and quantity", ""
