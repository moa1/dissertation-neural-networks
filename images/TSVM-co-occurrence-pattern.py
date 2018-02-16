#!/usr/bin/python

from random import *

print '''<?xml version="1.0" encoding="UTF-8"?>
<dia:diagram xmlns:dia="http://www.lysator.liu.se/~alla/dia/">
  <dia:diagramdata>
    <dia:attribute name="background">
      <dia:color val="#ffffff"/>
    </dia:attribute>
    <dia:attribute name="pagebreak">
      <dia:color val="#000099"/>
    </dia:attribute>
    <dia:attribute name="paper">
      <dia:composite type="paper">
        <dia:attribute name="name">
          <dia:string>#Letter#</dia:string>
        </dia:attribute>
        <dia:attribute name="tmargin">
          <dia:real val="2.5399999618530273"/>
        </dia:attribute>
        <dia:attribute name="bmargin">
          <dia:real val="2.5399999618530273"/>
        </dia:attribute>
        <dia:attribute name="lmargin">
          <dia:real val="2.5399999618530273"/>
        </dia:attribute>
        <dia:attribute name="rmargin">
          <dia:real val="2.5399999618530273"/>
        </dia:attribute>
        <dia:attribute name="is_portrait">
          <dia:boolean val="true"/>
        </dia:attribute>
        <dia:attribute name="scaling">
          <dia:real val="1"/>
        </dia:attribute>
        <dia:attribute name="fitto">
          <dia:boolean val="false"/>
        </dia:attribute>
      </dia:composite>
    </dia:attribute>
    <dia:attribute name="grid">
      <dia:composite type="grid">
        <dia:attribute name="width_x">
          <dia:real val="1"/>
        </dia:attribute>
        <dia:attribute name="width_y">
          <dia:real val="1"/>
        </dia:attribute>
        <dia:attribute name="visible_x">
          <dia:int val="1"/>
        </dia:attribute>
        <dia:attribute name="visible_y">
          <dia:int val="1"/>
        </dia:attribute>
        <dia:composite type="color"/>
      </dia:composite>
    </dia:attribute>
    <dia:attribute name="color">
      <dia:color val="#d8e5e5"/>
    </dia:attribute>
    <dia:attribute name="guides">
      <dia:composite type="guides">
        <dia:attribute name="hguides"/>
        <dia:attribute name="vguides"/>
      </dia:composite>
    </dia:attribute>
  </dia:diagramdata>
  <dia:layer name="Background" visible="true" active="true">
    <dia:object type="Standard - Box" version="0" id="O0">
      <dia:attribute name="obj_pos">
        <dia:point val="3,3"/>
      </dia:attribute>
      <dia:attribute name="obj_bb">
        <dia:rectangle val="2.95,2.95;4.05,4.05"/>
      </dia:attribute>
      <dia:attribute name="elem_corner">
        <dia:point val="3,3"/>
      </dia:attribute>
      <dia:attribute name="elem_width">
        <dia:real val="1"/>
      </dia:attribute>
      <dia:attribute name="elem_height">
        <dia:real val="1"/>
      </dia:attribute>
      <dia:attribute name="border_width">
        <dia:real val="0.10000000149011612"/>
      </dia:attribute>
      <dia:attribute name="border_color">
        <dia:color val="#ff0000"/>
      </dia:attribute>
      <dia:attribute name="inner_color">
        <dia:color val="#ff0000"/>
      </dia:attribute>
      <dia:attribute name="show_background">
        <dia:boolean val="true"/>
      </dia:attribute>
    </dia:object>'''

pattern=[[1,0,0,0,0,0,1,],
         [1,1,1,0,0,0,1,],
         [0,0,1,0,0,0,1,],
         [0,0,0,1,1,0,1,],
         [0,0,0,1,0,1,1,],
         [0,0,0,0,1,1,1,],]

for x in range(7):
    for y in range(6):
        if pattern[y][x]==1:
            color = '#000000'
        else:
            v=randint(196,255)
            vs=hex(v)[2:]
            color = '#'+vs+vs+vs
        print '''    <dia:object type="Standard - Box" version="0" id="O1">
      <dia:attribute name="obj_pos">
        <dia:point val="'''+str(x)+''','''+str(y)+'''"/>
      </dia:attribute>
      <dia:attribute name="obj_bb">
        <dia:rectangle val="'''+str(x)+'''.95,'''+str(y)+'''.95;'''+str(x+1)+'''.05,'''+str(y+1)+'''.05"/>
      </dia:attribute>
      <dia:attribute name="elem_corner">
        <dia:point val="'''+str(x)+''','''+str(y)+'''"/>
      </dia:attribute>
      <dia:attribute name="elem_width">
        <dia:real val="1"/>
      </dia:attribute>
      <dia:attribute name="elem_height">
        <dia:real val="1"/>
      </dia:attribute>
      <dia:attribute name="border_width">
        <dia:real val="0.10000000149011612"/>
      </dia:attribute>
      <dia:attribute name="border_color">
        <dia:color val="'''+color+'''"/>
      </dia:attribute>
      <dia:attribute name="inner_color">
        <dia:color val="'''+color+'''"/>
      </dia:attribute>
      <dia:attribute name="show_background">
        <dia:boolean val="true"/>
      </dia:attribute>
    </dia:object>'''

print '''  </dia:layer>
</dia:diagram>'''
