import sys
import heapq as heap
import collections

input = sys.stdin.readline

number = lambda: int(input().strip())
numbers = lambda: list(map(int, input().strip().split()))

# --- Segment Tree Implementation (Conceptual) ---
# This is a barebones structure. Actual implementation for
# range min queries and point updates (with associated index) is complex.
# You'd typically use coordinate compression for heights if range is too large.

class SegmentTree:
    def __init__(self, size, operation):
        self.size = size
        self.tree = [float('inf')] * (4 * size) # For min operation
        self.op = operation # e.g., min or some custom merge

    def _build(self, arr, node, start, end):
        # Not needed for this problem as we update points
        pass

    def update(self, idx, val, node, start, end, original_tower_idx):
        # Update value for a specific original_tower_idx at its height_id
        # val would be (arrival_time - height) or (arrival_time + height)
        # This requires careful mapping of original_tower_idx to height_id
        if start == end:
            # Here, store (val, original_tower_idx)
            # Example: self.tree[node] = (val, original_tower_idx)
            pass
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, val, 2 * node, start, mid, original_tower_idx)
            else:
                self.update(idx, val, 2 * node + 1, mid + 1, end, original_tower_idx)
            # self.tree[node] = self.op(self.tree[2*node], self.tree[2*node+1])
            pass

    def query(self, l, r, node, start, end):
        # Query for minimum value in range [l, r]
        # This needs to return (min_value, associated_original_tower_idx)
        if r < start or end < l:
            return (float('inf'), -1) # -1 indicates no valid index
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self.query(l, r, 2 * node, start, mid)
        p2 = self.query(l, r, 2 * node + 1, mid + 1, end)
        
        # This merge operation needs to be specific: find minimum based on value
        # and return its associated index.
        # return self.op(p1, p2)
        pass

# --- Dijkstra with Segment Tree ---

