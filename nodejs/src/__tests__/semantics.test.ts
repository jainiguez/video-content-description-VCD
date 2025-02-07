import { VCD, ElementType, RDF, OpenLABEL } from '../vcd.core'
import * as types from '../vcd.types'
import openlabel100_test_actions_a from '../../../tests/etc/openlabel100_test_actions_a.json'
import openlabel100_test_actions_b from '../../../tests/etc/openlabel100_test_actions_b.json'
import openlabel100_test_actions_c from '../../../tests/etc/openlabel100_test_actions_c.json'
import openlabel100_test_relations_1 from '../../../tests/etc/openlabel100_test_relations_1.json'
import openlabel100_test_relations_2 from '../../../tests/etc/openlabel100_test_relations_2.json'
import openlabel100_test_relations_3 from '../../../tests/etc/openlabel100_test_relations_3.json'
import openlabel100_test_semantics from '../../../tests/etc/openlabel100_test_semantics.json'
import openlabel100_kitti_tracking_0003 from '../../../tests/etc/openlabel100_kitti_tracking_0003.json'
import openlabel100_test_scene_KITTI_Tracking_3 from '../../../tests/etc/openlabel100_test_scene_KITTI_Tracking_3.json'

import { testEncodingDecoding } from '../vcd.poly2d'


test('test_semantics', () => {
    let vcd = new OpenLABEL()

    let ont_uid_0 = vcd.addOntology("http://www.vicomtech.org/viulib/ontology")
    let ont_uid_1 = vcd.addOntology("http://www.alternativeURL.org/ontology")

    //Let's create a static Context
    let officeUID = vcd.addContext('Office', '#Office',null, null,ont_uid_0)


    let talking_uid, start_talking_uid, noisy_uid, relation1_uid, relation2_uid;
    for(let frameNum=0; frameNum<30; frameNum++) {
        if (frameNum == 3) {
            start_talking_uid = vcd.addEvent('StartTalking', '#StartTalking', frameNum,null,ont_uid_0)
            talking_uid = vcd.addAction('Talking', '#Talking', frameNum,null,ont_uid_0)
            noisy_uid = vcd.addContext('Noisy', '', frameNum) //# No ontology

            let  relation1UID = vcd.addRelationSubjectObject('', '#Starts',
            ElementType.event, start_talking_uid,
            ElementType.action, talking_uid,null,ont_uid_0,null)

            let relation2UID = vcd.addRelationSubjectObject('', '#Causes',
            ElementType.action, talking_uid,
            ElementType.context, noisy_uid,
            null,ont_uid_0, null)


            expect(vcd.getNumRelations()).toBe(2)
            expect(vcd.getRelation(relation2UID)['rdf_subjects'].length).toBe(1)
            expect(vcd.getRelation(relation2UID)['rdf_subjects'][0]['uid']).toBe(talking_uid)
        }

        else if( frameNum >= 3 && frameNum <= 11) {            
            vcd.addAction('Talking', '#Talking', frameNum, talking_uid)
            vcd.addContext('Noisy', '', frameNum, noisy_uid)
        }
    }

    //console.log(vcd.stringify(false))
    let expected=new VCD(openlabel100_test_semantics, false).stringify(false)
    expect(vcd.stringify(false)).toBe(new VCD(openlabel100_test_semantics, false).stringify(false))
});

