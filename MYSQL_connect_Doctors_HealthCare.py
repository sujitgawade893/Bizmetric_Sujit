# import pyodbc

# server = r"SUJIT\SQLEXPRESS"
# database = "HEALTH_CARE"  

# connection_string = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     f"SERVER={server};"
#     f"DATABASE={database};"
#     "Trusted_Connection=yes;"
#     "TrustServerCertificate=yes;"
# )

# conn = pyodbc.connect(connection_string)
# cursor = conn.cursor()

# print("Connection Successful")

# # cursor.execute('select * from HEALTH_CARE.[dbo].[Doctors]')
# # records = cursor.fetchall()
# # for row in records:
#     print(row)


# cursor.execute("select* from HEALTH_CARE.[dbo].[Doctors]")
# row=cursor.fetchone()
# print(row)


from decimal import Decimal

doctors = [('D01', 'Robert', 'Smith', 'Cardiology', '987-111-0001', 'robert.smith@hospital.com', 'City Hospital', 15, Decimal('750.00'), 'Morning', 'Cardiology', 'C101', 12, 450, Decimal('4.80'), 'Fellowship', True, 'Senior Cardiologist')
,('D02', 'Emily', 'Johnson', 'Endocrinology', '987-111-0002', 'emily.j@hospital.com', 'City Hospital', 12, Decimal('650.00'), 'Afternoon', 'Endocrinology', 'E101', 8, 320, 
Decimal('4.70'), 'Board Certified', True, 'Diabetes specialist'),('D03', 'Michael', 'Williams', 'Pulmonology', '987-111-0003', 'michael.w@hospital.com', 'City Hospital', 18, Decimal('800.00'), 'Full Day', 'Pulmonology', 'P101', 15, 520, Decimal('4.90'), 'Fellowship', True, 'Asthma expert')
,('D04', 'Sarah', 'Brown', 'Rheumatology', '987-111-0004', 'sarah.b@hospital.com', 'City Hospital', 10, Decimal('600.00'), 'Morning', 'Rheumatology', 'R101', 6, 280, Decimal('4.60'), 'Board Certified', True, 'Joint specialist')
,('D05', 'David', 'Jones', 'Neurology', '987-111-0005', 'david.j@hospital.com', 'City Hospital', 14, Decimal('700.00'), 'Evening', 'Neurology', 'N101', 10, 380, Decimal('4.80'), 'Fellowship', False, 'On leave')
,('D06', 'Lisa', 'Davis', 'Cardiology', '987-111-0006', 'lisa.d@hospital.com', 'City Hospital', 8, Decimal('680.00'), 'Morning', 'Cardiology', 'C102', 9, 250, Decimal('4.50'), 'Resident', True, 'Junior cardiologist')
,('D07', 'Raj', 'Patel', 'Endocrinology', '987-111-0007', 'raj.p@hospital.com', 'City Hospital', 11, Decimal('620.00'), 'Afternoon', 'Endocrinology', 'E102', 7, 290, Decimal('4.60'), 'Board Certified', True, 'Thyroid specialist')
,('D08', 'Priya', 'Singh', 'Pulmonology', '987-111-0008', 'priya.s@hospital.com', 'City Hospital', 16, Decimal('780.00'), 'Full Day', 'Pulmonology', 'P102', 14, 410, Decimal('4.80'), 'Fellowship', True, 'COPD expert')
,('D09', 'Amit', 'Kumar', 'Rheumatology', '987-111-0009', 'amit.k@hospital.com', 'City Hospital', 9, Decimal('590.00'), 'Morning', 'Rheumatology', 'R102', 5, 220, Decimal('4.40'), 'Resident', True, 'Autoimmune diseases'),('D10', 'Neha', 'Sharma', 'Neurology', '987-111-0010', 'neha.sh@hospital.com', 'City Hospital', 13, Decimal('690.00'), 'Evening', 'Neurology', 'N102', 11, 340, Decimal('4.70'), 'Board Certified', True, 'Stroke specialist')
,('D11', 'James', 'Wilson', 'Cardiology', '987-111-0011', 'james.w@hospital.com', 'City Hospital', 20, Decimal('850.00'), 'Morning', 'Cardiology', 'C103', 18, 620, Decimal('4.90'), 'Fellowship', True, 'Heart failure')
,('D12', 'Anita', 'Gupta', 'Endocrinology', '987-111-0012', 'anita.g@hospital.com', 'City Hospital', 7, Decimal('580.00'), 'Afternoon', 'Endocrinology', 'E103', 6, 180, Decimal('4.30'), 'Resident', True, 'Pediatric endo')
,('D13', 'Vikram', 'Rao', 'Pulmonology', '987-111-0013', 'vikram.r@hospital.com', 'City Hospital', 19, Decimal('820.00'), 'Full Day', 'Pulmonology', 'P103', 16, 480, Decimal('4.90'), 'Fellowship', True, 'Lung cancer')
,('D14', 'Rina', 'Mehta', 'Rheumatology', '987-111-0014', 'rina.m@hospital.com', 'City Hospital', 12, Decimal('640.00'), 'Morning', 'Rheumatology', 'R103', 8, 310, Decimal('4.70'), 'Board Certified', True, 'Lupus specialist')
,('D15', 'Suresh', 'Nair', 'Neurology', '987-111-0015', 'suresh.n@hospital.com', 'City Hospital', 15, Decimal('720.00'), 'Evening', 'Neurology', 'N103', 12, 390, Decimal('4.80'), 'Fellowship', True, 'Epilepsy expert')
,('D16', 'Maria', 'Fernandes', 'Cardiology', '987-111-0016', 'maria.f@hospital.com', 'City Hospital', 6, Decimal('560.00'), 'Morning', 'Cardiology', 'C104', 4, 150, Decimal('4.20'), 'Resident', True, 'Echo specialist')
,('D17', 'Karan', 'Malhotra', 'Endocrinology', '987-111-0017', 'karan.m@hospital.com', 'City Hospital', 10, Decimal('610.00'), 'Afternoon', 'Endocrinology', 'E104', 7, 260, Decimal('4.50'), 'Board Certified', True, 'Obesity clinic')
,('D18', 'Deepa', 'Joshi', 'Pulmonology', '987-111-0018', 'deepa.j@hospital.com', 'City Hospital', 17, Decimal('790.00'), 'Full Day', 'Pulmonology', 'P104', 13, 430, Decimal('4.80'), 'Fellowship', True, 'Sleep apnea') ]


