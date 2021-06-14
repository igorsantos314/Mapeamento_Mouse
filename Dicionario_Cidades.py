
class citys:

    def __init__(self):
        #DICIONARIO
        self.disc_cidades = {
                        #AREA AZUL CLARO
                        4:'Barroquinha',
                        10:'Camocim',
                        24:'Chaval',
                        42:'Granja',
                        75:'Jijoca de Jericoacoara',
                        84:'Matinópole',
                        158:'Uruoca',
                        31:'Cruz',
                        7:'Bela Cruz',
                        83:'Marco',
                        96:'Morrinhos',
                        164:'Acaraú',
                        67:'Itarema',
                        #AREA VERMELHA
                        161:'Viçosa Do Ceará',
                        151:'Tianguá',
                        154:'Ubajara',
                        51:'Ibiapina',
                        138:'São Benedito',
                        18:'Carnaubal',
                        46:'Guaraciaba Do Norte',
                        30:'Croatá',
                        58:'Ipu',
                        #AREA VERMELHA
                        120:'Pires Ferreira',
                        159:'Varjota',
                        131:'Reriutaba',
                        107:'Pacujá',
                        41:'Graça',
                        15:'Cariré',
                        44:'Groaíras',
                        97:'Mucambo',
                        39:'Frecheirinha',
                        27:'Coreaú',
                        144:'Sobral',
                        36:'Forquilha',
                        87:'Meruoca',
                        167:'Alcântaras',
                        95:'Moraújo',
                        85:'Massapê',
                        135:'Santana Do Acaraú',
                        143:'Senador Sá',
                        #AREA AZUL
                        59:'Ipueiras',
                        48:'Hidrolândia',
                        137:'Santa Quitéria',
                        21:'Catunda',
                        93:'Monsenhor Tabosa',
                        147:'Tamboril',
                        100:'Nova Russas',
                        176:'Ararendá',
                        56:'Ipaporanga',
                        121:'Poranga',
                        28:'Crateús',
                        55:'Independência',
                        101:'Novo Oriente',
                        #AREA ROZA CLARO
                        125:'Quiterianópolis',
                        149:'Tauá',
                        179:'Arneiroz',
                        112:'Parambu',
                        166:'Aiuaba',
                        #AREA VERDE CLARO
                        134:'Salitre',
                        177:'Araripe',
                        11:'Campos Sales',
                        123:'Potengi',
                        136:'Santana Do Cariri',
                        168:'Altaneira',
                        180:'Assaré',
                        171:'Antonina Do Norte',
                        148:'Tarrafas',
                        35:'Farias Brito',
                        29:'Crato',
                        76:'Juazeiro Do Norte',
                        1:'Barbalha',
                        91:'Missão Velha',
                        162:'Abaiara',
                        9:'Brejo Santo',
                        74:'Jarti',
                        73:'Jardim',
                        115:'Penaforte',
                        16:'Caririaçu',
                        160:'Varzea Alegre',
                        43:'Granjeiro',
                        78:'Lavras Da Mangabeira',
                        181:'Aurora',
                        3:'Barro',
                        86:'Mauriti',
                        88:'Milagres',
                        122:'Porteiras',
                        #AREA ROZA ESCURO
                        57:'Ipaumirim',
                        182:'Baixio',
                        155:'Umari',
                        184:'Icó',
                        23:'Cedro',
                        103:'Orós',
                        127:'Quixelô',
                        54:'Iguatu',
                        17:'Cariús',
                        77:'Jucás',
                        165:'Acopiara',
                        133:'Saboeiro',
                        20:'Catarina',
                        #AREA AMARELO CLARO
                        119:'Piquet Carneiro',
                        32:'Dep. Irapuan Pinheiro',
                        145:'Solonópole',
                        89:'Milhã',
                        142:'Senador Pompeu',
                        92:'Mombaça',
                        114:'Pedra Branca',
                        128:'Quixeramobim',
                        183:'Banabuiú',
                        126:'Quixadá',
                        52:'Ibicuitinga',
                        50:'Ibaretama',
                        25:'Choró',
                        #AREA CINZA
                        8:'Boa Viagem',
                        80:'Madalena',
                        68:'Itatira',
                        12:'Canindé',
                        14:'Caridade',
                        113:'Paramoti',
                        #AREA LARANJA ESCURO
                        33:'Ereré',
                        117:'Pereiro',
                        71:'Jaguaribe',
                        60:'Iracema',
                        124:'Poteretama',
                        169:'Alto Santo',
                        70:'Jaguaribara',
                        69:'Jaguaretama',
                        94:'Morada Nova',
                        140:'São João Do Jaguaribe',
                        146:'Tabuleiro Do Norte',
                        79:'Limoeiro Do Norte',
                        129:'Quixeré',
                        132:'Russas',
                        108:'Palhano',
                        #AREA COR DE PELE
                        53:'Icapuí',
                        174:'Aracati',
                        72:'Jaguaruana',
                        62:'Itaiçaba',
                        38:'Aracati',
                        6:'Beberibe',
                        #AREA VERDE AMAZONIA
                        102:'Ocara',
                        175:'Aracoiaba',
                        2:'Barreira',
                        5:'Baturité',
                        13:'Capistrano',
                        66:'Itapiúna',
                        178:'Aratuba',
                        98:'Mulungu',
                        47:'Guaramiranga',
                        106:'Pacoti',
                        109:'Palmácia',
                        130:'Redenção',
                        163:'Acarape',
                        #AREA VERDE BANDEIRA
                        19:'Cascavel',
                        118:'Pindoretama',
                        173:'Aquiraz',
                        34:'Eusébio',
                        37:'Fortaleza',
                        63:'Itaitinga',
                        105:'Pacatuba',
                        81:'Maracanaú',
                        45:'Guaiúba',
                        49:'Horizonte',
                        104:'Pacajus',
                        26:'Chorozinho',
                        82:'Maranguape',
                        22:'Caucaia',
                        139:'São Gonçaalo Do Amarante',
                        141:'São Luís Do Curu',
                        110:'Paracuru',
                        111:'Paraipana',
                        152:'Trairi',
                        170:'Amontada',
                        65:'Itapipoca',
                        153:'Tururu',
                        156:'Umirim',
                        116:'Pentecoste',
                        172:'Apuiarés',
                        40:'General Sampaio',
                        150:'Tejuçuoca',
                        61:'Irauçuba',
                        90:'Miraíma',
                        157:'Uruburetama',
                        64:'Itapajé',
                        99:'Nova Olinda'
        }