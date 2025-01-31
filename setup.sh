#!/bin/bash

# Editar esta variable según sea interfaz del bus o de parada.
INTERFAZ="interfaz.py"

# Se usa el directorio donde se encuentra el script (gpsTCU)
# como el directorio base.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT="$SCRIPT_DIR/src/launchInterfaz.sh"
PYTH="$SCRIPT_DIR/src/$INTERFAZ"
VENV_DIR="$SCRIPT_DIR/venv"
AUTO_PATH="/home/$USER/.config/autostart"
AUTO_FILE="$AUTO_PATH/autoBusGPS.desktop"

# Se crean los directorios si no existen
mkdir -p "$AUTO_PATH"

# Se crea enviroment virtual si no existe
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip
    pip install -r "$SCRIPT_DIR/requirements.txt"
    deactivate
fi

# Se crea el script que ejecuta la interfaz.
cat > "$SCRIPT" << EOF
#!/bin/bash
export DISPLAY=:0

cd "$SCRIPT_DIR" || exit 1
source "$VENV_DIR/bin/activate"
python3 "$PYTH"
EOF

# Se da permisos de ejecución al script.
chmod +x "$SCRIPT"
chmod +x "$PYTH"

# Se crea archivo .desktop que se agrega a autostart.
cat > "$AUTO_FILE" << EOF
[Desktop Entry]
Type=Application
Name=Autostart interfaz de aplicación GPS TCU.
Exec="$SCRIPT"
EOF

echo "Setup finalizado."
