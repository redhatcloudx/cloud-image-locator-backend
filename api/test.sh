#!/usr/bin/env sh

# Change into containing folder to assure relative paths resolve
CURRENT_DIR=$(dirname `[[ $0 = /* ]] && echo "$0" || echo "$PWD/${0#./}"`)
cd $CURRENT_DIR

echo "Running API tests.."

# Run tests
./test/*/test.sh

exit $?

# TODO: ACTUALLY IMPLEMENT SOMETHING