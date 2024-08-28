from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    content = """
    <html>
        <head>
            <title>Welcome to My Blog</title>
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
                    padding: 15px 20px;
                    text-align: center;
                    font-size: 2em;
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
                    padding: 25px;
                    border-radius: 8px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
                }
                footer {
                    background-color: #333;
                    color: #fff;
                    text-align: center;
                    padding: 15px;
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
                <h1>Welcome to My Blog!</h1>
            </header>
            <div class="container">
                <div class="content">
                    <h2>About This Blog</h2>
                    <p>Hi there! I'm thrilled to have you here. This blog is a place where I pour out my thoughts, share my experiences, and delve into various intriguing topics that I’m passionate about. Whether it's a deep dive into tech trends, personal anecdotes, or just musings on life, you’ll find it here.</p>
                    <p>Stay tuned and feel free to <a href="#">subscribe</a> for the latest updates. Your support means the world to me!</p>
                </div>
            </div>
            <footer>
                <p>&copy; 2024 CLAUSS sANTIE. All rights reserved. Designed .</p>
            </footer>
        </body>
    </html>
    """
    return HttpResponse(content)
