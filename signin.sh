LOGIN=`awk -F: '/^login:/{print $2}' credential.txt`
PASSWORD=`awk -F: '/^password:/{print $2}' credential.txt`
curl -s -D - -b cookie.txt -d "{\"Login\":\"$LOGIN\",\"Password\":\"$PASSWORD\"}" https://mslon001pngx.saas.hp.com/auth/authentication-endpoint/authenticate/login
