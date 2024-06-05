def candlesoff(candle):
    if candle in candles:
        coff.append(candle)
        candles.remove(candle)
    else:
        candles.append(candle)
        coff.remove(candle)
if __name__=="__main__":
    candles = []
    coff=[i for i in range(101)]
    for person in range(1,101):
        for candle in range(0,101,person):
            candlesoff(candle)
    print(coff)
    print(candles)

#Задача-загадка:В комнате стоят сто не зажённых свечей.Снаружи комнаты стоят столько же людей.Каждый заходящий человек зажигает или тушит свечку
#(в зависимости от того потушена она или нет) по своему номеру. Т.е. Первый человек зажжёт(потушит) каждую первую, второй каждую вторую
# person - номер человека. candle - Номер свечки. coff и candles - массивы для потушенных или зажённых свечей.
