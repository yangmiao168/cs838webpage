import csv
import math
BIG_A = []
BIG_B = []
match = []
BIG_A_DIR="BIG_A.csv"
BIG_B_DIR="BIG_B.csv"
#define leagal year range
BEGIN_YEAR=1800
END_YEAR=2017

def load_table_A(table_A_dir):
	#load data from table A
	with open(table_A_dir, 'rb') as A:
		spamreader1 = csv.reader(A, delimiter=',', quotechar='|')
		for row in spamreader1:
			BIG_A.append(row)
	
	return BIG_A

def load_table_B(table_B_dir):
	#load data from table B
	with open(table_B_dir, 'rb') as B:
		spamreader1 = csv.reader(B, delimiter=',', quotechar='|')
		for row in spamreader1:
			BIG_B.append(row)
	
	return BIG_B
def find_row_by_id(id, isLeft):
	if isLeft:
		for i in range(len(BIG_A)):
			if BIG_A[i][0] == id:
				return BIG_A[i]
	else:
		for i in range(len(BIG_B)):
			if BIG_B[i][0] == id:
				return BIG_B[i]

def data_merging_and_creating_file(A_mat, B_mat):
	#implement data merging between data matrix A and B
	#write the merged and combined table into new matrix E
	with open("matches.csv", 'rb') as csvIn:
		reader1 = csv.reader(csvIn, delimiter=',',quotechar='|')
		for row in reader1:
			match.append(row)

		with open("table_E.csv", 'wb') as csvOut:
			writer = csv.writer(csvOut,delimiter = ',', quotechar='|')
			#remove titles
			A_mat = A_mat[1:]
			B_mat = B_mat[1:]
			l = len(match)
			for i in range(l):
				row = []
				id1 = match[0]
				id2 = match[4]
				row1 = find_row_by_id(id1, 1)
				row2 = find_row_by_id(id2, 0)
				#split name into first, middle, last name
				f1,m1,l1 = "","",""
				f2,m2,l2 = "","",""
				name = ""
				name1 = row1[0]
				name2 = row2[0]
				phone1 = row1[1]
				phone2 = row2[1]
				year1 = row1[2]
				year2 = row2[2]
				#begin merging between attributes of names
				name1 = name1.split()
				name2 = name2.split()
				#implement name merging rule
				f1 = name1[0].lower()
				if len(name1) == 3:
					m1 = name1[1].lower()
				l1 = name1[-1].lower()

				f2 = name2[0].lower()
				if len(name2) == 3:
					m2 = name2[1].lower()
				l2 = name2[-1].lower()

				if len(f1) > len(f2):
					name += f1
				else:
					name += f2
				name += " "
				if len(m1) > len(m2):
					name += m1
					name += " "
				else:
					name += m2
					name += " "

				if len(l1) > len(l2):
					name += l1
				else:
					name += l2

				row.append(name)

				# matching phone number

				real_phone1 = ""
				for c in phone1:
					if c.isdigit():
						real_phone1 += c

				real_phone2 = ""
				for c in phone2:
					if c.isdigit():
						real_phone2 += c
				phoneNum = ""
				if len(real_phone1) == 10:
					phoneNum = "(" + real_phone1[:3] + ")" +real_phone1[3:6] + "-" + real_phone1[6:]
				elif len(real_phone2) == 10:
					phoneNum = "(" + real_phone2[:3] + ")" +real_phone2[3:6] + "-" + real_phone2[6:]
				
				row.append(phoneNum)
				year_int_1 = 100000
				year_int_2 = 100000
				#merging attribute of year
				year1 = year1.strip()
				year2 = year2.strip()
				if year1.isdigit():
					year_int_1 = int(year1)
				if year2.isdigit():
					year_int_2 = int(year2)

				if year_int_1 in range(BEGIN_YEAR, END_YEAR) and year_int_2 not in range(BEGIN_YEAR, END_YEAR):
					year = year_int_1
				elif year_int_1 not in range(BEGIN_YEAR, END_YEAR) and year_int_2 in range(BEGIN_YEAR, END_YEAR):
					year = year_int_2
				else:
					year = min(year_int_2, year_int_1)
				if year == 100000:
					year = ""

				row.append(year)

				row.append(row1[3])
				row.append(row1[4])
				row.append(row2[3])
				row.append(row2[4])
				#write the merged value into data table E
				writer.writerow(row)	

if __name__ == "__main__":
	BIG_A = load_table_A(TABLE_A_DIR)
	BIG_B = load_table_B(TABLE_B_DIR)
	data_merging_and_creating_file(BIG_A, BIG_B)
	



