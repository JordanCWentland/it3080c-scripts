function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}
function getDate{
    Get-Date -Format "dddd, MMMM dd, yyyy"
}

$IP = getIP
$DATE = getDate
$USER = $env:UserName
$COMPNAME = $env:COMPUTERNAME
$PSVer = $HOST.Version.Major


$BODY = ("this machines IP is $IP. User is $USER. Hostname is $COMPNAME. Running PowerShell Version $PSVer. Todays Date is $DATE ")

Send-MailMessage -To "leonardf@ucmail.uc.edu" -Cc "wentlajc@mail.uc.edu" -From "WentlajcSandbox@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)