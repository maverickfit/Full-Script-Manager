#This test is to check for correct WebView signing keys
#Only works on MacBook?? ---> Look into this???? --> this test suite probs needs to be tested on other stuff too
#Color Palette
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[1;34m'
PURPLE='\033[1;35m'
YELLOW='\033[0;93m'
CYAN='\033[1;36m'
GRAY='\033[37m'
NC='\033[0m' #No Color'

echo "Collecting Android System WebView Signing Keys"
echo

WEBVIEW_PATH=$(adb shell pm path com.android.webview | sed 's/^package://')
mkdir ./Results/webviewPackage
adb pull $WEBVIEW_PATH ./Results/webviewPackage
PACKAGE_NAME=$(ls ./Results/webviewPackage)
unzip ./Results/webviewPackage/$PACKAGE_NAME -d ./Results/webviewPackage
keytool  -printcert -file ./Results/webviewPackage/META-INF/CERT.RSA > ./Results/webviewKeys.txt
rm -rf ./Results/webviewPackage #Clean up

cat ./Results/webviewKeys.txt | grep SHA1 | head -n1 | tr -d '[:blank:]' | sed 's/^SHA1://' > ./Results/SHA1.txt
cat ./Results/webviewKeys.txt | grep SHA256 | head -n1 | tr -d '[:blank:]' | sed 's/^SHA256://' > ./Results/SHA256.txt

