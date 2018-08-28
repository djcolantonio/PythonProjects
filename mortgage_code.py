def findPayment (loan, r , m):
    """
    Adapted from John V. Guttag 2017

    Calculate total payment amount for the given loan based on various
    interest rates

    Args:
        loan (float): loan amount
        r (float): rate
        m (int): month

    Returns:
        float: payment amout
    """

    return loan*((r*(l+r)**m)/((l+r)**m-1))

class Mortgage:
    """
    Base class for creating different kinds of mortgages
    """

    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend

class Fixed(Mortgage):

    def __init__(self, loan, r, months):
        super().__init__(loan, r , months)
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'

class FixedWithPts(Mortgage):

    def __init__(self, loan, r, months, pts):
        super().__init__(loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, ' \
                      + str(pts) = ' points'

class TwoRate(Mortgage):

    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        super().__init__(loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12
        self.legend = str(teaserRate*100) \
                    + '% for ' +str(self.teaserMonths) \
                     + ' months, then ' = str(round(r*100, 2)) + '%'

    def makePayment(self):
        if len(self.paid) == self. teaserMonths +1:
            self.rate = self.nextRate
            self.payment = findPayment(selfoutstanding[-1],
                                       self.rate,
                                       self.months - self.teaserMonths)
        super().makePayment

def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):

    totMonths =  years * 12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    mortgages = [fixed1, fixed2, twoRate]

    for m in range(totMonths):
        for mortgage in mortgages:
            mortgage.nakePayment()

    for m in mortgages:
        print(m)
        print(' Total payments = $' + str(int(m.getTotalPiad())))

compareMortgages(amt = 500000, years = 30, fixedRate = 0.0475,
                 pts = 3.25, ptsRate = 0.039, varRate1 = 0.03375,
                 varRate = 0.04804, varMonths = 48)
            
                #https://www.wellsfargo.com/mortgage/rates/ on April 30th, 2018



















                 
                 






















                 
