import unittest,sys
sys.path.insert(0, '.')
from quik import quik

class QDDETest(unittest.TestCase):

    def setUp(self):
        self.quik = quik.Quik("C:\\quik-bcs","QuikDDE")
        self.quik.register( "TICKERS",{"code":"Код бумаги","name":"Бумага","price":"Цена послед."}, lambda x: print(x) )

    def testRun(self):
        self.assertTrue(self.quik.error(),"OK")
        self.quik.execute({"trans_id":"1"}, lambda res,err,rep,tid,order,msg: print(msg) )
        self.quik.run()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QDDETest))
    unittest.TextTestRunner(verbosity=2).run(suite)
