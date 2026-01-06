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


<#
NOTE ON PARAMETER NAMING & DESIGN

Question:
Why is the script-level parameter ($ServiceName) different from the
function-level parameter ($Name)?

Explanation:
The script parameter and function parameter exist in different scopes.
$ServiceName represents user input provided when the script is executed,
while $Name is a local parameter used inside the function.

The value of $ServiceName is explicitly passed to the function:
Get-ServiceHealth -Name $ServiceName

This design keeps the function self-contained and reusable. The function
does not depend on external variables and can be independently called
with any service name.

Benefits:
- Clear separation of responsibilities
  * Script handles input
  * Function handles logic
- Improved reusability and testability
- Avoids hidden dependencies on global or script-level variables
- Aligns with PowerShell best practices for modular automation

This approach ensures cleaner, maintainable, and enterprise-ready code.
#>
