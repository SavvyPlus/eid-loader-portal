from web_app.app import create_app
from web_app import config


if __name__ == '__main__':
    app = create_app(config.DevelopmentConfig)

    # @app.route("/", methods=["GET", "POST"])
    # def index():
    #     return "Hello World!"

    app.run(host='0.0.0.0', port=5000, debug=True)
