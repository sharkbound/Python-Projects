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

if __name__ == '__main__':
    file = open(csv_path, 'r')
    reader = csv.reader(file)
    header = next(reader)

    total_donation_amount = 0
    all_valid_donations = []
    donations = []
    for row in reader:
        if "Donation Payment" in row:
            donations.append(row)

    for d in donations:
        if float(d[5]) <= 0.10:
            continue
        all_valid_donations.append(Donation(float(d[5]), d[11]))
        total_donation_amount += float(d[5])

    all_valid_donations.sort(key=lambda x: x.sender_donation, reverse=True)
    with open(output, 'w') as output_file:
        for donation in all_valid_donations:
            output_file.write(donation.formatted() + '\n')
        output_file.write(f'\n\nTotal donation count: {len(all_valid_donations)}\n')
        output_file.write(f'Total Donations: {total_donation_amount}\n')
        output_file.write(f'Average donation amount: {(total_donation_amount / len(all_valid_donations)):.3}')

    # print('Do you want to open the output text file? [Y/N]')
    # if (getch()):
    #     os.system(rf'{output}')
