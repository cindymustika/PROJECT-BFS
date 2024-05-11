peta= {'A': set (['B', 'H']),
       'B': set (['A', 'C', 'H']),
        'C': set (['B', 'D', 'E']),
        'D': set (['C', 'E', 'F', 'G', 'H']),
        'E': set (['C', 'D']),
        'F': set (['D', 'G']),
        'G': set (['F', 'D', 'H']),
        'H': set (['A', 'B', 'D', 'G']),}

def bfs_lintasan_terpendek(peta, mulai, tujuan):
    explored = [];
    queue = [[mulai]];

    if mulai == tujuan:
        return "Awal adalah tujuan";

    while queue:
        jalur = queue.pop(0);
        node = jalur[-1];

        if node not in explored:
            neighbours = peta[node];

            for neighbour in neighbours:
                jalur_baru = list(jalur);
                jalur_baru.append(neighbour);
                queue.append(jalur_baru);

                if neighbour == tujuan:
                    return jalur_baru; 

            explored.append(node);

    return "Mohon maaf node yang kalian pilih tidak ada";

mula = input("Masukkan awal: ");
tujuan = input("Masukkan akhir: ");