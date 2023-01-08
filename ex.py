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
    get_ai_processed_user_input(
        tb_user_input_str = 
        """
            Given these 2 dirs (d1 & d2) and 1 vid, d1 & d2 both contain a number of images,
            make 1 vid by contacting all imgs in d1, then play the vid, then concat all imgs in d2
        """,    
        output_type = "instructions_w_conditions",
        output_descrip = [],
        capability_descrip = {
            concat_imgs_into_vid : {
                "natural_lang_description" : "Concatenates given imgs into a slideshow-like video, optional audio",
                "param_natural_lang_description" :
                """
                    - 
                """
            }
        },
        external_knowledge = 
        """
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
        """,
        external_knowledge_type = "file_structure",
        num_allowed_revisions = 2)