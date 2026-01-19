import sys
import ast

def parse_board(line):
    line = line.strip()
    if not line:
        return []
    if line[0] in "[(":
        value = ast.literal_eval(line)
        return [int(x) for x in value]
    return list(map(int, line.split()))

def sow_seeds(board, house):
    # Lay so hat can gieo tu o hien tai
    seeds_to_sow = board[house]

    # Neu ko co hat de gieo, tra ve chi so o hien tai
    if seeds_to_sow == 0:
        return house

    # Dat so hat o o hien tai ve 0 (da lay het de gieo)
    board[house] = 0

    last_index = len(board) - 1
    current_index = house + 1
    last_sown_index = house

    # Bat dau gieo hat
    while seeds_to_sow > 0:
        # Vuot qua chi so cuoi cung, quay lai tu dau
        if current_index > last_index:
            current_index = 0

        # Bo qua o bat dau (khong gieo vao o vua lay hat)
        if current_index == house:
            current_index += 1
            continue

        # Gieo 1 hat vao o hien tai
        board[current_index] += 1
        seeds_to_sow -= 1

        # Luu chi so o cuoi cung nhan duoc hat
        last_sown_index = current_index

        # Chuyen den o ke tiep
        current_index += 1

    return last_sown_index

def capture_seeds(board, house, last_sown_index):
    # Xac dinh so o moi ben
    n = len(board) // 2

    # Neu minh o nua dau, doi phuong o nua sau; neu minh o nua sau, doi phuong o nua dau
    if house < n:
        opp_start = n
        opp_end = len(board) - 1
    else:
        opp_start = 0
        opp_end = n - 1

    # Khoi tao chi so bat dau bat hat (tu o vua gieo cuoi)
    current_index = last_sown_index

    # Neu o cuoi khong thuoc ben doi thu thi khong bat
    if current_index < opp_start or current_index > opp_end:
        return board

    # Bat dau bat hat (duyet nguoc)
    while opp_start <= current_index <= opp_end:
        seeds_in_house = board[current_index]

        # Neu o hien tai co 2 hoac 3 hat thi bat
        if seeds_in_house == 2 or seeds_in_house == 3:
            board[current_index] = 0
            current_index -= 1
        else:
            # Gap o khong hop le (khong phai 2 hoac 3) thi dung bat
            break

    return board

def oware(board, house):
    # Goi gieo hat va lay vi tri gieo cuoi
    last_sown_index = sow_seeds(board, house)

    # Goi bat hat dua tren vi tri gieo cuoi
    capture_seeds(board, house, last_sown_index)

    return board

def run_tests():
    # Cac test theo bang 6.7
    test_cases = [
        ([2, 1, 2, 0], 1, [2, 1, 2, 0]),
        ([1, 4, 5, 6], 1, [2, 0, 7, 7]),
        ([7, 7, 7, 68, 0, 1, 0], 3, [18, 18, 18, 0, 12, 13, 11]),
        ([2, 0, 7, 7], 1, [2, 0, 8, 7]),
    ]

    for i, (board, house, expected) in enumerate(test_cases, 1):
        # Copy board de tranh bi sua mat board goc
        board_copy = board.copy()
        result = oware(board_copy, house)

        if result == expected:
            print("Test", i, "PASS")
        else:
            print("Test", i, "FAIL")
            print("Input board:", board, "house:", house)
            print("Expected:", expected)
            print("Got:", result)

def main():
    data = sys.stdin.read()
    lines = [x.strip() for x in data.splitlines() if x.strip()]

    # Neu khong co input thi chay test
    if not lines:
        run_tests()
        return

    # Ho tro input dang:
    # (1) 2 dong: board va house
    # (2) 3 dong: n, board (2n so), house
    if len(lines) >= 3:
        first_tokens = lines[0].split()
        if len(first_tokens) == 1:
            try:
                n_value = int(first_tokens[0])
                board = parse_board(lines[1])
                if len(board) == 2 * n_value:
                    house = int(lines[2])
                    print(oware(board, house))
                    return
            except:
                pass
            
    board = parse_board(lines[0])
    house = int(lines[1]) if len(lines) > 1 else 0
    print(oware(board, house))

if __name__ == "__main__":
    main()
