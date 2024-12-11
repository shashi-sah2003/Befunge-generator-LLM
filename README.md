
## Demo video

[![Demo Video](https://img.youtube.com/vi/gG_97zVAWOE/0.jpg)](https://youtu.be/gG_97zVAWOE)

## Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/Befunge-generator-LLM.git
    cd Befunge-generator-LLM
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set the Groq API Key**:
    - Create a `.env` file in the project root directory and add your Groq API key:
        ```plaintext
        GROQ_API_KEY=your_actual_groq_api_key
        ```

## Usage

1. **Prepare the Expected Output**:
    - Create a text file (e.g., `expected_output.txt`) containing the desired output. For example:
        ```plaintext
        Hello World!
        ```

2. **Run the Generator Script**:
    - Open your terminal or Command Prompt.       
    - Navigate to your project directory
    - Execute the script:
        ```sh
        python befunge.py expected_output.txt generated_befunge_code.txt
        ```
## Sample Output
    - expected_output.txt = Hello guys how are you doing!
    - generated_befunge_code.txt - "!gniod uoy era woh syug olleH">:#,_@