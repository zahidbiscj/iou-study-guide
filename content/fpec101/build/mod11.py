MOD(qs=[15, 16])

CONCEPT("""
**Concept:** An **oligopoly** is a market dominated by **a few large firms**. Because there are so few, each firm watches the others: if one cuts its price, the rest react. This **mutual interdependence** makes oligopoly the hardest structure to model, so economists use several models: the **kinked demand curve**, **collusion (cartels)** and **price leadership**. Oligopolists also prefer to compete through **advertising** rather than price.

**Exam tip:** this is the fourth part of **Q15**; concentration measures and cartels also feed into **Q16** (anti-trust).
""", """
**ধারণা:** **অলিগোপলি** হলো **কয়েকটি বড় ফার্মের** আধিপত্যের বাজার। সংখ্যায় এত কম বলে প্রত্যেকে অন্যদের নজরে রাখে: একজন দাম কমালে বাকিরা সাড়া দেয়। এই **পারস্পরিক নির্ভরশীলতা** অলিগোপলিকে মডেল করা সবচেয়ে কঠিন করে, তাই অর্থনীতিবিদরা কয়েকটি মডেল ব্যবহার করেন: **বাঁকানো চাহিদা রেখা**, **যোগসাজশ (কার্টেল)** ও **দাম-নেতৃত্ব**। অলিগোপলিস্টরা দামের বদলে **বিজ্ঞাপনে** প্রতিযোগিতা পছন্দ করে।

**পরীক্ষার টিপস:** এটি **Q15**-এর চতুর্থ অংশ; কেন্দ্রীভবনের পরিমাপ ও কার্টেল **Q16**-এও (অ্যান্টি-ট্রাস্ট) কাজে লাগে।
""", fig='kinked')

WORDS([
    ('Oligopoly', 'A market dominated by a few large firms', 'অলিগোপলি — কয়েকটি বড় ফার্মের আধিপত্যের বাজার', 'Mobile operators, cement, steel.'),
    ('Mutual interdependence', 'Each firm\'s profit depends on rivals\' decisions too', 'পারস্পরিক নির্ভরশীলতা — প্রত্যেকের মুনাফা প্রতিদ্বন্দ্বীর সিদ্ধান্তের ওপরও নির্ভর করে', 'Robi cuts prices; GP must respond.'),
    ('Strategic behaviour', 'Acting while taking rivals\' reactions into account', 'কৌশলগত আচরণ — প্রতিদ্বন্দ্বীর প্রতিক্রিয়া মাথায় রেখে কাজ', 'Planning a price cut like a chess move.'),
    ('Concentration ratio', 'Share of industry output of the largest (usually 4) firms', 'কেন্দ্রীভবন অনুপাত — বৃহত্তম (সাধারণত ৪) ফার্মের উৎপাদনের অংশ', '4 firms = 85% → oligopoly.'),
    ('Herfindahl index', 'Sum of squared % market shares of all firms', 'হারফিন্ডাল সূচক — সব ফার্মের % বাজার-অংশের বর্গের যোগফল', 'Monopoly = 100² = 10,000.'),
    ('Kinked demand curve', 'Rivals match price cuts but ignore increases → sticky prices', 'বাঁকানো চাহিদা রেখা — প্রতিদ্বন্দ্বী দাম কমানো মানে, বাড়ানো মানে না → অনমনীয় দাম', 'Prices that rarely change.'),
    ('Collusion / cartel', 'Agreement among firms to fix prices or output', 'যোগসাজশ / কার্টেল — দাম বা উৎপাদন ঠিক করার চুক্তি', 'OPEC; a "syndicate" fixing onion prices.'),
    ('Price leadership', 'A dominant firm sets prices; others follow without a formal agreement', 'দাম-নেতৃত্ব — প্রভাবশালী ফার্ম দাম ঠিক করে, অন্যরা অনুসরণ করে', 'The biggest firm announces a price rise.'),
    ('Limit pricing', 'Keeping price low to discourage new entrants', 'সীমা-দাম — নতুন প্রবেশকারী নিরুৎসাহিত করতে দাম কম রাখা', 'A leader keeps price just below a newcomer\'s cost.'),
])

SLIDE([1, 2, 3, 4], 'Title and outline', 'শিরোনাম ও রূপরেখা',
    bn=['**স্লাইড ১–৪:** প্রিন্সিপলস অব ইকোনমিক্স — সালিমাহ মুশাররিফ। FPEC 101 – লেকচার ১১, ইউনিট ২। বাজার কাঠামো — অলিগোপলি। রূপরেখা: অলিগোপলি।'],
    ex="""The last market structure. Reading: McConnell & Brue pp. 451–464.""",
    exb="""শেষ বাজার কাঠামো। পড়া: ম্যাককনেল ও ব্রু পৃ. ৪৫১–৪৬৪।""")

SLIDE(5, 'What is oligopoly?', 'অলিগোপলি কী?',
    bn=['অলিগোপলি', 'সমজাতীয় বা পৃথকীকৃত পণ্যের কয়েকটি বড় উৎপাদকের আধিপত্যের বাজার। "সংখ্যায় কম" বলে অলিগোপলিস্টদের দামের ওপর উল্লেখযোগ্য নিয়ন্ত্রণ আছে, কিন্তু প্রত্যেককে তার দাম, উৎপাদন ও বিজ্ঞাপনের সিদ্ধান্তে প্রতিদ্বন্দ্বীদের সম্ভাব্য প্রতিক্রিয়া বিবেচনা করতে হয়।'],
    ex="""**Oligopoly** = a market dominated by **a few large producers** of a homogeneous or differentiated product. Being few, they have **considerable control over price**, but each must **consider rivals' possible reactions** to its own price, output and advertising decisions.""",
    exb="""**অলিগোপলি** = সমজাতীয় বা পৃথকীকৃত পণ্যের **কয়েকটি বড় উৎপাদকের** আধিপত্যের বাজার। কম বলে **দামের ওপর উল্লেখযোগ্য নিয়ন্ত্রণ** আছে, কিন্তু প্রত্যেককে নিজের দাম, উৎপাদন ও বিজ্ঞাপনের সিদ্ধান্তে **প্রতিদ্বন্দ্বীর সম্ভাব্য প্রতিক্রিয়া বিবেচনা** করতে হয়।""",
    eg="""Bangladesh: mobile telecom (4 operators), cement (a handful of big groups), soybean oil refining, steel rods, soft drinks.""",
    egb="""বাংলাদেশ: মোবাইল টেলিকম (৪ অপারেটর), সিমেন্ট (কয়েকটি বড় গ্রুপ), সয়াবিন তেল পরিশোধন, রড, কোমল পানীয়।""")