test('test_actions', () => {
    // 1.- Create VCD
    let vcd_a = new OpenLABEL()
    let vcd_b = new OpenLABEL()
    let vcd_c = new OpenLABEL()

    // 2.- Add ontology
    vcd_a.addOntology('http://vcd.vicomtech.org/ontology/automotive')
    vcd_b.addOntology('http://vcd.vicomtech.org/ontology/automotive')
    vcd_c.addOntology('http://vcd.vicomtech.org/ontology/automotive')

    // 3.- Add some objects
    let uid_pedestrian1 = vcd_a.addObject('', 'Pedestrian', null, null, "0")
    let uid_car1 = vcd_a.addObject('', 'Car', null, null, "0")
    uid_pedestrian1 = vcd_b.addObject('', 'Pedestrian', null, null, "0")
    uid_car1 = vcd_b.addObject('', 'Car', null, null, "0")
    uid_pedestrian1 = vcd_c.addObject('', 'Pedestrian', null, null, "0")
    uid_car1 = vcd_c.addObject('', 'Car', null, null, "0")

    // 4.- Add (intransitive actions)
    // Option a) Add (intransitive) Actions as Object attributes
    // Pro: simple, quick code, less bytes in JSON
    // Con: No explicit Relation, lack of extensibility, only valid for simple subject-predicates
    vcd_a.addObjectData(uid_pedestrian1, new types.Text("action", "Walking"))
    vcd_a.addObjectData(uid_car1, new types.Text("action", "Parked"))

    // Option b) Add (intransitive) Actions as Actions and use Relations to link to Objects
    // Pro: Action as element with entity, can add action_data, link to other Objects or complex Relations
    // Con: long to write, occupy more bytes in JSON, more difficult to parse
    let uid_action1 = vcd_b.addAction('', 'Walking', null, null, "0")
    let uid_rel1 = vcd_b.addRelationObjectAction('', 'performsAction', uid_pedestrian1, uid_action1, null, "0")
    let uid_action2 = vcd_b.addAction('', 'Parked', null, null, "0")
    let uid_rel2 = vcd_b.addRelationObjectAction('', 'performsAction', uid_car1, uid_action2, null, "0")

    // Option c) Add Actions as Actions, and use action_Data to point to subject Object
    // Pro: simple as option a
    // Con: sames as a
    uid_action1 = vcd_c.addAction("", "Walking", null, null, "0")
    uid_action2 = vcd_c.addAction("", "Parked", null, null, "0")
    vcd_c.addActionData(uid_action1, new types.Num("subject", +uid_pedestrian1))  // note UIDs are strings, need to convert to number
    vcd_c.addActionData(uid_action2, new types.Num("subject", +uid_car1))

    //console.log(vcd_a.stringify(false))
    //expect(vcd_a.stringify(false)).toBe('{"vcd":{"frames":{},"schema_version":"4.3.1","frame_intervals":[],"ontologies":{"0":"http://vcd.vicomtech.org/ontology/automotive"},"objects":{"0":{"name":"","type":"Pedestrian","ontology_uid":"0","object_data":{"text":[{"name":"action","val":"Walking"}]},"object_data_pointers":{"action":{"type":"text","frame_intervals":[]}}},"1":{"name":"","type":"Car","ontology_uid":"0","object_data":{"text":[{"name":"action","val":"Parked"}]},"object_data_pointers":{"action":{"type":"text","frame_intervals":[]}}}}}}')
    expect(vcd_a.stringify(false)).toBe(new VCD(openlabel100_test_actions_a, false).stringify(false))
    //console.log(vcd_b.stringify(false))
    //expect(vcd_b.stringify(false)).toBe('{"vcd":{"frames":{},"schema_version":"4.3.1","frame_intervals":[],"ontologies":{"0":"http://vcd.vicomtech.org/ontology/automotive"},"objects":{"0":{"name":"","type":"Pedestrian","ontology_uid":"0"},"1":{"name":"","type":"Car","ontology_uid":"0"}},"actions":{"0":{"name":"","type":"Walking","ontology_uid":"0"},"1":{"name":"","type":"Parked","ontology_uid":"0"}},"relations":{"0":{"name":"","type":"performsAction","ontology_uid":"0","rdf_subjects":[{"uid":"0","type":"object"}],"rdf_objects":[{"uid":"0","type":"action"}]},"1":{"name":"","type":"performsAction","ontology_uid":"0","rdf_subjects":[{"uid":"1","type":"object"}],"rdf_objects":[{"uid":"1","type":"action"}]}}}}')
    expect(vcd_b.stringify(false)).toBe(new VCD(openlabel100_test_actions_b, false).stringify(false))
    //console.log(vcd_c.stringify(false))
    //expect(vcd_c.stringify(false)).toBe('{"vcd":{"frames":{},"schema_version":"4.3.1","frame_intervals":[],"ontologies":{"0":"http://vcd.vicomtech.org/ontology/automotive"},"objects":{"0":{"name":"","type":"Pedestrian","ontology_uid":"0"},"1":{"name":"","type":"Car","ontology_uid":"0"}},"actions":{"0":{"name":"","type":"Walking","ontology_uid":"0","action_data":{"num":[{"name":"subject","val":0}]},"action_data_pointers":{"subject":{"type":"num","frame_intervals":[]}}},"1":{"name":"","type":"Parked","ontology_uid":"0","action_data":{"num":[{"name":"subject","val":1}]},"action_data_pointers":{"subject":{"type":"num","frame_intervals":[]}}}}}}')
    expect(vcd_c.stringify(false)).toBe(new VCD(openlabel100_test_actions_c, false).stringify(false))
});

