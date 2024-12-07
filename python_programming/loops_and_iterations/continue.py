while True:
    line = input("> ")
    # If the line starts with `#` jump to the next iteration (the top of the loop) and start the next iteration
    if line[0] == "#" :
        continue
    #argument for breaking the loop
    if line == "done" :
        # break the loop
        break
    print(line)
print("Done!")
