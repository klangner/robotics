'''
Created on 22-05-2013

@author: Krzysztof Langner
'''
from robotics.robot1.application import RobotApp
import os.path

RESOURCES_PATH = os.path.dirname(__file__) + '/resources/'

app = RobotApp()
app.loadMap(RESOURCES_PATH + 'map1/map1.tmx')
app.run()