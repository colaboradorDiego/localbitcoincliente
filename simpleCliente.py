import json
import sys
import os
import time

from lbcapi import api

# Apiauth-Nonce
# A nonce is an integer number, that needs to increase with every API request.
def getNonce():
    return  str(round(time.time() * 1000))


# /bitcoinaverage/ticker-all-currencies/
def getBitCoinAverage():
    pass


# Ofertas de los vendedores
class Seller:
    def __init__(self, data):
        self.data = data
        self.parse()

    def parse(self):
        self.userNm = self.data['profile']['username']
        self.min = self.data['min_amount']
        self.max = self.data['max_amount']
        self.price = self.data['temp_price']

    def mostrar(self):
        print('Data:', self.data)
        print()


# Conexcion a localbitcoin
def connect(conArgs):
    conn = api.hmac(conArgs['api']['key'], conArgs['api']['secret'])
    return conn


# trae precios desde localbitcoin
def requestMaker(conn, restId):
    if restId == 'p2pSellers':
        # get Sellers by currency & paymentMethod
        result = conn.call('GET', '/buy-bitcoins-online/usd/paypal/.json').json()
        # print(result)
        sellersList = result.get('data').get('ad_list')
        # print(sellersList)
        print(json.dumps(sellersList))
        if sellersList:
            mySellers = {}
            for i in sellersList:
                # print(i['data'])
                # print()
                o = Seller(i['data'])
                # o.mostrar()
                mySellers[o.userNm] = o
                # print(o.userNm)
                # print()

            # for i in mySellers:
            #     print('userName     CraMin     CpraMax     PrecioUSD')
            #     print(mySellers[i].userNm, '    ', mySellers[i].min, '    ', mySellers[i].max, '    ',
            #           mySellers[i].price)

        else:
            print('NO HAY VENDERORES PARA LA QUERY')

    elif restId == 'p2pBuyers':
        pass

    else:
        pass


def startApp(conArgs):
    conn = connect(conArgs)

    #loop
    while True:
        requestMaker(conn, 'p2pSellers')

        time.sleep(60)


def main(argv):

    # loads JSON from a file.
    parametros = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'localBitCoinApi.ini'))
    with open(parametros, 'r') as f:
        conArgs = json.load(f)
    startApp(conArgs)


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))

init()
