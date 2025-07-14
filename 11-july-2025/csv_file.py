import csv

"""one way to read and write into files"""
# with open('sales.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_sales.csv', 'w') as new_csvfile:
#         csv_writer = csv.writer(new_csvfile, delimiter='\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

"""Another way is through Dict methods"""
with open('sales.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_sales.csv', 'w') as new_csvfile:
        fieldnames = ['Name','City','JobTitle','FavoriteColor','FavoriteFood']
        csv_writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            del line['FavoriteFood']
            csv_writer.writerow(line)