# print(len(doctors))

#*********select all data from table
# for d in doctors:
#     print(d)

#***************NAME AND DEPARTMENT
# for d in doctors:
#     print(d[1], d[3])

# *****WHERE DEPARTMENT IS CARDIOLOGY
# for i in doctors:
#   if i[3] =='Cardiology':
#     print(i)

#*******WHERE Rating >= 4.8
# for i in doctors:
#     if i[14] >= 4.8:
#         print("name is : ",i[1]," and rating is :",i[14])


#5️⃣ WHERE Availability = True

# for s in doctors:
#     if s[16]== 1:
#         print(s[2],"Availability status : ",s[16])

#6️⃣ ORDER BY Fees ASC
# result = sorted(doctors, key=lambda x: x[8])
# for d in result:
#     print(d[1], d[8])


# 7️⃣ ORDER BY Experience DESC
# result = sorted(doctors, key=lambda x: x[7], reverse=True)
# for d in result:
#     print(d[1], d[7])

#8️⃣ COUNT Doctors
#print(len(doctors))

#9️⃣ COUNT Doctors WHERE Department='Neurology'
# count = 0
# for d in doctors:
#     if d[3] == 'Neurology':
#         count += 1
#print(count)

#🔟 AVG Fees
total = 0
for d in doctors:
    total += d[8]

avg = total / len(doctors)
print(avg)

