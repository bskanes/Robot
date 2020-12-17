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
def user_defined_end():
    global variable_room_number
    global variable_card_1_measurement_1
    global variable_card_1_measurement_2
    global variable_card_1_measurement_3
    global variable_start_measurement
    global variable_card_3_afterturn_1
    global variable_card_3_afterturn_2
    global variable_card_3_afterturn_3
    global variable_card_3_afterturn_4
    global variable_card_3_afterturn_5
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)
    chassis_ctrl.move_with_distance(0,1)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1)
def user_defined_left_turn():
    global variable_room_number
    global variable_card_1_measurement_1
    global variable_card_1_measurement_2
    global variable_card_1_measurement_3
    global variable_start_measurement
    global variable_card_3_afterturn_1
    global variable_card_3_afterturn_2
    global variable_card_3_afterturn_3
    global variable_card_3_afterturn_4
    global variable_card_3_afterturn_5
    chassis_ctrl.move_with_distance(0,1)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
def start():
    global variable_room_number
    global variable_card_1_measurement_1
    global variable_card_1_measurement_2
    global variable_card_1_measurement_3
    global variable_start_measurement
    global variable_card_3_afterturn_1
    global variable_card_3_afterturn_2
    global variable_card_3_afterturn_3
    global variable_card_3_afterturn_4
    global variable_card_3_afterturn_5
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    variable_room_number = 1
    while not variable_room_number == 5:
        if variable_room_number == 1:
            variable_start_measurement = 0
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 0
            variable_card_1_measurement_3 = 0
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
        if variable_room_number == 2:
            variable_start_measurement = 0
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 0
            variable_card_1_measurement_3 = 0
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
        if variable_room_number == 3:
            variable_start_measurement = 0
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 0
            variable_card_1_measurement_3 = 0
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
        if variable_room_number == 4:
            variable_start_measurement = 0
            variable_card_1_measurement_1 = 0
            variable_card_1_measurement_2 = 0
            variable_card_1_measurement_3 = 0
            variable_card_3_afterturn_1 = 0
            variable_card_3_afterturn_2 = 0
            variable_card_3_afterturn_3 = 0
            variable_card_3_afterturn_4 = 0
            variable_card_3_afterturn_5 = 0
        gimbal_ctrl.recenter()
        chassis_ctrl.set_trans_speed(1)
        chassis_ctrl.move_with_distance(0,variable_start_measurement)
        gimbal_ctrl.rotate(rm_define.gimbal_left)
        gun_ctrl.set_fire_count(3)
        time.sleep(1)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.set_marker_detection_distance(3)
        vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)
        time.sleep(1)
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_one):
            gimbal_ctrl.recenter()
            chassis_ctrl.move_with_distance(0,variable_card_1_measurement_1)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
            chassis_ctrl.move_with_distance(0,variable_card_1_measurement_2)
            time.sleep(1)
            vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
            gun_ctrl.fire_once()
            chassis_ctrl.move_with_distance(180,variable_card_1_measurement_3)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_two):
            gimbal_ctrl.recenter()
        if vision_ctrl.check_condition(rm_define.cond_recognized_marker_number_three):
            gimbal_ctrl.recenter()
            chassis_ctrl.move_with_distance(0,1)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
            chassis_ctrl.move_with_distance(0,1)
            time.sleep(1)
            if vision_ctrl.check_condition(rm_define.cond_recognized_people):
                if variable_room_number == 1:
                    media_ctrl.play_sound(rm_define.media_custom_audio_undefined,wait_for_complete_flag=True)
                    chassis_ctrl.move_with_distance(180,1)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
                    chassis_ctrl.move_with_distance(0,1)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
                    chassis_ctrl.move_with_distance(0,1)
                else:
                    media_ctrl.play_sound(rm_define.media_custom_audio_undefined,wait_for_complete_flag=True)
                    chassis_ctrl.move_with_distance(180,1)
                    if variable_room_number == 4:
                        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
                        user_defined_end()

                        rmexit()
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
                    chassis_ctrl.move_with_distance(0,1)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
                    chassis_ctrl.move_with_distance(0,1)
                    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
                    chassis_ctrl.move_with_distance(0,1)
                    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
                    chassis_ctrl.move_with_distance(0,1)
            else:
                chassis_ctrl.move_with_distance(180,1)
                chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
                if variable_room_number == 4:
                    user_defined_end()

                    rmexit()
        if variable_room_number == 1:
            user_defined_left_turn()

        variable_room_number = variable_room_number + 1
    user_defined_end()

    rmexit()