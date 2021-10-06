from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    directorySet = False
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.btnBrowse.clicked.connect(self.browse_folder) 
        self.btnShuffle.clicked.connect(self.shuffle)
    def browse_folder(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory
        if directory:
            self.directorySet = True
            self.btnShuffle.setEnabled(True)
            self.btnBrowse.setText(directory)

    def shuffle(self):
        if(self.directorySet):
            command = "python ipod-shuffle-4g.py"
            if self.chkTrackVoiceOver.isChecked():
                command = command + " -t "
            if self.chkPlaylistVoiceOver.isChecked():
                command = command + " -p "
            if self.chkRenameUnicode.isChecked():
                command = command + " -u "
            if self.chkTrackGain.isChecked():
                command = command + " -g " + str(self.trackGain.value())
            if self.chkAutoDirectoryPlaylist.isChecked():
                command = command + " -d "
            if self.chkID3Template.isChecked():
                command = command + " -i " + str(self.templateTxt.text()) + " "
            command = command + str(self.btnBrowse.text())
            print command
            import os
            os.system(command)
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
