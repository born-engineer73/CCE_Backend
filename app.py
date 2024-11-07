from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client, Client
import os

app = Flask(__name__)
app.secret_key = "a2xFh9$5%@29Q!"  # Replace with a secure random string

# Supabase credentials
SUPABASE_URL = "https://iltjvjetnlsrmhbetfmm.supabase.co"  # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlsdGp2amV0bmxzcm1oYmV0Zm1tIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA4Njg0MzksImV4cCI6MjA0NjQ0NDQzOX0.v0fG5hVnqPy61vphT6KqM0tZrJzII96Gi_x6mu6_3NM"  # Replace with your Supabase API Key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    # Render the HTML form for data entry
    return render_template('index.html')

@app.route('/add_news', methods=['POST'])
def add_news():
    # Capture form data
    news = request.form['news']
    link = request.form['link']

    # Insert data into the Supabase table
    response = supabase.table('news_links').insert({
        "news": news,
        "link": link
    }).execute()

    if response.data:
        flash("News entry added successfully!", "success")
    else:
        flash(f"Failed to add news entry. Error: {response.error}", "error")

    return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Use Railway's port if available
    app.run(host="0.0.0.0", port=port)
