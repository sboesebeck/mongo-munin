#!/bin/bash

cd $(dirname $0)
./build.sh

for i in mongo_*; do 
	echo "installing $i"
	cp $i /usr/share/munin/plugins	
	if [ ! -e /etc/munin/plugins/$i ]; then
		echo "Installing link"
		ln -s /usr/share/munin/plugins/$i /etc/munin/plugins/$i
	else
		echo "link exists"
	fi
done
echo "Done"
