echo " [] DownLoading messages ..."
urls=`head -n 1 urlss.txt`
wget https://emailfake.com/$urls -q -O facebook.txt
cat facebook.txt | nokogiri -e 'puts $_.search('\''div'\'')' >> codes.txt
code=`grep "confirm" codes.txt | grep -o -P '(?<=>).*(?= )' | grep -o '[0-9][0-9]*' | head -n 1`
clear
echo "$code" >> confirm_code.txt
email=`head -n 1 email.txt`
heads="email_and_pass: "
space="                     Confirm_code: "
code=`head -n 1 confirm_code.txt`
log=$heads$email$space$code
echo "$log" >> logs.txt