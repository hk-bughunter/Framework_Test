import xlsxwriter
class Export_Excelreport:
    @classmethod
    def makeExcel(cls):
        # 创建一个excel
        workbook = xlsxwriter.Workbook("export_report.xlsx")
        # 创建一个sheet
        worksheet = workbook.add_worksheet()
        workfomat = workbook.add_format({'bold': True,\
                                         'valign':'center',\
                                         'font_size':13})

        # --------1、准备数据并写入excel---------------
        # 向excel中写入数据，建立图标时要用到
        with open(r'WoniuBossTestLog.txt','r',encoding='utf-8') as f:
            eles = f.readlines()
            cmd = []
            for i in eles:
                ele = i.strip('\n')
                cmd.append(ele)
        k=0
        success = 0
        fail = 0
        for i in cmd:
            if '测试成功' in i:
                success+=1
            else:
                fail+=1
            data = [[i[5:]],[i[:4]]]

            # 写入数据
            worksheet.write_row('A1', ['用例编号'],workfomat)
            worksheet.write_row('B1', ['测试结果'],workfomat)
            worksheet.set_column(0,0,40)
            worksheet.write_row('A{}'.format(k+2), data[0])
            worksheet.write_row('B{}'.format(k+2), data[1])
            worksheet.write_row('C1', ['合计'],workfomat)
            worksheet.write_row('C2',['测试成功'])
            worksheet.write_row('C3',['测试失败'])
            worksheet.write_row('D2',[success])
            worksheet.write_row('D3',[fail])

            k+=1

        # --------2、生成图表并插入到excel---------------
        # 创建一个柱状图(pie chart)
        chart_col = workbook.add_chart({'type': 'column'})

        # 配置第一个系列数据
        chart_col.add_series({
            'name': 'Data statistics',
            'categories': '=Sheet1!$C$2:$C$3',     #x轴Item名称
            'values': '=Sheet1!$D$2:$D$3',         #x轴Item值
            'points': [
                {'fill': {'color': '#00CD00'}},
                {'fill': {'color': 'orange'}},
                {'fill': {'color': 'yellow'}},
                {'fill': {'color': 'gray'}},
            ],
            'data_labels':{'value': True},

        })

        # 设置图表的title 和 x，y轴信息
        chart_col.set_title({'name': 'Data statistics'})

        # 设置图表的风格
        chart_col.set_style(10)

        # 把图表插入到worksheet以及偏移
        worksheet.insert_chart('D8', chart_col, {'x_offset': 25, 'y_offset': 10})
        workbook.close()

        print('报告统计完成')

if __name__ == '__main__':
    re = Export_Excelreport()
    re.makeExcel()