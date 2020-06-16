# -*- coding: utf-8 -*-
# Counting expectation of gambling at https://www.wedefi.com/earn/safebet


def show_expectation_info(winning_hash, prize, tl_days, roi=19, ticket_price=10):
    # Leading zeroes
    i = 0
    leading_zeroes = 0
    while winning_hash[i] == '0':
        leading_zeroes += 1
        i += 1

    # probability to get smaller hash
    p_win = (int(winning_hash[leading_zeroes], 16) / 16)
    if leading_zeroes:
        p_win *= (1/16)**leading_zeroes

    risk_to_lose = ticket_price * tl_days * roi/365 * 0.01
    p_loose = 1 - p_win
    expectation = p_win * prize - p_loose*risk_to_lose

    print("__________________________________________________________________________________")
    print("Current price   = %s" % prize)
    print("Current winner  = %s" % winning_hash)
    print("Leading zeroes  = %s" % leading_zeroes)
    print("Win probability = {0:.6}".format(p_win))
    print("Risk to lose    = {0:.2}".format(risk_to_lose))
    print("Expectation     = {0:.2}".format(expectation))
    if expectation < 0:
        print("DON'T BET THIS GAME!")
    print()


show_expectation_info(winning_hash="05a8c4264518b953925963cb5519c721059b4f0ad4371ec191dec51000783b5d",
                      prize=100, tl_days=60)
show_expectation_info(winning_hash="000bb6564518b953925963cb5519c721059b4f0ad4371ec191dec51000783b5d",
                      prize=233, tl_days=75)
