import os
from dotenv import load_dotenv
from src.controller.generateBankHours import generate_bank_hours
from src.controller.generateDataForPandas import generate_data_for_pandas

load_dotenv()

if __name__ == '__main__':
    FOLDER = os.getenv('FOLDER_POINTS')
    data = generate_bank_hours(FOLDER)
    dfs, timer = generate_data_for_pandas(data)
    print(timer)