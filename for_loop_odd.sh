#!/bin/bash

for x in {1..99}
do
  if [ $(( $x % 2 )) -eq 1 ];
  then
    echo "$x"
  fi
done
