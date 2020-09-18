import win32com.client
ppt_instance = win32com.client.gencache.EnsureDispatch('PowerPoint.Application')
#open the powerpoint presentation headless in background
directory = 'C:\\Users\\Chris\\Desktop\\datos-ppt\\ppt_test\\'
ppt_a = 'ppt.pptx'
pres_a = directory + ppt_a
prs = ppt_instance.Presentations.Open(pres_a,ReadOnly=0)

n_cosas = 20
nr_slide = 1
#insert_index = 1
for i in range(1, n_cosas):
    prs.Slides(nr_slide).Copy()
    prs.Slides.Paste(Index=i)

pres_b = directory + 'new_ppt.pptx'
prs.SaveAs(pres_b)
prs.Close()

#kills ppt_instance
ppt_instance.Quit()
del ppt_instance