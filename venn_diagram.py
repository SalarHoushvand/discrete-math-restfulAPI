import base64
import matplotlib_venn as vplt
from matplotlib import pyplot as plt



def ven2( set1,  set2):
    """Venn Diagram example for 2 sets"""


    # length of sets for venn diagram
    a = len(set1)
    b = len(set2)
    c = len(set1.intersection(set2))
    print('Intersection : ' + str(set1.intersection(set2)))

    # Venn Diagram
    v = vplt.venn2(subsets={'10': a, '01': b, '11': c}, set_labels=('A', 'B'))
    l1 = ','.join(map(str, set1.difference(set2)))
    v.get_label_by_id('10').set_text(l1)
    l2 = ','.join(map(str, set2.difference(set1)))
    v.get_label_by_id('01').set_text(l2)
    l3 = ','.join(map(str, set2.intersection(set1)))
    v.get_label_by_id('11').set_text(l3)

    plt.savefig('figure.png')
    plt.close()
    encoded = str(base64.b64encode(open("figure.png", "rb").read())).replace("b'"," ").replace("'","")
    img = 'data:image/png;base64,%s' % encoded

    return img

