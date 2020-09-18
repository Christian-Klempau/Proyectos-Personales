import win32com.client

pptApp= win32com.client.gencache.EnsureDispatch('Powerpoint.Application')
presentation = pptApp.Presentations.Add()
slide = presentation.Slides.Add(1, 12)
myDiamond = slide.Shapes.AddShape(4, Top=100,Left=100, Width=20, Height=20)

presentation.SaveAs('newppt.pptx')
presentation.Close()

pptApp.Quit()
del pptApp