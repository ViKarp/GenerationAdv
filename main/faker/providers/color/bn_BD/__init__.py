from collections import OrderedDict

from .. import Provider as ColorProvider

localized = True


class Provider(ColorProvider):
    """Implement color provider for ``bn_BD`` locale."""

    all_colors = OrderedDict(
        (
            ("এলিস নীল", "#F0F8FF"),
            ("এন্টিক সাদা", "#FAEBD7"),
            ("জল রং", "#00FFFF"),
            ("হালকা নীল সবুজ", "#7FFFD4"),
            ("উজ্জ্বল নীল", "#F0FFFF"),
            ("ফ্যাকাশে বেলে হলুদ বাদামী", "#F5F5DC"),
            ("বিস্কুট রং", "#FFE4C4"),
            ("কালো", "#000000"),
            ("বালু রং", "#FFEBCD"),
            ("নীল", "#0000FF"),
            ("নীলাভ রক্তবর্ণ", "#8A2BE2"),
            ("বাদামী", "#A52A2A"),
            ("কাঠ রং", "#DEB887"),
            ("সামরিক নীল", "#5F9EA0"),
            ("উজ্জ্বল হলুদাভ সবুজ", "#7FFF00"),
            ("চকলেট রং", "#D2691E"),
            ("প্রবাল রং", "#FF7F50"),
            ("ঝুমকা ফুলের নীল", "#6495ED"),
            ("সিল্ক রং", "#FFF8DC"),
            ("অগ্নি রং", "#DC143C"),
            ("সায়ান", "#00FFFF"),
            ("কালচে নীল", "#00008B"),
            ("কালচে সায়ান", "#008B8B"),
            ("কালচে ধাতব সোনালি", "#B8860B"),
            ("কালচে ধূসর", "#A9A9A9"),
            ("কালচে সবুজ", "#006400"),
            ("কালচে খাকী", "#BDB76B"),
            ("কালচে হালকা বেগুনী লাল", "#8B008B"),
            ("কালচে জলপাই সবুজ", "#556B2F"),
            ("কালচে কমলা", "#FF8C00"),
            ("কালচে অর্কিড রং", "#9932CC"),
            ("কালচে লাল", "#8B0000"),
            ("কালচে স্যামন রং", "#E9967A"),
            ("কালচে সামুদ্রিক সবুজ", "#8FBC8F"),
            ("কালচে পাথুরে নীল", "#483D8B"),
            ("কালচে পাথুরে ধূসর", "#2F4F4F"),
            ("কালচে ফিরোজা", "#00CED1"),
            ("কালচে বেগুনী", "#9400D3"),
            ("গাঢ় গোলাপি", "#FF1493"),
            ("গাঢ় আকাশী নীল", "#00BFFF"),
            ("আবছা ধূসর", "#696969"),
            ("ডজার নীল", "#1E90FF"),
            ("পোড়া ইট রং", "#B22222"),
            ("ফুলেল সাদা", "#FFFAF0"),
            ("বন্য সবুজ", "#228B22"),
            ("উজ্জ্বল গোলাপি বেগুনী", "#FF00FF"),
            ("মেটে রং", "#DCDCDC"),
            ("টাইটান সাদা", "#F8F8FF"),
            ("সোনালি", "#FFD700"),
            ("ধাতব সোনালি", "#DAA520"),
            ("ধূসর", "#808080"),
            ("সবুজ", "#008000"),
            ("সবুজাভ হলুদ", "#ADFF2F"),
            ("মধু রং", "#F0FFF0"),
            ("উষ্ণ গোলাপি", "#FF69B4"),
            ("ভারতীয় লাল", "#CD5C5C"),
            ("বেগুনী নীল", "#4B0082"),
            ("আইভরি", "#FFFFF0"),
            ("খাকী", "#F0E68C"),
            ("ল্যাভেণ্ডার রং", "#E6E6FA"),
            ("ল্যাভেন্ডার লাল", "#FFF0F5"),
            ("তৃণ সবুজ", "#7CFC00"),
            ("হালকা সিল্ক রং", "#FFFACD"),
            ("হালকা নীল", "#ADD8E6"),
            ("হালকা প্রবাল রং", "#F08080"),
            ("হালকা সায়ান", "#E0FFFF"),
            ("হালকা ধাতব সোনালি হলুদ", "#FAFAD2"),
            ("হালকা ধূসর", "#D3D3D3"),
            ("হালকা সবুজ", "#90EE90"),
            ("হালকা গোলাপি", "#FFB6C1"),
            ("হালকা স্যামন রং", "#FFA07A"),
            ("হালকা সামুদ্রিক সবুজ", "#20B2AA"),
            ("হালকা আকাশী নীল", "#87CEFA"),
            ("হালকা পাথুরে ধূসর", "#778899"),
            ("হালকা ধাতব নীল", "#B0C4DE"),
            ("হালকা হলুদ", "#FFFFE0"),
            ("লাইম রং", "#00FF00"),
            ("লাইম সবুজ", "#32CD32"),
            ("পাট রং", "#FAF0E6"),
            ("হালকা বেগুনী লাল", "#FF00FF"),
            ("মেরুন", "#800000"),
            ("মাঝারী নীল সবুজ", "#66CDAA"),
            ("মাঝারী নীল", "#0000CD"),
            ("মাঝারী অর্কিড রং", "#BA55D3"),
            ("মাঝারী বেগুনী", "#9370DB"),
            ("মাঝারী সামুদ্রিক সবুজ", "#3CB371"),
            ("মাঝারী পাথুরে নীল", "#7B68EE"),
            ("মাঝারী বাসন্তী সবুজ", "#00FA9A"),
            ("মাঝারী ফিরোজা", "#48D1CC"),
            ("মাঝারী বেগুনী লাল", "#C71585"),
            ("মিডনাইট নীল", "#191970"),
            ("হালকা পীত পুদিনা রং", "#F5FFFA"),
            ("ধোঁয়াটে গোলাপ রং", "#FFE4E1"),
            ("মোকাসিন", "#FFE4B5"),
            ("নাভাজো সাদা", "#FFDEAD"),
            ("নেভি ব্লু", "#000080"),
            ("ওল্ড লেইস রং", "#FDF5E6"),
            ("জলপাই রং", "#808000"),
            ("ম্যাটমাটে জলপাই রং", "#6B8E23"),
            ("কমলা", "#FFA500"),
            ("কমলা লাল", "#FF4500"),
            ("অর্কিড রং", "#DA70D6"),
            ("ফ্যাকাশে ধাতব সোনালি", "#EEE8AA"),
            ("ফ্যাকাশে সবুজ", "#98FB98"),
            ("ফ্যাকাশে ফিরোজা", "#AFEEEE"),
            ("ফ্যাকাশে বেগুনী লাল", "#DB7093"),
            ("পাপায়াহুপ", "#FFEFD5"),
            ("পীচ রং", "#FFDAB9"),
            ("পেরু রং", "#CD853F"),
            ("গোলাপি", "#FFC0CB"),
            ("জাম রং", "#DDA0DD"),
            ("গুঁড়া নীল", "#B0E0E6"),
            ("বেগুনী", "#800080"),
            ("লাল", "#FF0000"),
            ("গোলাপী লাল", "#BC8F8F"),
            ("রয়্যাল ব্লু", "#4169E1"),
            ("স্যাডল ব্রাউন", "#8B4513"),
            ("স্যামন রং", "#FA8072"),
            ("বেলে বাদামী", "#F4A460"),
            ("সামুদ্রিক সবুজ", "#2E8B57"),
            ("ঝিনুক রং", "#FFF5EE"),
            ("মেটে রং", "#A0522D"),
            ("রূপালী", "#C0C0C0"),
            ("আকাশী নীল", "#87CEEB"),
            ("পাথুরে নীল", "#6A5ACD"),
            ("পাথুরে ধূসর", "#708090"),
            ("তুষার শুভ্র রং", "#FFFAFA"),
            ("বাসন্তী সবুজ", "#00FF7F"),
            ("ধাতব নীল", "#4682B4"),
            ("তামাটে রং", "#D2B48C"),
            ("পেষ্ট রং", "#008080"),
            ("থিসল রং", "#D8BFD8"),
            ("টমেটো রং", "#FF6347"),
            ("ফিরোজা", "#40E0D0"),
            ("রক্তবেগুনী", "#EE82EE"),
            ("গম রং", "#F5DEB3"),
            ("সাদা", "#FFFFFF"),
            ("ধোঁয়াটে সাদা", "#F5F5F5"),
            ("হলুদ", "#FFFF00"),
            ("হলুদাভ সবুজ", "#9ACD32"),
        )
    )

    safe_colors = (
        "কালো",
        "মেরুন",
        "সবুজ",
        "নেভি",
        "জলপাই রং",
        "বেগুনী",
        "পেষ্ট রং",
        "লাইম রং",
        "নীল",
        "রূপালী",
        "ধূসর",
        "হলুদ",
        "উজ্জ্বল গোলাপি বেগুনী",
        "জল রং",
        "সাদা",
    )
