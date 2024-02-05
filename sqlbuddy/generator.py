import re
from sqlbuddy.gpt import GPT
from sqlbuddy.constants import SQL_KEYWORDS  


class Generator:
    """
    This class is responsible for generating SQL statements based on the given prompt.
    It uses OpenAI's GPT-3.5 turbo model to generate text and then processes it into
    a valid SQL statement.
    Attributes:
    generator: GPT
        An instance of the GPT class that is used to generate text.
    SQL_KEYWORD: list
        A list of keywords from which the generated code will be selected as an SQL keyword.
    Methods:
    auto_complete(prompt: str) -> str:
        Generate text based on the given prompt. Then, select words from this text that are SQL keywords.
        Finally, formulate a complete SQL query using these keywords.
    extract_sql_statement(input_string: str) -> str:
        Extract SQL statement only from provided text.
    format_sql_statement(sql_statement: str) -> str:
        Add missing spaces around operators and brackets in the provided SQL code. Also, remove any unnecessary spaces.
        Format the generated SQL code by adding missing spaces or brackets where necessary.
    """
    def __init__(self):
        self.generator = GPT()
        self.SQL_KEYWORD = SQL_KEYWORDS

    def auto_complete(self, prompt: str):
        """
        Generate SQL statement based on the given prompt
        Args:
        prompt: str
            The prompt to generate the SQL statement from GPT
        Returns:
        str: The generated SQL statement
        """
        sql_statement = self.generator.generate_query(prompt)
        print(sql_statement, ';gggggggggggggggggggggggggggg')
        if sql_statement and sql_statement != '':
            extracted_query = self.extract_sql_statement(sql_statement)
            if extracted_query:
                return self.format_sql_statement(extracted_query)
            else:
                return None
        else:
            return None
    
    def extract_sql_statement(self, input_string: str):
        """
        Extracts the SQL statement from the input string
        Args:
        input_string: str
            The input string to extract the SQL statement from
        Returns:
        str: The extracted SQL statement
        """
        sql_pattern = r'\bSELECT\b.*?\bFROM\b.*?;'
        matches = re.search(sql_pattern, input_string, re.IGNORECASE)
        if matches:
            sql_statement = matches.group(0)
            return sql_statement
        else:
            return None
    
    def format_sql_statement(self, sql_statement: str):
        final_statement = None
        """
        Formats the SQL statement
        Args:
        sql_statement: str
            The SQL statement to format
        Returns:
        str: The formatted SQL statement
        """
        if sql_statement is None:
            return None
        formatted_statement = sql_statement.replace('\n', '').replace('\t', '')
        words = formatted_statement.split(' ')
        formatted_words = [word.upper() if word.lower() in self.SQL_KEYWORD else word for word in words]
        final_statement = ' '.join(formatted_words)
        if not ';' in final_statement:
            final_statement += ';'
        print(final_statement, 'ffffffffffffffffffffff')
        return final_statement

