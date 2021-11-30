import Bioadd

def test_translate():
    output = Bioadd.translate("ATGGATGGT")
    assert output == "MDG"

    output = Bioadd.translate("ATGGATG")
    assert output == "MD"

    output = Bioadd.translate(("ATG ATG"))
    assert output == "M"