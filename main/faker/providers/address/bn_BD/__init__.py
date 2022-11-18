from faker.providers.person.bn_BD import translate_to_bengali_digits

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    area_names = (
        "আলি",
        "আলম",
        "অভয়",
        "আনোয়ার",
        "ব্রাহ্মণ",
        "বটিয়া",
        "বাঘার",
        "বেগম",
        "বিজয়",
        "বন্দর",
        "বালিয়া",
        "বাজিত",
        "বাকের",
        "বোরহান",
        "বকশী",
        "বদর",
        "বিরাম",
        "বিশ্বনাথ",
        "চৌদ্দ",
        "চিতল",
        "দাউদ",
        "দৌলত",
        "দেব",
        "দেবী",
        "ইসলাম",
        "ফুল",
        "ফকির",
        "ফটিক",
        "গোপাল",
        "গৌর",
        "হাজী",
        "হরিরাম",
        "হোসেন",
        "হাকিম",
        "জীবন",
        "জগন্নাথ",
        "কুমার",
        "কালী",
        "কেশব",
        "কুতুব",
        "কবির",
        "কালিয়া",
        "করিম",
        "কাজী",
        "কমল",
        "লাল",
        "মুরাদ",
        "মনোহর",
        "মির",
        "মহেশ",
        "মোড়ল",
        "মোল্লা",
        "মোহাম্মদ",
        "মনিরাম",
        "মানিক",
        "মির্জা",
        "মধু",
        "মোহন",
        "মহাদেব",
        "মাধব",
        "নাসির",
        "নড়িয়া",
        "নাজির",
        "নালিতা",
        "নন্দী",
        "ওসমানী",
        "পাইক",
        "পলাশ",
        "পার্বতী",
        "রাম",
        "রায়",
        "রানী",
        "সোনা",
        "শরণ",
        "শ্যাম",
        "সুবর্ণ",
        "সিরাজ",
        "সখি",
        "সদর",
        "সুন্দর",
        "সৈয়দ",
        "শাজাহান",
        "শান্তি",
        "শিব",
        "তের",
        "তারা",
        "উজির",
    )

    building_names = (
        "বাড়ী নং",
        "বিল্ডিং নং",
        "বাসা নং",
        "হোল্ডিং নং",
    )

    building_number_formats = ("%", "%#", "%##")

    city_prefixes = ("উত্তর", "পূর্ব", "পশ্চিম", "দক্ষিণ", "মধ্য", "নতুন", "পুরাতন")

    city_suffixes = (
        "বাজার",
        "বাড়ি",
        "চর",
        "দিয়া",
        "ডাঙ্গা",
        "গঞ্জ",
        "গ্রাম",
        "গাঁও",
        "গাঁ",
        "গড়",
        "হাট",
        "হার",
        "খালি",
        "মাটি",
        "নগর",
        "পুর",
        "তলা",
    )

    cities = (
        "বরগুনা",
        "বরিশাল",
        "ভোলা",
        "বান্দরবান",
        "ব্রাহ্মণবাড়িয়া",
        "বাগেরহাট",
        "বগুড়া",
        "চাঁদপুর",
        "চট্টগ্রাম",
        "কুমিল্লা",
        "কক্সবাজার",
        "চুয়াডাঙ্গা",
        "ঢাকা",
        "দিনাজপুর",
        "ফরিদপুর",
        "ফেনী",
        "গাজীপুর",
        "গোপালগঞ্জ",
        "গাইবান্ধা",
        "হবিগঞ্জ",
        "ঝালকাঠি",
        "যশোর",
        "ঝিনাইদহ",
        "জামালপুর",
        "জয়পুরহাট",
        "খাগড়াছড়ি",
        "কিশোরগঞ্জ",
        "খুলনা",
        "কুষ্টিয়া",
        "কুড়িগ্রাম",
        "লক্ষ্মীপুর",
        "লালমনিরহাট",
        "মাদারীপুর",
        "মানিকগঞ্জ",
        "মুন্সীগঞ্জ",
        "মাগুরা",
        "মেহেরপুর",
        "ময়মনসিংহ",
        "মৌলভীবাজার",
        "নোয়াখালী",
        "নারায়ণগঞ্জ",
        "নরসিংদী",
        "নড়াইল",
        "নেত্রকোণা",
        "নওগাঁ",
        "নাটোর",
        "চাঁপাইনবাবগঞ্জ",
        "নীলফামারী",
        "পটুয়াখালী",
        "পিরোজপুর",
        "পাবনা",
        "পঞ্চগড়",
        "রাঙ্গামাটি",
        "রাজবাড়ী",
        "রাজশাহী",
        "রংপুর",
        "শরীয়তপুর",
        "সাতক্ষীরা",
        "শেরপুর",
        "সিরাজগঞ্জ",
        "সুনামগঞ্জ",
        "সিলেট",
        "টাঙ্গাইল",
        "ঠাকুরগাঁও",
    )

    countries = (
        "আফগানিস্তান",
        "আলবেনিয়া",
        "আলজেরিয়া",
        "আমেরিকান সামোয়া",
        "অ্যান্ডোরা",
        "অ্যাঙ্গোলা",
        "অ্যাঙ্গুইলা",
        "অ্যান্টার্কটিকা",
        "অ্যান্টিগুয়া ও বার্বুডা",
        "আর্জেন্টিনা",
        "আর্মেনিয়া",
        "আরুবা",
        "অস্ট্রেলিয়া",
        "অস্ট্রিয়া",
        "আজারবাইজান",
        "বাহামাস",
        "বাহরাইন",
        "বাংলাদেশ",
        "বার্বাডোস",
        "বেলারুশ",
        "বেলজিয়াম",
        "বেলিজ",
        "বেনিন",
        "বারমুডা",
        "ভুটান",
        "বলিভিয়া",
        "বসনিয়া-হার্জেগোভিনা",
        "বতসোয়ানা",
        "বাউবে দ্বীপ",
        "ব্রাজিল",
        "ব্রিটিশ ভারত মহাসাগরীয় অঞ্চল",
        "ব্রিটিশ ভার্জিন দ্বীপপুঞ্জ",
        "ব্রুনাই",
        "বুলগেরিয়া",
        "বুর্কিনা ফাসো",
        "বুরুন্ডি",
        "কম্বোডিয়া",
        "ক্যামেরুন",
        "কানাডা",
        "কেপ ভার্দে",
        "কেম্যান দ্বীপপুঞ্জ",
        "মধ্য আফ্রিকান প্রজাতন্ত্র",
        "চাদ",
        "চিলি",
        "চীন",
        "ক্রিস্টমাস দ্বীপ",
        "কোকোস দ্বীপপুঞ্জ",
        "কলাম্বিয়া",
        "কোমোরোস",
        "কঙ্গো প্রজাতন্ত্র",
        "কুক দ্বীপপুঞ্জ",
        "কোস্টারিকা",
        "আইভরি কোট",
        "ক্রোয়েশিয়া",
        "কিউবা",
        "সাইপ্রাস প্রজাতন্ত্র",
        "চেক প্রজাতন্ত্র",
        "ডেনমার্ক",
        "জিবুতি প্রজাতন্ত্র",
        "ডোমিনিকা",
        "ডোমিনিকান প্রজাতন্ত্র",
        "ইকুয়েডর",
        "মিশর",
        "এল সালভাদর",
        "নিরক্ষীয় গিনি",
        "ইরিত্রিয়া",
        "এস্তোনিয়া",
        "ইথিওপিয়া",
        "ফারো দ্বীপপুঞ্জ",
        "ফকল্যান্ড দ্বীপপুঞ্জ",
        "ফিজি প্রজাতন্ত্র",
        "ফিনল্যান্ড",
        "ফ্রান্স",
        "একটি দেশের নাম",
        "ফরাসি পলিনেশিয়া",
        "ফরাসি সুদূর দক্ষিণ দ্বীপপুঞ্জ",
        "গ্যাবন",
        "গাম্বিয়া",
        "জর্জিয়া",
        "জার্মানি",
        "ঘানা",
        "জিব্রাল্টার",
        "গ্রীস",
        "গ্রিনল্যান্ড",
        "গ্রেনাডা",
        "গুয়াডেলুপ",
        "গুয়াম",
        "গুয়াতেমালা",
        "গার্নসি",
        "গিনি",
        "গিনি-বিসাউ",
        "গিয়ানা",
        "হাইতি",
        "হার্ড আইল্যান্ড এবং ম্যাকডোনাল্ড দ্বীপপুঞ্জ",
        "ভ্যাটিকান সিটি",
        "হন্ডুরাস",
        "হংকং",
        "হাঙ্গেরি",
        "আইসল্যান্ড",
        "ভারত",
        "ইন্দোনেশিয়া",
        "ইরান",
        "ইরাক",
        "আপনি উত্তর দিবেন না",
        "আইল অফ ম্যান",
        "ইসরায়েল",
        "ইতালি",
        "জ্যামাইকা",
        "জাপান",
        "জার্সি",
        "জর্ডান",
        "কাজাখস্তান",
        "কেনিয়া",
        "কিরিবাতি",
        "কোরিয়া",
        "কোরিয়া",
        "কুয়েত",
        "কিরগিজস্তান প্রজাতন্ত্র",
        "পিপলস ডেমোক্রেটিক রিপাবলিক অফ লাওস",
        "লাটভিয়া",
        "লেবানন",
        "লেসোথো",
        "লাইবেরিয়া",
        "লিবিয়া",
        "লিচেনস্টাইন",
        "লিথুয়ানিয়া",
        "লাক্সেমবার্গ",
        "ম্যাকাও",
        "মেসিডোনিয়া প্রজাতন্ত্র",
        "মাদাগাস্কার",
        "মালাউই",
        "মালয়েশিয়া",
        "মালদ্বীপ",
        "মালি",
        "মাল্টা প্রজাতন্ত্র",
        "মার্শাল দ্বীপপুঞ্জ",
        "মার্টিনিক",
        "ইসলামী প্রজাতন্ত্র মৌরিতানিয়া",
        "মরিশাস",
        "মায়োট",
        "মেক্সিকো",
        "মাইক্রোনেশিয়ার ফেডারেটেড স্টেটস",
        "মোল্দোভা প্রজাতন্ত্র",
        "মোনাকোর রাজত্ব",
        "মঙ্গোলিয়া",
        "মন্টিনিগ্রো প্রজাতন্ত্র",
        "মন্টসেরাট",
        "মরক্কো",
        "মোজাম্বিক",
        "মিয়ানমার",
        "নামিবিয়া",
        "নাউরু",
        "নেপাল",
        "নেদারল্যান্ডস এন্টিলস",
        "নেদারল্যান্ডস",
        "নতুন ক্যালেডোনিয়া",
        "নিউজিল্যান্ড",
        "নিকারাগুয়া",
        "নাইজার",
        "নাইজেরিয়া",
        "সুন্দর",
        "নরফোক দ্বীপ",
        "উত্তর মারিয়ানা দ্বীপপুঞ্জ",
        "নরওয়ে",
        "ওমান",
        "পাকিস্তান",
        "পালাউ",
        "ফিলিস্তিন অঞ্চল",
        "পানামা",
        "পাপুয়া নিউ গিনি",
        "প্যারাগুয়ে",
        "পেরু",
        "ফিলিপাইন",
        "পিটকের্ন দ্বীপপুঞ্জ",
        "পোল্যান্ড",
        "পর্তুগাল",
        "পুয়ের্তো রিকো",
        "কাতার",
        "পুনর্মিলন",
        "রোমানিয়া",
        "রাশিয়া",
        "রুয়ান্ডা",
        "সেন্ট বার্থেলেমি",
        "সেন্ট হেলেনা",
        "সেন্ট কিটস ও নেভিস",
        "সেন্ট লুসিয়া",
        "সেন্ট মার্টিন",
        "সেন্ট পিয়ের এবং মিকেলন",
        "সেন্ট ভিনসেন্ট ও গ্রেনাডাইন দ্বীপপুঞ্জ",
        "সামোয়া",
        "সান মারিনো",
        "স্যান্টোম প্রিন্সিপ",
        "সৌদি আরব",
        "সেনেগাল",
        "সার্বিয়া",
        "সেশেলস",
        "সিয়েরা লিওন",
        "সিঙ্গাপুর",
        "স্লোভাকিয়া",
        "স্লোভেনিয়া",
        "সলোমান দ্বীপপুঞ্জ",
        "সোমালিয়া",
        "দক্ষিণ আফ্রিকা প্রজাতন্ত্র",
        "দক্ষিণ জর্জিয়া এবং দক্ষিণ স্যান্ডউইচ দ্বীপপুঞ্জ",
        "স্পেন",
        "শ্রীলংকা",
        "সুদান",
        "সুরিনাম",
        "স্বালবার্ড এবং জানমায়েন দ্বীপপুঞ্জ",
        "সোয়াজিল্যান্ডের রাজ্য",
        "সুইডেন",
        "সুইজারল্যান্ড",
        "সিরিয়া",
        "তাইওয়ান",
        "তাজিকিস্তান প্রজাতন্ত্র",
        "তানজানিয়া",
        "থাইল্যান্ড",
        "পূর্ব তিমুর",
        "যাও",
        "টোকেলাউ",
        "টোঙ্গা",
        "ত্রিনিদাদ ও টোবাগো প্রজাতন্ত্র",
        "তিউনিসিয়া",
        "তুরস্ক",
        "তুর্কমেনিস্তান",
        "টার্কস্ ও কেইকোস দ্বীপপুঞ্জ",
        "টুভালু",
        "উগান্ডা",
        "ইউক্রেন",
        "সংযুক্ত আরব আমিরাত",
        "ইংল্যান্ড",
        "মার্কিন যুক্তরাষ্ট্র",
        "ইউএস মাইনর আউটলি আইল্যান্ড",
        "আমেরিকান ভার্জিন আইল্যান্ডস",
        "উরুগুয়ে",
        "উজবেকিস্তান",
        "ভানুয়াতু",
        "ভেনিজুয়েলা",
        "ভিয়েতনাম",
        "ওয়ালিস এবং ফুটুনা",
        "পশ্চিম সাহারা",
        "ইয়েমেন",
        "জাম্বিয়া",
        "জিম্বাবুয়ে",
    )

    secondary_address_formats = (
        "ফ্ল্যাট %",
        "ফ্ল্যাট %#",
        "ষ্টুডিও %",
        "ষ্টুডিও %#",
        "অ্যাপার্টমেন্ট %",
        "অ্যাপার্টমেন্ট %#",
    )

    street_suffixes = (
        "এভিনিউ",
        "সেন্টার",
        "চত্বর",
        "গলি",
        "ঘাট",
        "কর্নার",
        "লেন",
        "মহাসড়ক",
        "মহল্লা",
        "মোড়",
        "পাড়া",
        "পার্ক",
        "প্লাজা",
        "রাস্তা",
        "রোড",
        "সড়ক",
        "স্টেশন",
        "স্ট্যান্ড",
    )

    postcode_formats = ("%###",)
    street_name_formats = (
        "{{area_name}}{{street_suffix}}",
        "{{city_prefix}} {{area_name}}{{street_suffix}}",
        "{{city_prefix}} {{area_name}}{{city_suffix}}",
        "{{area_name}}{{city_suffix}}",
        "{{area_name}}{{city_suffix}} {{street_suffix}}",
        "{{city_prefix}} {{area_name}}{{city_suffix}} {{street_suffix}}",
    )
    street_address_formats = (
        "{{building_name}} {{building_number}}, {{street_name}}",
        "{{secondary_address}}, {{building_name}} {{building_number}}, {{street_name}}",
    )
    town_formats = ("{{area_name}}{{city_suffix}}",)
    address_formats = ("{{street_address}}, {{town}}, {{city}}, {{postcode}}",)

    def administrative_unit(self) -> str:
        """
        :example: 'ঢাকা'
        """
        return self.random_element(self.cities)

    def area_name(self) -> str:
        """
        :example: 'উজির'
        """
        return self.random_element(self.area_names)

    def building_name(self) -> str:
        """
        :example: 'বাড়ী নং'
        """
        return self.random_element(self.building_names)

    def building_number(self) -> str:
        """
        :example: '791' to '৭৯১'
        """
        return translate_to_bengali_digits(self.numerify(self.random_element(self.building_number_formats)))

    def city_prefix(self) -> str:
        """
        :example: 'উত্তর'
        """
        return self.random_element(self.city_prefixes)

    def city(self) -> str:
        """
        :example: 'ঢাকা'
        """
        return self.random_element(self.cities)

    def postcode(self) -> str:
        """
        See
        https://bdpost.portal.gov.bd/site/page/6aaeabe4-479b-4e5a-a671-e9e5b994bf9a
        """
        return translate_to_bengali_digits(self.numerify(self.random_element(self.postcode_formats)))

    def secondary_address(self) -> str:
        """
        As the generated string format is a Bengali word but English number so splitting the value by space
        and then convert the English number to Bengali number and concat with generated Bengali word
        and return
        : example : 'অ্যাপার্টমেন্ট 14' to 'অ্যাপার্টমেন্ট ১৪'
        """
        value = self.bothify(self.random_element(self.secondary_address_formats))
        word_list = value.split(" ")
        return word_list[0] + " " + translate_to_bengali_digits(word_list[1])

    def town(self) -> str:
        """
        :example: 'নবাব'
        """
        pattern: str = self.random_element(self.town_formats)
        return self.generator.parse(pattern)