SLIDE([6, 7], 'Characteristics of oligopoly', 'অলিগোপলির বৈশিষ্ট্য',
    bn=['**স্লাইড ৬:** কয়েকটি বড় উৎপাদক। সমজাতীয় (সাধারণত শিল্পপণ্য) বা পৃথকীকৃত (সাধারণত ভোগ্যপণ্য) পণ্য। দামের ওপর নিয়ন্ত্রণ, কিন্তু পারস্পরিক নির্ভরশীলতা — প্রত্যেক ফার্ম একচেটিয়ার মতো "দাম নির্ধারক", মুনাফা সর্বোচ্চ করতে দাম ও উৎপাদন ঠিক করতে পারে; কিন্তু প্রতিদ্বন্দ্বী আছে বলে তার দাম, উৎপাদন, পণ্য বা বিজ্ঞাপনের পরিবর্তনে তারা কী প্রতিক্রিয়া করবে বিবেচনা করতে হয়। • কৌশলগত আচরণ — অন্যদের প্রতিক্রিয়া বিবেচনা করা • পারস্পরিক নির্ভরশীলতা — প্রত্যেকের মুনাফা শুধু নিজের নয়, অন্যদের দাম ও বিক্রয় কৌশলের ওপরও নির্ভর করে।',
        '**স্লাইড ৭ — প্রবেশে বাধা** (একচেটিয়ার মতো): বৃহদায়তনের সুবিধা · উচ্চ মূলধন ব্যয় · কাঁচামালের মালিকানা — আগাম ও প্রতিশোধমূলক দাম ও বিজ্ঞাপন কৌশলে নতুন প্রতিযোগীর প্রবেশ ঠেকাতে পারে। **একীভবন:** দুই বা ততোধিক প্রতিযোগী ফার্ম বাজার-অংশ বাড়াতে মিলে যায়; বেশি বৃহদায়তনের সুবিধা; বেশি একচেটিয়া ক্ষমতা; ফার্ম যত বড়, বাজারের যোগান ও দামের ওপর নিয়ন্ত্রণ তত বেশি; বড় ক্রেতা হিসেবে উপকরণ কম দামে পেতে পারে।'],
    ex="""Five characteristics:

1. **A few large producers.**
2. **Homogeneous** (usually industrial: steel, cement) **or differentiated** products (usually consumer: phones, soft drinks).
3. **Control over price, but mutual interdependence:** each is a price maker, but must think about how rivals will react. This needs **strategic behaviour**.
4. **Barriers to entry** (as for monopoly): economies of scale, high capital costs, ownership of raw materials, plus aggressive pricing and advertising to scare off newcomers.
5. **Mergers:** firms combine to gain market share, economies of scale, monopoly power, control over price, and cheaper inputs as big buyers.""",
    exb="""পাঁচটি বৈশিষ্ট্য:

1. **কয়েকটি বড় উৎপাদক।**
2. **সমজাতীয়** (সাধারণত শিল্পপণ্য: স্টিল, সিমেন্ট) **বা পৃথকীকৃত** পণ্য (সাধারণত ভোগ্যপণ্য: ফোন, কোমল পানীয়)।
3. **দামের ওপর নিয়ন্ত্রণ, কিন্তু পারস্পরিক নির্ভরশীলতা:** প্রত্যেকে দাম নির্ধারক, কিন্তু প্রতিদ্বন্দ্বীর প্রতিক্রিয়া ভাবতে হয়। এর জন্য লাগে **কৌশলগত আচরণ**।
4. **প্রবেশে বাধা** (একচেটিয়ার মতো): বৃহদায়তনের সুবিধা, উচ্চ মূলধন ব্যয়, কাঁচামালের মালিকানা, আর নবাগতকে ভয় দেখাতে আক্রমণাত্মক দাম ও বিজ্ঞাপন।
5. **একীভবন:** বাজার-অংশ, বৃহদায়তনের সুবিধা, একচেটিয়া ক্ষমতা, দামের নিয়ন্ত্রণ আর বড় ক্রেতা হিসেবে সস্তা উপকরণ পেতে ফার্মগুলো মিলে যায়।""",
    eg="""When Grameenphone launches a cheap data pack, Robi and Banglalink usually respond within days: mutual interdependence. The Robi–Airtel merger (2016) is an oligopoly merger.""",
    egb="""গ্রামীণফোন সস্তা ডেটা প্যাক ছাড়লে রবি ও বাংলালিংক সাধারণত কয়েক দিনের মধ্যে সাড়া দেয়: পারস্পরিক নির্ভরশীলতা। রবি–এয়ারটেল একীভবন (২০১৬) অলিগোপলির একীভবন।""")

SLIDE([8, 9], 'Measuring industry concentration', 'শিল্পের কেন্দ্রীভবন পরিমাপ',
    bn=['**স্লাইড ৮ — কেন্দ্রীভবন অনুপাত:** শিল্পের বৃহত্তম ফার্মগুলোর উৎপাদিত ও বিক্রীত মোট উৎপাদনের শতকরা অংশ। সূত্র: ফার্মের উৎপাদন ÷ শিল্পের মোট উৎপাদন। অনুপাত যত কম, কেন্দ্রীভবন তত কম, কারণ ফার্মগুলোর বাজার-অংশ ছোট। অলিগোপলি ও বিশুদ্ধ একচেটিয়ায় বেশি। চার-ফার্ম অনুপাত > ৪০% হলে শিল্প অলিগোপলি ধরা হয়; < ৪০% হলে একচেটিয়া প্রতিযোগিতা।',
        '**স্লাইড ৯ — হারফিন্ডাল সূচক:** শিল্পের সব ফার্মের শতকরা বাজার-অংশের বর্গের যোগফল। সূত্র: (%S1)² + (%S2)² + … + (%Sn)²। বড় ও শক্তিশালী ফার্মকে বেশি গুরুত্ব দিতে বর্গ করা হয়। বিশুদ্ধ প্রতিযোগিতায় সূচক শূন্যের কাছাকাছি; একচেটিয়ায় ১০,০০০ অর্থাৎ (১০০)²।'],
    ex="""Two ways to measure **how concentrated** an industry is:

**1. Concentration ratio (CR4):** the % of industry output produced by the **four largest firms**. CR4 > 40% → **oligopoly**; < 40% → **monopolistic competition**.

**2. Herfindahl index (HHI):** **square** each firm's % market share and **add them up**. Squaring gives **more weight to big firms**. Perfect competition → close to **0**; monopoly → 100² = **10,000**.

**Worked example:** four firms with shares 40%, 30%, 20%, 10%. CR4 = 100%. HHI = 1,600 + 900 + 400 + 100 = **3,000** (highly concentrated).""",
    exb="""শিল্প **কতটা কেন্দ্রীভূত** তা মাপার দুই উপায়:

**১. কেন্দ্রীভবন অনুপাত (CR4):** **চারটি বৃহত্তম ফার্মের** উৎপাদনের শতকরা অংশ। CR4 > ৪০% → **অলিগোপলি**; < ৪০% → **একচেটিয়া প্রতিযোগিতা**।

**২. হারফিন্ডাল সূচক (HHI):** প্রতিটি ফার্মের % বাজার-অংশ **বর্গ** করে **যোগ করো**। বর্গ করায় **বড় ফার্ম বেশি গুরুত্ব পায়**। পূর্ণ প্রতিযোগিতা → **০**-র কাছে; একচেটিয়া → ১০০² = **১০,০০০**।

**হাতে-কলমে:** চার ফার্মের অংশ ৪০%, ৩০%, ২০%, ১০%। CR4 = ১০০%। HHI = ১,৬০০ + ৯০০ + ৪০০ + ১০০ = **৩,০০০** (খুব কেন্দ্রীভূত)।""",
    tip="If the exam gives market shares, calculate both CR4 and HHI and say what they mean.",
    tipb="পরীক্ষায় বাজার-অংশ দিলে CR4 ও HHI দুটোই হিসাব করে অর্থ লেখো।")

