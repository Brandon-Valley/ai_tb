
import subprocess


TEST_TB_USER_INPUT_STR =  """
        Given these 2 dirs (d1 & d2) and 1 vid, d1 & d2 both contain a number of images,
        make 1 vid by contacting all imgs in d1, then play the vid, then concat all imgs in d2
    """

CONCAT_VIDS_DESCRIP_D = {
    "natural_lang_description" : "Concatenates given vids into single vid in order given",
    "param_natural_lang_description" : 
        [
            {
                "param_name" : "vid_l",
                "param_natural_lang_description" : "List of vids to be concatenated in order",
                "optional" : False
            }
        ]
}

CONCAT_IMGS_DESCRIP_D = {
    "natural_lang_description" : "Concatenates given imgs into a slideshow-like video, optional audio",
    "param_natural_lang_description" : 
        [
            {
                "param_name" : "img_list",
                "param_natural_lang_description" : "List of imgs to be concatenated",
                "optional" : False
            },
            {
                "param_name" : "num_sec_per_img",
                "param_natural_lang_description" : "Number of seconds to display each img"
            }
        ]
}
INSERT_VID_DESCRIP_D = {} # TODO

VID_AND_2_IMG_DIRS_FILE_STRUC_EXTERNAL_KNOWLEDGE = """
    - d0 /
        - vid0.mp4
        - d1 /
            - i.jpg
            - i.png
            - i.png
            - i.bmp
            - i.jpg
        - d2 /
            - i.jpg
            - i.png
            - i.png
            - i.bmp
            - i.jpg
    """

def get_ai_processed_user_input(tb_user_input_str, output_type, output_descrip, capability_descrip = None, external_knowledge = None, external_knowledge_type = None, num_allowed_revisions = 0):
    """
        output_type:
            - "simple_instructions"
            - "instructions_w_conditions"
            - "settings_search" - compatibility/capability?
        num_allowed_revisions
        external_knowledge_type:
            - "file_structure"
            - # TODO
    """


# Test - achieving same result from different capabilities
def test_0():
    output = get_ai_processed_user_input(
        tb_user_input_str = TEST_TB_USER_INPUT_STR,    
        output_type = "instructions_w_conditions",
        output_descrip = [], # TODO
        capability_descrip = {
            # ??? will AI be better at dealing with audio_track param here or adding a separate add_audio_to_vid() func?
            "concat_imgs_into_vid(img_list, num_sec_per_img = 2)" : CONCAT_IMGS_DESCRIP_D,
            "concat_vids(vid_l)" : CONCAT_VIDS_DESCRIP_D
            },
        external_knowledge = VID_AND_2_IMG_DIRS_FILE_STRUC_EXTERNAL_KNOWLEDGE,
        external_knowledge_type = "file_structure",
        num_allowed_revisions = 2)

    # TODO write convo between ai text box user clarifying what they want, maybe about if user doesn't give num_sec_per_img?
    # TODO should it change if num_sec_per_img is not given a default value?
    # TODO Should there be a param for if a default is given but no time per img is given by user, about if AI should use 
    # TODO  a revision to ask "you didn't give a num_sec_per_img, is 2 seconds alright?"

    return output

# TODO show what output looks like - just a super simply py program using capability functions
    
# Test - achieving same result from different capabilities
def test_1():
    output = get_ai_processed_user_input(
        tb_user_input_str = TEST_TB_USER_INPUT_STR,    
        output_type = "instructions_w_conditions",
        output_descrip = [], # TODO
        capability_descrip = {
            # ??? will AI be better at dealing with audio_track param here or adding a separate add_audio_to_vid() func?
            "concat_imgs_into_vid(img_list, num_sec_per_img = 2)" : CONCAT_IMGS_DESCRIP_D,
            "insert_vid(base_vid, vid_to_insert, timestamp" : INSERT_VID_DESCRIP_D,
            },
        external_knowledge = VID_AND_2_IMG_DIRS_FILE_STRUC_EXTERNAL_KNOWLEDGE,
        external_knowledge_type = "file_structure",
        num_allowed_revisions = 2)

    # TODO How much do you trust the AI to handle internal relation of capabilities?
    # TODO - ie. do you need to some kind of "predict_vid_len_from_concatenated_imgs()" func to know where to insert given vid?
    # TODO  - even then you still need it to store that value and remember how to use it
    return output

# TODO show what output looks like - just a super simply py program using capability functions

# somehow this magically handles importing all capabilities as a library or something such that ai_tb_output executes as a valid ?python? program
def execute_ai_instructions(ai_instructions):
    # pretend this outputs the content of a written file or something?
    return subprocess.call(f"python {ai_instructions}", shell=True)

def main():
    if execute_ai_instructions(test_0()) == execute_ai_instructions(test_1()):
        print("Success!")