variable_room_number = 0
variable_card_1_measurement_1 = 0
variable_card_1_measurement_2 = 0
variable_card_1_measurement_3 = 0
variable_start_measurement = 0
variable_card_3_afterturn_1 = 0
variable_card_3_afterturn_2 = 0
variable_card_3_afterturn_3 = 0
variable_card_3_afterturn_4 = 0
variable_card_3_afterturn_5 = 0
variable_start_measurement_2 = 0
variable_turn_left_1 = 0
variable_turn_left_2 = 0
variable_left_turn_degree = 0
looking_for_marker = False
looking_for_people = False


def vision_recognized_marker_number_four(msg):
    global looking_for_people
    print("Found Marker 4!")
    if looking_for_people:
        looking_for_people = False
        media_ctrl.play_sound(rm_define.media_custom_audio_0)
        chassis_ctrl.move_with_distance(180, 3)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, variable_card_3_afterturn_1)
        chassis_ctrl.move_with_distance(0, variable_card_3_afterturn_2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        time.sleep(12)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4)

"""
def vision_recognized_people(msg):
    global looking_for_people
    print("Found person!")
    if looking_for_people:
        looking_for_people = False
        vision_ctrl.disable_detection(rm_define.vision_detection_people)
        media_ctrl.play_sound(rm_define.media_custom_audio_0)
        chassis_ctrl.move_with_distance(180, 2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
            #  rmexit()
"""

def vision_recognized_marker_number_one(msg):
    global looking_for_marker
    if looking_for_marker:
        looking_for_marker = False
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, variable_card_1_measurement_1)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, variable_card_1_measurement_2)
        time.sleep(1)
        vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
        gun_ctrl.fire_once()
        time.sleep(1)
        gimbal_ctrl.yaw_ctrl(-50)
        vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
        gun_ctrl.fire_once()
        chassis_ctrl.move_with_distance(180, variable_card_1_measurement_3)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        if variable_room_number == 4:
            user_defined_end()
            rmexit()


def vision_recognized_marker_number_two(msg):
    global looking_for_marker
    if looking_for_marker:
        looking_for_marker = False
        gimbal_ctrl.recenter()


def vision_recognized_marker_number_three(msg):
    global looking_for_marker, looking_for_people
    if looking_for_marker:
        looking_for_marker = False
        gimbal_ctrl.recenter()
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 3)
        time.sleep(1)
        gimbal_ctrl.recenter()
        gimbal_ctrl.yaw_ctrl(-25)
        gimbal_ctrl.pitch_ctrl(15)
        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.set_marker_detection_distance(3)
        looking_for_people = True
        print("Looking for people is set to true.")


def user_defined_end():
    global variable_room_number, variable_card_1_measurement_1, variable_card_1_measurement_2, \
        variable_card_1_measurement_3, variable_start_measurement, variable_card_3_afterturn_1, \
        variable_card_3_afterturn_3, variable_card_3_afterturn_4, variable_card_3_afterturn_5, \
        variable_start_measurement_2, variable_turn_left_1, variable_turn_left_2, variable_left_turn_degree, \
        looking_for_marker, looking_for_people

    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
    chassis_ctrl.move_with_distance(0, 1)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 1)


def user_defined_left_turn():
    global variable_room_number, variable_card_1_measurement_1, variable_card_1_measurement_2, \
        variable_card_1_measurement_3, variable_start_measurement, variable_card_3_afterturn_1, \
        variable_card_3_afterturn_2, variable_card_3_afterturn_3, variable_card_3_afterturn_4, \
        variable_card_3_afterturn_5, variable_start_measurement_2, variable_turn_left_1, variable_turn_left_2, \
        variable_left_turn_degree

    chassis_ctrl.move_with_distance(0, variable_turn_left_1)
    chassis_ctrl.move_with_distance(0, variable_turn_left_2)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, variable_left_turn_degree)


def start():
    global variable_room_number, variable_card_1_measurement_1, variable_card_1_measurement_2, \
        variable_card_1_measurement_3, variable_start_measurement, variable_card_3_afterturn_1, \
        variable_card_3_afterturn_2, variable_card_3_afterturn_3, variable_card_3_afterturn_4, \
        variable_card_3_afterturn_5, variable_start_measurement_2, variable_turn_left_1, variable_turn_left_2, \
        variable_left_turn_degree, looking_for_marker, looking_for_people

    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(50)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    variable_room_number = 1

    while not variable_room_number == 5:

        if variable_room_number == 1:
            variable_start_measurement = 5
            variable_start_measurement_2 = 2
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 0
            variable_card_1_measurement_3 = 0
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
            variable_turn_left_1 = 5
            variable_turn_left_2 = 4
            variable_left_turn_degree = 90

        if variable_room_number == 2:
            variable_start_measurement = 5
            variable_start_measurement_2 = 1.6
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 2
            variable_card_1_measurement_3 = 2
            variable_card_3_afterturn_1 = 5
            variable_card_3_afterturn_2 = 1.6
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
            variable_turn_left_1 = 0
            variable_turn_left_2 = 0
            variable_left_turn_degree = 0

        if variable_room_number == 3:
            variable_start_measurement = 5
            variable_start_measurement_2 = 3.8
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 2
            variable_card_1_measurement_3 = 2
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
            variable_turn_left_1 = 0
            variable_turn_left_2 = 0
            variable_left_turn_degree = 0

        if variable_room_number == 4:
            variable_start_measurement = 5
            variable_start_measurement_2 = 5
            variable_card_1_measurement_1 = 1
            variable_card_1_measurement_2 = 2
            variable_card_1_measurement_3 = 2
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
            variable_turn_left_1 = 0
            variable_turn_left_2 = 0
            variable_left_turn_degree = 0

        gimbal_ctrl.recenter()
        chassis_ctrl.set_trans_speed(2)
        chassis_ctrl.move_with_distance(0,variable_start_measurement)
        chassis_ctrl.move_with_distance(0, variable_start_measurement_2)
        gimbal_ctrl.yaw_ctrl(-40)
        gun_ctrl.set_fire_count(3)
        time.sleep(1)

        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.set_marker_detection_distance(3)
        vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)
        time.sleep(1)
        looking_for_marker = True
        while looking_for_marker:
            gimbal_ctrl.yaw_ctrl(-250)
            gimbal_ctrl.yaw_ctrl(250)

        vision_ctrl.enable_detection(rm_define.vision_detection_people)

        while looking_for_people:
            gimbal_ctrl.yaw_ctrl(-250)
            gimbal_ctrl.yaw_ctrl(250)
            print("Looking for people.")

        vision_ctrl.disable_detection(rm_define.vision_detection_marker)

        if variable_room_number == 1:
            user_defined_left_turn()

        variable_room_number = variable_room_number + 1

    user_defined_end()
    rmexit()