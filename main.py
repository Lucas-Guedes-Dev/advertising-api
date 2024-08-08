from aplications import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host="10.10.1.213", port=5050, debug=True)