test('test_relations', () => {
    // This tests shows how relations can be created with and without frame interval information
    let vcd = new OpenLABEL()

    // Case 1: RDF elements don't have frame interval, but relation does
    // So objects don't appear in frames, but relation does. Reading the relation leads to the static objects
    let uid1 = vcd.addObject("", "Car")
    let uid2 = vcd.addObject("", "Pedestrian")

    vcd.addRelationObjectObject("", "isNear",
                                    uid1, uid2, null, null, 
                                    [0, 10])

    expect(vcd.getData()['openlabel']['frame_intervals'][0]['frame_start']).toBe(0)
    expect(vcd.getData()['openlabel']['frame_intervals'][0]['frame_end']).toBe(10)
    expect(vcd.getData()['openlabel']['relations'][0]['frame_intervals'][0]['frame_start']).toBe(0)
    expect(vcd.getData()['openlabel']['relations'][0]['frame_intervals'][0]['frame_end']).toBe(10)
    for (let frame_key in vcd.getData()['openlabel']['frames']) {        
        let relations = vcd.getData()['openlabel']['frames'][frame_key]['relations']        
        expect(Object.keys(relations).length).toBe(1)
    }

    //console.log(vcd.stringify(false))
    //expect(vcd.stringify(false)).toBe('{"vcd":{"frames":{"0":{"relations":{"0":{}}},"1":{"relations":{"0":{}}},"2":{"relations":{"0":{}}},"3":{"relations":{"0":{}}},"4":{"relations":{"0":{}}},"5":{"relations":{"0":{}}},"6":{"relations":{"0":{}}},"7":{"relations":{"0":{}}},"8":{"relations":{"0":{}}},"9":{"relations":{"0":{}}},"10":{"relations":{"0":{}}}},"schema_version":"4.3.1","frame_intervals":[{"frame_start":0,"frame_end":10}],"objects":{"0":{"name":"","type":"Car"},"1":{"name":"","type":"Pedestrian"}},"relations":{"0":{"name":"","type":"isNear","frame_intervals":[{"frame_start":0,"frame_end":10}],"rdf_subjects":[{"uid":"0","type":"object"}],"rdf_objects":[{"uid":"1","type":"object"}]}}}}')
    expect(vcd.stringify(false)).toBe(new VCD(openlabel100_test_relations_1, false).stringify(false))

    // Case 2: RDF elements defined with long frame intervals, and relation with smaller inner frame interval
    vcd = new VCD()

    uid1 = vcd.addObject("", "Car", [0, 10])
    uid2 = vcd.addObject("", "Pedestrian", [5, 15])

    vcd.addRelationObjectObject("", "isNear",
                                    uid1, uid2, null, null,
                                    [7, 9])

    expect(vcd.getData()['openlabel']['frame_intervals'][0]['frame_start']).toBe(0)
    expect(vcd.getData()['openlabel']['frame_intervals'][0]['frame_end']).toBe(15)
    expect(vcd.getData()['openlabel']['relations'][0]['frame_intervals'][0]['frame_start']).toBe(7)
    expect(vcd.getData()['openlabel']['relations'][0]['frame_intervals'][0]['frame_end']).toBe(9)
    for (let frame_key in vcd.getData()['openlabel']['frames']) {
        if (7 <= +frame_key && +frame_key <= 9) {  // + operator to convert from string to number
            let frame_val = vcd.getData()['openlabel']['frames'][frame_key]
            let relations = frame_val['relations']
            expect(Object.keys(relations).length).toBe(1)
        }
    }

    //console.log(vcd.stringify(false))
    //expect(vcd.stringify(false)).toBe('{"vcd":{"frames":{"0":{"objects":{"0":{}}},"1":{"objects":{"0":{}}},"2":{"objects":{"0":{}}},"3":{"objects":{"0":{}}},"4":{"objects":{"0":{}}},"5":{"objects":{"0":{},"1":{}}},"6":{"objects":{"0":{},"1":{}}},"7":{"objects":{"0":{},"1":{}},"relations":{"0":{}}},"8":{"objects":{"0":{},"1":{}},"relations":{"0":{}}},"9":{"objects":{"0":{},"1":{}},"relations":{"0":{}}},"10":{"objects":{"0":{},"1":{}}},"11":{"objects":{"1":{}}},"12":{"objects":{"1":{}}},"13":{"objects":{"1":{}}},"14":{"objects":{"1":{}}},"15":{"objects":{"1":{}}}},"schema_version":"4.3.1","frame_intervals":[{"frame_start":0,"frame_end":15}],"objects":{"0":{"name":"","type":"Car","frame_intervals":[{"frame_start":0,"frame_end":10}]},"1":{"name":"","type":"Pedestrian","frame_intervals":[{"frame_start":5,"frame_end":15}]}},"relations":{"0":{"name":"","type":"isNear","frame_intervals":[{"frame_start":7,"frame_end":9}],"rdf_subjects":[{"uid":"0","type":"object"}],"rdf_objects":[{"uid":"1","type":"object"}]}}}}')
    expect(vcd.stringify(false)).toBe(new VCD(openlabel100_test_relations_2, false).stringify(false))

    // Case 3: RDF elements have frame interval and relation doesn't (so it is left frame-less)
    vcd = new VCD()

    uid1 = vcd.addObject("", "Car", [0, 10])
    uid2 = vcd.addObject("", "Pedestrian", [5, 15])
    let uid3 = vcd.addObject("", "Other", [15, 20])

    let uid4 = vcd.addRelationObjectObject("", "isNear",
                                    uid1, uid2)

    // The relation does not have frame information
    expect('frame_intervals' in vcd.getRelation(uid4)).toBe(false)

    expect(vcd.getData()['openlabel']['frame_intervals'][0]['frame_start']).toBe(0)
    expect(vcd.getData()['openlabel']['frame_intervals'][0]['frame_end']).toBe(20)
    for (let frame_key in vcd.getData()['openlabel']['frames']) {
        if (0 <= +frame_key && +frame_key <= 15) {
            let frame_val = vcd.getData()['openlabel']['frames'][frame_key]            
            expect(!('relations' in frame_val)).toBe(true)
        }
    }

    //console.log(vcd.stringify(false))
    //expect(vcd.stringify(false)).toBe('{"vcd":{"frames":{"0":{"objects":{"0":{}}},"1":{"objects":{"0":{}}},"2":{"objects":{"0":{}}},"3":{"objects":{"0":{}}},"4":{"objects":{"0":{}}},"5":{"objects":{"0":{},"1":{}}},"6":{"objects":{"0":{},"1":{}}},"7":{"objects":{"0":{},"1":{}}},"8":{"objects":{"0":{},"1":{}}},"9":{"objects":{"0":{},"1":{}}},"10":{"objects":{"0":{},"1":{}}},"11":{"objects":{"1":{}}},"12":{"objects":{"1":{}}},"13":{"objects":{"1":{}}},"14":{"objects":{"1":{}}},"15":{"objects":{"1":{},"2":{}}},"16":{"objects":{"2":{}}},"17":{"objects":{"2":{}}},"18":{"objects":{"2":{}}},"19":{"objects":{"2":{}}},"20":{"objects":{"2":{}}}},"schema_version":"4.3.1","frame_intervals":[{"frame_start":0,"frame_end":20}],"objects":{"0":{"name":"","type":"Car","frame_intervals":[{"frame_start":0,"frame_end":10}]},"1":{"name":"","type":"Pedestrian","frame_intervals":[{"frame_start":5,"frame_end":15}]},"2":{"name":"","type":"Other","frame_intervals":[{"frame_start":15,"frame_end":20}]}},"relations":{"0":{"name":"","type":"isNear","rdf_subjects":[{"uid":"0","type":"object"}],"rdf_objects":[{"uid":"1","type":"object"}]}}}}')
    expect(vcd.stringify(false)).toBe(new VCD(openlabel100_test_relations_3, false).stringify(false))
   
});

