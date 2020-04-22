# # Encapsulation - when you used method from the same class - all methods within a class
from datetime import date

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day


# main class that will be used as the basis to get the data necessary to do calculations
class Calculate:
    def __init__(self, pia, month, day, year, protfl_month, pfdate):
        self.pia = float(pia)
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)
        self.protfl_month = protfl_month
        self.pfdate = "n" if pfdate is None or "" else pfdate

    def __repr__(self):
        if self.pfdate == "y":
            self.protfl_month = int(protfl_month)

    # Calculate age with months
    def current_age_with_months(self):
        current_age = current_year - self.year
        months_age = 0

        if current_month == self.month:
            months_age = 0
        elif current_month < self.month:
            months_age = (12 - self.month) + current_month
            current_age = current_age - 1
        else:
            months_age = current_month - self.month

        return current_age, months_age

    def min_month_year(self, min_age=None):
        min_year = min_age + self.year
        min_month = self.month
        if self.day == 1 or self.day == 2:
            pass

        else:
            min_month = min_month + 1
            if min_month > 12:
                min_month = min_month - 12
                min_year = min_year + 1

        return f'Minimum month and year is {min_month}/{min_year}'


# Class created to calculate rib benefits - inherits from Calculate class - Inheritance
class CalcRib(Calculate):
    def min_month_year(self):
        return super().min_month_year(min_age=62)

    def calc_fra_age_rib_spouse(self):

        if self.month == 1 and self.day == 1 and self.year == 1943 or self.year < 1943:
            fra_age = 65

        elif (
                self.month >= 1 and self.day >= 2 and 1943 <= self.year <= 1959 or self.month >= 2 and self.day >= 1 and 1943 <= self.year <= 1959
                or self.month == 1 and self.day == 1 and self.year == 1960):
            fra_age = 66

        else:
            fra_age = 67

        return fra_age

    def calc_fra_month_rib_spouse(self):
        fra_age = self.calc_fra_age_rib_spouse()
        fra_month = self.month
        fra_year = self.year + fra_age

        if (self.month >= 1 and self.day > 1 and self.year == 1938 or
                self.month >= 2 and self.day >= 1 and self.year == 1938 or
                self.month == 1 and self.day == 1 and self.year == 1939 or
                self.month >= 1 and self.day >= 2 and self.year == 1955 or
                self.month >= 2 and self.day >= 1 and self.year == 1955 or
                self.month == 1 and self.day == 1 and self.year == 1956):
            fra_month = self.month + 2

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
                    fra_year = fra_year - 1;
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1939 or
              self.month >= 2 and self.day >= 1 and self.year == 1939 or
              self.month == 1 and self.day == 1 and self.year == 1940 or
              self.month >= 1 and self.day >= 2 and self.year == 1956 or
              self.month >= 2 and self.day >= 1 and self.year == 1956 or
              self.month == 1 and self.day == 1 and self.year == 1957):
            fra_month = self.month + 4

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1940 or
              self.month >= 2 and self.day >= 1 and self.year == 1940 or
              self.month == 1 and self.day == 1 and self.year == 1941 or
              self.month >= 1 and self.day >= 2 and self.year == 1957 or
              self.month >= 2 and self.day >= 1 and self.year == 1957 or
              self.month == 1 and self.day == 1 and self.year == 1958):
            fra_month = self.month + 6

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month == 1 and self.day > 1 and self.year == 1941 or
              self.month >= 2 and self.day >= 1 and self.year == 1941 or
              self.month == 1 and self.day == 1 and self.year == 1942 or
              self.month == 1 and self.day > 1 and self.year == 1958 or
              self.month >= 2 and self.day >= 1 and self.year == 1958 or
              self.month == 1 and self.day == 1 and self.year == 1959):
            fra_month = self.month + 8

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12

            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1942 or
              self.month >= 2 and self.day >= 1 and self.year == 1942 or
              self.month == 1 and self.day == 1 and self.year == 1943 or
              self.month >= 1 and self.day >= 2 and self.year == 1959 or
              self.month >= 2 and self.day >= 1 and self.year == 1959 or
              self.month == 1 and self.day == 1 and self.year == 1960):
            fra_month = self.month + 10

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        else:
            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
                    fra_year = fra_year - 1

        return fra_month, fra_year

    # Calculates reduction factors
    def calc_rf(self):
        current_month = date.today().month
        fra_month, fra_year = self.calc_fra_month_rib_spouse()

        if self.pfdate == 'y':
            pass
            if int(self.protfl_month) < current_month:
                current_month = int(self.protfl_month)
                rf = (fra_year - current_year) * 12 + (fra_month - current_month)
            elif int(self.protfl_month) > current_month:
                current_month = int(self.protfl_month)
                rf = (fra_year - current_year + 1) * 12 + (fra_month - current_month)
        else:
            rf = (fra_year - current_year) * 12 + (fra_month - current_month)

        if rf < 0:
            rf = 0
        elif rf >= 51 and self.year == 1956:
            rf = 51;
        elif rf >= 53 and self.year == 1957:
            rf = 53;
        elif rf >= 55 and self.year == 1958:
            rf = 55;
        elif rf >= 57 and self.year == 1959:
            rf = 57;
        elif rf >= 59 and self.year >= 1960:
            rf = 59;

        # else:
        #     rf = 60

        return rf

    # Calculates rib benefits
    def calc_benefits(self):
        rf = self.calc_rf()
        calculated_benefits = []
        rib_benefits = [self.pia, ((((self.pia * 179) / 180) * 10) / 10), ((((self.pia * 178) / 180) * 10) / 10),
                        ((((self.pia * 177) / 180) * 10) / 10), ((((self.pia * 176) / 180) * 10) / 10),
                        ((((self.pia * 175) / 180) * 10) / 10), ((((self.pia * 174) / 180) * 10) / 10),
                        ((((self.pia * 173) / 180) * 10) / 10), ((((self.pia * 172) / 180) * 10) / 10),
                        ((((self.pia * 171) / 180) * 10) / 10), ((((self.pia * 170) / 180) * 10) / 10),
                        ((((self.pia * 169) / 180) * 10) / 10), ((((self.pia * 168) / 180) * 10) / 10),
                        ((((self.pia * 167) / 180) * 10) / 10), ((((self.pia * 166) / 180) * 10) / 10),
                        ((((self.pia * 165) / 180) * 10) / 10), ((((self.pia * 164) / 180) * 10) / 10),
                        ((((self.pia * 163) / 180) * 10) / 10), ((((self.pia * 162) / 180) * 10) / 10),
                        ((((self.pia * 161) / 180) * 10) / 10), ((((self.pia * 160) / 180) * 10) / 10),
                        ((((self.pia * 159) / 180) * 10) / 10), ((((self.pia * 158) / 180) * 10) / 10),
                        ((((self.pia * 157) / 180) * 10) / 10), ((((self.pia * 156) / 180) * 10) / 10),
                        ((((self.pia * 155) / 180) * 10) / 10), ((((self.pia * 154) / 180) * 10) / 10),
                        ((((self.pia * 153) / 180) * 10) / 10), ((((self.pia * 152) / 180) * 10) / 10),
                        ((((self.pia * 151) / 180) * 10) / 10), ((((self.pia * 150) / 180) * 10) / 10),
                        ((((self.pia * 149) / 180) * 10) / 10), ((((self.pia * 148) / 180) * 10) / 10),
                        ((((self.pia * 147) / 180) * 10) / 10), ((((self.pia * 146) / 180) * 10) / 10),
                        ((((self.pia * 145) / 180) * 10) / 10), ((((self.pia * 144) / 180) * 10) / 10),
                        ((((self.pia * 191) / 240) * 10) / 10), ((((self.pia * 190) / 240) * 10) / 10),
                        ((((self.pia * 189) / 240) * 10) / 10), ((((self.pia * 188) / 240) * 10) / 10),
                        ((((self.pia * 187) / 240) * 10) / 10), ((((self.pia * 186) / 240) * 10) / 10),
                        ((((self.pia * 185) / 240) * 10) / 10), ((((self.pia * 184) / 240) * 10) / 10),
                        ((((self.pia * 183) / 240) * 10) / 10), ((((self.pia * 182) / 240) * 10) / 10),
                        ((((self.pia * 181) / 240) * 10) / 10), ((((self.pia * 180) / 240) * 10) / 10),
                        ((((self.pia * 179) / 240) * 10) / 10), ((((self.pia * 178) / 240) * 10) / 10),
                        ((((self.pia * 177) / 240) * 10) / 10), ((((self.pia * 176) / 240) * 10) / 10),
                        ((((self.pia * 175) / 240) * 10) / 10), ((((self.pia * 174) / 240) * 10) / 10),
                        ((((self.pia * 173) / 240) * 10) / 10), ((((self.pia * 172) / 240) * 10) / 10),
                        ((((self.pia * 171) / 240) * 10) / 10), ((((self.pia * 170) / 240) * 10) / 10),
                        ((((self.pia * 169) / 240) * 10) / 10), ((((self.pia * 168) / 240) * 10) / 10)]

        # return [round_down(x, 2) for x in rib_benefits]

        for i, rib_mba in zip(range(rf + 1), rib_benefits):
            rib_mba = "{:.3f}".format(rib_mba)
            total = str(rib_mba)[:-2] + "0"
            calculated_benefits.append(total)

        return calculated_benefits

    def month_year(self):
        results = []
        rf = self.calc_rf()
        fra_month, fra_year = self.calc_fra_month_rib_spouse()
        for i in range(rf + 1):
            results.append(f'{fra_month}/{fra_year}')
            fra_month = fra_month - 1
            if fra_month <= 0:
                fra_month = 12
                fra_year = fra_year - 1
        return results

    def calc_drcs(self):
        fra_month, fra_year = self.calc_fra_month_rib_spouse()
        max_drcs = (self.month - fra_month) + (((self.year + 70) - fra_year) * 12)
        current_drcs_left = (self.month - current_month) + (((self.year + 70) - current_year) * 12)
        if current_drcs_left > max_drcs:
            current_drcs_left = max_drcs

        return max_drcs, current_drcs_left

    def calc_mba_drcs(self):
        max_drcs, current_drcs = self.calc_drcs()
        drc_amounts = []

        if self.year <= 1916:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * drcs) / 1200)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif 1916 < self.year <= 1924:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * drcs) / 400)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1925 or self.year == 1926:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 7 * drcs) / 2400)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1927 or self.year == 1928:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * drcs) / 300)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1929 or self.year == 1930:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 3 * drcs) / 800)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1931 or self.year == 1932:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 5 * drcs) / 1200)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1933 or self.year == 1934:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 11 * drcs) / 2400)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1935 or self.year == 1936:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * drcs) / 200)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1937 or self.year == 1938:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 13 * drcs) / 2400)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1939 or self.year == 1940:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 7 * drcs) / 1200)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year == 1941 or self.year == 1942:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 5 * drcs) / 800)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

        elif self.year >= 1943:
            for drcs in range(max_drcs + 1):
                drc_formula = "{:.3f}".format(self.pia + (self.pia * 2 * drcs) / 300)
                total = str(drc_formula)[:-2] + "0"
                drc_amounts.append(total)
            return drc_amounts

    def drc_months(self):
        fra_month, fra_year = self.calc_fra_month_rib_spouse()
        max_drcs, drcs_left = self.calc_drcs()
        results = []
        message = []

        for i in range(max_drcs + 1):
            results.append(f'{fra_month}/{fra_year}')
            fra_month = fra_month + 1
            january = results[i].find(f'1/{fra_year}')
            december = results[i].find(f'12/{fra_year}')

            if fra_month > 12:
                fra_month = 1
                fra_year = fra_year + 1

            if i == 0:
                message.append('')
            elif january == 0:
                message.append(f'1/{fra_year}')
            elif december == 0:
                message.append(f'1/{fra_year}')
            elif 0 < i < max_drcs:
                message.append(f'1/{fra_year + 1}')
            elif i == max_drcs:
                message.append(f'{self.month}/{fra_year}')

        return results, message


