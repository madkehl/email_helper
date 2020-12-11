import pandas as pd


def create_template(part_name, id_code):
    """
    uses template to create email
    :param part_name: participant name
    :param id_code: id code (no prefix)
    :return:
    """

    key_dict = {
        'participant_name': part_name,
        'lab_name': 'Personality Processes and Outcomes Laboratory',
        'id_code': 'AGCW' + str(id_code),
        'my_name': 'Madeline Kehl'
    }

    template = """
    Dear {participant_name},
    My name is {my_name}, from the {lab_name} at the University of Pittsburgh. You participated in our study Mental Health and Coping During COVID-19. When you participated in that study, you agreed to be contacted for participation in follow up surveys for this study. We are reaching out now to ask you to complete a follow up survey for this study.
    Coronavirus/COVID-19 is a stressful experience that is different from anything that most of us have experienced in our lifetime. As researchers, we want to understand the effects of the current crisis on mental health. To ask that question, we need to reach out to people (like you) who participated in research related to mental health before COVID-19, so that we can see how mental health has changed from then to now.
    One of the most important parts of answering this question is recruiting a very large and diverse sample of participants who already answered questions about their mental health in the past (before COVID-19). Because of this, we have joined forces with research labs across the United States and abroad to recruit a combined sample of as many as 10,000 people who previously completed studies in our labs and are willing to answer follow-up questions about their mental health now. This will be the first and largest mental health dataset of its kind.
    As a thank you for your time, you will have the option to be compensated with a $10 Amazon e-gift card, a $10 Apple i-Tunes electronic gift card, or a $10 Google Play electronic gift card. (Due to terms of service restrictions, Apple i-Tunes and Google Play compensation options are only available to individuals who reside in the United States.) Compensation will be emailed to you from the lab in which you previously had contact with.
    More detail about the survey is provided in the online consent (link below). You can also feel free to get in touch by emailing the Study Coordinator at ppolpitt@pitt.edu if you have any questions or would like to speak to a researcher directly.
    Just like the last survey, to keep your responses strictly confidential, we are sending all participants a personalized study link and ID code. Authorized individuals from the Personality Processes and Outcomes Lab are the only people who will have access to your name, contact information, and any other personal information. We keep this information in a secure and password protected electronic file that is not shared with anyone else.
    Your ID code: {id_code}
    Please keep this ID code nearby, because we will ask you to enter it a few times during the survey.
    Your personalized study link:
    https://pitt.co1.qualtrics.com/jfe/form/SV_29LSpFZNx3RDRvD
    This link will only work for you, so please do not share it.
    If you no longer want to be contacted for this study, please contact the Study Coordinator at ppolpitt@pitt.edu.
    
    Sincerely,
    
    {my_name}, B.Phil.
    
    Department of Psychology
    University of Pittsburgh""".format(**key_dict)

    return id_code, template


def full_path(df):
    """

    :param df: AAPECS recontacts subset
    :return: df of emales and template
    """
    results = pd.DataFrame(columns=['email', 'template'])
    for j, row in enumerate(df.iterrows()):
        id_code, template = create_template(row['Name'], row['ID'])
        email = row['E-mail']
        results[j]['email'] = email
        results[j]['template'] = template

    return results