test('test_scene_KITTI_Tracking_3', () => {
    let sequence_number = 3
    //vcd_file_name = './etc/' + openlabel_version_name + '_kitti_tracking_' + str(sequence_number).zfill(4) + ".json"
    let vcd = new OpenLABEL(openlabel100_kitti_tracking_0003)

    let frame_num_last = vcd.getFrameIntervals().getOuter()['frame_end']

    //In a city, being sunny, the ego-vehicle drives in the left lane of a single-way two-lanes road, 
    //Two other cars drive in the right lane. When the cars pass the ego-vehicle, then the ego-vehicle changes 
    //to the right lane, and then the ego-vehicle drives in the right lane."
  
    vcd.addMetadataProperties({"cnl_text": "In a city, being sunny, the ego-vehicle drives in the left lane of a single-way two-lanes road, Two other cars drive in the right lane. When the cars pass the ego-vehicle, then the ego-vehicle changes to the right lane, and then the ego-vehicle drives in the right lane."})

    //Let's add VCD entries following the order
    //Contexts (1-2)
    vcd.addContext("City1", "City")
    vcd.addContext("Sunny1", "Sunny")

    //Add non-labeled actors (Ego-vehicle and lanes)
    let uid_ego = vcd.getObjectUidByName("Egocar")
    let uid_lane_left = vcd.addObject("Lane1", "Lane")
    let uid_lane_right = vcd.addObject("Lane2", "Lane")
    let uid_road = vcd.addObject("Road1", "Road")

    vcd.addElementData(ElementType.object, uid_lane_left, new types.Text("Position", "Left"))
    vcd.addElementData(ElementType.object, uid_lane_right,new types.Text("Position", "Right"))
    vcd.addElementData(ElementType.object, uid_road, new types.Text("Direction", "Single-way"))
    vcd.addElementData(ElementType.object, uid_road, new types.Num("NumberOfLanes", 2))

    vcd.addRelationObjectObject("", "isPartOf", uid_lane_left, uid_road)
    vcd.addRelationObjectObject("", "isPartOf", uid_lane_right,uid_road)

    //Actors
    let uid_car_a = "0"   // (0, 75)
    let uid_car_b = "1"   // (22, 143)
    let uid_car_other_a = "3"
    let uid_car_other_b = "4"
    let uid_van = "5"
    let uid_car_other_c = "6"
    let uid_car_other_d = "7"
    let uid_car_other_e = "8"

    //Actions
    //Driving straight before lane change
    let uid_action_drive_straight_1 = vcd.addAction("DriveStraight1", "DriveStraight", new Array(0, 31))  //Approx. at frame 31, the ego vehicle starts changing lane
    vcd.addRelationObjectAction("", "isSubjectOfAction", uid_ego, uid_action_drive_straight_1)
    vcd.addRelationObjectAction("", "isObjectOfAction", uid_lane_left,uid_action_drive_straight_1)

    let uid_action_drive_straight_2 = vcd.addAction("DriveStraight2", "DriveStraight", vcd.getElementFrameIntervals(ElementType.object, uid_car_a).get())
    vcd.addRelationObjectAction("", "isSubjectOfAction", uid_car_a, uid_action_drive_straight_2)
    vcd.addRelationObjectAction("", "isObjectOfAction", uid_lane_right, uid_action_drive_straight_2)

    let uid_action_drive_straight_3 = vcd.addAction("DriveStraight3", "DriveStraight", vcd.getElementFrameIntervals(ElementType.object, uid_car_b).get())
    vcd.addRelationObjectAction("", "isSubjectOfAction", uid_car_b,uid_action_drive_straight_3)
    vcd.addRelationObjectAction("", "isObjectOfAction", uid_lane_right,uid_action_drive_straight_3)

    //Lane changing (event and action)
    let uid_action_lane_change = vcd.addAction("LaneChange1", "LaneChange", new Array(33, 75))
    vcd.addRelationObjectAction("", "isSubjectOfAction", uid_ego, uid_action_lane_change)
        
    let uid_event_pass = vcd.addEvent("Pass1", "Pass", 32)
    vcd.addRelationSubjectObject("", "isSubjectOfEvent", ElementType.object, uid_car_b, ElementType.event, uid_event_pass,null,null,null,null,null)
    vcd.addRelationSubjectObject("", "isObjectOfEvent", ElementType.object, uid_ego, ElementType.event, uid_event_pass,null,null,null,null,null)
    vcd.addRelationSubjectObject("", "causes",ElementType.event,uid_event_pass,ElementType.action, uid_action_lane_change,null,null,null,null,null)

    //Driving straight after lane change
    let uid_action_drive_straight_4 = vcd.addAction("DriveStraight1", "DriveStraight", new Array(76, frame_num_last))  // Approx. at frame 31, the ego vehicle starts changing lane
    vcd.addRelationObjectAction("", "isSubjectOfAction", uid_ego, uid_action_drive_straight_4)
    vcd.addRelationObjectAction("", "isObjectOfAction", uid_lane_right,uid_action_drive_straight_4)

    
    vcd.addRelationActionAction("", "meets",uid_action_lane_change,uid_action_drive_straight_4,null,null,75)

    let expected=new VCD(openlabel100_test_scene_KITTI_Tracking_3, false).stringify(false)
    //Check equal to reference JSON
    expect(vcd.stringify(false)).toBe(new VCD(openlabel100_test_scene_KITTI_Tracking_3, false).stringify(false))



})