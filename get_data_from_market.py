import market_actions as ma


def get_volume_pos(coin_prices: dict, volume_pos: int) -> dict:
    """
    Получаем размер позиции для данной монеты из расчета размера депозита на данный момент
    """
    coin_vol_pos = {coin_price: volume_pos * ma.get_deposit_size() / coin_price for coin_price in coin_prices}
    # TODO исправить захардкоженный вариант после отработки работоспособности других функций
    coin_vol_pos = {'BLZUSDT': 0.01, 'XRPUSDT': 0.01}  # TODO вручную скорректировать в момент тестирования
    return coin_vol_pos


def coins_prices(coins):
    a = {}
    b = ma.query_new_prices()
    for coin in coins:
        a[coin] = b[coin]
    return a


def all_coins_prices():
    a = {}
    b = ma.query_new_prices()
    for coin in b:
        a[coin] = b[coin]
    return a


def get_data(coins):
    d = {}
    for coin in coins:
        data = ma.get_klines(coin)
        d[coin] = data
    return d


if __name__ == '__main__':
    # входящие данные ['BTCUSDT', 'ETHUSDT', 'LTCUSDT']
    # результат {'BTCUSDT': [[время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6],
    #                       [время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6],
    #                       [время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6]],
    #           'ETHUSDT': [[время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6],
    #                       [время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6],
    #                       [время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6]],
    #           'LTCUSDT': [[время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6],
    #                       [время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6],
    #                        [время входа, цена открытия, максимум свечи, минимум свечи, цена закрытия, объем, и еще 6]]}
    print(get_data(['1000PEPEUSDT', 'WLDUSDT']))

    # входящие данные ['BTCUSDT', 'ETHUSDT', 'LTCUSDT']
    # результат {'BTCUSDT': 67282.0, 'ETHUSDT': 3568.53, 'LTCUSDT': 85.68}
    # print(coins_prices(['BTCUSDT', 'ETHUSDT', 'LTCUSDT']))

    # входящие данные пустые
    # результат все цены в USDT {'BTCUSDT': 67282.0, 'ETHUSDT': 3568.53, 'LTCUSDT': 85.68}
    # print(all_coins_prices())

