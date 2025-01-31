#!/bin/bash

# Editar esta variable según sea interfaz del bus o de parada.
INTERFAZ="interfaz.py"

# Se usa el directorio donde se encuentra el script (gpsTCU)
# como el directorio base.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT="$SCRIPT_DIR/src/launchInterfaz.sh"
PYTH="$SCRIPT_DIR/src/$INTERFAZ"
AUTO_PATH="/home/$USER/.config/autostart"
AUTO_FILE="$AUTO_PATH/autoBusGPS.desktop"

# Se crean los directorios si no existen
mkdir -p "$AUTO_PATH"

# Se crea el script que se ejecuta en cron, con la dirección correcta.
cat > "$SCRIPT" << EOF
#!/bin/sh
export DISPLAY=:0

cd "$SCRIPT_DIR" || exit 1
/usr/bin/python3 "$PYTH"
EOF

# Se da permisos de ejecución al script.
chmod +x "$SCRIPT"
chmod +x "$PYTH"

cat > "$AUTO_FILE" << EOF
[Desktop Entry]
Type=Application
Name=Autostart interfaz de aplicación GPS TCU.
Exec="$SCRIPT"
EOF

echo "Setup de crontab finalizado."
