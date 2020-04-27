import json

def write_output(text):
    with open(output_file, 'a') as output:
        print(text)
        output.write('%s\n' % text)

json_file = 'test task data/OntoNotes.json'
output_file = 'test task data/OntoNotes output.txt'

with open(json_file) as json_data:
    data = json.load(json_data)

t_index = 0
for entry in data:
    t_index += 1
    text = entry[0]
    entities = entry[1]["entities"]

    write_output('Text %d : %s' % (t_index, text))

    a_index = 0
    for annotation_info in entities:
        a_index += 1
        a_start = annotation_info[0]
        a_end = annotation_info[1]
        a_label = annotation_info[2]
        a_text = text[a_start:a_end]
        write_output('Annotation %d (%s): %s' % (a_index, a_label, a_text))
