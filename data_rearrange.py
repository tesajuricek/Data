import pandas as pd
import openpyxl


df = pd.read_excel('F00008126-WV3_Data_Slovakia_Excel_v20221107.xlsx', sheet_name='Data')
mean_value = df['V110: Willingness to fight for country'].mean()
print(f"The mean value of the Willingness to fight for country column is: {mean_value}")

df = pd.read_excel('F00008126-WV3_Data_Slovakia_Excel_v20221107.xlsx', sheet_name='Data')

key_values = dict(zip(df['N_REGION_ISO: Region ISO'], df['V110: Willingness to fight for country']))

print(key_values)


# for index, row in df.iterrows():
#     column2_value = row.loc['V110: Willingness to fight for country']
#     print("Kraj x 1998 " + str(column2_value))

# N_REGION_ISO: Region ISO 3166-2
    
df = pd.read_excel('F00012987-WVS_Wave_7_Slovakia_Excel_v5.0.xlsx', sheet_name='Data')
mean_value = df['Q151: Willingness to fight for country'].mean()
print(f"The mean value of the Willingness to fight for country column is: {mean_value}")

list = []

for index, row in df.iterrows():
    column1_value = row.loc['N_REGION_ISO: Region ISO 3166-2']
    column2_value = row.loc['Q151: Willingness to fight for country']
    dvojica = [column1_value, column2_value]
    list.append(dvojica)

workbook = openpyxl.Workbook()
worksheet = workbook.active


for row in list:
    worksheet.append(row)

workbook.save('data.xlsx')
# print(list)
# print(worksheet)

dic = { "703001":"SK032",
   "703002":"SK010",
   "703003":"SK042",
   "703004":"SK023",
   "703005":"SK041",
   "703006":"SK022",
   "703007":"SK021",
   "703008":"SK031",}

SK010 = []
SK021 = []
SK022 = []
SK023 = []
SK031 = []
SK032 = []
SK041 = []
SK042 = []

for x in list:
    if str(x[0]) in dic:
        if dic[str(x[0])] == 'SK032':
            SK032.append(x[1])
        elif dic[str(x[0])] == 'SK010':
            SK010.append(x[1])
        elif dic[str(x[0])] == 'SK042':
            SK042.append(x[1])
        elif dic[str(x[0])] == 'SK023':
            SK023.append(x[1])
        elif dic[str(x[0])] == 'SK041':
            SK041.append(x[1])
        elif dic[str(x[0])] == 'SK022':
            SK022.append(x[1])
        elif dic[str(x[0])] == 'SK021':
            SK021.append(x[1])
        elif dic[str(x[0])] == 'SK031':
            SK031.append(x[1])

regions = [SK010, SK021, SK022, SK023, SK031, SK032, SK041, SK042]
region_names = ["SK010", "SK021", "SK022", "SK023", "SK031", "SK032", "SK041", "SK042"]
mean_regions = []

ochotny = 0


for x in regions:
    mean = sum(x) / len(x)
    mean_regions.append(mean)

reg_count = 0
for x in regions:
    for y in x:
        if y == 1:
            ochotny += 1
    print(f"Region {region_names[reg_count]}: {int(ochotny / (len(x)) * 100)}")
    reg_count += 1
    ochotny = 0
    
    
ochotny = 0
ucastnici = 0
 
for x in regions:
    ucastnici += len(x)
    for y in x:
        if y == 1:
            ochotny += 1

print(f"{ochotny/ucastnici*100 }")