SLIDE(10, 'Oligopoly pricing models: why several?', 'অলিগোপলির দাম-মডেল: কেন কয়েকটি?',
    bn=['অলিগোপলির দাম-মডেল', '• বাঁকানো চাহিদা রেখা', '• যোগসাজশমূলক দাম', '• দাম-নেতৃত্ব', 'ভিন্ন মডেলের কারণ: • অলিগোপলির বৈচিত্র্য • পারস্পরিক নির্ভরশীলতার জটিলতা'],
    ex="""There is **no single model** of oligopoly because (1) oligopolies are **diverse** (2 firms or 10, identical or differentiated products) and (2) **interdependence is complicated**: what a firm does depends on what it thinks rivals will do. Three models: **kinked demand** (no collusion), **collusion/cartel**, **price leadership**.""",
    exb="""অলিগোপলির **একক মডেল নেই**, কারণ (১) অলিগোপলি **বৈচিত্র্যময়** (২টি বা ১০টি ফার্ম, একই বা পৃথকীকৃত পণ্য) এবং (২) **পারস্পরিক নির্ভরশীলতা জটিল**: ফার্ম কী করবে তা নির্ভর করে প্রতিদ্বন্দ্বী কী করবে বলে সে ভাবে তার ওপর। তিনটি মডেল: **বাঁকানো চাহিদা** (যোগসাজশ নেই), **যোগসাজশ/কার্টেল**, **দাম-নেতৃত্ব**।""")

SLIDE([11, 12, 13], 'Kinked demand curve (non-collusive oligopoly)', 'বাঁকানো চাহিদা রেখা (যোগসাজশহীন অলিগোপলি)',
    bn=['**স্লাইড ১১:** বাঁকানো চাহিদা রেখা অলিগোপলি বাজারে ফার্মগুলোর পারস্পরিক নির্ভরশীলতা দেখায়। **দাম পরিবর্তন মেলানো:** এক ফার্ম দাম কমালে অন্যরাও কমায়, দামযুদ্ধ হয়; মোট আয় কমে, সময়ের সাথে বাজার-অংশ তেমন বদলায় না। এক ফার্ম দাম বাড়ালে অন্যরাও বাড়ালে সামান্য আয় ও বিক্রি হারায়; শিল্প অন্য শিল্পের কাছে বিক্রি হারায়। **দাম পরিবর্তন উপেক্ষা:** এক ফার্ম দাম কমাল আর অন্যরা মানল না → তার বিক্রি প্রতিদ্বন্দ্বীর খরচে অনেক বাড়ে। এক ফার্ম দাম বাড়াল আর অন্যরা মানল না → তার বাজার-অংশ ও মোট আয় কমে, তবে বিক্রি শূন্য হয় না, কিছু ক্রেতা বেশি দামেও কেনে।',
        '**স্লাইড ১২:** উঁচু ও নিচু দামে চাহিদার স্থিতিস্থাপকতা ভিন্ন হওয়ায় চাহিদা রেখায় বাঁক আসে — নিচু দামে অস্থিতিস্থাপক, উঁচু দামে স্থিতিস্থাপক। দুই অংশ যেখানে মেলে সেখানে বাঁক। MC বদলালেও দাম-উৎপাদন একই স্তরে থাকে। অনমনীয় দাম।',
        '**স্লাইড ১৩:** অলিগোপলির দাম-মডেল — বাঁকানো চাহিদা রেখা (ম্যাককনেল ও ব্রু পৃ. ৪৫৬)।'],
    fig='kinked',
    ex="""**The logic (rivals are not colluding):**
- If a firm **raises** its price, rivals **ignore** it (they happily take its customers) → the firm loses many sales → demand **above** the current price is **elastic**.
- If a firm **cuts** its price, rivals **match** it (to keep their customers) → the firm gains few sales and starts a price war → demand **below** the current price is **inelastic**.

So the demand curve has a **kink** at the current price. The kink creates a **vertical gap in the MR curve**. MC can move up or down **within that gap** and MR = MC still gives the **same price and output**.

**Result: sticky (inflexible) prices.** Oligopoly prices tend to stay the same for long periods, and firms compete in other ways (advertising).""",
    exb="""**যুক্তি (প্রতিদ্বন্দ্বীরা যোগসাজশ করছে না):**
- ফার্ম দাম **বাড়ালে** প্রতিদ্বন্দ্বী **উপেক্ষা** করে (খুশি হয়ে তার ক্রেতা নেয়) → ফার্ম অনেক বিক্রি হারায় → বর্তমান দামের **ওপরে** চাহিদা **স্থিতিস্থাপক**।
- ফার্ম দাম **কমালে** প্রতিদ্বন্দ্বীও **কমায়** (নিজের ক্রেতা ধরে রাখতে) → ফার্ম সামান্য বিক্রি পায়, দামযুদ্ধ শুরু হয় → বর্তমান দামের **নিচে** চাহিদা **অস্থিতিস্থাপক**।

তাই চাহিদা রেখায় বর্তমান দামে একটি **বাঁক**। বাঁক **MR রেখায় খাড়া ফাঁক** তৈরি করে। MC **ওই ফাঁকের মধ্যে** ওঠানামা করলেও MR = MC **একই দাম ও উৎপাদন** দেয়।

**ফল: অনমনীয় দাম।** অলিগোপলির দাম দীর্ঘ সময় একই থাকে, আর ফার্মগুলো অন্যভাবে (বিজ্ঞাপনে) প্রতিযোগিতা করে।""",
    tip="Draw the kinked curve with the MR gap and two MC curves in Q15; write \"sticky prices\".",
    tipb="Q15-এ MR-এর ফাঁক আর দুটি MC রেখাসহ বাঁকানো রেখা আঁকো; লেখো \"sticky prices\"।")

CHECK([
    Q('Four firms have market shares 50%, 20%, 20%, 10%. The Herfindahl index is…', 'চার ফার্মের অংশ ৫০%, ২০%, ২০%, ১০%। হারফিন্ডাল সূচক…',
      ['100 · ১০০', '3,400 · ৩,৪০০', '10,000 · ১০,০০০', '1,000 · ১,০০০'], 1,
      '2,500 + 400 + 400 + 100 = 3,400.', '২,৫০০ + ৪০০ + ৪০০ + ১০০ = ৩,৪০০।'),
    Q('The kinked demand curve explains why oligopoly prices are…', 'বাঁকানো চাহিদা রেখা ব্যাখ্যা করে অলিগোপলির দাম কেন…',
      ['Always falling · সবসময় কমে', 'Sticky (rarely change) · অনমনীয় (কমই বদলায়)', 'Equal to MC · MC-র সমান', 'Set by government · সরকার ঠিক করে'], 1,
      'Rivals match cuts but ignore rises, and MC can change within the MR gap without moving price.', 'প্রতিদ্বন্দ্বী দাম কমানো মানে, বাড়ানো মানে না; আর MR-এর ফাঁকে MC বদলালেও দাম নড়ে না।'),
])

