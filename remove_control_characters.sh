# remove control characters such as ^H, ^M, ...
tr -d '\000-\010\013\014\016-\037' < in_file.csv > out_file.csv
