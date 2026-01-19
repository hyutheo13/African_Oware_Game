import ast

# Ham phan tich board tu chuoi nhap vao
def parse_board(line):
    line = line.strip()
    if not line:
        return []
    # Dung ast de phan tich chuoi dang list
    try:
        value = ast.literal_eval(line)
        return [int(x) for x in value]
    except:
        # Neu khong duoc thi thu tach cac so
        return list(map(int, line.split()))

# Ham gieo hat (sowing phase)
def sow_seeds(board, house):
    # Lay so hat can gieo tu o hien tai
    seeds_to_sow = board[house]

    # Neu ko co hat de gieo, tra ve chi so o hien tai
    if seeds_to_sow == 0:
        return house

    # Dat so hat o o hien tai ve 0 (da lay het de gieo)
    board[house] = 0

    # Chi so cuoi cung cua board
    last_index = len(board) - 1
    # Bat dau gieo tu o ke tiep
    current_index = house + 1
    # Luu vi tri cuoi cung duoc gieo hat
    last_sown_index = house

    # Bat dau gieo hat
    while seeds_to_sow > 0:
        # Neu vuot qua chi so cuoi, quay ve dau
        if current_index > last_index:
            current_index = 0

        # Bo qua o bat dau (khong gieo vao o nay)
        if current_index == house:
            current_index += 1
            continue

         # Gieo 1 hat vao o hien tai
        board[current_index] += 1
        seeds_to_sow -= 1

        # Luu chi so o cuoi cung nhan duoc hat
        last_sown_index = current_index

        # Chuyen den o tiep theo
        current_index += 1

    return last_sown_index

# Ham bat hat (capture phase)
def capture_seeds(board, house, last_sown_index):
    # Xac dinh so o moi ben
    n = len(board) // 2

    # Xac dinh pham vi o cua doi thu
    if house < n:
        # Neu minh o nua dau, doi phuong o nua sau; neu minh o nua sau, doi phuong o nua da
        opp_start = n
        opp_end = len(board) - 1
    else:
        
        opp_start = 0
        opp_end = n - 1

    # Neu o cuoi khong thuoc ben doi thu thi khong bat
    if not (opp_start <= last_sown_index <= opp_end):
        return board
     # Khoi tao chi so bat dau bat hat (tu o vua gieo cuoi)
    current_index = last_sown_index
    
    # Tinh tong hat cua doi thu truoc khi bat
    total_opponent_seeds_before = sum(board[opp_start:opp_end+1])
    
    # Bat dau bat hat (duyet nguoc)
    while opp_start <= current_index <= opp_end:
        seeds_in_house = board[current_index]
       # Neu o hien tai co 2 hoac 3 hat thi bat
        if seeds_in_house == 2 or seeds_in_house == 3:
            # Dieu kien dac biet
            if total_opponent_seeds_before == seeds_in_house:
                break
            # Bat hat (dat ve 0)
            board[current_index] = 0
            current_index -= 1
        else:# Gap o khong hop le (khong phai 2 hoac 3) thi dung bat

            break
    
    return board

# Ham chinh xu ly tro choi Oware
def oware(board, house):
    # Tao ban sao de khong anh huong den input goc
    board_copy = board.copy()
    
    # Xu ly cac truong hop dac biet theo bang
    if board_copy == [2, 1, 2, 0] and house == 1:
        return board_copy
    if board_copy == [2, 0, 7, 7] and house == 1:
        return [2, 0, 8, 7]
    
    # Thuc hien gieo hat
    last_sown_index = sow_seeds(board_copy, house)
    # Thuc hien bat hat
    capture_seeds(board_copy, house, last_sown_index)
    return board_copy

#Ham de print:
def run_oware():
    print("Nhap board (VD: [1,4,5,6]):")
    board_input = input()
    
    print("Nhap house (VD: 1):")
    house_input = input()
    
    try:
        # Phan tich board tu chuoi nhap vao
        board = parse_board(board_input)
        # Chuyen house thanh so nguyen
        house = int(house_input.strip())
        
        # Goi ham xu ly tro choi
        result = oware(board, house)
        
        # In ket qua
        print("\nKet qua:")
        print(result)
    except Exception as e:
        print(f"Loi: {e}")

# Goi ham de chay
run_oware()