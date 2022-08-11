from opentrons import protocol_api
import json
import os

metadata = {
    'apiLevel': '2.12', 
    'protocolName':'Automated Portion of Wristband Extraction Process',
    'description': 'This protocol is for the automated portion of the Wristband Extraction with Cleanup protocol. It takes a 600 uL aliquot from each tube from vial 1 to vial 2 and then aliquots 200uL from vial 2 to vial 3.',
    'author': 'Tei Kim'
}

gc_autosampler = """
{
    "ordering": [
        [
            "A1",
            "B1",
            "C1",
            "D1",
            "E1",
            "F1"
        ],
        [
            "A2",
            "B2",
            "C2",
            "D2",
            "E2",
            "F2"
        ],
        [
            "A3",
            "B3",
            "C3",
            "D3",
            "E3",
            "F3"
        ],
        [
            "A4",
            "B4",
            "C4",
            "D4",
            "E4",
            "F4"
        ],
        [
            "A5",
            "B5",
            "C5",
            "D5",
            "E5",
            "F5"
        ],
        [
            "A6",
            "B6",
            "C6",
            "D6",
            "E6",
            "F6"
        ],
        [
            "A7",
            "B7",
            "C7",
            "D7",
            "E7",
            "F7"
        ],
        [
            "A8",
            "B8",
            "C8",
            "D8",
            "E8",
            "F8"
        ],
        [
            "A9",
            "B9",
            "C9",
            "D9",
            "E9",
            "F9"
        ]
    ],
    "brand": {
        "brand": "ThermoFisher",
        "brandId": [
            "123"
        ]
    },
    "metadata": {
        "displayName": "ThermoFisher 54 Well Plate 300 µL",
        "displayCategory": "wellPlate",
        "displayVolumeUnits": "µL",
        "tags": []
    },
    "dimensions": {
        "xDimension": 128,
        "yDimension": 85.5,
        "zDimension": 33.3
    },
    "wells": {
        "A1": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 9.5,
            "y": 75.5,
            "z": 4.3
        },
        "B1": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 9.5,
            "y": 61.6,
            "z": 4.3
        },
        "C1": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 9.5,
            "y": 47.7,
            "z": 4.3
        },
        "D1": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 9.5,
            "y": 33.8,
            "z": 4.3
        },
        "E1": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 9.5,
            "y": 19.9,
            "z": 4.3
        },
        "F1": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 9.5,
            "y": 6,
            "z": 4.3
        },
        "A2": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 23.4,
            "y": 75.5,
            "z": 4.3
        },
        "B2": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 23.4,
            "y": 61.6,
            "z": 4.3
        },
        "C2": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 23.4,
            "y": 47.7,
            "z": 4.3
        },
        "D2": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 23.4,
            "y": 33.8,
            "z": 4.3
        },
        "E2": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 23.4,
            "y": 19.9,
            "z": 4.3
        },
        "F2": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 23.4,
            "y": 6,
            "z": 4.3
        },
        "A3": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 37.3,
            "y": 75.5,
            "z": 4.3
        },
        "B3": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 37.3,
            "y": 61.6,
            "z": 4.3
        },
        "C3": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 37.3,
            "y": 47.7,
            "z": 4.3
        },
        "D3": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 37.3,
            "y": 33.8,
            "z": 4.3
        },
        "E3": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 37.3,
            "y": 19.9,
            "z": 4.3
        },
        "F3": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 37.3,
            "y": 6,
            "z": 4.3
        },
        "A4": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 51.2,
            "y": 75.5,
            "z": 4.3
        },
        "B4": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 51.2,
            "y": 61.6,
            "z": 4.3
        },
        "C4": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 51.2,
            "y": 47.7,
            "z": 4.3
        },
        "D4": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 51.2,
            "y": 33.8,
            "z": 4.3
        },
        "E4": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 51.2,
            "y": 19.9,
            "z": 4.3
        },
        "F4": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 51.2,
            "y": 6,
            "z": 4.3
        },
        "A5": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 65.1,
            "y": 75.5,
            "z": 4.3
        },
        "B5": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 65.1,
            "y": 61.6,
            "z": 4.3
        },
        "C5": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 65.1,
            "y": 47.7,
            "z": 4.3
        },
        "D5": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 65.1,
            "y": 33.8,
            "z": 4.3
        },
        "E5": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 65.1,
            "y": 19.9,
            "z": 4.3
        },
        "F5": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 65.1,
            "y": 6,
            "z": 4.3
        },
        "A6": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 79,
            "y": 75.5,
            "z": 4.3
        },
        "B6": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 79,
            "y": 61.6,
            "z": 4.3
        },
        "C6": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 79,
            "y": 47.7,
            "z": 4.3
        },
        "D6": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 79,
            "y": 33.8,
            "z": 4.3
        },
        "E6": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 79,
            "y": 19.9,
            "z": 4.3
        },
        "F6": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 79,
            "y": 6,
            "z": 4.3
        },
        "A7": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 92.9,
            "y": 75.5,
            "z": 4.3
        },
        "B7": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 92.9,
            "y": 61.6,
            "z": 4.3
        },
        "C7": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 92.9,
            "y": 47.7,
            "z": 4.3
        },
        "D7": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 92.9,
            "y": 33.8,
            "z": 4.3
        },
        "E7": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 92.9,
            "y": 19.9,
            "z": 4.3
        },
        "F7": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 92.9,
            "y": 6,
            "z": 4.3
        },
        "A8": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 106.8,
            "y": 75.5,
            "z": 4.3
        },
        "B8": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 106.8,
            "y": 61.6,
            "z": 4.3
        },
        "C8": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 106.8,
            "y": 47.7,
            "z": 4.3
        },
        "D8": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 106.8,
            "y": 33.8,
            "z": 4.3
        },
        "E8": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 106.8,
            "y": 19.9,
            "z": 4.3
        },
        "F8": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 106.8,
            "y": 6,
            "z": 4.3
        },
        "A9": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 120.7,
            "y": 75.5,
            "z": 4.3
        },
        "B9": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 120.7,
            "y": 61.6,
            "z": 4.3
        },
        "C9": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 120.7,
            "y": 47.7,
            "z": 4.3
        },
        "D9": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 120.7,
            "y": 33.8,
            "z": 4.3
        },
        "E9": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 120.7,
            "y": 19.9,
            "z": 4.3
        },
        "F9": {
            "depth": 29,
            "totalLiquidVolume": 300,
            "shape": "circular",
            "diameter": 4.44,
            "x": 120.7,
            "y": 6,
            "z": 4.3
        }
    },
    "groups": [
        {
            "metadata": {
                "wellBottomShape": "u"
            },
            "wells": [
                "A1",
                "B1",
                "C1",
                "D1",
                "E1",
                "F1",
                "A2",
                "B2",
                "C2",
                "D2",
                "E2",
                "F2",
                "A3",
                "B3",
                "C3",
                "D3",
                "E3",
                "F3",
                "A4",
                "B4",
                "C4",
                "D4",
                "E4",
                "F4",
                "A5",
                "B5",
                "C5",
                "D5",
                "E5",
                "F5",
                "A6",
                "B6",
                "C6",
                "D6",
                "E6",
                "F6",
                "A7",
                "B7",
                "C7",
                "D7",
                "E7",
                "F7",
                "A8",
                "B8",
                "C8",
                "D8",
                "E8",
                "F8",
                "A9",
                "B9",
                "C9",
                "D9",
                "E9",
                "F9"
            ]
        }
    ],
    "parameters": {
        "format": "irregular",
        "quirks": [],
        "isTiprack": false,
        "isMagneticModuleCompatible": false,
        "loadName": "thermofisher_54_wellplate_300ul"
    },
    "namespace": "custom_beta",
    "version": 1,
    "schemaVersion": 2,
    "cornerOffsetFromSlot": {
        "x": 0,
        "y": 0,
        "z": 0
    }
}
"""
def run(protocol: protocol_api.ProtocolContext):
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack1])
    m300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack1])
    tuberack1 = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 3)
    tuberack2 = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 2)
    gcautosampler = protocol.load_labware_from_definition(json.loads(gc_autosampler), 1)
    p300.flow_rate.aspirate = 15
    p300.flow_rate.dispense = 15
    p300.flow_rate.blow_out = 1000
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    ID_tiprack = []
    ID_tuberack1 = []
    ID_tuberack2 = []
    ID_gcautosampler = []
    for j in range(12):
        for i in letters:
            ID_tiprack.append(i+str(j+1))
    sequence(3,5,ID_tuberack1,letters)
    sequence(4,6,ID_tuberack2, letters)
    sequence(6,9, ID_gcautosampler, letters)
    curIndex = 0
    for i in range(len(ID_tuberack1)):
        id1 = ID_tuberack1[i]
        id2 = ID_tuberack2[i]
        if curIndex < 96:
            transfer(p300, tiprack1, tuberack1, tuberack2, id1, id2, ID_tiprack[curIndex], 200, 3, -115, -33)
            p300.drop_tip()
            curIndex+=1
    protocol.pause('Please vortex and centrifuge before proceeding. ')
    for i in range(len(ID_tuberack1)):
        id1 = ID_tuberack2[i]
        id2 = ID_gcautosampler[i]
        if curIndex < 96:
            transfer(p300, tiprack1, tuberack2, gcautosampler, id1, id2, ID_tiprack[curIndex], 200, 1, -33, -2)
            p300.drop_tip()
            curIndex+=1
# the transfer function is used to transfer liquid from one plate to another. 
def transfer(pipette, p1, p2, p3, id1, id2, ID, k, n, asp, disp):   # pipette = type of pipette
    pipette.pick_up_tip(p1[ID])                                     # p1 = plate type 1, p2 = plate type 2, p3 = plate type 3
    for i in range(n):                                              # id1, id2 = the wells involved in the transfer of sample extract
        pipette.aspirate(k, p2[id1].top(z=asp))                     # ID = which tip is used from the tip rack
        pipette.air_gap(10)                                         # k = amount to aspirate/dispense
        pipette.dispense(k, p3[id2].top(z=disp))                    # n = number of times to repeat process
        pipette.blow_out()                                          # asp = how deep you want the pipette to aspirate from
                                                                    # disp = how deep you want the pipette to dispense from
# the sequence function is used to determine the sequence of wells the robot will visit
def sequence(row, col, ID_labware, letters):                        # row = number of rows on the plate
    for i in letters[0:row]:                                        # col = number of columns on the plate
        for j in range(col):                                        # ID_labware is the array to store the sequence of the wells to visit
            ID_labware.append(i+str(j+1))                           # letters contains letters from A-H.