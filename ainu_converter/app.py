from flask import Flask, request
app = Flask(__name__)

@app.route('/projects', methods=['GET', 'POST'])
def convertText():
    entertext = request.form['entertext']
    ainudict = {
        'チュ':'cu',
        'チェ':'ce',
        'チョ':'co',
        'ウォ': 'wo',
        'ウィ': 'wi',
        'イェ': 'ye',
        'ショ': 'so',
        'シェ':'se',
        'シュ':'su',
        'ウェ':'we',
        'シャ':'sa',
        'チャ':'ca',
        'ア':'a',
        'エ':'e',
        'オ':'o',
        'セ゚':'ce',
        'カ':'ka',
        'キ':'ki',
        'ㇷ゚':'p',
        'ク':'ku',
        'ケ':'ke',
        'コ':'ko',
        'ㇰ':'k',
        'サ':'sa',
        'シ':'si',
        'ス':'su',
        'セ':'se',
        'ソ':'so',
        'ㇱ':'s',
        'ㇲ':'s',
        'タ':'ta',
        'ト゚':'tu',
        'ツ゚':'tu',
        'テ':'te',
        'ト':'to',
        'ㇳ':'t',
        'チ':'ci',
        'ツ':'cu',
        'ナ':'na',
        'ニ':'ni',
        'ヌ':'nu',
        'ネ':'ne',
        'ノ':'no',
        'ㇴ':'n',
        'ハ':'ha',
        'ヒ':'hi',
        'フ':'hu',
        'ヘ':'he',
        'ホ':'ho',
        'ㇵ':'h',
        'ㇶ':'h',
        'ㇷ':'h',
        'ㇸ':'h',
        'ㇹ':'h',
        'パ':'pa',
        'ピ':'pi',
        'プ':'pu',
        'ペ':'pe',
        'ポ':'po',
        'マ': 'ma',
        'ミ':'mi',
        'ム':'mu',
        'メ':'me',
        'モ':'mo',
        'ㇺ':'m',
        'ヤ':'ya',
        'ユ':'yu',
        'ヨ':'yo',
        'ラ':'ra',
        'リ':'ri',
        'ル':'ru',
        'レ':'re',
        'ロ':'ro',
        'ㇻ':'r',
        'ㇼ':'r',
        'ㇽ':'r',
        'ㇾ':'r',
        'ㇿ':'r',
        'ワ':'wa',
        'ヰ':'wi',
        'ヱ':'we',
        'ヲ':'wo',
        'ィ':'y',
        'ゥ':'w',
        '。':'.',
        '？':'?',
        '、':','
    }
    list_text = entertext.split('　')
    ainu_items = ainudict.items()
    converted_list = []
    for word in list_text:
        for kana, latin in ainudict.items():
            word = word.replace(kana, latin)
        if word.endswith('イ'):
            word = word.replace('イ', 'y')
        elif 'イ' in word:
            word = word.replace('イ', 'i')
        if word.endswith('ウ'):
            word = word.replace('ウ', 'w')
        elif 'ウ' in word:
            word = word.replace('ウ', 'u')
        if word.endswith('ッ'):
            word = word.replace('ッ', 't')
        elif 'ッ' in word:
            word = word.replace('ッ', word[(word.index('ッ')+1)])
        if 'ン' in word:
            if word[(word.index('ン')-1)] == 'u':
                word = word.replace('ン', 'm')
            else:
                word = word.replace('ン', 'n')
        word = word.replace('\u3000', ' ')
        converted_list.append(word)
    converted = ' '.join(converted_list)
    converted = converted.capitalize()
    return converted