# Class created to calculate spouse benefits - inherits from CalcRib class - Inheritance
class CalcSpouse(CalcRib):
    def __init__(self, spouse_pia, month, day, year, protfl_month, pfdate):
        self.spouse_pia = float(spouse_pia)
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)
        self.protfl_month = protfl_month
        self.pfdate = pfdate

    def calc_benefits_b(self):
        rf = self.calc_rf()
        calculated_benefits_b = []
        spo_rate = self.spouse_pia / 2
        fra_month, fra_year = self.calc_fra_month_rib_spouse()
        spouse_benefits = [spo_rate, ((((spo_rate * 143) / 144) * 10) / 10),
                           ((((spo_rate * 142) / 144) * 10) / 10), ((((spo_rate * 141) / 144) * 10) / 10),
                           ((((spo_rate * 140) / 144) * 10) / 10), ((((spo_rate * 139) / 144) * 10) / 10),
                           ((((spo_rate * 138) / 144) * 10) / 10), ((((spo_rate * 137) / 144) * 10) / 10),
                           ((((spo_rate * 136) / 144) * 10) / 10), ((((spo_rate * 135) / 144) * 10) / 10),
                           ((((spo_rate * 134) / 144) * 10) / 10), ((((spo_rate * 133) / 144) * 10) / 10),
                           ((((spo_rate * 132) / 144) * 10) / 10), ((((spo_rate * 131) / 144) * 10) / 10),
                           ((((spo_rate * 130) / 144) * 10) / 10), ((((spo_rate * 129) / 144) * 10) / 10),
                           ((((spo_rate * 128) / 144) * 10) / 10), ((((spo_rate * 127) / 144) * 10) / 10),
                           ((((spo_rate * 126) / 144) * 10) / 10), ((((spo_rate * 125) / 144) * 10) / 10),
                           ((((spo_rate * 124) / 144) * 10) / 10), ((((spo_rate * 123) / 144) * 10) / 10),
                           ((((spo_rate * 122) / 144) * 10) / 10), ((((spo_rate * 121) / 144) * 10) / 10),
                           ((((spo_rate * 120) / 144) * 10) / 10), ((((spo_rate * 119) / 144) * 10) / 10),
                           ((((spo_rate * 118) / 144) * 10) / 10), ((((spo_rate * 117) / 144) * 10) / 10),
                           ((((spo_rate * 116) / 144) * 10) / 10), ((((spo_rate * 115) / 144) * 10) / 10),
                           ((((spo_rate * 114) / 144) * 10) / 10), ((((spo_rate * 113) / 144) * 10) / 10),
                           ((((spo_rate * 112) / 144) * 10) / 10), ((((spo_rate * 111) / 144) * 10) / 10),
                           ((((spo_rate * 110) / 144) * 10) / 10), ((((spo_rate * 109) / 144) * 10) / 10),
                           ((((spo_rate * 108) / 144) * 10) / 10), ((((spo_rate * 179) / 240) * 10) / 10),
                           ((((spo_rate * 178) / 240) * 10) / 10), ((((spo_rate * 177) / 240) * 10) / 10),
                           ((((spo_rate * 176) / 240) * 10) / 10), ((((spo_rate * 175) / 240) * 10) / 10),
                           ((((spo_rate * 174) / 240) * 10) / 10), ((((spo_rate * 173) / 240) * 10) / 10),
                           ((((spo_rate * 172) / 240) * 10) / 10), ((((spo_rate * 171) / 240) * 10) / 10),
                           ((((spo_rate * 170) / 240) * 10) / 10), ((((spo_rate * 169) / 240) * 10) / 10),
                           ((((spo_rate * 168) / 240) * 10) / 10), ((((spo_rate * 167) / 240) * 10) / 10),
                           ((((spo_rate * 166) / 240) * 10) / 10), ((((spo_rate * 165) / 240) * 10) / 10),
                           ((((spo_rate * 164) / 240) * 10) / 10), ((((spo_rate * 163) / 240) * 10) / 10),
                           ((((spo_rate * 162) / 240) * 10) / 10), ((((spo_rate * 161) / 240) * 10) / 10),
                           ((((spo_rate * 160) / 240) * 10) / 10), ((((spo_rate * 159) / 240) * 10) / 10),
                           ((((spo_rate * 158) / 240) * 10) / 10), ((((spo_rate * 157) / 240) * 10) / 10),
                           ((((spo_rate * 156) / 240) * 10) / 10)]

        for i, aux_mba in zip(range(rf + 1), spouse_benefits):
            aux_mba = "{:.3f}".format(aux_mba)
            total = str(aux_mba)[:-2] + "0"
            calculated_benefits_b.append(total)
        return calculated_benefits_b


