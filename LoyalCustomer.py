from collections import defaultdict

# Paso 1: Cargar los datos de los logs
def load_logs(file_path):
    logs = defaultdict(set)
    with open(file_path, 'r') as file:
        for line in file:
            _, page_id, customer_id = line.strip().split(',')
            logs[customer_id].add(page_id)
    return logs


def find_loyal_customers(logs_day1, logs_day2):
    loyal_customers = []    
    # Solution with O(n) complexity
    # common_customers = set(logs_day1.keys()) & set(logs_day2.keys())
    # print("Common Customers:", common_customers)
    # print(logs_day1.keys())

    # HashMap con los clientes logs_days1
    for customer_id, page_id in logs_day1.items():
        logs_day1[customer_id] = set(page_id)

    for customer_id, page_id in logs_day2.items():
        print("Log_day2",customer_id)
        if customer_id in logs_day1:
            print("Log_day1",customer_id)
            unique_pages_day1 = logs_day1[customer_id]
            print(unique_pages_day1)
            unique_pages_day2 = set(page_id)
            print(unique_pages_day2)

            if len(unique_pages_day1) >= 2 and len(unique_pages_day2) >= 2:
                loyal_customers.append(customer_id)


    # for customer in common_customers:
    #     unique_pages_day1 = logs_day1[customer]
    #     unique_pages_day2 = logs_day2[customer]

    #     if len(unique_pages_day1) >= 2 and len(unique_pages_day2) >= 2:
    #         loyal_customers.append(customer)

    # Paso 5: Resultado
    return loyal_customers

# Paso 2: Leer los logs del día 1 y día 2
logs_day1 = load_logs('log_day1.txt')
logs_day2 = load_logs('log_day2.txt')

# Paso 6: Llamar a la función para obtener los clientes leales
loyal_customers = find_loyal_customers(logs_day1, logs_day2)

# Paso 7: Resultado
print("Loyal Customers:", loyal_customers)