"""
latencies = [1  ,12,43,4,150,160]
buckets = 11
bucket_width = 10 

#Always begin by 0

0-9 : 2
10-19 : 1
…
90-99: 0
100+: 2

a) Always the 0 and +100 

Questions?
1. What is the maximum latency?
2. What is the minimum latency?
3. How do we need to return the data?
4. Are the latencies orderd?

Naive approach:
    def count_concurrencies → latencies, buckets, buckets width

No se puede repetir hash maps→dictonary there we can store the latencies
buckets = [0]*


loop len(latencies)
O(n) → Time complexity

i - 12 - 1 to 10
(12 // 10)

there's no buckets we just add 0 and in case we +1 to the bucket
counter += 1
print ({Bbucket}-{bucket} )

"""



latencies = [1, 12, 43, 4, 150, 160]
buckets_counts = 11
bucket_width = 10

buckets = [0] * buckets_counts

for latency in latencies:
    if latency > 100:
        buckets[-1] += 1
    else:
        pos = latency // bucket_width
        buckets[pos] += 1

for i in range(buckets_counts - 1):
    print(f"{i * bucket_width} - {(i+1)*bucket_width-1} : {buckets[i]}")
print(f"100+: {buckets[-1]}")





























# # Inicializamos una lista con ceros para contar cuántos valores caen en cada bucket
# bucket_counts = [0] * bucket_width
# print(bucket_counts)

# for latency in latencies:
#     if latency >= 100:
#         bucket_counts[-1] += 1
#     else: 
#         bucket_index = latency // bucket_width
#         print(bucket_index)
#         bucket_counts[bucket_index] += 1

# print(bucket_counts)


# # Imprimir los resultados
# for i in range(buckets - 1):  # Los primeros buckets
#     print(f"{i * bucket_width}-{(i + 1) * bucket_width - 1}: {bucket_counts[i]}")
# print(f"100+: {bucket_counts[-1]}")


# # for latency in latencies:
# #     if latency >= 100:
# #         # Si la latencia es mayor o igual a 100, la ponemos en el último bucket (bucket 100+)
# #         bucket_counts[-1] += 1
# #     else:
# #         # Calculamos a qué bucket pertenece la latencia
# #         bucket_index = latency // bucket_width
# #         bucket_counts[bucket_index] += 1

# # # Imprimir los resultados
# # for i in range(buckets - 1):  # Los primeros buckets
# #     print(f"{i * bucket_width}-{(i + 1) * bucket_width - 1}: {bucket_counts[i]}")
# # print(f"100+: {bucket_counts[-1]}")
