import units
import file_sys_funcs

kb = units.Kilobyte
mb = units.Megabyte
gb = units.Gigabyte


def main():
    file_sys_funcs.write_new_vol("C:\\vol1", 5*gb)

if __name__ == "__main__":
    main()