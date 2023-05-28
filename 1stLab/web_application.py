from flask import Flask, request

from solutions.fixed_solution import FixedSolution

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main_page():
    tipabackend = FixedSolution()
    if request.method == 'POST':
        coins = list(map(int, request.form['coins'].split()))
        return str(tipabackend.coinChange(coins, int(request.form['amount'])))
    return f"<html> <head><title>Minimal coins</title></head>" \
           f"<body><h1>Заданная сумма из минимального количества монет</h1>" \
           f"<form action='/' method='POST'>" \
           f"<label id='coinslabel'><input id='coinsinput' type='text' name='coins'> Достоинства монет через пробел</label>" \
           f"<label id='amountlabel'><input id='amountinput' type='text' name='amount'> Нужная сумма</label>" \
           f"<button id='send' 'type='submit'>Отправить</button> <form>" \
           f"<div></div></body></html>"
