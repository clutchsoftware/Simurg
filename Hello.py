import uno
import unohelper

from com.sun.star.task import XJobExecutor

class HelloWorldJob(unohelper.Base, XJobExecutor):
    def __init__(self, ctx):
        self.ctx = ctx

    def trigger(self, args):
        desktop = self.ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", self.ctx)
        model = desktop.getCurrentComponent()
        text = model.Text
        cursor = text.createTextCursor()
        text.insertString(cursor, "Hello World! \n", 0)

g_ImplementationHelper = unohelper.ImplementationHelper()

g_ImplementationHelper.addImplementation( \
    HelloWorldJob,
    "org.libreoffice.Hello",
    ("com.sun.star.task.Job",),)
