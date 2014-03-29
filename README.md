Last-3000ish-Tweets
===================

After using twitter-log to extract your (or another persons) last 3,000ish tweets, this script creates a CSV and text file, one for graphing, the other for wordclouds.

It is designed to be executed from the command line.

Assumptions:

You have Python installed.
You have already run twitter-log to obtain the source tweet file.

Example command line:
python p_twitter-log.py -u davispg -i /home/pauldavis/Documents/davis.txt -c /home/pauldavis/Documents/davis.csv -t /home/pauldavis/Documents/davis-tweets.txt ABC YaThinkN MyBroadbandvReality pascalg15

Note the fully qualified path statements for the input, CSV output and tweets file.

The "ABC YaThinkN MyBroadbandvReality pascalg15" text is optional words the script searches for in the tweets. When it encounteres one of these words, it increments a counter in the CSV file. This in case you would like to graph things.

Planned future enhancements:
Allow hourly (rather than daily) aggregates (to allow more graphing fun).
