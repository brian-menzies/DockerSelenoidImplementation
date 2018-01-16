<#

	.Synopsis 
        Disables Internet Explorer Enhanced Security(IE ESC).
        
    .Description
        This script disables IE ESC on list of given Windows 2008 servers
 
    .Parameter ComputerName    
        Computer name(s) for which you want to disable IE ESC.
	
	.Parameter OutputToLogs
		This option allows you to save the failed and successful computer names to text files in
		c:\ drive. The successful computer will be avialable in c:\successcomps.txt file and the 
		failed computers will be in c:\failedcomps.txt
	
	.Example
        Disable-IEESC.PS1 -ComputerName Comp1, Comp2
		
		Disables IE ESC on Comp1 and Comp2
    .Example
        Disable-IEESC.PS1 -ComputerName Comp1, Comp2 -OutputToLogs
        
		Disables IE ESC and stores output in logfiles located in c:\ 
		
	.Example
        Get-Content c:\servers.txt | Disable-IEESC.PS1 -OutputToLogs
        
		Disables IE ESC on computers listed in servers.txt and saves success and failed computers list to c:\	
       
    .Notes
        NAME:      Disable-IEESC.PS1
        AUTHOR:    Sitaram Pamarthi
		WEBSITE:   http://techibee.com

#>

[cmdletbinding()]
param(
	[parameter(ValueFromPipeline=$true,ValueFromPipelineByPropertyName=$true)]
	[string[]]$ComputerName = $env:computername,
	[switch]$OutputToLogs
	
)

begin {
	$AdministratorsKey = "SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}"
	$UsersKey = "SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}"
	$SuccessComps =@();
	$FailedComps = @();
}

process {
	foreach($Computer in $ComputerName) {
		if(!(Test-Connection -Computer $Computer -count 1 -ea 0)) {
			Write-Host "$Computer NOT REACHABLE"
			$FailedComps += $Computer
			continue
		}

		Write-Host "Working on $Computer"
		try {
			$BaseKey = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey("LocalMachine",$Computer)
			$SubKey = $BaseKey.OpenSubKey($AdministratorsKey,$true)
			$SubKey.SetValue("IsInstalled",0,[Microsoft.Win32.RegistryValueKind]::DWORD)
			$SubKey = $BaseKey.OpenSubKey($UsersKey,$true)
			$SubKey.SetValue("IsInstalled",0,[Microsoft.Win32.RegistryValueKind]::DWORD)
			Write-Host "Successfully disabled IE ESC on $Computer"
			$SuccessComps += $Computer
		}
		catch {
			Write-Host "Failed to disable IE ESC on $Computer"
			$FailedComps += $Computer
		}
		
	}
}

end{
	if($OutputToLogs) {
		$SuccessComps | Out-File "c:\successcomps.txt"
		$FailedComps | Out-File "c:\failedcomps.txt"
	}
}
