function getIP{
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}

function getVersion{
(Get-Host).Version.Major
}

$IP = getIP
$VERSION = getVersion
$DATE = Get-Date
$BODY = "This machine's IP is $IP. User is $env:USERNAME. Host is $env:computername. Powershell Version $VERSION. Today's Date is $DATE."

#Write-Host("This machine's IP is $IP")
#Write-Host("$BODY")
$BODY | Out-File -FilePath C:\Users\Administrator\Downloads\sysinfo.txt
#Failed: "This machine's IP is " + $IP +". User is " + $env:USERNAME + ". Host is "+ $env:computername + ". Powershell Version " + $VERSION + ". Today's Date is " + $DATE + "."

#Next line is to make sure it prints correctly. Will be commented out when confirmed output is correct.
#This works, but putting it into a variable doesn't??: Write-Host("This machine's IP is $IP. User is $env:USERNAME. Host is $env:computername. Powershell Version $VERSION. Today's Date is $DATE.") 
#"This machine's IP is $IP. User is $env:USERNAME. Host is $env:computername. Powershell Version $VERSION. Today's Date is $DATE." | Out-File -FilePath C:\Users\Administrator\Downloads\sysinfo.txt

#Send-MailMessage -To "chambesi@mail.uc.edu" 
#-From "chambesi@mail.uc.edu" 
#-Subject "IT3038C Windows SysInfo" 
#-Body $BODY 
#-SmtpServer smtp.office365.com -port 587 -UseSSL