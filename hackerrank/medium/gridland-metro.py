# O(n*m + (m+n)log(m+n)) time and space
# link: https://www.hackerrank.com/challenges/gridland-metro

from collections import defaultdict

def gridlandMetro(n, m, k, track):
    total_cells = n * m
    tracks_by_row = defaultdict(list)
    for r, c1, c2 in track:
        tracks_by_row[r].append([min(c1, c2), max(c1, c2)])

    for r in tracks_by_row:
        intervals = tracks_by_row[r]
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []
        for start, end in intervals:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        for start, end in merged_intervals:
            total_cells -= (end - start + 1)

    return total_cells