class DualAB(CalcSpouse):
    def __init__(self, spouse_pia, pia, month, day, year, protfl_month, pfdate):
        self.spouse_pia = float(spouse_pia)
        self.pia = float(pia)
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)
        self.protfl_month = protfl_month
        self.pfdate = pfdate

    def calc_benefits_spouse_portion(self):
        rf = self.calc_rf()
        rib = super().calc_benefits()
        spo_rate = (self.spouse_pia / 2) - self.pia
        calculated_rib = []
        total_mba = []
        aux_portion = []

        spouse_benefits = [spo_rate, ((((spo_rate * 143) / 144) * 10) / 10),
                           ((((spo_rate * 142) / 144) * 10) / 10), ((((spo_rate * 141) / 144) * 10) / 10),
                           ((((spo_rate * 140) / 144) * 10) / 10), ((((spo_rate * 139) / 144) * 10) / 10),
                           ((((spo_rate * 138) / 144) * 10) / 10), ((((spo_rate * 137) / 144) * 10) / 10),
                           ((((spo_rate * 136) / 144) * 10) / 10), ((((spo_rate * 135) / 144) * 10) / 10),
                           ((((spo_rate * 134) / 144) * 10) / 10), ((((spo_rate * 133) / 144) * 10) / 10),
                           ((((spo_rate * 132) / 144) * 10) / 10), ((((spo_rate * 131) / 144) * 10) / 10),
                           ((((spo_rate * 130) / 144) * 10) / 10), ((((spo_rate * 129) / 144) * 10) / 10),
                           ((((spo_rate * 128) / 144) * 10) / 10), ((((spo_rate * 127) / 144) * 10) / 10),
                           ((((spo_rate * 126) / 144) * 10) / 10), ((((spo_rate * 125) / 144) * 10) / 10),
                           ((((spo_rate * 124) / 144) * 10) / 10), ((((spo_rate * 123) / 144) * 10) / 10),
                           ((((spo_rate * 122) / 144) * 10) / 10), ((((spo_rate * 121) / 144) * 10) / 10),
                           ((((spo_rate * 120) / 144) * 10) / 10), ((((spo_rate * 119) / 144) * 10) / 10),
                           ((((spo_rate * 118) / 144) * 10) / 10), ((((spo_rate * 117) / 144) * 10) / 10),
                           ((((spo_rate * 116) / 144) * 10) / 10), ((((spo_rate * 115) / 144) * 10) / 10),
                           ((((spo_rate * 114) / 144) * 10) / 10), ((((spo_rate * 113) / 144) * 10) / 10),
                           ((((spo_rate * 112) / 144) * 10) / 10), ((((spo_rate * 111) / 144) * 10) / 10),
                           ((((spo_rate * 110) / 144) * 10) / 10), ((((spo_rate * 109) / 144) * 10) / 10),
                           ((((spo_rate * 108) / 144) * 10) / 10), ((((spo_rate * 179) / 240) * 10) / 10),
                           ((((spo_rate * 178) / 240) * 10) / 10), ((((spo_rate * 177) / 240) * 10) / 10),
                           ((((spo_rate * 176) / 240) * 10) / 10), ((((spo_rate * 175) / 240) * 10) / 10),
                           ((((spo_rate * 174) / 240) * 10) / 10), ((((spo_rate * 173) / 240) * 10) / 10),
                           ((((spo_rate * 172) / 240) * 10) / 10), ((((spo_rate * 171) / 240) * 10) / 10),
                           ((((spo_rate * 170) / 240) * 10) / 10), ((((spo_rate * 169) / 240) * 10) / 10),
                           ((((spo_rate * 168) / 240) * 10) / 10), ((((spo_rate * 167) / 240) * 10) / 10),
                           ((((spo_rate * 166) / 240) * 10) / 10), ((((spo_rate * 165) / 240) * 10) / 10),
                           ((((spo_rate * 164) / 240) * 10) / 10), ((((spo_rate * 163) / 240) * 10) / 10),
                           ((((spo_rate * 162) / 240) * 10) / 10), ((((spo_rate * 161) / 240) * 10) / 10),
                           ((((spo_rate * 160) / 240) * 10) / 10), ((((spo_rate * 159) / 240) * 10) / 10),
                           ((((spo_rate * 158) / 240) * 10) / 10), ((((spo_rate * 157) / 240) * 10) / 10),
                           ((((spo_rate * 156) / 240) * 10) / 10)]

        for i, rib_mba, spo_mba in zip(range(rf + 1), rib, spouse_benefits):
            rib_mba = "{:.3f}".format(float(rib_mba))
            rib_amt = str(rib_mba)[:-2] + "0"
            spo_mba = "{:.3f}".format(float(spo_mba))
            aux_bene = str(spo_mba)[:-2] + "0"
            calc_total = float(aux_bene) + float(rib_amt)
            calc_total = "{:.3f}".format(calc_total)
            total_amt = str(calc_total)[:-2] + "0"
            calculated_rib.append(rib_amt)
            aux_portion.append(aux_bene)
            total_mba.append(total_amt)

        return calculated_rib, aux_portion, total_mba


