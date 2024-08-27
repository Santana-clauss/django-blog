from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    content = """
    <html>
        <head>
            <title>My Blog</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }
                header {
                    background-color: #333;
                    color: #fff;
                    padding: 10px 20px;
                    text-align: center;
                }
                .container {
                    width: 80%;
                    margin: auto;
                    overflow: hidden;
                }
                h1 {
                    margin-top: 0;
                }
                .content {
                    background: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                footer {
                    background-color: #333;
                    color: #fff;
                    text-align: center;
                    padding: 10px;
                    position: fixed;
                    width: 100%;
                    bottom: 0;
                }
                a {
                    color: #3498db;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Welcome to My Blog</h1>
            </header>
            <div class="container">
                <div class="content">
                    <h2>About This Blog</h2>
                    <p>This is the homepage of my blog where I share my thoughts, experiences, and insights on various topics.</p>
                    <p>Feel free to explore and <a href="#">subscribe</a> for updates!</p>
                </div>
            </div>
            <footer>
                <p>&copy; 2024 My Blog. All rights reserved.</p>
            </footer>
        </body>
    </html>
    """
    return HttpResponse(content)
