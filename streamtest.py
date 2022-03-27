import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_team(code):
    for team in teams:
        if team[0] == str(code):
            return team

def sim(team1, team2, graph=True):
    gfor1 = []
    gvs1 = []
    gfor2 = []
    gvs2 = []

    wins1 = 0
    wins2 = 0
    ties = 0
    total = 0

    for i in range(2, len(team1)):
        weight = 1
        gf, gv, opp = team1[i]
        if opp == team2[0]:
            weight += 6
        if team1[i] in team1[-5:]:
            weight += 3
        for i in range(weight):
            gfor1.append(gf)
            gvs1.append(gv)
    for i in range(2, len(team2)):
        weight = 1
        gf, gv, opp = team2[i]
        if opp == team1[0]:
            weight += 6
        if team2[i] in team2[-5:]:
            weight += 3
        for i in range(weight):
            gfor2.append(gf)
            gvs2.append(gv)

    goals1 = np.random.normal(np.mean(gfor1 + gvs2), np.std(gfor1 + gvs2), simnum)
    goals2 = np.random.normal(np.mean(gfor2 + gvs1), np.std(gfor2 + gvs1), simnum)

    maxgoals = max(goals1 + goals2)

    for i in range(2, len(team1)):
        if int(goals1[i]) > int(goals2[i]):
            wins1 += 1
        elif int(goals1[i]) < int(goals2[i]):
            wins2 += 1
        else:
            ties += 1
        total += 1
    f = '{} - {}% \n{} - {}% \nTies - {}%'
    # print(wins1, '-', wins2, '-', ties)
    st.write(f.format(team1[1], round((wins1/total)*100, 1), team2[1], round((wins2/total)*100, 1), round((ties/total)*100), 1))
    if graph == True:
        fig = plt.figure(figsize=(maxgoals, maxgoals))
        plt.scatter(goals1, goals2)
        plt.xlim(0, int(maxgoals * 0.75))
        plt.ylim(0, int(maxgoals * 0.75))
        plt.title('Score Outcomes')
        plt.xlabel(team1[1])
        plt.ylabel(team2[1])
        plt.plot([0, maxgoals], [0, maxgoals], "-r")
        st.pyplot(fig)

simnum = 100000

