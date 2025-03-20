from flask import Flask

HOST = "0.0.0.0"
PORT = 5151

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello jupiter"


def main() -> None:
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
