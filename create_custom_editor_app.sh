#!/bin/bash

# === Configuration ===
APP_NAME="GodotJenova"
ICON_NAME="custom.icns"
EDITOR_BINARY="bin/godot.macos.editor.arm64"

# === Setup .app Folder ===
APP_PATH="${APP_NAME}.app"
CONTENTS_PATH="${APP_PATH}/Contents"
MACOS_PATH="${CONTENTS_PATH}/MacOS"
RESOURCES_PATH="${CONTENTS_PATH}/Resources"

mkdir -p "$MACOS_PATH"
mkdir -p "$RESOURCES_PATH"

# === Copy Editor Binary ===
cp "$EDITOR_BINARY" "${MACOS_PATH}/${APP_NAME}"
chmod +x "${MACOS_PATH}/${APP_NAME}"

# === Copy Icon ===
cp "$ICON_NAME" "${RESOURCES_PATH}/${ICON_NAME}"

# === Create Info.plist ===
cat > "${CONTENTS_PATH}/Info.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleName</key>            <string>${APP_NAME}</string>
  <key>CFBundleExecutable</key>     <string>${APP_NAME}</string>
  <key>CFBundleIdentifier</key>     <string>com.yourcompany.${APP_NAME}</string>
  <key>CFBundleVersion</key>        <string>1.0</string>
  <key>CFBundlePackageType</key>    <string>APPL</string>
  <key>CFBundleIconFile</key>       <string>${ICON_NAME%.*}</string>
  <key>LSMinimumSystemVersion</key> <string>10.14</string>
</dict>
</plist>
EOF

echo "✅ Created ${APP_NAME}.app"
echo "➡️  Run it with: open \"${APP_PATH}\""
