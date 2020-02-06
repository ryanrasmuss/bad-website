from mysite import *

if __name__ == "__main__":
    app.secret_key = 'slyther1n'
    login_manager.init_app(app)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()