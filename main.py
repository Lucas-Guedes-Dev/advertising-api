from aplications import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host="192.168.0.84", port=5050, debug=True)
