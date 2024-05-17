# SQL Injection Demo App
This app is built using Flask and demonstrates a simple SQL Injection vulnerability. The app has a form where a user can input their name and search for blog posts. However, the search query is not sanitized and thus is vulnerable to SQL injection attacks.

### Instructions
1. Clone the app from the GitHub repository:

```git clone https://github.com/KetanKochhar/vulsite```<br>
3. Navigate to the app directory:

```cd sql-injection-demo-app```<br>
4. Install the required dependencies:

```pip install -r requirements.txt```<br>
5. Start the app:

```python app.py```<br>
6. Open your web browser and visit http://localhost/

7. You can now interact with the app 

### Conclusion
This simple Flask app demonstrates how easy it is to create a SQL Injection vulnerability by not sanitizing user input. To protect against SQL injection attacks, always sanitize user input and consider using libraries like SQLAlchemy for safer database interactions.
Remember to replace the username with your actual GitHub username and the repository name with the actual name of your repository.Here is an example MD file for your Flask app demonstrating SQL Injection vulnerability:

This app is built using Flask and demonstrates a simple SQL Injection vulnerability. The app has a form where a user can input their name and search for blog posts. However, the search query is not sanitized and thus is vulnerable to SQL injection attacks.
