b = 10.0


def lot_size_precision(a):
    precision = 0
    for i in str(a):
        if i == '1':
            return precision
        elif i == '.':
             pass
        else:
            precision += 1


if __name__ == '__main__':
    a = {'BTCUSDT': '0.001', 'ETHUSDT': '0.001', 'BCHUSDT': '0.001', 'XRPUSDT': '0.1', 'EOSUSDT': '0.1',
         'LTCUSDT': '0.001',
         'TRXUSDT': '1', 'ETCUSDT': '0.01', 'LINKUSDT': '0.01', 'XLMUSDT': '1', 'ADAUSDT': '1', 'XMRUSDT': '0.001',
         'DASHUSDT': '0.001', 'ZECUSDT': '0.001', 'XTZUSDT': '0.1', 'BNBUSDT': '0.01', 'ATOMUSDT': '0.01',
         'ONTUSDT': '0.1',
         'IOTAUSDT': '0.1', 'BATUSDT': '0.1', 'VETUSDT': '1', 'NEOUSDT': '0.01', 'QTUMUSDT': '0.1', 'IOSTUSDT': '1',
         'THETAUSDT': '0.1', 'ALGOUSDT': '0.1', 'ZILUSDT': '1', 'KNCUSDT': '1', 'ZRXUSDT': '0.1', 'COMPUSDT': '0.001',
         'OMGUSDT': '0.1', 'DOGEUSDT': '1', 'SXPUSDT': '0.1', 'KAVAUSDT': '0.1', 'BANDUSDT': '0.1', 'RLCUSDT': '0.1',
         'WAVESUSDT': '0.1', 'MKRUSDT': '0.001', 'SNXUSDT': '0.1', 'DOTUSDT': '0.1', 'DEFIUSDT': '0.001',
         'YFIUSDT': '0.001', 'BALUSDT': '0.1', 'CRVUSDT': '0.1', 'TRBUSDT': '0.1', 'RUNEUSDT': '1', 'SUSHIUSDT': '1',
         'EGLDUSDT': '0.1', 'SOLUSDT': '1', 'ICXUSDT': '1', 'STORJUSDT': '1', 'BLZUSDT': '1', 'UNIUSDT': '1',
         'AVAXUSDT': '1', 'FTMUSDT': '1', 'ENJUSDT': '1', 'FLMUSDT': '1', 'RENUSDT': '1', 'KSMUSDT': '0.1',
         'NEARUSDT': '1',
         'AAVEUSDT': '0.1', 'FILUSDT': '0.1', 'RSRUSDT': '1', 'LRCUSDT': '1', 'MATICUSDT': '1', 'OCEANUSDT': '1',
         'CVCUSDT': '1', 'BELUSDT': '1', 'CTKUSDT': '1', 'AXSUSDT': '1', 'ALPHAUSDT': '1', 'ZENUSDT': '0.1',
         'SKLUSDT': '1',
         'GRTUSDT': '1', '1INCHUSDT': '1', 'CHZUSDT': '1', 'SANDUSDT': '1', 'ANKRUSDT': '1', 'LITUSDT': '0.1',
         'UNFIUSDT': '0.1', 'REEFUSDT': '1', 'RVNUSDT': '1', 'SFPUSDT': '1', 'XEMUSDT': '1', 'BTCSTUSDT': '0.1',
         'COTIUSDT': '1', 'CHRUSDT': '1', 'MANAUSDT': '1', 'ALICEUSDT': '0.1', 'HBARUSDT': '1', 'ONEUSDT': '1',
         'LINAUSDT': '1', 'STMXUSDT': '1', 'DENTUSDT': '1', 'CELRUSDT': '1', 'HOTUSDT': '1', 'MTLUSDT': '1',
         'OGNUSDT': '1',
         'NKNUSDT': '1', 'SCUSDT': '1', 'DGBUSDT': '1', '1000SHIBUSDT': '1', 'BAKEUSDT': '1', 'GTCUSDT': '0.1',
         'BTCDOMUSDT': '0.001', 'IOTXUSDT': '1', 'RAYUSDT': '0.1', 'C98USDT': '1', 'MASKUSDT': '1', 'ATAUSDT': '1',
         'DYDXUSDT': '0.1', '1000XECUSDT': '1', 'GALAUSDT': '1', 'CELOUSDT': '0.1', 'ARUSDT': '0.1', 'KLAYUSDT': '0.1',
         'ARPAUSDT': '1', 'CTSIUSDT': '1', 'LPTUSDT': '0.1', 'ENSUSDT': '0.1', 'PEOPLEUSDT': '1', 'ROSEUSDT': '1',
         'DUSKUSDT': '1', 'FLOWUSDT': '0.1', 'IMXUSDT': '1', 'API3USDT': '0.1', 'GMTUSDT': '1', 'APEUSDT': '1',
         'WOOUSDT': '1', 'FTTUSDT': '0.1', 'JASMYUSDT': '1', 'DARUSDT': '0.1', 'GALUSDT': '1', 'OPUSDT': '0.1',
         'INJUSDT': '0.1', 'STGUSDT': '1', 'SPELLUSDT': '1', '1000LUNCUSDT': '1', 'LUNA2USDT': '1', 'LDOUSDT': '1',
         'CVXUSDT': '1', 'ICPUSDT': '1', 'APTUSDT': '0.1', 'QNTUSDT': '0.1', 'FETUSDT': '1', 'FXSUSDT': '0.1',
         'HOOKUSDT': '0.1', 'MAGICUSDT': '0.1', 'TUSDT': '1', 'RNDRUSDT': '0.1', 'HIGHUSDT': '0.1', 'MINAUSDT': '1',
         'ASTRUSDT': '1', 'AGIXUSDT': '1', 'PHBUSDT': '1', 'GMXUSDT': '0.01', 'CFXUSDT': '1', 'STXUSDT': '1',
         'BNXUSDT': '0.1', 'ACHUSDT': '1', 'SSVUSDT': '0.01', 'CKBUSDT': '1', 'PERPUSDT': '0.1', 'TRUUSDT': '1',
         'LQTYUSDT': '0.1', 'USDCUSDT': '1', 'IDUSDT': '1', 'ARBUSDT': '0.1', 'JOEUSDT': '1', 'TLMUSDT': '1',
         'AMBUSDT': '1', 'LEVERUSDT': '1', 'RDNTUSDT': '1', 'HFTUSDT': '1', 'XVSUSDT': '0.1', 'ETHBTC': '0.01',
         'BLURUSDT': '1', 'EDUUSDT': '1', 'IDEXUSDT': '1', 'SUIUSDT': '0.1', '1000PEPEUSDT': '1', '1000FLOKIUSDT': '1',
         'UMAUSDT': '1', 'RADUSDT': '1', 'KEYUSDT': '1', 'COMBOUSDT': '0.1', 'NMRUSDT': '0.1', 'MAVUSDT': '1',
         'MDTUSDT': '1', 'XVGUSDT': '1', 'WLDUSDT': '1', 'PENDLEUSDT': '1', 'ARKMUSDT': '1', 'AGLDUSDT': '1',
         'YGGUSDT': '1', 'DODOXUSDT': '1', 'BNTUSDT': '1', 'OXTUSDT': '1', 'SEIUSDT': '1', 'CYBERUSDT': '0.1',
         'HIFIUSDT': '1', 'ARKUSDT': '1', 'FRONTUSDT': '1', 'GLMRUSDT': '1', 'BICOUSDT': '1', 'STRAXUSDT': '1',
         'LOOMUSDT': '1', 'BIGTIMEUSDT': '1', 'BONDUSDT': '0.1', 'ORBSUSDT': '1', 'STPTUSDT': '1', 'WAXPUSDT': '1',
         'BSVUSDT': '0.1', 'RIFUSDT': '1', 'POLYXUSDT': '1', 'GASUSDT': '0.1', 'POWRUSDT': '1', 'SLPUSDT': '1',
         'TIAUSDT': '1', 'SNTUSDT': '1', 'CAKEUSDT': '1', 'MEMEUSDT': '1', 'TWTUSDT': '1', 'TOKENUSDT': '1',
         'ORDIUSDT': '0.1', 'STEEMUSDT': '1', 'BADGERUSDT': '1', 'ILVUSDT': '0.1', 'NTRNUSDT': '1', 'KASUSDT': '1',
         'BEAMXUSDT': '1', '1000BONKUSDT': '1', 'PYTHUSDT': '1', 'SUPERUSDT': '1', 'USTCUSDT': '1', 'ONGUSDT': '1',
         'ETHWUSDT': '1', 'JTOUSDT': '1', '1000SATSUSDT': '1', 'AUCTIONUSDT': '0.01', '1000RATSUSDT': '1',
         'ACEUSDT': '0.01', 'MOVRUSDT': '0.01', 'NFPUSDT': '0.1', 'BTCUSDT_240628': '0.001', 'ETHUSDT_240628': '0.001',
         'BTCUSDC': '0.001', 'ETHUSDC': '0.001', 'BNBUSDC': '0.01', 'SOLUSDC': '0.01', 'XRPUSDC': '0.1', 'AIUSDT': '1',
         'XAIUSDT': '1', 'DOGEUSDC': '1', 'WIFUSDT': '0.1', 'MANTAUSDT': '0.1', 'ONDOUSDT': '0.1', 'LSKUSDT': '1',
         'ALTUSDT': '1', 'JUPUSDT': '1', 'ZETAUSDT': '1', 'RONINUSDT': '0.1', 'DYMUSDT': '0.1', 'SUIUSDC': '0.1',
         'OMUSDT': '0.1', 'LINKUSDC': '0.01', 'PIXELUSDT': '1', 'STRKUSDT': '0.1', 'MAVIAUSDT': '0.1',
         'ORDIUSDC': '0.1',
         'GLMUSDT': '1', 'PORTALUSDT': '0.1', 'TONUSDT': '0.1', 'AXLUSDT': '0.1', 'MYROUSDT': '1', '1000PEPEUSDC': '1',
         'METISUSDT': '0.01', 'AEVOUSDT': '0.1', 'WLDUSDC': '0.1', 'VANRYUSDT': '1', 'BOMEUSDT': '1',
         'ETHFIUSDT': '0.1',
         'AVAXUSDC': '0.01', '1000SHIBUSDC': '1', 'BTCUSDT_240927': '0.001', 'ETHUSDT_240927': '0.001', 'ENAUSDT': '1',
         'WUSDT': '0.1', 'WIFUSDC': '0.1', 'BCHUSDC': '0.001', 'TNSRUSDT': '0.1', 'SAGAUSDT': '0.1', 'LTCUSDC': '0.001',
         'NEARUSDC': '1', 'TAOUSDT': '0.001', 'OMNIUSDT': '0.01', 'ARBUSDC': '0.1', 'NEOUSDC': '0.01', 'FILUSDC': '0.1',
         'MATICUSDC': '1', 'TIAUSDC': '1', 'BOMEUSDC': '1', 'REZUSDT': '1', 'ENAUSDC': '1', 'ETHFIUSDC': '0.1',
         '1000BONKUSDC': '1', 'BBUSDT': '1', 'NOTUSDT': '1', 'TURBOUSDT': '1'}
    print(lot_size_precision(b))
