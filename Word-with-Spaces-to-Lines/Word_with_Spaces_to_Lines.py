
print("Start")
channel_output_file="text8"
channel_values = open(channel_output_file).read().split()


f = open('words.txt', 'w')
for word in channel_values:
    f.write(word+'\n')
f.close()

print("Done")