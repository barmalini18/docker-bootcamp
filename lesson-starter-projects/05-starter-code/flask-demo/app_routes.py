def configure_routes(app):
    @app.route('/')
    def hello():
        return ("<pre>"
                "    ____        _   _                  _    \n"
                "   |  _ \\ _   _| |_| |__   ___  _ __  / \\   \n"
                "   | |_) | | | | __| '_ \\ / _ \\| '_ \\/  /   \n"
                "   |  __/| |_| | |_| | | | (_) | | | /\\_/    \n"
                "   |_|    \\__, |\\__|_| |_|\\___/|_| |_(_)    \n"
                "          |___/                             \n"
                "\n"
                "             -- Python --                   "
                "</pre>")
    
    @app.route('/fuck')
    def fuck():
        return ("<pre>"
                "    ____        _   _                  _    \n"
                "   |  _ \\ _   _| |_| |__   ___  _ __  / \\   \n"
                "   | |_) | | | | __| '_ \\ / _ \\| '_ \\/  /   \n"
                "   |  __/| |_| | |_| | | | (_) | | | /\\_/    \n"
                "   |_|    \\__, |\\__|_| |_|\\___/|_| |_(_)    \n"
                "          |___/                             \n"
                "\n"
                "             -- Python Fuck --                   "
                "</pre>")