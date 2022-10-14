import synchronous_SMD as synch
# import asynchronous_SMD as asynch
import asynchronus_SM as asynch
import graphics


def main_s():
    synch.make()
    graphics.draw_synch_D()
    graphics.draw_synch_N()


def main_as():
    # asynch.make()
    graphics.draw_asynch_D()
    # graphics.draw_synch_N()


def main():
    synch.make()
    asynch.make()
    graphics.draw_all_graphics()


if __name__ == '__main__':
    # main_as()
    main()