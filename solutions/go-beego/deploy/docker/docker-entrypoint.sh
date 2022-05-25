#!/bin/sh

# Get Linter
go get golang.org/x/lint/golint

# Get Bee
go get github.com/beego/bee/v2

# Migrate
postgres_url=$(sed -nr "/^\[prod\]/ { :l /^postgres_url[ ]*=/ { s/[^=]*=[ ]*//; p; q;}; n; b l;}" "${CURRENT_MOUNT_DIR}/app/conf/app.conf" | tr -d '"')
/root/go/bin/bee migrate -driver=postgres -conn="${postgres_url}"