# Class created to calculate rib benefits - inherits from Calculate class - Inheritance
class CalcWidow(Calculate):
    def __init__(self, nh_deceased_pia, month, day, year, pension, rib_lim, nh_rib_amt, protfl_month):
        self.nh_deceased_pia = float(nh_deceased_pia)
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)
        self.pension = pension
        self.rib_lim = rib_lim
        self.nh_rib_amt = nh_rib_amt
        self.protfl_month = protfl_month

    def min_month_year(self, min_age=60):
        min_year = min_age + self.year
        min_month = self.month

        if self.day == 1:
            min_month = min_month - 1
            if min_month < 1:
                min_month = 12
                min_year = min_year - 1

        print(f'Minimum month and year is {min_month}/{min_year}')

    # Calculate FRA age for widows benefits
    def calc_fra_age_widows(self):

        if self.month == 1 and self.day == 1 and self.year == 1943 or self.year < 1943:
            fra_age = 65

        elif (self.month >= 1 and self.day >= 2 and 1943 <= self.year <= 1959 or self.month == 1 and
              self.day == 1 and self.year == 1960):
            fra_age = 66

        else:
            fra_age = 67

        return fra_age

    # Calculate fra month and year for widows benefits
    def calc_fra_month_year_widows(self):
        fra_month = self.month
        fra_age = self.calc_fra_age_widows()
        fra_year = self.year + fra_age

        if (self.month >= 1 and self.day > 1 and self.year == 1940 or
                self.month >= 2 and self.day >= 1 and self.year == 1940 or
                self.month == 1 and self.day == 1 and self.year == 1941 or
                self.month >= 1 and self.day >= 2 and self.year == 1957 or
                self.month >= 2 and self.day >= 1 and self.year == 1957 or
                self.month == 1 and self.day == 1 and self.year == 1958):
            fra_month = self.month + 2

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1941 or
              self.month >= 2 and self.day >= 1 and self.year == 1941 or
              self.month == 1 and self.day == 1 and self.year == 1942 or
              self.month >= 1 and self.day >= 2 and self.year == 1958 or
              self.month >= 2 and self.day >= 1 and self.year == 1958 or
              self.month == 1 and self.day == 1 and self.year == 1959):
            fra_month = self.month + 4

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1942 or
              self.month >= 2 and self.day >= 1 and self.year == 1942 or
              self.month == 1 and self.day == 1 and self.year == 1943 or
              self.month >= 1 and self.day >= 2 and self.year == 1959 or
              self.month >= 2 and self.day >= 1 and self.year == 1959 or
              self.month == 1 and self.day == 1 and self.year == 1960):
            fra_month = self.month + 6

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1943 or
              self.month >= 2 and self.day >= 1 and self.year == 1943 or
              self.month == 1 and self.day == 1 and self.year == 1944 or
              self.month >= 1 and self.day >= 2 and self.year == 1960 or
              self.month >= 2 and self.day >= 1 and self.year == 1960 or
              self.month == 1 and self.day == 1 and self.year == 1961):
            fra_month = self.month + 8

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        elif (self.month >= 1 and self.day > 1 and self.year == 1944 or
              self.month >= 2 and self.day >= 1 and self.year == 1944 or
              self.month == 1 and self.day == 1 and self.year == 1945 or
              self.month >= 1 and self.day >= 2 and self.year == 1961 or
              self.month >= 2 and self.day >= 1 and self.year == 1961 or
              self.month == 1 and self.day == 1 and self.year == 1962):
            fra_month = self.month + 10

            if self.day == 1:
                fra_month = fra_month - 1
                if fra_month < 1:
                    fra_month = 12
            if fra_month > 12:
                fra_month = fra_month - 12
                fra_year = fra_year + 1

        else:
            if self.day == 1:
                fra_month - fra_month - 1
                if fra_month < 1:
                    fra_month = 12

        return fra_month, fra_year

    # Calculates reduction factors for Widows/ers benefits
    def calc_rf_d(self):
        fra_month, fra_year = self.calc_fra_month_year_widows()
        rf = (fra_year - current_year) * 12 + (fra_month - current_month)
        max_rf = 0

        if rf <= 0:
            rf = 0

        elif self.year < 1940 or self.month == 1 and self.day == 1 and self.year == 1940:
            max_rf = 60
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1940 or
              self.month >= 2 and self.day >= 1 and self.year == 1940 or
              self.month == 1 and self.day == 1 and self.year == 1941):
            max_rf = 62
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1941 or
              self.month >= 2 and self.day >= 1 and self.year == 1941 or
              self.month == 1 and self.day == 1 and self.year == 1942):
            max_rf = 64
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1942 or
              self.month >= 2 and self.day >= 1 and self.year == 1942 or
              self.month == 1 and self.day == 1 and self.year == 1943):
            max_rf = 66
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1943 or
              self.month >= 2 and self.day >= 1 and self.year == 1943 or
              self.month == 1 and self.day == 1 and self.year == 1944):
            max_rf = 68
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1944 or
              self.month >= 2 and self.day >= 1 and self.year == 1944 or
              self.month == 1 and self.day == 1 and self.year == 1945):
            max_rf = 70
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year >= 1945 or
              self.month >= 2 and self.day >= 1 and self.year >= 1945 or
              self.month == 1 and self.day == 1 and self.year == 1957):
            max_rf = 72
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1957 or
              self.month >= 2 and self.day >= 1 and self.year == 1957 or
              self.month == 1 and self.day == 1 and self.year == 1958):
            max_rf = 74
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1958 or
              self.month >= 2 and self.day >= 1 and self.year == 1958 or
              self.month == 1 and self.day == 1 and self.year == 1959):
            max_rf = 76
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1959 or
              self.month >= 2 and self.day >= 1 and self.year == 1959 or
              self.month == 1 and self.day == 1 and self.year == 1960):
            max_rf = 78
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1960 or
              self.month >= 2 and self.day >= 1 and self.year == 1960 or
              self.month == 1 and self.day == 1 and self.year == 1961):
            max_rf = 80
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1961 or
              self.month >= 2 and self.day >= 1 and self.year == 1961 or
              self.month == 1 and self.day == 1 and self.year == 1962):
            max_rf = 82
            if rf >= max_rf:
                rf = max_rf

        elif (self.month >= 1 and self.day > 1 and self.year == 1962 or
              self.month >= 2 and self.day >= 1 and self.year == 1962 or
              self.year >= 1963):
            max_rf = 84
            if rf >= max_rf:
                rf = max_rf

        else:
            pass
        return rf, max_rf

    # Create month and year for result in widows benefits table
    def month_year(self):
        results = []
        rf, max_rf = self.calc_rf_d()
        fra_month, fra_year = self.calc_fra_month_year_widows()
        for i in range(rf + 1):
            results.append(f'{fra_month}/{fra_year}')
            fra_month = fra_month - 1
            if fra_month <= 0:
                fra_month = 12
                fra_year = fra_year - 1
        return results

    # Calculates widows benefits
    def calc_benefits_d(self):
        rib_lim = self.rib_lim
        rf, max_rf = self.calc_rf_d()
        if rf > 0 and rib_lim == 'n':
            for i in range(rf + 1):
                reduced_widow_mba = self.nh_deceased_pia - ((self.nh_deceased_pia * 0.285 * i) / max_rf)
                reduced_widow_mba = "{:.3f}".format(reduced_widow_mba)
                reduced_widow_mba = str(reduced_widow_mba)[:-2] + "0"
                yield reduced_widow_mba

        elif rf > 0 and rib_lim == 'y':
            rib_lim_amt = (((self.nh_deceased_pia * 0.825) * 10) / 10)
            if rib_lim_amt < float(self.nh_rib_amt):
                rib_lim_amt = self.nh_rib_amt

            for i in range(rf + 1):
                reduced_widow_mba = self.nh_deceased_pia - ((self.nh_deceased_pia * 0.285 * i) / max_rf)
                reduced_widow_mba = "{:.3f}".format(reduced_widow_mba)
                reduced_widow_mba = float(str(reduced_widow_mba)[:-2] + "0")

                if reduced_widow_mba > float(rib_lim_amt):
                    reduced_widow_mba = float(rib_lim_amt)
                    reduced_widow_mba = "{:.3f}".format(reduced_widow_mba)
                    reduced_widow_mba = str(reduced_widow_mba)[:-2] + "0"
                    yield reduced_widow_mba

                elif reduced_widow_mba < float(rib_lim_amt):
                    reduced_widow_mba = "{:.3f}".format(reduced_widow_mba)
                    reduced_widow_mba = str(reduced_widow_mba)[:-2] + "0"
                    yield reduced_widow_mba

        elif rf == 0 and rib_lim == "y":
            for i in range(rf):
                rib_lim_amt = (((self.nh_deceased_pia * 0.825) * 10) / 10)

            return rib_lim_amt

        else:
            return self.nh_deceased_pia

    # Calculate GPO offset
    def gpo_amount(self):
        gpo = round((float(self.pension) * 2) / 3, 2)
        return gpo

    # Calculate widows benefits after GPO
    def wib_with_gpo(self):
        gpo = self.gpo_amount()
        rf, max_rf = self.calc_rf_d()
        rib_lim_mba = self.calc_benefits_d()
        rib_lim = self.rib_lim

        # if rib limitation field is answered yes
        if rib_lim == "y":
            for i, gpo_mba in zip(range(rf + 1), rib_lim_mba):
                gpo_mba = yield str("{:.3f}".format(float(gpo_mba) - gpo))[:-2] + "0"
        else:
            for i in range(rf + 1):
                gpo_mba = yield str("{:.3f}".format(
                    (round((float(self.nh_deceased_pia - ((self.nh_deceased_pia * 0.285 * i) / max_rf) - gpo)), 3))))[
                                :-2] + "0"

        for i, reduced_widow_mba in zip(range(rf + 1), gpo_mba):
            if reduced_widow_mba <= 0:
                return 'Total Government Pension Offset - LAF SH'

            else:
                return reduced_widow_mba[:-2]


