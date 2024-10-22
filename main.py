from dash import Dash
from app.layout import create_layout  # Updated import
from app.callbacks import register_callbacks  # Updated import

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = 'Finance Dashboard'
app.layout = create_layout()

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(port=8040, debug=True)  # Change the port if needed