SLIDE([14, 15, 16], 'Collusion and joint-profit maximisation', 'যোগসাজশ ও যৌথ মুনাফা সর্বোচ্চকরণ',
    bn=['**স্লাইড ১৪ — কার্টেল ও যোগসাজশ:** যোগসাজশ হলো দাম ঠিক করা, বাজার ভাগ করা বা অন্যভাবে প্রতিযোগিতা সীমিত করার যেকোনো চুক্তি। প্রত্যেক ফার্ম বিশুদ্ধ একচেটিয়ার মতো আচরণ করে। অলিগোপলি ফার্মগুলোর চাহিদা ও খরচের অবস্থা একই বা খুব কাছাকাছি হলে তারা যৌথ উৎপাদন সীমিত করে একটি সাধারণ দাম ঠিক করতে যোগসাজশ করতে পারে।',
        '**স্লাইড ১৫:** [চিত্র: যোগসাজশ ও যৌথ মুনাফা সর্বোচ্চকরণ — MR = MC, অর্থনৈতিক মুনাফা]',
        '**স্লাইড ১৬:** প্রতিদ্বন্দ্বীর চেয়ে বেশি দাম নিলে চাহিদা ও মোট আয় হারায়, বিশেষত প্রতিদ্বন্দ্বী দাম না বাড়ালে। প্রতিদ্বন্দ্বী ভারসাম্যের নিচে দাম রাখলে ফার্ম পাল্টা দাম কমাতে পারে, কিন্তু তাতে তিন ফার্মই চাহিদা রেখা ধরে নিচে নামে, মুনাফা কমে, এমনকি গড় মোট ব্যয় দামের চেয়ে বেশি হয়ে লোকসান হতে পারে। একই চাহিদা ও খরচে প্রত্যেকের জন্য একই দাম নেওয়াই সবচেয়ে লাভজনক। এসব এড়াতে ফার্মগুলো যোগসাজশ করে একই দাম ঠিক করে সর্বোচ্চ মুনাফা নিতে পারে।'],
    ex="""**Collusion** = any agreement to **fix prices, divide up the market or restrict competition**. Colluding firms act **together like one monopolist**: they set total output where **MR = MC** for the group and share the **monopoly profit**.

Why collude? Without agreement, raising price loses customers and cutting price starts a **price war** that can push everyone into losses. With similar costs and demand, the most profitable outcome for all is to **charge the same (monopoly) price**, so they agree to do so.""",
    exb="""**যোগসাজশ** = **দাম ঠিক করা, বাজার ভাগ করা বা প্রতিযোগিতা সীমিত করার** যেকোনো চুক্তি। যোগসাজশকারী ফার্মগুলো **একসাথে এক একচেটিয়ার মতো** চলে: দলের জন্য **MR = MC**-তে মোট উৎপাদন ঠিক করে আর **একচেটিয়া মুনাফা** ভাগ করে।

কেন যোগসাজশ? চুক্তি ছাড়া দাম বাড়ালে ক্রেতা হারায়, কমালে **দামযুদ্ধ** শুরু হয়, সবাই লোকসানে পড়তে পারে। খরচ ও চাহিদা এক রকম হলে সবার জন্য সবচেয়ে লাভজনক হলো **একই (একচেটিয়া) দাম** নেওয়া, তাই তারা তাতে একমত হয়।""",
    eg="""In Bangladesh, sudden jumps in the prices of onions, eggs or edible oil are often blamed on traders' "syndicates": informal collusion to restrict supply and raise prices, which the Competition Commission investigates.""",
    egb="""বাংলাদেশে পেঁয়াজ, ডিম বা ভোজ্যতেলের দাম হঠাৎ লাফালে প্রায়ই ব্যবসায়ীদের "সিন্ডিকেট"-কে দায়ী করা হয়: যোগান সীমিত করে দাম বাড়ানোর অনানুষ্ঠানিক যোগসাজশ, যা প্রতিযোগিতা কমিশন তদন্ত করে।""")

SLIDE(17, 'Overt and covert collusion', 'প্রকাশ্য ও গোপন যোগসাজশ',
    bn=['কার্টেল ও যোগসাজশ', '**প্রকাশ্য যোগসাজশ — কার্টেল:** উৎপাদকদের একটি গোষ্ঠী, যারা সাধারণত লিখিত আনুষ্ঠানিক চুক্তি করে প্রত্যেক সদস্য কত উৎপাদন করবে ও কত দাম নেবে তা ঠিক করে। সম্মত দাম ধরে রাখতে উৎপাদন নিয়ন্ত্রণ — বাজার ভাগ — করতে হয়। (উদাহরণ: ওপেক)',
        '**গোপন যোগসাজশ:** যেখানে কার্টেল অবৈধ, সেখানে যোগসাজশ গোপনে হয় — দাম ও বিক্রির পরিমাণ ঠিক করার অনানুষ্ঠানিক চুক্তি। • মৌন সমঝোতা (ঐতিহাসিকভাবে "ভদ্রলোকের চুক্তি") — প্রায়ই অনানুষ্ঠানিক সংগঠন ও সামাজিক অনুষ্ঠানে হয়। প্রতিযোগী ফার্মের মধ্যে পণ্যের দাম নিয়ে মৌখিক চুক্তি, বাজার-অংশ অ-দাম প্রতিযোগিতায় ঠিক হয়।'],
    ex="""- **Overt collusion — a cartel:** a group of producers with a **formal (often written) agreement** on how much each will produce and charge. Output must be controlled (the market divided) to hold the price. Example: **OPEC** (oil-exporting countries).
- **Covert collusion:** where cartels are **illegal**, firms collude **secretly**: informal agreements on prices and sales. **Tacit understandings ("gentlemen's agreements")** are made informally, e.g. at social gatherings: they agree on price and leave market shares to non-price competition.""",
    exb="""- **প্রকাশ্য যোগসাজশ — কার্টেল:** প্রত্যেকে কত উৎপাদন ও কত দাম নেবে তা নিয়ে **আনুষ্ঠানিক (প্রায়ই লিখিত) চুক্তির** উৎপাদক-গোষ্ঠী। দাম ধরে রাখতে উৎপাদন নিয়ন্ত্রণ (বাজার ভাগ) করতে হয়। উদাহরণ: **ওপেক** (তেল রপ্তানিকারক দেশ)।
- **গোপন যোগসাজশ:** যেখানে কার্টেল **অবৈধ**, সেখানে ফার্মগুলো **গোপনে** যোগসাজশ করে: দাম ও বিক্রি নিয়ে অনানুষ্ঠানিক চুক্তি। **মৌন সমঝোতা ("ভদ্রলোকের চুক্তি")** অনানুষ্ঠানিকভাবে হয়, যেমন সামাজিক অনুষ্ঠানে: দামে একমত হয়, বাজার-অংশ ছেড়ে দেয় অ-দাম প্রতিযোগিতায়।""")

