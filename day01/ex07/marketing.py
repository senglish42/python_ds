import sys


def clients_list():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return clients


def participants_list():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return participants


def recipients_list():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return recipients


def list_to_set(lst):
    return set(lst)


def all_users(clients_set, participants_set):
    return clients_set.union(participants_set)


def call_to_users_list(clients, participants, recipients):
    users_set = all_users(list_to_set(clients), list_to_set(participants))
    recipients_set = list_to_set(recipients)
    not_seen_promo_users = users_set.difference(recipients_set)
    not_seen_promo_users_list = list(not_seen_promo_users)
    return not_seen_promo_users_list


def call_center(lst):
    print(lst)


def potential_clients_list(clients, participants):
    clients_set = list_to_set(clients)
    users_set = all_users(clients_set, list_to_set(participants))
    return list(users_set ^ clients_set)


def not_participated_clients_list(clients, participants):
    clients_set = list_to_set(clients)
    participants_set = list_to_set(participants)
    clients_not_participants_set = clients_set - participants_set
    return list(clients_not_participants_set)


def run():
    if len(sys.argv) != 2:
        exit(1)
    if sys.argv[1] == 'call_center':
        lst = call_to_users_list(clients_list(), participants_list(), recipients_list())
        call_center(lst)
    elif sys.argv[1] == 'potential_clients':
        lst = potential_clients_list(clients_list(), participants_list())
        print(lst)
    elif sys.argv[1] == 'loyalty_program':
        lst = not_participated_clients_list(clients_list(), participants_list())
        print(lst)
    else:
        raise Exception("Wrong argument name is given")


if __name__ == '__main__':
    run()
