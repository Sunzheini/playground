# importing windows c# dll

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import *
from System.Drawing import *


class MyForm(Form):
    def __init__(self):
        self.Text = "Hello World"
        self.Width = 300
        self.Height = 200
        self.CenterToScreen()

        self.button = Button()
        self.button.Text = "Click Me"
        self.button.Location = Point(100, 50)
        self.button.Click += self.button_click

        self.Controls.Add(self.button)

    def button_click(self, sender, args):
        MessageBox.Show("Hello World")


form = MyForm()
Application.Run(form)