# Calculate Disabled Widows Benefits
class CalcDwb(CalcWidow):
    def __init__(self, nh_deceased_pia, month, day, year, pension):
        self.nh_deceased_pia = float(nh_deceased_pia)
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)
        self.pension = pension

    # Function that calculates DWB benefits
    def calc_benefits_w(self):
        current_age, months = super().current_age_with_months()
        dwb_mba = str("{:.3f}".format(self.nh_deceased_pia * 0.715))[:-2] + "0"
        if 50 <= current_age < 60:
            return f"Monthly benefits will be {dwb_mba}"
        elif current_age >= 60:
            return 'Claimant is not 50 to 59 1/2 years old. Please consider Widows Benefits or DWB for Medicare purpose'
        else:
            return 'Too young for disabled widows and aged widows benefits'

    # Function that calculates disabled widows benefits with GPO
    def dwb_with_gpo(self):
        gpo = super().gpo_amount()
        current_age, months = super().current_age_with_months()
        dwb_mba_gpo = round((self.nh_deceased_pia * 0.715) - gpo, 2)

        if 50 <= current_age <= 60:
            if dwb_mba_gpo <= 0:
                return 'Total Government Pension Offset - LAF SH'
            else:
                return f"Disabled Widows after government pension offset is {dwb_mba_gpo}"
        else:
            return 'Claimant is not 50 to 59 1/2 years old. Please consider Widows Benefits'


