import json
import csv


def main():
    path = 'pokedex.json'
    with open(path, encoding='utf8') as jsonfile:
        indata = json.load(jsonfile)
        headers = create_headers(indata)

        with open('out.tsv', 'w', encoding='utf8') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow(h for h in headers)
            for d in indata:
                row = []
                for k, v in d.items():
                    counter = 0
                    if type(v) == dict:
                        for k1, v1 in v.items():
                            row.append(v1)
                    elif type(v) == list:
                        for h in headers:
                            newh = h.split('.')
                            if len(newh) > 1 and k == newh[0] and newh[1].isdigit() == True:
                                #count number of potential occurrences of current key
                                counter += 1
                        # append elements and complete with empty string if not all values occur
                        for element in v:
                            row.append(str(element))
                            counter-=1
                        while(counter > 0):
                            row.append("")
                            counter -= 1
                    else:
                        row.append(str(v))
                writer.writerow(row)


def create_headers(indata):
    """
    This function created list of all possible headers
    :param indata: out data
    :return: list of headers
    """
    headers = {}
    for dict in indata:
        for k, v in dict.items():
            outh = transform_header(k, v)
            if len(outh) > 1:
                for element in outh:
                    key = element.split(".")[0]
                    if key in headers.keys():
                        if element not in headers[key]:
                            headers[key].append(element)
                    else:
                        headers[key] = [element]
            elif len(outh) == 1:
                if outh[0].split('.')[0] not in headers.keys():
                    headers[outh[0]] = ""
    out = []
    for k, v in headers.items():
        if type(v) == list:
            l = v
            for e in v:
                if e.split('.')[1].isdigit() == True:
                    l = sorted(v)
                    break

            for e in l:
                out.append(e)
        else:
            out.append(k)
    return out


def transform_header(key, value):
    """
    This functions different datatype of value
    :param key: name of field
    :param value:
    :return: new header with transformed objects as list
    """
    out = []
    index = 0
    if type(value) == list:
        for l in value:
            newl = str(key) + '.' + str(index)
            out.append(newl)
            index+=1
    elif type(value) == dict:
        for k in value.keys():
            newk = str(key) + '.' + str(k)
            out.append(newk)
            index+=1
    else:
        out.append(str(key))
    return out


if __name__ == '__main__':
    main()
