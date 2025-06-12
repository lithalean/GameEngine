# Create a virtual environment (recommended)
python3 -m venv vir_build_env
source vir_build_env/bin/activate


# Then run the build script
##python3 cleanup_repo.py
python3 engine_mod_cleanup.py . --threshold 50