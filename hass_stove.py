from hassapi import Hass

import common

hass, hassurl, hasstoken, hassboolean, current_state = [None] * 5

config = common.get_config()

if 'hassurl' in config:
    hassurl, hasstoken, hassboolean = (config['hassurl'], config['hasst\
oken'], config['hassboolean'])
    hass = Hass(hassurl=hassurl, token=hasstoken)

def get_state():
    return hass.get_state(hassboolean).state

def turn_on():
    return hass.turn_on(hassboolean)

def turn_off():
    hass.turn_off(hassboolean)
