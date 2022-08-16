for tc in range(1, 11):
    dump_count = int(input())
    flat = list(map(int,input().split()))
    for i in range(dump_count):
        index_max= flat.index(max(flat))
        index_min= flat.index(min(flat))
        flat[index_max] -= 1
        flat[index_min] += 1
    print(f'#{tc} {max(flat)-min(flat)}')