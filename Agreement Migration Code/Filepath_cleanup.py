import os
import xlwt
from xlwt import Workbook
import xlsxwriter

#counter = 000001
#ID = "DOC" + counter
row=1
IDrow = 0
destTypecolumn = 1
destID = 2
destAttrPathcolumn = 3
destAttrIsSetcolumn = 4
friendlyFileNamecolumn = 5
RelativeFilePathcolumn = 6


wb = xlsxwriter.Workbook('/Users/everetmm/Desktop/Agreement_Documentspt2.xlsx')

ws = wb.add_worksheet()

ws.write('A1','id')
ws.write('B1','destType')
ws.write('C1','destID')
ws.write('D1','destAttrPath')
ws.write('E1','destAttrIsSet')
ws.write('F1','friendlyFileName')
ws.write('G1','relativeFilePath')


root_dir = "/Users/everetmm/Desktop/Agreement_Migration_pt2"

#NO ./ for filepath names!, FUTURE MADISON
#Agreements should have custom attributes

for dir_, _,files in os.walk(root_dir):
     for file_name in files:
               if "(Original)" in file_name:
                   ws.write(row, destTypecolumn, '_ClickAgreement')
                   ws.write(row,destID,file_name[19:24])
                   rel_dir = os.path.relpath(dir_,root_dir)
                   rel_file = os.path.join(rel_dir, file_name)
                   ws.write(row, RelativeFilePathcolumn, "Agreement_Migration_pt2/"+rel_file)
                   ws.write(row, friendlyFileNamecolumn, file_name[27:(len(file_name)-4)])
                   ws.write(row, destAttrPathcolumn, 'customAttributes.agreement')
                   ws.write(row, destAttrIsSetcolumn, '0')
                   row +=1
               if "(Original)" not in file_name:
                    ws.write(row, destTypecolumn, '_ClickAgreement')
                    ws.write(row,destID,file_name[9:14])
                    rel_dir = os.path.relpath(dir_,root_dir)
                    rel_file = os.path.join(rel_dir, file_name)
                    ws.write(row, RelativeFilePathcolumn, "Agreement_Migration_pt2/"+rel_file)
                    ws.write(row, friendlyFileNamecolumn, file_name[17:(len(file_name)-4)])
                    ws.write(row, destAttrPathcolumn, 'documents')
                    ws.write(row, destAttrIsSetcolumn, '1')
                    row +=1

    
    
wb.close()