def solve():
    n, k = numbers()
    h = numbers()

    max_height = max(h)
    
    # Early exit if already at max height
    if h[k - 1] == max_height:
        print("YES")
        return

    # 1. Coordinate Compression for heights
    # Map unique heights to 0-indexed IDs
    unique_heights = sorted(list(set(h)))
    height_to_id = {height: i for i, height in enumerate(unique_heights)}
    id_to_height = unique_heights
    num_unique_heights = len(unique_heights)

    # Segment trees for range queries. We need two, or a more complex single tree.
    # Segtree 1: to find min (arrival_time - height) for jumps to shorter towers
    # Segtree 2: to find min (arrival_time + height) for jumps to taller towers
    # Each leaf node will store a tuple (value, original_tower_idx)
    # The 'min' operation for tuples should compare by value first.

    # This is highly simplified. A real segment tree needs to know
    # the original_tower_idx corresponding to the min value in its range.
    seg_tree_minus_h = SegmentTree(num_unique_heights, min) # min( (v1, i1), (v2, i2) ) -> (min(v1,v2), corresponding_i)
    seg_tree_plus_h = SegmentTree(num_unique_heights, min)

    min_arrival_time = [float('inf')] * n
    pq = [(0, k - 1)] # (current_time, tower_index)
    min_arrival_time[k - 1] = 0

    # Initial population of segment trees
    # For tower k-1 (starting tower)
    initial_h_id = height_to_id[h[k-1]]
    # Update seg_tree_minus_h at initial_h_id with (0 - h[k-1], k-1)
    # Update seg_tree_plus_h at initial_h_id with (0 + h[k-1], k-1)
    # seg_tree_minus_h.update(initial_h_id, (0 - h[k-1], k-1), 1, 0, num_unique_heights - 1, k-1)
    # seg_tree_plus_h.update(initial_h_id, (0 + h[k-1], k-1), 1, 0, num_unique_heights - 1, k-1)

    # For all other towers, they are initially at inf.
    # A more robust segment tree setup would populate with (inf, idx) for all.

    processed_towers = [False] * n # To ensure a tower is processed only once as source

    while pq:
        current_time, u_idx = heap.heappop(pq)

        if processed_towers[u_idx]: # If this tower was already processed with a better time
            continue
        
        if current_time > min_arrival_time[u_idx]: # This path is worse than one already found
            continue

        processed_towers[u_idx] = True # Mark as processed

        if h[u_idx] == max_height:
            print("YES")
            return
        
        # Remove u_idx from segment trees to prevent re-selection as target for other nodes
        u_h_id = height_to_id[h[u_idx]]
        # seg_tree_minus_h.update(u_h_id, (float('inf'), -1), 1, 0, num_unique_heights - 1, u_idx)
        # seg_tree_plus_h.update(u_h_id, (float('inf'), -1), 1, 0, num_unique_heights - 1, u_idx)


        # --- Explore Neighbors using Segment Tree Queries ---
        # Remember to map height ranges to their corresponding height_ids for segment tree queries

        # Case 1: Jump to shorter or equal tower (h_v <= h_u)
        # Conditions: h_v >= current_time AND h_v > (current_time + h_u) / 2
        # Maximize h_v to minimize cost: current_time + h_u - h_v
        
        # Calculate lower bound for h_v
        min_allowed_h_v_1 = (current_time + h[u_idx]) / 2.0
        
        # Find the range of height_ids to query in seg_tree_minus_h
        # search for h_v in [floor(min_allowed_h_v_1) + 1, h[u_idx]]
        
        # Example:
        # query_start_id = bisect_left(id_to_height, floor(min_allowed_h_v_1) + 1)
        # query_end_id = bisect_right(id_to_height, h[u_idx]) - 1

        # if query_start_id <= query_end_id:
        #     (min_val_neg, v_idx_candidate_1) = seg_tree_minus_h.query(query_start_id, query_end_id, 1, 0, num_unique_heights - 1)
        #     if v_idx_candidate_1 != -1 and min_val_neg != float('inf'):
        #         next_arrival_time_1 = current_time + h[u_idx] + min_val_neg
        #         # Final check for survival at destination v_idx_candidate_1
        #         if h[v_idx_candidate_1] > next_arrival_time_1: # Water level check
        #             if next_arrival_time_1 < min_arrival_time[v_idx_candidate_1]:
        #                 min_arrival_time[v_idx_candidate_1] = next_arrival_time_1
        #                 heap.heappush(pq, (next_arrival_time_1, v_idx_candidate_1))


        # Case 2: Jump to taller tower (h_v > h_u)
        # Pre-check: You must survive on u_idx until arrival at v_idx
        if h[u_idx] <= current_time: # You drown on u_idx right now
            pass # Cannot make any jumps to higher towers
        else:
            # Conditions: h_v <= 2*h_u - current_time
            # Minimize h_v to minimize cost: current_time - h_u + h_v
            
            # Calculate upper bound for h_v
            max_allowed_h_v_2 = 2 * h[u_idx] - current_time

            # Find the range of height_ids to query in seg_tree_plus_h
            # search for h_v in [h[u_idx] + 1, floor(max_allowed_h_v_2)]

            # Example:
            # query_start_id = bisect_left(id_to_height, h[u_idx] + 1)
            # query_end_id = bisect_right(id_to_height, floor(max_allowed_h_v_2)) - 1

            # if query_start_id <= query_end_id:
            #     (min_val_pos, v_idx_candidate_2) = seg_tree_plus_h.query(query_start_id, query_end_id, 1, 0, num_unique_heights - 1)
            #     if v_idx_candidate_2 != -1 and min_val_pos != float('inf'):
            #         next_arrival_time_2 = current_time - h[u_idx] + min_val_pos
            #         # Final check for survival at destination v_idx_candidate_2
            #         if h[v_idx_candidate_2] > next_arrival_time_2: # Water level check
            #             if next_arrival_time_2 < min_arrival_time[v_idx_candidate_2]:
            #                 min_arrival_time[v_idx_candidate_2] = next_arrival_time_2
            #                 heap.heappush(pq, (next_arrival_time_2, v_idx_candidate_2))
    
    # If the loop finishes, no path found
    print("NO")

if __name__ == "__main__":
    for _ in range(number()):
        solve()