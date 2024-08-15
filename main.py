from aplications import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host="10.10.3.212", port=5050, debug=True)
