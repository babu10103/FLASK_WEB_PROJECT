from website import create_app

app = create_app()

""" 
 meaning of 
 if __name__ == '__main__': 
 is, only if we run main.py not if we import main.py
 we are going to execute code in that conditional block
"""
if __name__ == '__main__' :
    """
    debug=True means, anytime we make any change to our python
    code, this check will automatically rerun the web server
    """
    app.run(debug=True)
