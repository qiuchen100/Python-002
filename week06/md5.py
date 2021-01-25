
HASH_MOD = 20


def save_md5_mod_file(md5_str):
    mod = hash(md5_str) % HASH_MOD
    with open('md5_part_' + str(mod), 'a+') as f:
        f.write(md5_str)


def save_target_file(md5):
    pass


def distinct_md5(md5_part_file):
    with open(md5_part_file, 'r') as f:
        md5_list = f.readlines()
        md5_set = set(md5_list)
        save_target_file(md5_set)


def main():
    """
    docstring
    """
    with open('test_md5.txt', 'r') as f:
        md5_str = f.readline()
        save_md5_mod_file(md5_str)
        for i in range(HASH_MOD):
            md5_part_file = 'md5_part_' + str(i)
            distinct_md5(md5_part_file)


if __name__ == "__main__":
    pass
