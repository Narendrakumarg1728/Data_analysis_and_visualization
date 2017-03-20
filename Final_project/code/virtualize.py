from bokeh.io import vplot, output_file, show, hplot
from bokeh.plotting import figure, ColumnDataSource #, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, Legend, Label
from bokeh.embed import components
from numpy import nan
import xlrd
excel_sheet = xlrd.open_workbook("../data/SurvivalByStage.xlsx")
sheet1= excel_sheet.sheet_by_name('All US')
cancer_type_survival={}

c_type_list = []
survival_list = []
stage1_list = []
stage2_list = []
stage3_list = []
stage4_list = []
                                                                                         #Data Wrangling to get the data from SurvivalByStage.xlsx
for i in range(8, sheet1.nrows):                              
    row = sheet1.row_slice(i)
    c_type = row[0].value
    survival = row[1].value
    stage1 = row[5].value
    stage2 = row[6].value
    stage3 = row[7].value
    stage4 = row[8].value
    print c_type,survival, stage1, stage2, stage3, stage4
    c_type_list.append(c_type)
    survival_list.append(survival)
    stage1_list.append(stage1)
    stage2_list.append(stage2)
    stage3_list.append(stage3)
    stage4_list.append(stage4)
    print c_type_list
    print stage1_list
    print stage2_list
    print stage3_list
    print stage4_list

"""for i in range(8, sheet1.nrows):        
    row = sheet1.row_slice(i)        
    country = row[1].value        
    survival = row[2].value        
    stage1 = row[6].value
    stage2 = row[7].value
    stage3 = row[8].value
    stage4 = row[9].value
    print country,survival, stage1, stage2, stage3, stage4"""
                                                                                        #Function to select different colors depending on the survival rate and mortality
def color_filler(x):                                                                        
    y = []
    colors_rgb = ["rgb(255, 0, 0)", "rgb(0, 255, 0)", "rgb(0, 0, 255)"]

    red = "rgb(255, 0, 0)"
    green = "rgb(0, 255, 0)"
    yellow = "rgb(255, 255, 0)"
    cyan = "rgb(0,255,255)"
    magenta = "rgb(255,0,255)"

    for i in x:
        if i == 101:
            y.append(cyan)
        elif i == 102:
            y.append(magenta)
        elif i >=90:
            y.append(green)
        elif i >= 40:
            y.append(yellow)
        else:
            y.append(red)
    print y
    return y
                                                                                    #Different cancer type
factors = ["Brain and other nervous system", "Breast", "Cervix", "Colorectum", "Esophagus", "Hodgkin lymphoma", "Kidney and renal pelvis","Larynx", "Liver and intrahepatic bile duct", "Lung and bronchus", "Melanoma of the skin","Myeloma", "Non-Hodgkin lymphoma", "Oral cavity and pharynx", "Ovary","Pancreas","Prostate", "Stomach", "Testis", "Thyroid", "Urinary bladder", "Uterine corpus"]  
x = [34,90,68,65,18,86,74,61,18,18,92,49,71,64,46,8,99,30,95,98,78,82]                         #Average Survival rate for all cancer types
                                                                                               #% year average survival rate graph plot confi
hover1 = HoverTool(
        tooltips=[
                 ("Cancer Type",  "$y"),
                     ("Survival rate",  "$x{int}")])
s1 = figure(y_range=factors,tools=[hover1],plot_width=700, plot_height=800,title="5 Years Relative Survival Rate", title_location="above", toolbar_location=None)
col = color_filler(x)
s1.circle(x, factors, size=20, fill_color=col, line_width=1)
s1.xaxis.axis_label = 'Survival Rate (in %)'
s1.yaxis.axis_label = 'Cancer Type'
s1.title.text_font_size = "25px"
                                                                                               #5 Year survival rate for breast and colon cancer for different stages data config

x1 = [100,92]
col1 = color_filler(x1)

cancer_type = ["Breast", "Colorectum"]
source1 = ColumnDataSource(
        data=dict(
                  x1=[100,92],
                  cancer_type = ["Breast", "Colorectum"],
                  stages=['1', '1']
                                  ))

x2 = [93,63]
col2 = color_filler(x2)
source2 = ColumnDataSource(
        data=dict(
                  x2=[93,63],
                  cancer_type = ["Breast", "Colorectum"],
                  stages=['2', '2']
                                  ))

x3 = [72,53]
col3 = color_filler(x3)

source3 = ColumnDataSource(
        data=dict(
                  x3=[72,53],
                  cancer_type = ["Breast", "Colorectum"],
                  stages=['3', '3']
                                  ))

x4 = [22,11]
col4 = color_filler(x4)
source4 = ColumnDataSource(
          data=dict(
                  x4=[22,11],
                  cancer_type = ["Breast", "Colorectum"],
                  stages=['4', '4']
                                  ))
