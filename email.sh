#!/bin/bash

# If it redirects to http://www.facebook.com/login.php at the end, wait a few minutes and try again

user=$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM
domain=`shuf -n 1 new_domain.txt`
amp="@"
email=$user$amp$domain
slash="/"
urls=$domain$slash$user$slash
echo "$urls" >> urlss.txt
echo "$User" >> user.txt
echo "$domain" >> domain.txt
echo "$email" >> email.txt

clear





