#!/usr/bin/en bash
export SRC_PATH="$( dirname "${BASHSOURCE[0]}" )"
export $(cat $SRC_PATH/.env-dev | xargs)
