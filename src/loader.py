def load(file_path=''):
    with open(file_path) as file:
        data = []
        for line in file:
            i = 0
            row = ['']

            for char in line:
                match char:
                    case ',':
                        i += 1
                        row.append('')
                    case '\n':
                        pass
                    case _:
                        row[i] += char

            data.append(row)
        
        print(data)

def save(save_data,save_path=''):
    pass

if __name__ == "__main__":
    pass
