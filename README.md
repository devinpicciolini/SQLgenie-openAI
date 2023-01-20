## OpenAI SQL Query Generator

This code allows you to use the OpenAI API to generate SQL queries based on a user's prompt and the structure of a table in a CSV file. The code uses the Pandas library to read and convert the data to a DataFrame.

### Getting Started

1. Clone the repository: 
git clone https://github.com/devinpicciolini/SQLgenie-openAI.git

Copy code

2. Install the required dependencies: 
pip install -r requirements.txt

Copy code

3. Replace the `openai.api_key` value in the code with your OpenAI API key.

4. Run the script by executing the following command in your terminal:
python openai_query_generator.py

Copy code

5. Enter the file path of the CSV file when prompted.

6. Enter your query prompt when prompted. The script will continue to prompt for queries until you exit the script.

7. The generated query will be displayed on the terminal.

### Security

- Remove any hardcoded sensitive information from the code, such as credentials or API keys.

- Use encryption for sensitive information, such as user credentials.

- Make sure to keep all dependencies and libraries up to date to ensure that any known vulnerabilities are patched.

### Built With

- [OpenAI](https://openai.com/) - The AI platform used
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis library for Python

### Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Create a new Pull Request

### Author

- [Devin Picciolini](https://github.com/devinpicciolini)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Acknowledgments

- Hat tip to anyone who's code was used
- Inspiration
- etc
