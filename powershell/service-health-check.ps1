<#
.SYNOPSIS
Checks the status of a Windows service.

.DESCRIPTION
This script checks whether a specified Windows service
is running and logs the result. Designed as a reusable
automation function.

.AUTHOR
Glory Synala

.DATE
2026
#>

param (
    [Parameter(Mandatory = $true)]
    [string]$ServiceName
)

function Get-ServiceHealth {
    param (
        [string]$Name
    )

    try {
        $service = Get-Service -Name $Name -ErrorAction Stop
        Write-Output "$(Get-Date) - Service '$Name' is $($service.Status)"
    }
    catch {
        Write-Output "$(Get-Date) - Service '$Name' not found or inaccessible"
    }
}

Get-ServiceHealth -Name $ServiceName
