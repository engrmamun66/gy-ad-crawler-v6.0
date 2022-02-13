:fromStart
@echo off
SET var=%cd%
color a
title GY Ad Crawer - V6.0
cls


echo.

echo       ohNMMNmyo  mmmmmmmds:      mNNNo     hmmd- -dddy  ydmm: hmdm+      ymmmddmmmy  dmmmmmmmmm 
echo     /NMMMMNMMMN  MMMNhdMMMMy    hMMMMM.    NMMM: :MMMd  dMMM+ mMMM+      hMMMNmmNNN  MMMMhdNMMMm    
echo    -MMMM         MMMy   MMMm   +MMMNMMN    mMMM- /MMMd  dMMM+ dMMM:      yMMMd       MMMN   MMMM
echo    oMMMh         MMMNddMMMN/  -MMM   MMm   :MMMm`dMMMM/+MMMy  dMMM:      yMMMMMMMMM  MMMMddNMMMs    
echo    -MMMM+        MMMNyNMMM:  `mMMMNNMMMMh   /MMMNMMMMMMMMMh   dMMM:      yMMMh       MMMMymMMMo     
echo     +NMMMMMMMMN  MMMd :MMMN- hMMMNmmmMMMMo   /MMMMM/mMMMMd    dMMMNmNNNm dMMMMNNNMM  MMMM  NMMM+    
echo      `+hmNMNdsN  mmmd  +mmmd mmmd     /mmmd   /mmmo .dmmh     dMMMNmNNNm dMMMMNNNMM  mmmm   dmmm

echo.
echo     ============================                                    ============================
echo     ============================ Powerful Google And Youtube Crawer ============================
echo     ============================                                    ============================
echo. 


set /p con=.   START CRAWL(y/n)? 
echo.
if %con%==y (
    
    @REM python operation start 
    @REM python pc.py
    python cli.py
    @REM dir /b
       
)


echo.
echo.

Goto  fromStart

