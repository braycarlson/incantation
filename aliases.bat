@echo off

REM File and directory operations
doskey ls=dir /B $*
doskey ll=dir /B $*
doskey la=dir /A $*
doskey lal=dir /B /A $*
doskey rm=del $*
doskey cp=copy $*
doskey mv=move $*
doskey mkdir=md $*
doskey rmdir=rd $*

REM Searching and file content viewing
doskey grep=findstr $*
doskey cat=type $*
doskey less=more $*

REM System operations
doskey reboot=shutdown /r /t 0 $*
doskey halt=shutdown /s /t 0 $*
doskey pw=powercfg $*

REM Network operations
doskey ping=ping $*
doskey ifconfig=ipconfig $*

REM Miscellaneous
doskey clear=cls $*
doskey which=where $*
doskey history=doskey /history $*
