prices=[105,110,108,112,115,116,114]
window=3
rolling_avg=[]
for i in range(len(prices)-window+1):
    avg=sum(prices[i:i+window])/window
    rolling_avg.append(avg)

#print results
for i,avg in enumerate(rolling_avg,start=1):
    print(f"Day {i}-{i+2} average:{avg:.2f}")    