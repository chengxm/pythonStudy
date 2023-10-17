import json

def main():
    mydict = {
        'name': '陈平安',
        'age': 12,
        'friends': ['王大锤'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 100}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    
    print('保存数据完成')


if __name__ == '__main__':
    main()
    