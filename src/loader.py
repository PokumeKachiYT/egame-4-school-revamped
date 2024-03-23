PLACEHOLDER_DATA = """


"""

def load(file_path=''):
    try:
        file = open(file_path)
    except:
        file = open(file_path,"w")
        file.write(PLACEHOLDER_DATA)
        file.close()
    else:
        file.close()

    with open(file_path) as file:
        data = [
            [],[],
            [],[],
        ]

        i = 0

        for line in file:
            row = line.split(',')

            match row[0]:
                case 'Phần thi':
                    pass
                case 'Khởi động':
                    pass
                case 'Vượt chướng ngại vật':
                    pass
                case 'Tăng tốc':
                    pass
                case 'Về đích':
                    pass

            print(row)
            data.append(row)
        
        return data

def save(save_data,save_path=''):
    pass

if __name__ == "__main__":
    pass
