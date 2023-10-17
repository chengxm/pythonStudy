def main():
    f = None
    try:

        # with 关键字指定文件对象的上下文环境，并在离开上下文环境时候，自动释放文件资源
        with open('test.txt', 'a+', encoding='utf-8') as fwr:
            fwr.write('\n11112222')
            print(fwr.read())
    except FileNotFoundError:
        print("无法打开指定的文件")
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

if __name__ == '__main__':
    main()
    