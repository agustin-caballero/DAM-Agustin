@echo off
echo Iniciando copia de seguridad en Git...

:: Cambiar a la carpeta de tu proyecto
cd /d "C:\Users\Administrator\Documents\DAM-Agustin"

:: Comprobar si hay cambios para evitar commits vacios
git status --porcelain | findstr /R "^" >nul
if %errorlevel% equ 0 (
    echo Guardando cambios locales...
    git add .
    git commit -m "Auto-commit antes de apagar (%date% %time%)"
    
    echo Subiendo a GitHub/GitLab...
    git push origin main
) else (
    echo No hay cambios nuevos que subir.
)

echo.
echo Todo listo. El ordenador se apagara en 10 segundos...
shutdown /s /t 10
