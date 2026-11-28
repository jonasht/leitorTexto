sudo pacman -S --needed uv
cd ~/kokoro
uv python install 3.12
uv venv --python 3.12 .venv
source .venv/bin/activate
python --version
uv pip install kokoro