pp = ['pp', 'Piedmont', (2, 4, 'lf'), (2, 5, 'lf'), (12, 2, 'bd'), (6, 1, 'jr'), (3, 1, 'jt'), (4, 1, 'jr'), (2, 7, 'lf'), (5, 8, 'bd'), (0, 5, 'bj'), (1, 3, 'ib'), (0, 8, 'sc'), (2, 1, 'st'), (11, 2, 'rr'), (1, 3, 'tc'), (3, 1, 'lp'), (4, 7, 'sh'), (3, 1, 'lv'), (4, 3, 'sh'), (5, 2, 'lp'), (3, 4, 'tc'), (4, 4, 'bd'), (10, 0, 'cc'), (1, 2, 'ny'), (1, 4, 'rs'), (6, 4, 'jt'), (7, 2, 'rr'), (4, 3, 'rs'), (0, 5, 'jf'), (4, 4, 'pb'), (1, 3, 'lp'), (2, 3, 'pb'), (4, 3, 'tc'), (8, 2, 'lv'), (5, 3, 'bd'), (5, 1, 'rr'), (5, 7, 'ny'), (10, 1, 'cc'), (7, 2, 'bd'), (4, 1, 'rr'), (3, 0, 'cc'), (1, 1, 'jf'), (2, 9, 'lf'), (5, 2, 'pb'), (7, 0, 'cc'), (5, 2, 'pb'), (8, 2, 'rr'), (3, 5, 'tc'), (7, 1, 'bd'), (5, 2, 'rr'), (3, 2, 'tc'), (0, 3, 'gs'), (1, 1, 'hb'), (0, 5, 'ch'), (2, 2, 'pr'), (6, 0, 'bd'), (3, 1, 'tc'), (5, 2, 'tc'), (5, 2, 'fl')]
tc = ['tc', 'Tri City', (2, 1, 'jr'), (3, 0, 'lv'), (3, 1, 'lp'), (5, 2, 'pb'), (3, 1, 'lp'), (2, 0, 'ny'), (11, 2, 'jt'), (3, 2, 'sh'), (4, 1, 'sh'), (7, 2, 'rr'), (5, 5, 'rr'), (2, 1, 'jr'), (2, 0, 'jf'), (4, 1, 'bd'), (3, 1, 'pp'), (7, 0, 'lp'), (6, 2, 'rr'), (7, 2, 'jr'), (4, 3, 'pp'), (6, 2, 'bd'), (2, 0, 'rs'), (1, 2, 'pb'), (6, 0, 'cc'), (5, 1, 'rs'), (3, 4, 'pp'), (8, 4, 'ie'), (6, 2, 'bd'), (4, 0, 'lv'), (0, 1, 'lf'), (2, 3, 'ny'), (9, 0, 'rr'), (5, 1, 'lp'), (0, 3, 'lf'), (1, 3, 'ie'), (1, 3, 'sd'), (1, 2, 'yd'), (0, 1, 'jf'), (1, 7, 'jf'), (3, 1, 'lv'), (5, 1, 'bd'), (1, 3, 'pb'), (11, 1, 'cc'), (5, 3, 'pp'), (14, 0, 'rr'), (6, 0, 'bd'), (2, 3, 'pp'), (2, 0, 'cc'), (4, 0, 'cc'), (7, 4, 'rr'), (1, 0, 'pc'), (1, 2, 'lf'), (1, 3, 'pp'), (2, 5, 'pp'), (1, 7, 'np')]
bd = ['bd', 'Montgomery', (2, 12, 'pp'), (1, 5, 'hh'), (8, 5, 'pp'), (4, 5, 'fl'), (2, 7, 'rm'), (3, 3, 'ri'), (3, 3, 'ec'), (1, 4, 'tc'), (0, 2, 'rr'), (4, 4, 'pp'), (2, 6, 'tc'), (6, 0, 'cc'), (6, 0, 'rr'), (2, 6, 'tc'), (3, 5, 'pp'), (1, 1, 'cc'), (3, 1, 'rr'), (2, 7, 'pp'), (3, 2, 'cc'), (5, 1, 'cc'), (1, 5, 'tc'), (6, 6, 'rr'), (1, 7, 'pp'), (0, 6, 'tc'), (0, 6, 'pp')]
rr = ['rr', 'Reston', (2, 7, 'tc'), (5, 5, 'tc'), (2, 11, 'pp'), (2, 0, 'bd'), (2, 6, 'tc'), (0, 10, 'sd'), (2, 3, 'ss'), (3, 12, 'sl'), (0, 5, 'rs'), (2, 7, 'pp'), (0, 6, 'bd'), (1, 9, 'ie'), (4, 1, 'cc'), (2, 7, 'pp'), (0, 9, 'tc'), (1, 3, 'bd'), (3, 2, 'cc'), (1, 4, 'pp'), (4, 4, 'cc'), (1, 1, 'cc'), (6, 6, 'bd'), (2, 8, 'pp'), (0, 14, 'tc'), (2, 5, 'pp'), (1, 2, 'lk'), (1, 0, 'ce'), (1, 4, 'pw'), (4, 7, 'tc')]
cc = ['cc', 'Chevy Chase', (0, 10, 'pp'), (0, 6, 'bd'), (0, 6, 'tc'), (1, 4, 'rr'), (1, 1, 'bd'), (1, 10, 'cc'), (2, 3, 'rr'), (2, 3, 'bd'), (4, 4, 'rr'), (0, 3, 'pp'), (1, 5, 'bd'), (1, 1, 'rr'), (0, 7, 'pp'), (1, 11, 'tc'), (0, 2, 'tc'), (0, 4, 'tc')]

teams = [pp, tc, bd, rr, cc]

st.title("Game Odds")

option1 = st.selectbox(
    'Select a team',
    (' ', 'Piedmont', 'Tri City', 'Montgomery', 'Reston', 'Chevy Chase'))

option2 = st.selectbox(
    'Select a team',
    ('', 'Piedmont', 'Tri City', 'Montgomery', 'Reston', 'Chevy Chase'))

team1 = get_team(option1)
team2 = get_team(option2)

try:
    sim(team1, team2)
except:
    pass