"""
m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
[{'symbol': 'KNCUSDT', 'price': '0.72480', 'time': 1703425210607},
{'symbol': 'LOOMUSDT', 'price': '0.1111000', 'time': 1703425202236}, 
{'symbol': 'MINAUSDT', 'price': '1.1383000', 'time': 1703425217269}, 
{'symbol': 'BCHUSDT', 'price': '231.18', 'time': 1703425217894}, 
{'symbol': 'ARPAUSDT', 'price': '0.05598', 'time': 1703425217876}, 
{'symbol': 'RLCUSDT', 'price': '1.7072', 'time': 1703425215320}, 
{'symbol': 'MANAUSDT', 'price': '0.5176', 'time': 1703425218523}, 
{'symbol': 'STPTUSDT', 'price': '0.0638400', 'time': 1703425210558}, 
{'symbol': 'TUSDT', 'price': '0.0260700', 'time': 1703425176115}, 
{'symbol': '1000SATSUSDT', 'price': '0.0006391', 'time': 1703425215929}, 
{'symbol': 'AVAXUSDT', 'price': '47.7470', 'time': 1703425218385}, 
{'symbol': '1000RATSUSDT', 'price': '0.3255000', 'time': 1703425216563}, 
{'symbol': 'SKLUSDT', 'price': '0.05448', 'time': 1703425217995}, 
{'symbol': 'SPELLUSDT', 'price': '0.0007007', 'time': 1703425215438}, 
{'symbol': 'BLUEBIRDUSDT', 'price': '8.04800', 'time': 1703425144621}, 
{'symbol': 'CTKUSDT', 'price': '0.84240', 'time': 1703425211077}, 
{'symbol': 'KSMUSDT', 'price': '55.100', 'time': 1703425217988}, 
{'symbol': 'OGNUSDT', 'price': '0.1549', 'time': 1703425211062}, 
{'symbol': 'JASMYUSDT', 'price': '0.006625', 'time': 1703425217994}, 
{'symbol': 'BICOUSDT', 'price': '0.4687000', 'time': 1703425218746}, 
{'symbol': 'ACHUSDT', 'price': '0.0227500', 'time': 1703425210747}, 
{'symbol': 'AUDIOUSDT', 'price': '0.2402', 'time': 1703425197025}, 
{'symbol': 'USTCUSDT', 'price': '0.0358100', 'time': 1703425218047}, 
{'symbol': 'TOMOUSDT', 'price': '1.2792', 'time': 1699952397314}, 
{'symbol': 'DODOXUSDT', 'price': '0.1980200', 'time': 1703425218569}, 
{'symbol': 'BELUSDT', 'price': '0.74150', 'time': 1703425215366}, 
{'symbol': 'ALICEUSDT', 'price': '1.498', 'time': 1703425209698}, 
{'symbol': 'KEYUSDT', 'price': '0.0057880', 'time': 1703425218034}, 
{'symbol': '1000PEPEUSDT', 'price': '0.0014090', 'time': 1703425217771}, 
{'symbol': 'MATICUSDT', 'price': '0.84790', 'time': 1703425217431}, 
{'symbol': 'USDCUSDT', 'price': '0.9991200', 'time': 1703425029793}, 
{'symbol': 'TLMUSDT', 'price': '0.0176200', 'time': 1703425181245}, 
{'symbol': 'CFXUSDT', 'price': '0.1939000', 'time': 1703425217929}, 
{'symbol': 'BTCDOMUSDT', 'price': '2109.9', 'time': 1703425215428}, 
{'symbol': 'YGGUSDT', 'price': '0.4148000', 'time': 1703425217831}, 
{'symbol': 'AXSUSDT', 'price': '8.00300', 'time': 1703425214805}, 
{'symbol': 'ALGOUSDT', 'price': '0.2406', 'time': 1703425216300}, 
{'symbol': 'RENUSDT', 'price': '0.06860', 'time': 1703425217815}, 
{'symbol': 'EOSUSDT', 'price': '0.830', 'time': 1703425218015}, 
{'symbol': 'IOTXUSDT', 'price': '0.05115', 'time': 1703425218569}, 
{'symbol': 'SUSHIUSDT', 'price': '1.2451', 'time': 1703425217876}, 
{'symbol': 'C98USDT', 'price': '0.2955', 'time': 1703425216636}, 
{'symbol': 'OXTUSDT', 'price': '0.0990000', 'time': 1703425214035}, 
{'symbol': 'MTLUSDT', 'price': '1.6568', 'time': 1703425218031}, 
{'symbol': 'ONTUSDT', 'price': '0.2413', 'time': 1703425218644}, 
{'symbol': 'POLYXUSDT', 'price': '0.1956000', 'time': 1703425174997}, 
{'symbol': 'ARBUSDT', 'price': '1.380100', 'time': 1703425217995}, 
{'symbol': 'BAKEUSDT', 'price': '0.5978', 'time': 1703425217442}, 
{'symbol': 'CELOUSDT', 'price': '0.727', 'time': 1703425216318}, 
{'symbol': 'APTUSDT', 'price': '9.56900', 'time': 1703425216293}, 
{'symbol': 'LINAUSDT', 'price': '0.01106', 'time': 1703425214618}, 
{'symbol': 'TWTUSDT', 'price': '1.232900', 'time': 1703425217485}, 
{'symbol': 'OMGUSDT', 'price': '0.8875', 'time': 1703425218517}, 
{'symbol': 'BIGTIMEUSDT', 'price': '0.6055000', 'time': 1703425217744}, 
{'symbol': 'IOSTUSDT', 'price': '0.010209', 'time': 1703425219111}, 
{'symbol': 'IOTAUSDT', 'price': '0.2849', 'time': 1703425213304}, 
{'symbol': 'SLPUSDT', 'price': '0.0031350', 'time': 1703425210970}, 
{'symbol': 'BANDUSDT', 'price': '1.8023', 'time': 1703425216913}, 
{'symbol': 'AAVEUSDT', 'price': '102.880', 'time': 1703425215933}, 
{'symbol': 'STRAXUSDT', 'price': '1.2035000', 'time': 1703425217960}, 
{'symbol': 'COCOSUSDT', 'price': '1.454000', 'time': 1685005226255}, 
{'symbol': '1INCHUSDT', 'price': '0.4170', 'time': 1703425209251}, 
{'symbol': 'ZECUSDT', 'price': '30.76', 'time': 1703425212411}, 
{'symbol': 'WLDUSDT', 'price': '3.5092000', 'time': 1703425216425}, 
{'symbol': 'RIFUSDT', 'price': '0.1433500', 'time': 1703425218300}, 
{'symbol': 'STXUSDT', 'price': '1.4293000', 'time': 1703425218522}, 
{'symbol': 'BNXUSDT', 'price': '0.302900', 'time': 1703425212255}, 
{'symbol': 'CRVUSDT', 'price': '0.636', 'time': 1703425215258}, 
{'symbol': 'LDOUSDT', 'price': '2.393200', 'time': 1703425217740}, 
{'symbol': 'GLMRUSDT', 'price': '0.6155000', 'time': 1703425216785}, 
{'symbol': 'NKNUSDT', 'price': '0.12788', 'time': 1703425217870}, 
{'symbol': 'ETHUSDT_231229', 'price': '2297.03', 'time': 1703425216916}, 
{'symbol': 'NEARUSDT', 'price': '3.7990', 'time': 1703425217078}, 
{'symbol': 'FILUSDT', 'price': '5.680', 'time': 1703425212528}, 
{'symbol': 'XVGUSDT', 'price': '0.0037740', 'time': 1703425216499}, 
{'symbol': 'ETHBTC', 'price': '0.052520', 'time': 1703425167519}, 
{'symbol': 'POWRUSDT', 'price': '0.3773000', 'time': 1703425216346}, 
{'symbol': 'WOOUSDT', 'price': '0.46799', 'time': 1703425218216}, 
{'symbol': 'SNXUSDT', 'price': '4.115', 'time': 1703425215590}, 
{'symbol': 'DYDXUSDT', 'price': '3.182', 'time': 1703425218156}, 
{'symbol': 'WAXPUSDT', 'price': '0.0730100', 'time': 1703425210704}, 
{'symbol': 'ETCUSDT', 'price': '21.152', 'time': 1703425217993}, 
{'symbol': 'LEVERUSDT', 'price': '0.0014540', 'time': 1703425145409}, 
{'symbol': 'KLAYUSDT', 'price': '0.2415', 'time': 1703425211468}, 
{'symbol': 'GALAUSDT', 'price': '0.03114', 'time': 1703425215137}, 
{'symbol': 'HOOKUSDT', 'price': '1.203000', 'time': 1703425217483}, 
{'symbol': 'THETAUSDT', 'price': '1.2462', 'time': 1703425217746}, 
{'symbol': 'STGUSDT', 'price': '0.6132000', 'time': 1703425211927}, 
{'symbol': 'ORBSUSDT', 'price': '0.0408300', 'time': 1703425211053}, 
{'symbol': 'RSRUSDT', 'price': '0.003083', 'time': 1703425217479}, 
{'symbol': 'ICPUSDT', 'price': '9.816000', 'time': 1703425218041}, 
{'symbol': 'GASUSDT', 'price': '7.017000', 'time': 1703425218525}, 
{'symbol': 'VETUSDT', 'price': '0.035910', 'time': 1703425211205}, 
{'symbol': 'FXSUSDT', 'price': '8.805000', 'time': 1703425211122}, 
{'symbol': 'DGBUSDT', 'price': '0.01006', 'time': 1703425207583}, 
{'symbol': 'SSVUSDT', 'price': '24.150000', 'time': 1703425216420}, 
{'symbol': 'ANTUSDT', 'price': '5.843', 'time': 1703425218565}, 
{'symbol': 'FLMUSDT', 'price': '0.0979', 'time': 1703425118377}, 
{'symbol': 'OCEANUSDT', 'price': '0.54620', 'time': 1703425218209}, 
{'symbol': 'LTCUSDT', 'price': '72.33', 'time': 1703425210827}, 
{'symbol': 'ETHUSDT', 'price': '2294.28', 'time': 1703425217990}, 
{'symbol': 'SUPERUSDT', 'price': '0.7029000', 'time': 1703425217040}, 
{'symbol': 'NEOUSDT', 'price': '13.898', 'time': 1703425217745}, 
{'symbol': 'ENJUSDT', 'price': '0.37820', 'time': 1703425210838}, 
{'symbol': 'FRONTUSDT', 'price': '0.3972000', 'time': 1703425213679}, 
{'symbol': 'LITUSDT', 'price': '1.181', 'time': 1703425215575}, 
{'symbol': 'IDUSDT', 'price': '0.3356000', 'time': 1703425217870}, 
{'symbol': 'CHRUSDT', 'price': '0.1733', 'time': 1703425217395}, 
{'symbol': 'ATOMUSDT', 'price': '11.675', 'time': 1703425215871}, 
{'symbol': 'RUNEUSDT', 'price': '6.3490', 'time': 1703425216639}, 
{'symbol': 'BSVUSDT', 'price': '49.62000', 'time': 1703425218187}, 
{'symbol': 'SOLUSDT', 'price': '112.1140', 'time': 1703425217754}, 
{'symbol': 'WAVESUSDT', 'price': '2.7037', 'time': 1703425217802}, 
{'symbol': 'FOOTBALLUSDT', 'price': '390.88000', 'time': 1703425210963}, 
{'symbol': 'GMXUSDT', 'price': '46.290000', 'time': 1703425218004}, 
{'symbol': '1000BONKUSDT', 'price': '0.0190210', 'time': 1703425218047}, 
{'symbol': 'ILVUSDT', 'price': '102.49000', 'time': 1703425217932}, 
{'symbol': 'CYBERUSDT', 'price': '6.850000', 'time': 1703425212745}, 
{'symbol': 'MKRUSDT', 'price': '1428.50', 'time': 1703425216811}, 
{'symbol': 'XRPUSDT', 'price': '0.6205', 'time': 1703425217029}, 
{'symbol': 'CKBUSDT', 'price': '0.0037800', 'time': 1703425216761}, 
{'symbol': 'BALUSDT', 'price': '4.214', 'time': 1703425202086}, 
{'symbol': 'MEMEUSDT', 'price': '0.0311840', 'time': 1703425216272}, 
{'symbol': 'SFPUSDT', 'price': '0.8256', 'time': 1703425216628}, 
{'symbol': 'QNTUSDT', 'price': '116.800000', 'time': 1703425216454}, 
{'symbol': 'DENTUSDT', 'price': '0.001592', 'time': 1703425217425}, 
{'symbol': 'XTZUSDT', 'price': '0.988', 'time': 1703425204869}, 
{'symbol': 'GALUSDT', 'price': '1.89580', 'time': 1703425213675}, 
{'symbol': 'SEIUSDT', 'price': '0.3577000', 'time': 1703425216061}, 
{'symbol': 'RVNUSDT', 'price': '0.02264', 'time': 1703425211460}, 
{'symbol': 'SXPUSDT', 'price': '0.3988', 'time': 1703425218522}, 
{'symbol': 'TIAUSDT', 'price': '13.7479000', 'time': 1703425217006}, 
{'symbol': 'GTCUSDT', 'price': '1.357', 'time': 1703425208021}, 
{'symbol': 'STORJUSDT', 'price': '0.8205', 'time': 1703425218571}, 
{'symbol': 'BTCUSDT', 'price': '43726.20', 'time': 1703425217854}, 
{'symbol': 'COMBOUSDT', 'price': '0.881100', 'time': 1703425215953}, 
{'symbol': 'ARUSDT', 'price': '10.540', 'time': 1703425217607}, 
{'symbol': 'PYTHUSDT', 'price': '0.3646000', 'time': 1703425216920}, 
{'symbol': 'AGIXUSDT', 'price': '0.3429000', 'time': 1703425213436}, 
{'symbol': 'EDUUSDT', 'price': '0.7258000', 'time': 1703425218568}, 
{'symbol': 'JTOUSDT', 'price': '2.591900', 'time': 1703425217135}, 
{'symbol': 'GMTUSDT', 'price': '0.28140', 'time': 1703425214887}, 
{'symbol': 'COMPUSDT', 'price': '55.47', 'time': 1703425218133}, 
{'symbol': 'ZENUSDT', 'price': '10.180', 'time': 1703425218516}, 
{'symbol': 'HIGHUSDT', 'price': '1.847000', 'time': 1703425217466}, 
{'symbol': 'ENSUSDT', 'price': '9.069', 'time': 1703425210793}, 
{'symbol': 'ACEUSDT', 'price': '13.192000', 'time': 1703425217440}, 
{'symbol': 'YFIUSDT', 'price': '8452.0', 'time': 1703425211331}, 
{'symbol': 'STEEMUSDT', 'price': '0.254200', 'time': 1703425185651}, 
{'symbol': 'GRTUSDT', 'price': '0.18709', 'time': 1703425216752}, 
{'symbol': 'ROSEUSDT', 'price': '0.13006', 'time': 1703425216869}, 
{'symbol': 'UNIUSDT', 'price': '6.7190', 'time': 1703425213811}, 
{'symbol': 'ARKUSDT', 'price': '1.0233000', 'time': 1703425214365}, 
{'symbol': 'STMXUSDT', 'price': '0.00900', 'time': 1703425218523}, 
{'symbol': 'TRXUSDT', 'price': '0.10632', 'time': 1703425210760}, 
{'symbol': 'LUNA2USDT', 'price': '0.9709000', 'time': 1703425216805}, 
{'symbol': '1000XECUSDT', 'price': '0.03304', 'time': 1703425144628}, 
{'symbol': 'DASHUSDT', 'price': '33.92', 'time': 1703425217195}, 
{'symbol': 'BADGERUSDT', 'price': '4.224000', 'time': 1703425219089}, 
{'symbol': 'ICXUSDT', 'price': '0.2638', 'time': 1703425215554}, 
{'symbol': 'SANDUSDT', 'price': '0.54270', 'time': 1703425210577}, 
{'symbol': 'PHBUSDT', 'price': '1.3292000', 'time': 1703425216522}, 
{'symbol': 'INJUSDT', 'price': '41.897000', 'time': 1703425217995}, 
{'symbol': 'BTCUSDT_240329', 'price': '45349.4', 'time': 1703425215650}, 
{'symbol': 'TRBUSDT', 'price': '185.748', 'time': 1703425217635}, 
{'symbol': 'KASUSDT', 'price': '0.1078400', 'time': 1703425198928}, 
{'symbol': 'REEFUSDT', 'price': '0.002512', 'time': 1703425218053}, 
{'symbol': 'PEOPLEUSDT', 'price': '0.01429', 'time': 1703425209414}, 
{'symbol': 'ONEUSDT', 'price': '0.01852', 'time': 1703425209416}, 
{'symbol': 'XEMUSDT', 'price': '0.0395', 'time': 1703425207192}, 
{'symbol': 'UMAUSDT', 'price': '2.253000', 'time': 1703425180282}, 
{'symbol': 'LRCUSDT', 'price': '0.29420', 'time': 1703425217326}, 
{'symbol': 'HOTUSDT', 'price': '0.002400', 'time': 1703425216010}, 
{'symbol': 'CTSIUSDT', 'price': '0.2120', 'time': 1703425217443}, 
{'symbol': 'FETUSDT', 'price': '0.7325000', 'time': 1703425217874}, 
{'symbol': 'IDEXUSDT', 'price': '0.0621200', 'time': 1703425210915}, 
{'symbol': 'ORDIUSDT', 'price': '54.844000', 'time': 1703425215946}, 
{'symbol': 'LQTYUSDT', 'price': '1.435100', 'time': 1703425216352}, 
{'symbol': 'QTUMUSDT', 'price': '3.254', 'time': 1703425217520}, 
{'symbol': 'AGLDUSDT', 'price': '1.2050000', 'time': 1703425218466}, 
{'symbol': 'FLOWUSDT', 'price': '0.932', 'time': 1703425218517}, 
{'symbol': 'XMRUSDT', 'price': '176.29', 'time': 1703425218572}, 
{'symbol': 'JOEUSDT', 'price': '0.6775000', 'time': 1703425218171}, 
{'symbol': 'RADUSDT', 'price': '1.793000', 'time': 1703425215512}, 
{'symbol': 'CELRUSDT', 'price': '0.02188', 'time': 1703425218037}, 
{'symbol': 'HBARUSDT', 'price': '0.09284', 'time': 1703425218271}, 
{'symbol': 'AUCTIONUSDT', 'price': '41.600000', 'time': 1703425216939}, 
{'symbol': 'TRUUSDT', 'price': '0.0569200', 'time': 1703425216638}, 
{'symbol': 'IMXUSDT', 'price': '2.4251', 'time': 1703425218002}, 
{'symbol': 'ATAUSDT', 'price': '0.1238', 'time': 1703425208756}, 
{'symbol': 'ZRXUSDT', 'price': '0.3682', 'time': 1703425218594}, 
{'symbol': 'NMRUSDT', 'price': '17.190000', 'time': 1703425200262}, 
{'symbol': 'APEUSDT', 'price': '1.7040', 'time': 1703425201177}, 
{'symbol': 'NTRNUSDT', 'price': '1.142300', 'time': 1703425218064}, 
{'symbol': '1000LUNCUSDT', 'price': '0.1620400', 'time': 1703425216427}, 
{'symbol': 'ALPHAUSDT', 'price': '0.13728', 'time': 1703425217932}, 
{'symbol': 'DOGEUSDT', 'price': '0.094410', 'time': 1703425217992}, 
{'symbol': 'OPUSDT', 'price': '3.5415000', 'time': 1703425216365}, 
{'symbol': 'BLZUSDT', 'price': '0.35038', 'time': 1703425218033}, 
{'symbol': 'TOKENUSDT', 'price': '0.0395800', 'time': 1703425210744}, 
{'symbol': 'MDTUSDT', 'price': '0.0602700', 'time': 1703425210707}, 
{'symbol': 'XLMUSDT', 'price': '0.12774', 'time': 1703425211379}, 
{'symbol': 'ASTRUSDT', 'price': '0.1080000', 'time': 1703425214414}, 
{'symbol': 'BTCUSDT_231229', 'price': '43858.8', 'time': 1703425203267}, 
{'symbol': 'KAVAUSDT', 'price': '0.8665', 'time': 1703425217870}, 
{'symbol': 'MAGICUSDT', 'price': '1.053200', 'time': 1703425211468}, 
{'symbol': 'XVSUSDT', 'price': '12.400000', 'time': 1703425217104}, 
{'symbol': 'PENDLEUSDT', 'price': '1.1581000', 'time': 1703425204256}, 
{'symbol': 'RNDRUSDT', 'price': '4.673400', 'time': 1703425217995}, 
{'symbol': 'MAVUSDT', 'price': '0.3837000', 'time': 1703425214780}, 
{'symbol': 'DUSKUSDT', 'price': '0.17258', 'time': 1703425214309}, 
{'symbol': 'COTIUSDT', 'price': '0.07275', 'time': 1703425218567}, 
{'symbol': 'EGLDUSDT', 'price': '72.330', 'time': 1703425217158}, 
{'symbol': 'ARKMUSDT', 'price': '0.7365000', 'time': 1703425217199}, 
{'symbol': 'CHZUSDT', 'price': '0.08656', 'time': 1703425210868}, 
{'symbol': 'CVXUSDT', 'price': '3.598000', 'time': 1703425218059}, 
{'symbol': 'ETHWUSDT', 'price': '3.475000', 'time': 1703425215477}, 
{'symbol': 'BONDUSDT', 'price': '4.693000', 'time': 1703425216869}, 
{'symbol': 'BNTUSDT', 'price': '0.7799000', 'time': 1703425218517}, 
{'symbol': 'CAKEUSDT', 'price': '2.8512000', 'time': 1703425212619}, 
{'symbol': 'API3USDT', 'price': '1.9316', 'time': 1703425218154}, 
{'symbol': 'ZILUSDT', 'price': '0.02674', 'time': 1703425206826}, 
{'symbol': 'AMBUSDT', 'price': '0.0085550', 'time': 1703425218045}, 
{'symbol': 'ONGUSDT', 'price': '0.3728000', 'time': 1703425129640}, 
{'symbol': 'BEAMXUSDT', 'price': '0.0191960', 'time': 1703425211898}, 
{'symbol': 'SUIUSDT', 'price': '0.729100', 'time': 1703425217785}, 
{'symbol': '1000SHIBUSDT', 'price': '0.010925', 'time': 1703425215333}, 
{'symbol': 'HIFIUSDT', 'price': '0.7259000', 'time': 1703425213768}, 
{'symbol': 'HFTUSDT', 'price': '0.3813000', 'time': 1703425217411}, 
{'symbol': 'ETHUSDT_240329', 'price': '2370.10', 'time': 1703425192258}, 
{'symbol': '1000FLOKIUSDT', 'price': '0.0361100', 'time': 1703425217812}, 
{'symbol': 'LINKUSDT', 'price': '15.758', 'time': 1703425218524}, 
{'symbol': 'SNTUSDT', 'price': '0.0437400', 'time': 1703425218518}, 
{'symbol': 'ADAUSDT', 'price': '0.61800', 'time': 1703425215463}, 
{'symbol': 'MBLUSDT', 'price': '0.0050100', 'time': 1703425209144}, 
{'symbol': 'MASKUSDT', 'price': '3.6060', 'time': 1703425211188}, 
{'symbol': 'ANKRUSDT', 'price': '0.031400', 'time': 1703425215022}, 
{'symbol': 'BATUSDT', 'price': '0.2535', 'time': 1703425216853}, 
{'symbol': 'BNBUSDT', 'price': '269.300', 'time': 1703425218517}, 
{'symbol': 'PERPUSDT', 'price': '0.845200', 'time': 1703425217429}, 
{'symbol': 'LPTUSDT', 'price': '9.562', 'time': 1703425215216}, 
{'symbol': 'DOTUSDT', 'price': '9.022', 'time': 1703425216204}, 
{'symbol': 'FTMUSDT', 'price': '0.524200', 'time': 1703425210607}, 
{'symbol': 'UNFIUSDT', 'price': '7.963', 'time': 1703425216785}, 
{'symbol': 'DARUSDT', 'price': '0.1522', 'time': 1703425210919}, 
{'symbol': 'BLURUSDT', 'price': '0.5201000', 'time': 1703425218220}, 
{'symbol': 'DEFIUSDT', 'price': '986.2', 'time': 1703425212455}, 
{'symbol': 'RDNTUSDT', 'price': '0.2993000', 'time': 1703425217992}]

время входа      открытие    максимум  минимум    закрытие  объем    время закрытия   Qобъем    
[[1703426460000, '0.35182', '0.35214', '0.35152', '0.35204', '49136', 1703426519999, '17288.37870', 210, '24672', '8682.47203', '0'], 
[1703426520000, '0.35206', '0.35207', '0.35151', '0.35202', '64188', 1703426579999, '22582.99633', 194, '35438', '12469.83002', '0'], 
[1703426580000, '0.35200', '0.35200', '0.35156', '0.35164', '22211', 1703426639999, '7813.71639', 83, '7782', '2737.27425', '0'], 
[1703426640000, '0.35169', '0.35200', '0.35165', '0.35184', '21555', 1703426699999, '7584.33260', 80, '14834', '5219.96487', '0'], 

{'BLZUSDT': 
     {'price': 0.33933, 
      14: ['0.34028', '0.34050', '0.34164', '0.34370', '0.34818', '0.34800', '0.34788', '0.34705', '0.34754', '0.33911', '0.33805', '0.34189', '0.33958', '0.33933'], 
      5: ['0.33936', '0.34047', '0.34000', '0.33943', '0.33933']}, 
 'AVAXUSDT': 
     {'price': 39.091, 
      14: ['39.9310', '39.6720', '39.2680', '39.8210', '39.5580', '39.3490', '39.3820', '39.5170', '39.2190', '38.2550', '38.5890', '38.9870', '39.4230', '39.0920'], 
      5: ['39.1440', '39.0250', '39.0260', '39.1070', '39.0920']}, 
 'ARBUSDT': 
     {'price': 1.5789, 
      14: ['1.612500', '1.613000', '1.585300', '1.585000', '1.573700', '1.588800', '1.576300', '1.561200', '1.562200', '1.542800', '1.562600', '1.575900', '1.586800', '1.578500'], 
      5: ['1.601500', '1.593600', '1.584200', '1.582700', '1.578500']}}
"""