SLIDE([18, 19, 20], 'Obstacles to collusion', 'যোগসাজশের বাধা',
    bn=['**স্লাইড ১৮ — যোগসাজশমূলক দামের বাধা:** **চাহিদা ও খরচের পার্থক্য** দাম নিয়ে মতভেদ আনে, বিশেষত যেখানে পণ্য পৃথকীকৃত ও প্রায়ই বদলায়। প্রমিত পণ্যেও ফার্মগুলোর বাজার-অংশ ও খরচ ভিন্ন হয়। **ফার্মের সংখ্যা:** ফার্ম যত বেশি, কার্টেল বা যোগসাজশ তত কঠিন; বাইরের ছোট ফার্মগুলো প্রতিযোগিতা করতে পারে।',
        '**স্লাইড ১৯ — প্রতারণা:** যোগসাজশকারী অলিগোপলিস্টরা বিক্রি ও মুনাফা বাড়াতে গোপনে দাম কমাতে পারে। বেশি দাম দেওয়া ক্রেতারা কম দামের বিক্রির কথা জানলে একই দাম চায়। এক উৎপাদকের কাছ থেকে ছাড় পাওয়া ক্রেতা অন্যদের কাছেও একই ছাড় চায়, ফলে যোগসাজশ ভেঙে পড়ে।',
        '**স্লাইড ২০ — মন্দা:** দীর্ঘ মন্দায় চাহিদা কমে, আয় কমে, অতিরিক্ত সক্ষমতায় গড় মোট ব্যয় বাড়ে, মুনাফা কমে; ফার্মগুলো লোকসান কমাতে দাম কাটতে পারে। **সম্ভাব্য প্রবেশ:** যোগসাজশের বেশি দাম ও মুনাফা বিদেশি ফার্মসহ নতুনদের টানে, যোগান বাড়িয়ে দাম ও মুনাফা কমায়; সফল যোগসাজশে নতুনদের প্রবেশ আটকাতে হয়। **আইনি বাধা — অ্যান্টি-ট্রাস্ট আইন:** যুক্তরাষ্ট্রের অ্যান্টি-ট্রাস্ট আইন কার্টেল ও দাম ঠিক করার যোগসাজশ নিষিদ্ধ করে, তাই দাম নিয়ন্ত্রণের কম প্রকাশ্য উপায় গড়ে উঠেছে।'],
    ex="""Six reasons collusion often breaks down:

1. **Demand and cost differences:** firms with different costs and products disagree on the "right" price.
2. **Number of firms:** the more firms, the harder it is to agree; outsiders keep competing.
3. **Cheating:** each member gains by **secretly cutting its price** to sell more. When buyers find out, everyone demands the low price and the cartel collapses.
4. **Recession:** falling demand and excess capacity tempt firms to cut prices.
5. **Potential entry:** high cartel profits attract new (including foreign) firms.
6. **Legal obstacles:** **anti-trust laws** ban cartels and price-fixing (Lecture 12; in Bangladesh, the Competition Act 2012).""",
    exb="""যোগসাজশ প্রায়ই ভেঙে পড়ার ছয়টি কারণ:

1. **চাহিদা ও খরচের পার্থক্য:** ভিন্ন খরচ ও পণ্যের ফার্মগুলো "সঠিক" দাম নিয়ে একমত হয় না।
2. **ফার্মের সংখ্যা:** ফার্ম যত বেশি, একমত হওয়া তত কঠিন; বাইরের ফার্ম প্রতিযোগিতা চালায়।
3. **প্রতারণা:** প্রত্যেক সদস্য বেশি বেচতে **গোপনে দাম কমিয়ে** লাভবান হয়। ক্রেতা জানলে সবাই কম দাম চায়, কার্টেল ভেঙে পড়ে।
4. **মন্দা:** কমতে থাকা চাহিদা ও অতিরিক্ত সক্ষমতা দাম কমাতে প্রলুব্ধ করে।
5. **সম্ভাব্য প্রবেশ:** কার্টেলের বেশি মুনাফা নতুন (বিদেশিসহ) ফার্ম টানে।
6. **আইনি বাধা:** **অ্যান্টি-ট্রাস্ট আইন** কার্টেল ও দাম ঠিক করা নিষিদ্ধ করে (লেকচার ১২; বাংলাদেশে প্রতিযোগিতা আইন ২০১২)।""",
    tip="Memory trick for the obstacles: **\"Do Not Cheat Recklessly, Players Lose\"**: Differences, Number, Cheating, Recession, Potential entry, Legal.",
    tipb="বাধা মনে রাখার কৌশল: **\"Do Not Cheat Recklessly, Players Lose\"**: পার্থক্য, সংখ্যা, প্রতারণা, মন্দা, সম্ভাব্য প্রবেশ, আইনি।")

SLIDE([21, 22, 23], 'Price leadership model', 'দাম-নেতৃত্ব মডেল',
    bn=['**স্লাইড ২১ — দাম-নেতৃত্ব মডেল:** প্রভাবশালী ফার্ম পথ দেখায় — আনুষ্ঠানিক চুক্তি ও গোপন বৈঠক ছাড়াই অলিগোপলিস্টরা দাম সমন্বয়ের একটি অন্তর্নিহিত সমঝোতা। সাধারণত বৃহত্তম বা সবচেয়ে দক্ষ ফার্ম দাম পরিবর্তন শুরু করে, অন্যরা কমবেশি স্বয়ংক্রিয়ভাবে অনুসরণ করে। • নেতৃত্বের কৌশল • দাম-নেতৃত্বের ভাঙন: দামযুদ্ধ',
        '**স্লাইড ২২ — নেতৃত্বের কৌশল:** **কদাচিৎ দাম বদল** — প্রতিদ্বন্দ্বী অনুসরণ না করার ঝুঁকি থাকায় দাম কমই বদলানো হয়, মূলত যখন শিল্পজুড়ে খরচ ও চাহিদা উল্লেখযোগ্যভাবে বদলায়। **যোগাযোগ** — বাণিজ্য পত্রিকার সাক্ষাৎকার ইত্যাদির মাধ্যমে দাম বদলের প্রয়োজনীয়তা অনানুষ্ঠানিকভাবে জানানো, যাতে প্রতিযোগীরা অনুসরণ করে। **সীমা-দাম** — নতুন প্রতিযোগী নিরুৎসাহিত করতে ও বর্তমান অলিগোপলি কাঠামো ধরে রাখতে নেতা স্বল্পমেয়াদি সর্বোচ্চ-মুনাফার স্তরের নিচে দাম রাখতে পারে, যা অদক্ষ বা ছোট নতুন ফার্মের প্রবেশে বাধা।',
        '**স্লাইড ২৩ — দাম-নেতৃত্বের ভাঙন: দামযুদ্ধ।** বেশিরভাগ দামযুদ্ধ একসময় শেষ হয়। সবাই যখন বোঝে কম দাম তাদের মুনাফা মারাত্মকভাবে কমাচ্ছে, তখন আবার শিল্পের এক নেতৃস্থানীয় ফার্মকে দাম-নেতৃত্ব ছেড়ে দেয়। সেই ফার্ম ধীরে দাম বাড়াতে শুরু করে, অন্যরা অনুসরণ করে।'],
    ex="""**Price leadership** = a **tacit (unspoken) way to coordinate prices** without formal agreements or secret meetings. The **dominant firm** (largest or most efficient) changes its price and the others **follow**.

**Leadership tactics:**
- **Infrequent price changes:** only when costs or demand change significantly across the industry (changes are risky).
- **Communication:** signalling through press interviews, trade publications ("costs have risen…").
- **Limit pricing:** keeping price **below** the short-run profit-maximising level to **discourage entry** of new firms.

**Breakdown — price wars:** sometimes a firm refuses to follow and prices tumble. When all see their profits collapsing, they return to following the leader, who slowly raises prices again.""",
    exb="""**দাম-নেতৃত্ব** = আনুষ্ঠানিক চুক্তি বা গোপন বৈঠক ছাড়াই **দাম সমন্বয়ের মৌন উপায়**। **প্রভাবশালী ফার্ম** (বৃহত্তম বা সবচেয়ে দক্ষ) দাম বদলায়, অন্যরা **অনুসরণ** করে।

**নেতৃত্বের কৌশল:**
- **কদাচিৎ দাম বদল:** শুধু শিল্পজুড়ে খরচ বা চাহিদা উল্লেখযোগ্যভাবে বদলালে (বদল ঝুঁকিপূর্ণ)।
- **যোগাযোগ:** সংবাদ সাক্ষাৎকার, বাণিজ্য পত্রিকায় সংকেত ("খরচ বেড়েছে…")।
- **সীমা-দাম:** **নতুন ফার্মের প্রবেশ নিরুৎসাহিত** করতে স্বল্পমেয়াদি সর্বোচ্চ-মুনাফার স্তরের **নিচে** দাম রাখা।

**ভাঙন — দামযুদ্ধ:** কখনো কোনো ফার্ম অনুসরণ না করলে দাম পড়ে যায়। সবাই মুনাফা ধসে পড়তে দেখলে আবার নেতাকে অনুসরণে ফেরে, নেতা ধীরে দাম বাড়ায়।""",
    eg="""When the largest cement company announces a price rise per bag "because of higher clinker costs", other cement brands usually raise their prices within days: price leadership.""",
    egb="""বৃহত্তম সিমেন্ট কোম্পানি "ক্লিংকারের খরচ বাড়ায়" ব্যাগপ্রতি দাম বাড়ানোর ঘোষণা দিলে অন্য সিমেন্ট ব্র্যান্ডগুলো সাধারণত কয়েক দিনের মধ্যে দাম বাড়ায়: দাম-নেতৃত্ব।""")

