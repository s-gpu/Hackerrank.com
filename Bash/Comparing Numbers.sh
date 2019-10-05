read x
read y

if [ "$(( $x > $y ))" == "1" ]
then
	echo "X is greater than Y"
elif [ "$(( $x < $y ))" == "1" ]
then
	echo "X is less than Y"
else
	echo "X is equal to Y"
fi
