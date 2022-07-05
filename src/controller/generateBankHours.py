from src.controller.listFiles import get_list_itens
from src.helpers.orderPoints import order_times_by_month
from src.helpers.calculateHours import generate_banktime

def generate_bank_hours(folder):
    result_list = get_list_itens(folder)
    result_order = order_times_by_month(result_list)
    bank_hours = generate_banktime(result_order)
    return bank_hours