SLIDE([24, 25, 26], 'Oligopoly and advertising', 'অলিগোপলি ও বিজ্ঞাপন',
    bn=['**স্লাইড ২৪ — অলিগোপলি ও বিজ্ঞাপন:** অলিগোপলিস্টরা দামে প্রতিযোগিতা করতে চায় না, তাই মনোযোগ অ-দাম প্রতিযোগিতায়। পণ্য উন্নয়ন ও বিজ্ঞাপন পছন্দ, কারণ এতে বাজার-অংশে বেশি স্থায়ী লাভ হয়, আর দাম কমানোর মতো দ্রুত ও পুরোপুরি নকল করা যায় না। অলিগোপলিস্টদের যথেষ্ট আর্থিক সম্পদ আছে — অতীতের অর্থনৈতিক মুনাফা বর্তমান বিজ্ঞাপন ও পণ্য উন্নয়নে অর্থ জোগায়।',
        '**স্লাইড ২৫ — বিজ্ঞাপনের ইতিবাচক প্রভাব:** ভোক্তার জন্য তথ্যের সস্তা উৎস · একচেটিয়া ক্ষমতা কমাতে পারে · বিদ্যমান ব্র্যান্ডের সাথে প্রতিযোগিতার জন্য নতুন পণ্য চালু। অলিগোপলিতে: ভোক্তাকে কম খরচে দরকারি তথ্য দেয়, খোঁজার খরচ কমায়; প্রতিযোগিতা বাড়ায়, ফলে বেশি অর্থনৈতিক দক্ষতা; নতুন পণ্য চালু সহজ করে, প্রযুক্তিগত অগ্রগতি উৎসাহিত করে।',
        '**স্লাইড ২৬ — বিজ্ঞাপনের নেতিবাচক প্রভাব:** শুধু প্ররোচনা, পণ্য সম্পর্কে তথ্য নয় — ভোক্তাকে প্রশংসিত কিন্তু নিম্নমানের পণ্যে বেশি দাম দিতে প্ররোচিত করতে পারে, কম দামের ভালো কিন্তু বিজ্ঞাপনহীন পণ্য বাদ দিয়ে। প্রবেশে বাধা — ভালো বিজ্ঞাপনের ফার্ম বেশি বাজার-অংশ ও মুনাফা পায়, আরও ভালো বিজ্ঞাপন দেয়, আরও বাজার পায়, ফলে বাজার একচেটিয়া হয়ে ভোক্তা প্রতিযোগিতার সুফল হারায়। আত্ম-বাতিলকারী বিজ্ঞাপন — এক ফার্মের বিপুল বিজ্ঞাপন খরচ, প্রতিযোগীরাও একই করলে চাহিদা তেমন বাড়ে না।'],
    ex="""**Why oligopolists advertise instead of cutting prices:** a price cut is copied immediately (price war), but a successful product or advert gives a **more lasting** gain that rivals cannot copy as fast. And oligopolists have past **profits** to pay for it.

<div class="tbl"><table><thead><tr><th>Positive effects</th><th>Negative effects</th></tr></thead><tbody>
<tr><td>Cheap information for consumers (lower search costs)</td><td>Persuasion, not information: people pay more for heavily advertised but inferior products</td></tr>
<tr><td>Can reduce monopoly power (more competition)</td><td>Barrier to entry: big advertisers get bigger, market becomes monopolised</td></tr>
<tr><td>Helps introduce new products; encourages innovation</td><td>Self-cancelling: rivals' ads cancel out, huge cost for little extra demand</td></tr></tbody></table></div>""",
    exb="""**অলিগোপলিস্টরা দাম না কমিয়ে বিজ্ঞাপন দেয় কেন:** দাম কমালে সঙ্গে সঙ্গে নকল হয় (দামযুদ্ধ), কিন্তু সফল পণ্য বা বিজ্ঞাপন **বেশি স্থায়ী** লাভ দেয়, যা প্রতিদ্বন্দ্বী দ্রুত নকল করতে পারে না। আর অলিগোপলিস্টদের অতীতের **মুনাফা** আছে খরচ মেটানোর।

<div class="tbl"><table><thead><tr><th>ইতিবাচক প্রভাব</th><th>নেতিবাচক প্রভাব</th></tr></thead><tbody>
<tr><td>ভোক্তার জন্য সস্তা তথ্য (খোঁজার খরচ কম)</td><td>তথ্য নয়, প্ররোচনা: বেশি বিজ্ঞাপিত কিন্তু নিম্নমানের পণ্যে বেশি দাম</td></tr>
<tr><td>একচেটিয়া ক্ষমতা কমাতে পারে (বেশি প্রতিযোগিতা)</td><td>প্রবেশে বাধা: বড় বিজ্ঞাপনদাতা আরও বড় হয়, বাজার একচেটিয়া হয়</td></tr>
<tr><td>নতুন পণ্য চালুতে সাহায্য; উদ্ভাবনে উৎসাহ</td><td>আত্ম-বাতিলকারী: প্রতিদ্বন্দ্বীর বিজ্ঞাপন একে অপরকে বাতিল করে, বিপুল খরচে সামান্য বাড়তি চাহিদা</td></tr></tbody></table></div>""",
    eg="""Mobile operators and soft-drink brands spend heavily on Eid and cricket-season ads. When all of them advertise, each one's market share hardly changes: self-cancelling advertising.""",
    egb="""মোবাইল অপারেটর ও কোমল পানীয়ের ব্র্যান্ড ঈদ ও ক্রিকেট মৌসুমে বিপুল বিজ্ঞাপন দেয়। সবাই বিজ্ঞাপন দিলে কারো বাজার-অংশ প্রায় বদলায় না: আত্ম-বাতিলকারী বিজ্ঞাপন।""")

SLIDE(27, 'Summary of Lecture 11', 'লেকচার ১১-এর সারসংক্ষেপ',
    bn=['সারসংক্ষেপ', 'অলিগোপলি — বৈশিষ্ট্য · শিল্পের কেন্দ্রীভবন · দাম-মডেল (বাঁকানো চাহিদা রেখা, যোগসাজশমূলক দাম, দাম-নেতৃত্ব) · অলিগোপলি ও বিজ্ঞাপন'],
    ex="""Answer plan for the **oligopoly part of Q15**: definition → characteristics (few firms, products, interdependence, barriers, mergers) → concentration (CR4, HHI) → three pricing models (kinked demand with diagram, collusion/cartels and their obstacles, price leadership) → advertising (positive and negative).""",
    exb="""**Q15-এর অলিগোপলি অংশের** উত্তর পরিকল্পনা: সংজ্ঞা → বৈশিষ্ট্য (কয়েকটি ফার্ম, পণ্য, পারস্পরিক নির্ভরশীলতা, বাধা, একীভবন) → কেন্দ্রীভবন (CR4, HHI) → তিনটি দাম-মডেল (চিত্রসহ বাঁকানো চাহিদা, যোগসাজশ/কার্টেল ও তাদের বাধা, দাম-নেতৃত্ব) → বিজ্ঞাপন (ইতিবাচক ও নেতিবাচক)।""")

