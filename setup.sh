#!/bin/bash

# Se instala crontab si no se ha instalado.
if ! command -v crontab &> /dev/null; then
    sudo apt update && sudo apt install -y cron
fi

# Se usa el directorio donde se encuentra el script (gpsTCU)
# como el directorio base.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/cron"
SCRIPT="$SCRIPT_DIR/launcherGPS.sh"
LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/cronlog"

# Se crean los directorios si no existen
mkdir -p "$SCRIPT_DIR" "$LOG_DIR"

# Se crea el script que se ejecuta en cron, con la dirección correcta.
cat > "$SCRIPT" << EOF
#!/bin/sh
export DISPLAY=:0

cd "$SCRIPT_DIR" || exit 1
cd ../
/usr/bin/python3 "src/interfaz.py"
EOF

# Se da permisos de ejecución al script.
chmod +x "$SCRIPT"

#### Pasos para agregar tarea al crontab:
# Lee los crontabs del usuario, si no tiene evita error
# crontab -l 2>/dev/null

# Elimina crontabs hechas con launcher.sh
# rep -v "$SCRIPT_DIR/launcherGPS.sh"

# Agrega la tarea nueva al crontab
# echo "@reboot $SCRIPT_DIR/launcherGPS.sh > $LOG_FILE 2>&1"
(crontab -l 2>/dev/null | grep -v "$SCRIPT_DIR/launcherGPS.sh"; echo "@reboot $SCRIPT_DIR/launcherGPS.sh > $LOG_FILE 2>&1") | crontab -

echo "Setup de crontab finalizado."
