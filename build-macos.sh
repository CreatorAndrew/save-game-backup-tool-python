python2 -m PyInstaller --noconsole --icon=BackupTool.png BackupTool.py
cp *.json dist
cp LICENSE dist
cp *.command dist
cp -r Test dist/Test
rm -rf dist/BackupTool
codesign --force --timestamp --sign $SIGN_CERT_NAME dist/BackupTool.app/Contents/MacOS/*.dylib
codesign --force --timestamp --sign $SIGN_CERT_NAME dist/BackupTool.app/Contents/MacOS/*.so
codesign --force --timestamp --sign $SIGN_CERT_NAME dist/BackupTool.app/Contents/MacOS/Python
codesign --force --timestamp --sign $SIGN_CERT_NAME dist/BackupTool.app/Contents/MacOS/BackupTool
mv ./dist/BackupTool.app ./dist/Save\ Game\ Backup\ Tool.app
mv ./dist ./Save\ Game\ Backup\ Tool
7z a save-game-backup-tool-darwin-amd64.zip ./Save\ Game\ Backup\ Tool
rm -rf ./Save\ Game\ Backup\ Tool ./build