hover2 = HoverTool( 
        tooltips=[
                 ("Cancer Type",  "$y"),
                 ("Survival rate",  "$x{int}"),
                 ("Stage", "@stages"),
                                                             ]
                                                                                               #5 Year survival rate for breast and colon cancer plot config
                                                             )
s2 = figure(y_range=cancer_type, tools=[hover2], plot_width=700, plot_height=375,title="5 Years Survival Rate at Different Stages", toolbar_location=None )
r1 =  s2.circle(x1, cancer_type, size=20, fill_color=col1, line_width=1, source=source1,)# legend ="Promising")
s2.circle(x2, cancer_type, size=20, fill_color=col2, line_width=1, source=source2) 
r3 = s2.circle(x3, cancer_type, size=20, fill_color=col3, line_width=1, source=source3,)# legend = "Moderate")
r4 = s2.circle(x4, cancer_type, size=20, fill_color=col4, line_width=1, source=source4,)# legend = "Terminal")
output_file("Cancer_survival.html")

legend = Legend(items=[
                       ("Promising"   , [r1]),
                       ("Moderate" , [r3]),
                       ("Terminal" , [r4]),
                                               ], location=(10,-50))


s2.xaxis.axis_label = 'Survival Rate (in %)'
s2.yaxis.axis_label = 'Cancer Type'
s2.title.text_font_size = "25px"
#p = hplot(s1,s2)

s2.add_layout(legend, 'right')


label_opts2 = dict(
    x=230, y=0,
        x_units='screen', y_units='screen'
        )

msg = '(For Breast and Colorectum Cancer)'                                                    #Subtitle addition hack as it is not supported adding through label for plot breats and cancer survival for different cancers        
caption = Label(text =msg, **label_opts2)
s2.add_layout(caption, "above")

                                                                                              #Data config for for plot breats and cancer survival for different cancers
countries = ["World - New Cases", "World - Deaths", "Developed Regions - New Cases","Developed Regions - Deaths", "Under Developed Regions - New Cases", "Under Developed Regions - Deaths"]
countries_new_cases= ["World New Cases", "Developed Regions - New Cases", "Under Developed Regions - New Cases"]
countries_deaths= [ "World Deaths", "More Developed Regions Deaths",  "Under Developed Regions - Deaths"]
stats_new_cases = [1671, nan, 788, nan, 883, nan]
stats_deaths = [nan, 522, nan, 198, nan, 324]

col_cayan = color_filler([101,101,101,101,101,101])
col_magenta = color_filler([102,102,102,102,102,102])
#col_yellow = "rgb(255, 255, 0)"  
#col_red = "rgb(255, 255, 0)"  
stats_data = ColumnDataSource(
                  data=dict(
                  stats_new_cases = [1671, nan, 788, nan, 883, nan],
                  countries = ["World New Cases", "World Deaths", " More developed regions New Cases"," More developed regions Deaths", "Less developed regions New Cases", "Less developed regions Deaths"]
                                  ))
                                                                                              #Plot config for breats and cancer survival for different cancers
hover3 = HoverTool( 
        tooltips=[
                 ("Location:",  "$y"),
                 ("Number of cases reported:",  "$x{int}"),
                                                             ]
                                                             )
s3 = figure(y_range = countries, tools=[hover3], plot_width=700, plot_height=425,title="Breast Cancer Mortality & New Cases", toolbar_location=None )
l1 = s3.circle(stats_new_cases, countries, size=20, fill_color=col_cayan, line_width=1, source=stats_data,)# legend ="Promising")
l2 = s3.circle(stats_deaths, countries, size=20, fill_color=col_magenta, line_width=1,) #source=stats_data) 

legend_stat = Legend(items=[
                       ("New Cases" , [l1]),
                       ("Deaths" , [l2]),
                                            ], location=(10,-50))
s3.add_layout(legend_stat, 'right')
"""s3 = figure(width=300, height=300)
s3.hbar(y = [1,2,3], height=0.5, left = 0, right = stats_new_cases, color="#CAB2D6")
s3.hbar(y = [1,2,3], height=0.5, left = 0, right = stats_deaths, color="#CAB2D6")"""
#vertical_plot = vplot(p,s3)
s3.xaxis.axis_label = 'Estimated Number of Cases (1000)'
#s3.yaxis.axis_label = 'Cancer Type'
s3.title.text_font_size = "25px"

label_opts = dict(
    x=230, y=0,
        x_units='screen', y_units='screen'
        )

msg1 = '(Based on Developed and under developed Region)'                                                   #Subtitle addition hack as it is not supported adding through label for plot: mortality and new cases for breast cancer plot.        
caption1 = Label(text =msg1, **label_opts)
s3.add_layout(caption1, "above")

p = hplot(s1,vplot(s2,s3))

"""p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"""
#show(vertical_plot)
show(p)



#plots = {'Average': s1, "Stages": s2}

#script, div = components(plots)

#print script
#print div


