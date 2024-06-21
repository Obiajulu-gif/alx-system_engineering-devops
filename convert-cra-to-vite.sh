#!/bin/bash

# ensure the script exits on any error.
set -e

# Check for yarn installation.
if ! command -v yarn &> /dev/null
then
    echo "yarn could not be found, please install it first."
    exit 1
fi

# Remove react-scripts
yarn remove react-scripts

# Add Vite and necessary plugins
yarn add -D vite @vitejs/plugin-react

# Update package.json scripts
if [ -f package.json ]; then
    # Use jq to update the scripts in package.json
    jq '.scripts |= {
        "dev": "vite",
        "build": "vite build",
        "serve": "vite preview",
        "test": .test,
        "eject": .eject
    }' package.json > package_tmp.json && mv package_tmp.json package.json
else
    echo "package.json not found!"
    exit 1
fi

# Create Vite configuration file
cat > vite.config.js <<EOL
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    open: true
  }
});
EOL

# Move index.html to the public folder if it's not there
if [ ! -f public/index.html ]; then
    echo "index.html not found in public folder. Please ensure your index.html is in the public folder."
    exit 1
fi

# Update public/index.html
cat > public/index.html <<EOL
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/index.jsx"></script>
  </body>
</html>
EOL

# Rename .js files to .jsx
find src -name "*.js" -exec bash -c 'mv "$0" "${0%.js}.jsx"' {} \;

# Update imports in .jsx files
grep -rl --include=\*.jsx "from './" src | xargs sed -i '' 's/from '\''\.\/\(.*\)\.js'\''/from '\''\.\/\1.jsx'\''/g'
grep -rl --include=\*.jsx "from \"./" src | xargs sed -i '' 's/from "\.\/\(.*\)\.js"/from "\.\/\1.jsx"/g'

echo "Conversion complete! Run 'yarn dev' to start the development server."