TOGETHER("""
### The four market structures: final summary for Q15
<div class="tbl"><table><thead><tr><th></th><th>Perfect competition</th><th>Monopolistic competition</th><th>Oligopoly</th><th>Monopoly</th></tr></thead><tbody>
<tr><td>Firms</td><td>Very many</td><td>Many</td><td>Few</td><td>One</td></tr>
<tr><td>Product</td><td>Identical</td><td>Differentiated</td><td>Identical or differentiated</td><td>Unique</td></tr>
<tr><td>Price control</td><td>None</td><td>Some</td><td>Considerable, interdependent</td><td>Considerable</td></tr>
<tr><td>Entry barriers</td><td>None</td><td>Low</td><td>High</td><td>Blocked</td></tr>
<tr><td>Short run</td><td>Profit/loss/shutdown</td><td>Profit/loss</td><td>Kinked demand, collusion, leadership</td><td>Profit (or loss)</td></tr>
<tr><td>Long run</td><td>Normal profit, P = min ATC</td><td>Normal profit, excess capacity</td><td>Economic profit can persist</td><td>Abnormal profit persists</td></tr>
<tr><td>Concentration (CR4)</td><td>Very low</td><td>&lt; 40%</td><td>&gt; 40%</td><td>100% (HHI 10,000)</td></tr>
<tr><td>Example (Bangladesh)</td><td>Rice, vegetables</td><td>Restaurants, boutiques</td><td>Telecom, cement</td><td>WASA, power distribution</td></tr></tbody></table></div>
""", """
### চারটি বাজার কাঠামো: Q15-এর চূড়ান্ত সারসংক্ষেপ
<div class="tbl"><table><thead><tr><th></th><th>পূর্ণ প্রতিযোগিতা</th><th>একচেটিয়া প্রতিযোগিতা</th><th>অলিগোপলি</th><th>একচেটিয়া</th></tr></thead><tbody>
<tr><td>ফার্ম</td><td>অসংখ্য</td><td>অনেক</td><td>কয়েকটি</td><td>একটি</td></tr>
<tr><td>পণ্য</td><td>একই</td><td>পৃথকীকৃত</td><td>একই বা পৃথকীকৃত</td><td>অনন্য</td></tr>
<tr><td>দামের নিয়ন্ত্রণ</td><td>নেই</td><td>কিছুটা</td><td>যথেষ্ট, পারস্পরিক নির্ভরশীল</td><td>যথেষ্ট</td></tr>
<tr><td>প্রবেশে বাধা</td><td>নেই</td><td>কম</td><td>বেশি</td><td>বন্ধ</td></tr>
<tr><td>স্বল্পমেয়াদ</td><td>মুনাফা/লোকসান/বন্ধ</td><td>মুনাফা/লোকসান</td><td>বাঁকানো চাহিদা, যোগসাজশ, নেতৃত্ব</td><td>মুনাফা (বা লোকসান)</td></tr>
<tr><td>দীর্ঘমেয়াদ</td><td>স্বাভাবিক মুনাফা, P = সর্বনিম্ন ATC</td><td>স্বাভাবিক মুনাফা, অতিরিক্ত সক্ষমতা</td><td>অর্থনৈতিক মুনাফা টিকতে পারে</td><td>অস্বাভাবিক মুনাফা টেকে</td></tr>
<tr><td>কেন্দ্রীভবন (CR4)</td><td>খুব কম</td><td>&lt; ৪০%</td><td>&gt; ৪০%</td><td>১০০% (HHI ১০,০০০)</td></tr>
<tr><td>উদাহরণ (বাংলাদেশ)</td><td>চাল, সবজি</td><td>রেস্তোরাঁ, বুটিক</td><td>টেলিকম, সিমেন্ট</td><td>ওয়াসা, বিদ্যুৎ বিতরণ</td></tr></tbody></table></div>
""")

MIDTERM("""
Full card: <a href="#e15">Q15</a>.

### Q15 (part 4) — Oligopoly
**Definition:** a market dominated by a few large producers of a homogeneous or differentiated product; each has considerable control over price but must consider rivals' reactions. **Characteristics:** few large producers; homogeneous (industrial) or differentiated (consumer) products; control over price with **mutual interdependence** and **strategic behaviour**; **entry barriers** (economies of scale, high capital costs, ownership of raw materials, retaliatory pricing); **mergers** to gain market share, scale economies and monopoly power. **Concentration:** four-firm concentration ratio (> 40% = oligopoly); **Herfindahl index** = sum of squared % shares (monopoly = 10,000).
**Pricing models:** (1) **Kinked demand** (non-collusive): rivals ignore price increases (elastic above the kink) but match cuts (inelastic below), creating a gap in MR, so changes in MC leave price and output unchanged: **sticky prices**. _(Draw.)_ (2) **Collusion/cartels:** agreements to fix price and divide the market; firms act like a monopolist (MR = MC) and share profit; overt (cartel, e.g. OPEC) or covert (tacit "gentlemen's agreements"); **obstacles**: demand and cost differences, number of firms, cheating, recession, potential entry, anti-trust laws. (3) **Price leadership:** a dominant firm sets price and others follow; tactics: infrequent changes, communication, limit pricing; breakdowns into price wars. **Advertising:** oligopolists prefer non-price competition; positive (information, more competition, new products) and negative (persuasion, barrier to entry, self-cancelling) effects. **Long run:** barriers allow economic profits to persist.
""", """
পূর্ণ কার্ড: <a href="#e15">Q15</a>।

### Q15 (অংশ ৪) — অলিগোপলি
**সংজ্ঞা:** সমজাতীয় বা পৃথকীকৃত পণ্যের কয়েকটি বড় উৎপাদকের আধিপত্যের বাজার; প্রত্যেকের দামের ওপর উল্লেখযোগ্য নিয়ন্ত্রণ, কিন্তু প্রতিদ্বন্দ্বীর প্রতিক্রিয়া বিবেচনা করতে হয়। **বৈশিষ্ট্য:** কয়েকটি বড় উৎপাদক; সমজাতীয় (শিল্প) বা পৃথকীকৃত (ভোগ্য) পণ্য; **পারস্পরিক নির্ভরশীলতা** ও **কৌশলগত আচরণসহ** দামের নিয়ন্ত্রণ; **প্রবেশে বাধা** (বৃহদায়তনের সুবিধা, উচ্চ মূলধন, কাঁচামালের মালিকানা, প্রতিশোধমূলক দাম); বাজার-অংশ, বৃহদায়তনের সুবিধা ও একচেটিয়া ক্ষমতার জন্য **একীভবন**। **কেন্দ্রীভবন:** চার-ফার্ম কেন্দ্রীভবন অনুপাত (> ৪০% = অলিগোপলি); **হারফিন্ডাল সূচক** = % অংশের বর্গের যোগফল (একচেটিয়া = ১০,০০০)।
**দাম-মডেল:** (১) **বাঁকানো চাহিদা** (যোগসাজশহীন): প্রতিদ্বন্দ্বী দাম বাড়ানো উপেক্ষা করে (বাঁকের ওপরে স্থিতিস্থাপক), কমানো মানে (নিচে অস্থিতিস্থাপক); MR-এ ফাঁক তৈরি হয়, তাই MC বদলালেও দাম-উৎপাদন একই: **অনমনীয় দাম**। _(আঁকো।)_ (২) **যোগসাজশ/কার্টেল:** দাম ঠিক ও বাজার ভাগের চুক্তি; ফার্মগুলো একচেটিয়ার মতো চলে (MR = MC), মুনাফা ভাগ করে; প্রকাশ্য (কার্টেল, যেমন ওপেক) বা গোপন (মৌন "ভদ্রলোকের চুক্তি"); **বাধা**: চাহিদা ও খরচের পার্থক্য, ফার্মের সংখ্যা, প্রতারণা, মন্দা, সম্ভাব্য প্রবেশ, অ্যান্টি-ট্রাস্ট আইন। (৩) **দাম-নেতৃত্ব:** প্রভাবশালী ফার্ম দাম ঠিক করে, অন্যরা অনুসরণ করে; কৌশল: কদাচিৎ বদল, যোগাযোগ, সীমা-দাম; ভেঙে দামযুদ্ধ। **বিজ্ঞাপন:** অলিগোপলিস্ট অ-দাম প্রতিযোগিতা পছন্দ করে; ইতিবাচক (তথ্য, বেশি প্রতিযোগিতা, নতুন পণ্য) ও নেতিবাচক (প্ররোচনা, প্রবেশে বাধা, আত্ম-বাতিলকারী) প্রভাব। **দীর্ঘমেয়াদ:** বাধার কারণে অর্থনৈতিক মুনাফা টিকে থাকতে পারে।
""")

