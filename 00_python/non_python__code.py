def make_chai():
    if not kettle_has_water():
        fill_kattle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea leaves")
    add_to_cup("sugar")
    stie("boilded water")
    stie("cup")
    serve("chai")

    make_chai() 