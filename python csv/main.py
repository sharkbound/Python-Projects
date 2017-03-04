import csv
import os
from msvcrt import getch

csv_path = "paypal.CSV"
output = "output.txt"


class Donation:
    def __init__(self, amt, name):
        self.sender_donation = amt
        self.sender_name = name

    def formatted(self):
        return f'{self.sender_name} -> ${self.sender_donation}'

    def __str__(self):
        return f'{self.sender_name} -> ${self.sender_donation}'


if __name__ == '__main__':
    file = open(csv_path, 'r')
    reader = csv.reader(file)
    header = next(reader)

    total_donation_amount = 0
    donations = []
    for row in reader:
        if "Donation Payment" in row:
            if float(row[5]) <= 0.10:
                continue

            gross = float(row[5])
            donations.append(Donation(gross, row[11]))
            total_donation_amount += gross

    donations.sort(key=lambda x: x.sender_donation, reverse=True)
    with open(output, 'w') as output_file:
        for donation in donations:
            output_file.write(str(donation) + '\n')
        output_file.write(f'\nTotal donation count: {len(donations)}\n')
        output_file.write(f'Total Donation Amount: ${total_donation_amount}\n')
        output_file.write(f'Average donation amount: ${(total_donation_amount / len(donations)):.3}')
    # os.system(output)
    print('Do you want to open the output text file? [Y/N]')
    if (ord(getch()) == 121):
        os.system(rf'{output}')
