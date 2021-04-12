from app.application import app
from app.views.index import bp_index

# ルーティング
app.register_blueprint(bp_index)