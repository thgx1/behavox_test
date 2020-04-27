import json

def write_output(text):
    with open(output_file, 'a') as output:
        print(text)
        output.write('%s\n' % text)

json_file = 'test task data/Enron sentences .json'
output_file = 'test task data/Enron sentences output.txt'

with open(json_file) as json_data:
    data = json.load(json_data)

t_index = 0
for entry in data:
    t_index += 1
    text = entry["text"]
    m_entities = entry["machine_entities"]
    h_entities = entry["human_entities"]

    write_output('Text %d : %s' % (t_index, text))

    if len(m_entities) != 0:
        a_index = 0
        for annot_info in m_entities:
            a_index += 1
            a_start = annot_info[0]
            a_end = annot_info[1]
            a_text = text[a_start:a_end]
            write_output('Machine Annotation %d : %s' % (a_index, a_text))
    if len(h_entities) != {}:
        for a_id in h_entities:
            annotations = h_entities[a_id]
            a_index = 0
            for annot_info in annotations:
                a_index += 1
                a_start = annot_info[0]
                a_end = annot_info[1]
                if annot_info[2] == "ORG" and annot_info[3] == "human": # this is based on the annotation guidelines
                    a_type = "False Negative" 
                elif annot_info[2] == "":
                    a_type = "False Positive"
                else:
                    a_type = 'True Positive'
                a_text = text[a_start:a_end]
                write_output('Human Annotation (%s) %d (%s): %s' % (a_id, a_index, a_type, a_text))