QUIZ([
    Q('The key feature that distinguishes oligopoly is…', 'অলিগোপলির পার্থক্যসূচক মূল বৈশিষ্ট্য…',
      ['Free entry · অবাধ প্রবেশ', 'Mutual interdependence · পারস্পরিক নির্ভরশীলতা', 'Identical products only · শুধু একই পণ্য', 'One seller · একজন বিক্রেতা'], 1,
      'With few firms, each must consider how rivals will react.', 'কয়েকটি ফার্ম বলে প্রত্যেককে প্রতিদ্বন্দ্বীর প্রতিক্রিয়া ভাবতে হয়।'),
    Q('An industry is considered oligopolistic if the four-firm concentration ratio is above…', 'চার-ফার্ম কেন্দ্রীভবন অনুপাত কত শতাংশের বেশি হলে শিল্পকে অলিগোপলি ধরা হয়?',
      ['10% · ১০%', '25% · ২৫%', '40% · ৪০%', '90% · ৯০%'], 2,
      'Slide 8: CR4 > 40% → oligopoly; < 40% → monopolistic competition.', 'স্লাইড ৮: CR4 > ৪০% → অলিগোপলি; < ৪০% → একচেটিয়া প্রতিযোগিতা।'),
    Q('Cartel members secretly cutting prices to sell more is called…', 'কার্টেল সদস্যদের বেশি বেচতে গোপনে দাম কমানোকে বলে…',
      ['Price leadership · দাম-নেতৃত্ব', 'Cheating · প্রতারণা', 'Limit pricing · সীমা-দাম', 'Merger · একীভবন'], 1,
      'Cheating is one of the main obstacles that makes collusion break down.', 'প্রতারণা যোগসাজশ ভেঙে পড়ার প্রধান বাধাগুলোর একটি।'),
    Q('A price leader keeping price low to discourage new entrants is using…', 'নতুন প্রবেশকারী নিরুৎসাহিত করতে দাম-নেতার দাম কম রাখা হলো…',
      ['Limit pricing · সীমা-দাম', 'Predatory merger · লুণ্ঠনমূলক একীভবন', 'Kinked demand · বাঁকানো চাহিদা', 'Self-cancelling advertising · আত্ম-বাতিলকারী বিজ্ঞাপন'], 0,
      'Slide 22: limit pricing keeps price below the short-run profit-maximising level as a barrier to entry.', 'স্লাইড ২২: সীমা-দাম প্রবেশে বাধা হিসেবে স্বল্পমেয়াদি সর্বোচ্চ-মুনাফার স্তরের নিচে দাম রাখে।'),
    Q('Which is a NEGATIVE effect of advertising?', 'কোনটি বিজ্ঞাপনের নেতিবাচক প্রভাব?',
      ['Cheap information · সস্তা তথ্য', 'Helps new products enter · নতুন পণ্য চালুতে সাহায্য', 'Self-cancelling expenditure · আত্ম-বাতিলকারী খরচ', 'More competition · বেশি প্রতিযোগিতা'], 2,
      'When all rivals advertise, the ads cancel out: high cost, little extra demand.', 'সব প্রতিদ্বন্দ্বী বিজ্ঞাপন দিলে একে অপরকে বাতিল করে: বেশি খরচ, সামান্য বাড়তি চাহিদা।'),
])

SUMMARY("""
- **Oligopoly:** a few large firms; homogeneous or differentiated products; price control with **mutual interdependence**; high entry barriers; mergers.
- **Concentration:** CR4 (> 40% = oligopoly), **Herfindahl** = Σ (% share)² (monopoly 10,000).
- **Kinked demand:** rivals match cuts, ignore rises → MR gap → **sticky prices**.
- **Collusion/cartels:** act like a monopolist; overt (OPEC) or covert (tacit); obstacles: differences, number, cheating, recession, entry, law.
- **Price leadership:** dominant firm leads; infrequent changes, communication, limit pricing; price wars.
- **Advertising:** preferred to price competition; positive (information, competition, new products) and negative (persuasion, barrier, self-cancelling).

**Next:** Lecture 12: how government controls monopoly and oligopoly: **competition policy and regulation** (Q16).
""", """
- **অলিগোপলি:** কয়েকটি বড় ফার্ম; সমজাতীয় বা পৃথকীকৃত পণ্য; **পারস্পরিক নির্ভরশীলতাসহ** দামের নিয়ন্ত্রণ; প্রবেশে বড় বাধা; একীভবন।
- **কেন্দ্রীভবন:** CR4 (> ৪০% = অলিগোপলি), **হারফিন্ডাল** = Σ (% অংশ)² (একচেটিয়া ১০,০০০)।
- **বাঁকানো চাহিদা:** প্রতিদ্বন্দ্বী কমানো মানে, বাড়ানো মানে না → MR-এ ফাঁক → **অনমনীয় দাম**।
- **যোগসাজশ/কার্টেল:** একচেটিয়ার মতো চলে; প্রকাশ্য (ওপেক) বা গোপন (মৌন); বাধা: পার্থক্য, সংখ্যা, প্রতারণা, মন্দা, প্রবেশ, আইন।
- **দাম-নেতৃত্ব:** প্রভাবশালী ফার্ম পথ দেখায়; কদাচিৎ বদল, যোগাযোগ, সীমা-দাম; দামযুদ্ধ।
- **বিজ্ঞাপন:** দাম প্রতিযোগিতার চেয়ে পছন্দের; ইতিবাচক (তথ্য, প্রতিযোগিতা, নতুন পণ্য) ও নেতিবাচক (প্ররোচনা, বাধা, আত্ম-বাতিলকারী)।

**পরবর্তী:** লেকচার ১২: সরকার একচেটিয়া ও অলিগোপলি কীভাবে নিয়ন্ত্রণ করে: **প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ** (Q16)।
""")