# Calculates dual entitlement RIB and widows benefits
class DualAD(CalcRib, CalcWidow):
    def __init__(self, nh_deceased_pia, pia, month, day, year):
        self.nh_deceased_pia = float(nh_deceased_pia)
        self.pia = float(pia)
        self.month = int(month)
        self.day = int(day)
        self.year = int(year)

    def calc_benefits_widows_portion(self):
        rf = self.calc_rf()
        widow_rf = self.calc_rf_d()
        widow_mba = super().calc_benefits_d()
        # rib_mba = super().calc_benefits()


# ribBenefits = CalcRib(800, 12, 12, 1970)
# spouseBenefits = CalcSpouse(2000, 12, 12, 1970)
# widowsBenefits = CalcWidow(1000.00, 1, 14, 1970, 300)
dwb_benefits = CalcDwb(1250.90, 1, 14, 1970, 100)
# dual_entitlement = DualAB(2000, 800, 12, 2, 1958)
# widowsBenefitsDual = DualAD(1000.00, 300.00, 1, 14, 1970)

# print(dual_entitlement.calc_benefits())
# print(widowsBenefits.calc_benefits_d())
# print(dual_entitlement.calc_benefits_spouse_portion())
# print(spouseBenefits.calc_benefits_b())

# print(dwb_benefits.current_age())

# testing = CalcRib(1000, 3, 27, 1954, 0, "n")
# print(testing.calc_drcs())
# print(testing.drc_months())
# print(testing.calc_mba_drcs())
# print(testing.calc_fra_month_rib_spouse())
