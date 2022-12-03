if [ $# -eq 0 ]
  then
    echo "Usage: ./setup_day.sh <day_number>"
	exit 1
fi

echo "setting up day $1"
folder=day$1

if [ ! -d "$folder" ]; then
	mkdir $folder
	touch $folder/day$1.in
	touch $folder/day$1.py
else
	echo "$folder already exists"
	exit 1
fi
