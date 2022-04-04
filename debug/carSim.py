# using an assertion in a traffic light simulation
# intersection north-south (ns) and east-west (ew)

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switch_lights(stopligth):
    for k in stopligth.keys():

        if stopligth[k] == 'green':
            stopligth[k] = 'yellow'

        elif stopligth[k] == 'yellow':
            stopligth[k] = 'red'

        elif stopligth[k] == 'red':
            stopligth[k] = 'green'

    assert 'red' in stopligth.values(), 'Neither light is red!' + str(stopligth)


switch_lights(market_2nd)
