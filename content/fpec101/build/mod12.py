MOD(qs=[16])

CONCEPT("""
**Concept:** Lectures 9–11 showed that monopolies and oligopolies can charge high prices, restrict output and collude. Lecture 12 asks: **what can the government do about it?** Three tools:

1. **Anti-trust (competition) policy:** laws that prevent monopoly and promote competition.
2. **Industrial regulation:** the government sets prices in selected industries, mainly **natural monopolies**.
3. **Social regulation:** rules about **how** goods are produced and their **impact on society** (safety, health, environment).

Plus **deregulation**: removing regulations so firms can compete. This lecture is midterm **Q16**.
""", """
**ধারণা:** লেকচার ৯–১১ দেখিয়েছে একচেটিয়া ও অলিগোপলি বেশি দাম নিতে, উৎপাদন সীমিত করতে ও যোগসাজশ করতে পারে। লেকচার ১২ জিজ্ঞেস করে: **সরকার কী করতে পারে?** তিনটি হাতিয়ার:

1. **অ্যান্টি-ট্রাস্ট (প্রতিযোগিতা) নীতি:** একচেটিয়া ঠেকাতে ও প্রতিযোগিতা বাড়াতে আইন।
2. **শিল্প নিয়ন্ত্রণ:** নির্বাচিত শিল্পে, মূলত **প্রাকৃতিক একচেটিয়ায়**, সরকার দাম ঠিক করে।
3. **সামাজিক নিয়ন্ত্রণ:** পণ্য **কীভাবে** উৎপাদিত হয় ও **সমাজে প্রভাব** নিয়ে নিয়ম (নিরাপত্তা, স্বাস্থ্য, পরিবেশ)।

সাথে **বিনিয়ন্ত্রণ**: ফার্মগুলো যাতে প্রতিযোগিতা করতে পারে সেজন্য নিয়ম তুলে নেওয়া। এই লেকচার মিডটার্ম **Q16**।
""")

WORDS([
    ('Antitrust policy', 'Laws and actions to prevent monopoly and promote competition', 'অ্যান্টি-ট্রাস্ট নীতি — একচেটিয়া ঠেকানো ও প্রতিযোগিতা বাড়ানোর আইন ও পদক্ষেপ', 'Bangladesh Competition Act 2012.'),
    ('Industrial regulation', 'Government control of prices (rates) in selected industries', 'শিল্প নিয়ন্ত্রণ — নির্বাচিত শিল্পে সরকারের দাম নিয়ন্ত্রণ', 'BERC sets electricity tariffs.'),
    ('Social regulation', 'Rules on production conditions, product quality and social impact', 'সামাজিক নিয়ন্ত্রণ — উৎপাদনের অবস্থা, পণ্যের মান ও সামাজিক প্রভাবের নিয়ম', 'Factory fire-safety rules, food standards.'),
    ('Rule of reason', 'Courts judge a monopoly by its behaviour, not just its size', 'যুক্তির নিয়ম — আকার নয়, আচরণ দেখে একচেটিয়ার বিচার', 'Big is not illegal; abuse is.'),
    ('Relevant market', 'How broadly the market is defined when measuring market share', 'প্রাসঙ্গিক বাজার — বাজার-অংশ মাপতে বাজারকে কত বিস্তৃত ধরা হয়', '"Soft drinks" vs "all beverages".'),
    ('Tying contract', 'Requiring buyers to buy another product as a condition of sale', 'বাঁধা চুক্তি — একটি কিনতে আরেকটি কিনতে বাধ্য করা', 'Buy our printer, use only our ink.'),
    ('Legal cartel theory', 'Firms may want regulation because it guarantees them a legal monopoly', 'আইনি কার্টেল তত্ত্ব — নিয়ন্ত্রণ আইনি একচেটিয়া নিশ্চিত করে বলে ফার্মই তা চায়', 'Regulator blocks new entrants.'),
    ('Deregulation', 'Removing restrictions so private firms can compete', 'বিনিয়ন্ত্রণ — বেসরকারি ফার্মের প্রতিযোগিতার জন্য নিয়ম তুলে নেওয়া', 'Opening telecom and airlines to private firms.'),
])

SLIDE([1, 2, 3, 4], 'Title and outline', 'শিরোনাম ও রূপরেখা',
    bn=['**স্লাইড ১–৪:** প্রিন্সিপলস অব ইকোনমিক্স — সালিমাহ মুশাররিফ। FPEC 101 – লেকচার ১২, ইউনিট ২। প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ। রূপরেখা: প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ · অ্যান্টি-ট্রাস্ট আইন।'],
    ex="""Topic: **competition policy and regulation**. Reading: McConnell & Brue pp. 583–595 (the slides follow the US system; we add Bangladesh examples).""",
    exb="""বিষয়: **প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ**। পড়া: ম্যাককনেল ও ব্রু পৃ. ৫৮৩–৫৯৫ (স্লাইড যুক্তরাষ্ট্রের ব্যবস্থা অনুসরণ করে; আমরা বাংলাদেশের উদাহরণ যোগ করেছি)।""")

SLIDE(5, 'Three kinds of government policy', 'সরকারি নীতির তিন ধরন',
    bn=['প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ', '**অ্যান্টি-ট্রাস্ট নীতি** হলো একচেটিয়া ঠেকানো ও প্রতিযোগিতা বাড়ানোর জন্য আইন ও সরকারি পদক্ষেপ।', '**শিল্প নিয়ন্ত্রণ** হলো নির্বাচিত শিল্পে ফার্মের দাম (বা "রেট") সরকারি নিয়ন্ত্রণ।',
        '**সামাজিক নিয়ন্ত্রণ** হলো পণ্য উৎপাদনের অবস্থা, পণ্যের ভৌত বৈশিষ্ট্য এবং পণ্য উৎপাদন ও ভোগের সমাজের ওপর প্রভাব নিয়ে সরকারি নিয়ন্ত্রণ।'],
    ex="""Learn the three definitions word for word: they open Q16.

- **Antitrust policy:** laws and actions to **prevent monopoly and promote competition**.
- **Industrial regulation:** government control of **prices/rates** in selected industries.
- **Social regulation:** control of **production conditions**, **product characteristics** and the **impact on society**.""",
    exb="""তিনটি সংজ্ঞা হুবহু শেখো: Q16 এগুলো দিয়েই শুরু।

- **অ্যান্টি-ট্রাস্ট নীতি:** **একচেটিয়া ঠেকাতে ও প্রতিযোগিতা বাড়াতে** আইন ও পদক্ষেপ।
- **শিল্প নিয়ন্ত্রণ:** নির্বাচিত শিল্পে **দাম/রেটের** সরকারি নিয়ন্ত্রণ।
- **সামাজিক নিয়ন্ত্রণ:** **উৎপাদনের অবস্থা**, **পণ্যের বৈশিষ্ট্য** ও **সমাজে প্রভাবের** নিয়ন্ত্রণ।""",
    eg="""**Bangladesh:** Competition Commission (antitrust); BERC and BTRC set energy and telecom tariffs (industrial regulation); BSTI food standards and DIFE factory-safety inspections after Rana Plaza (social regulation).""",
    egb="""**বাংলাদেশ:** প্রতিযোগিতা কমিশন (অ্যান্টি-ট্রাস্ট); বিইআরসি ও বিটিআরসি জ্বালানি ও টেলিকমের দাম ঠিক করে (শিল্প নিয়ন্ত্রণ); বিএসটিআই খাদ্যমান আর রানা প্লাজার পর ডিআইএফই-র কারখানা নিরাপত্তা পরিদর্শন (সামাজিক নিয়ন্ত্রণ)।""")

SLIDE([6, 7], 'Antitrust laws: purpose and issues', 'অ্যান্টি-ট্রাস্ট আইন: উদ্দেশ্য ও সমস্যা',
    bn=['**স্লাইড ৬ — অ্যান্টি-ট্রাস্ট আইন:** একচেটিয়া ঠেকানো, প্রতিযোগিতা বাড়ানো ও বণ্টন দক্ষতা অর্জনের জন্য অ্যান্টি-ট্রাস্ট বা একচেটিয়াবিরোধী নীতি। এই নীতির উপযোগিতা ও কার্যকারিতা প্রশ্নসাপেক্ষ। ঐতিহাসিক পটভূমি: ম্যাককনেল ও ব্রু পৃ. ৫৮৩–৫৮৪।',
        '**স্লাইড ৭ — অ্যান্টি-ট্রাস্ট নীতি: সমস্যা ও প্রভাব:** ব্যাখ্যার সমস্যা · সরকারের প্রয়োগের সমস্যা · কার্যকারিতা — আদালতের অসামঞ্জস্যপূর্ণ ব্যাখ্যা।'],
    ex="""**Purpose:** prevent monopolisation, promote competition, achieve **allocative efficiency** (P = MC, Lecture 8). Historically the US passed the **Sherman Act (1890)** and **Clayton Act (1914)** against monopolies and price-fixing.

The policy has **three problem areas**, explained next: **interpretation** (what counts as illegal?), **enforcement** (how actively the government acts) and **effectiveness** (courts interpret the laws inconsistently).""",
    exb="""**উদ্দেশ্য:** একচেটিয়া ঠেকানো, প্রতিযোগিতা বাড়ানো, **বণ্টন দক্ষতা** অর্জন (P = MC, লেকচার ৮)। ঐতিহাসিকভাবে যুক্তরাষ্ট্র একচেটিয়া ও দাম ঠিক করার বিরুদ্ধে **শারম্যান আইন (১৮৯০)** ও **ক্লেটন আইন (১৯১৪)** পাস করে।

নীতির **তিনটি সমস্যার জায়গা**, পরে ব্যাখ্যা: **ব্যাখ্যা** (কী অবৈধ?), **প্রয়োগ** (সরকার কতটা সক্রিয়) ও **কার্যকারিতা** (আদালত আইন অসামঞ্জস্যভাবে ব্যাখ্যা করে)।""",
    note="Bangladesh's equivalent is the **Competition Act 2012**, enforced by the **Bangladesh Competition Commission**; it bans cartels, abuse of dominant position and anti-competitive mergers.",
    noteb="বাংলাদেশে এর সমতুল্য **প্রতিযোগিতা আইন ২০১২**, প্রয়োগ করে **বাংলাদেশ প্রতিযোগিতা কমিশন**; এটি কার্টেল, প্রভাবশালী অবস্থানের অপব্যবহার ও প্রতিযোগিতাবিরোধী একীভবন নিষিদ্ধ করে।")

SLIDE(8, 'Issues of interpretation', 'ব্যাখ্যার সমস্যা',
    bn=['অ্যান্টি-ট্রাস্ট আইন — ব্যাখ্যার সমস্যা (ম্যাককনেল ও ব্রু পৃ. ৫৮৪–৫৮৫)', '**একচেটিয়া আচরণ বনাম একচেটিয়া কাঠামো:** আদালত আবার যুক্তির নিয়মে (rule of reason) ফিরে গেছে।',
        '**প্রাসঙ্গিক বাজার:** ৯০-৬০-৩০ নিয়ম। বাজার-অংশ নির্ভর করে বাজারকে কীভাবে সংজ্ঞায়িত করা হয় তার ওপর। মোটামুটি একই রকম পণ্যের বিস্তৃত পরিসর ধরলে ফার্মের অংশ ছোট দেখায়; সরুভাবে ধরলে অংশ বড় দেখায়।'],
    ex="""Two big questions courts must answer:

1. **Behaviour or structure?** Is a firm guilty just because it is **big** (structure), or only if it **behaves** badly (predatory pricing, exclusive dealing)? Courts follow the **rule of reason**: being large is not illegal; **abusing** market power is.
2. **Relevant market:** market share depends on **how the market is defined**. A cola maker may have 70% of "colas" but 20% of "all drinks". Rough **90-60-30 rule**: over 90% share = monopoly; 60% = probably; under 30% = not a monopoly.""",
    exb="""আদালতকে দুটি বড় প্রশ্নের উত্তর দিতে হয়:

1. **আচরণ না কাঠামো?** ফার্ম কি শুধু **বড়** বলে (কাঠামো) দোষী, নাকি শুধু খারাপ **আচরণ** করলে (লুণ্ঠনমূলক দাম, একচেটিয়া লেনদেন)? আদালত **যুক্তির নিয়ম** মানে: বড় হওয়া অবৈধ নয়; বাজারক্ষমতার **অপব্যবহার** অবৈধ।
2. **প্রাসঙ্গিক বাজার:** বাজার-অংশ নির্ভর করে **বাজার কীভাবে সংজ্ঞায়িত** তার ওপর। এক কোলা কোম্পানির "কোলা"-য় ৭০% কিন্তু "সব পানীয়"-তে ২০% থাকতে পারে। মোটামুটি **৯০-৬০-৩০ নিয়ম**: ৯০%-এর বেশি = একচেটিয়া; ৬০% = সম্ভবত; ৩০%-এর নিচে = একচেটিয়া নয়।""")

SLIDE([9, 10], 'Issues of enforcement', 'প্রয়োগের সমস্যা',
    bn=['**স্লাইড ৯:** কেন্দ্রীয় (ফেডারেল) অ্যান্টি-ট্রাস্ট প্রয়োগ অর্থনীতিতে সামগ্রিক অ্যান্টি-ট্রাস্ট পদক্ষেপের মাত্রায় পার্থক্য আনে। বড় মামলা বছরের পর বছর চলে, খুব ব্যয়বহুল, তাই ক্ষতিগ্রস্তরা প্রায়ই সরকারের মামলা শুরুর অপেক্ষায় থাকে। সরকার দোষী সাব্যস্ত করলে ক্ষতিগ্রস্তদের আর দোষ প্রমাণ করতে হয় না, শুধু ক্ষতিপূরণের মামলা করে। তাই সরকারের পদক্ষেপ না থাকলে ফার্মগুলোর আইনি পদক্ষেপও কমে।',
        '**স্লাইড ১০:** অ্যান্টি-ট্রাস্ট নীতি নিয়ে দুটি বিপরীত দৃষ্টিভঙ্গি: **সক্রিয় দৃষ্টিভঙ্গি** — কিছু ক্ষেত্রে প্রতিযোগিতা বণ্টন দক্ষতা অর্জন ও ভোক্তা-প্রতিযোগীর প্রতি ন্যায্যতা নিশ্চিত করতে যথেষ্ট নয়। **লেসে-ফেয়ার দৃষ্টিভঙ্গি** — অ্যান্টি-ট্রাস্ট হস্তক্ষেপ মূলত অপ্রয়োজনীয়, বিশেষত একচেটিয়ার ক্ষেত্রে।'],
    ex="""**Enforcement depends on the government.** Antitrust cases are long and expensive, so private victims wait for the government to sue first; after a government conviction they only need to claim damages. So **when the government is passive, there is less antitrust action overall**.

**Two views:**
- **Active antitrust:** competition alone is often not enough for efficiency and fairness, so government should intervene.
- **Laissez-faire:** intervention is mostly **unnecessary**; monopolies are temporary because new firms and technologies challenge them (recall "unsustainable monopoly", Lecture 9).""",
    exb="""**প্রয়োগ সরকারের ওপর নির্ভরশীল।** অ্যান্টি-ট্রাস্ট মামলা দীর্ঘ ও ব্যয়বহুল, তাই ক্ষতিগ্রস্তরা আগে সরকারের মামলার অপেক্ষা করে; সরকার দোষী সাব্যস্ত করলে তাদের শুধু ক্ষতিপূরণ চাইতে হয়। তাই **সরকার নিষ্ক্রিয় হলে সামগ্রিক অ্যান্টি-ট্রাস্ট পদক্ষেপ কমে**।

**দুটি দৃষ্টিভঙ্গি:**
- **সক্রিয় অ্যান্টি-ট্রাস্ট:** দক্ষতা ও ন্যায্যতার জন্য শুধু প্রতিযোগিতা প্রায়ই যথেষ্ট নয়, তাই সরকারের হস্তক্ষেপ দরকার।
- **লেসে-ফেয়ার:** হস্তক্ষেপ মূলত **অপ্রয়োজনীয়**; নতুন ফার্ম ও প্রযুক্তি চ্যালেঞ্জ করে বলে একচেটিয়া সাময়িক (লেকচার ৯-এর "অস্থায়ী একচেটিয়া" মনে করো)।""")

SLIDE([11, 12, 13], 'Effectiveness of antitrust laws', 'অ্যান্টি-ট্রাস্ট আইনের কার্যকারিতা',
    bn=['**স্লাইড ১১ — প্রভাব বিশ্লেষণ:** **একচেটিয়া:** সরকার কোনো ফার্মের বিরুদ্ধে মামলা করে শুধু তখনই যখন তার বাজার-অংশ খুব বেশি এবং আধিপত্য অর্জন, ধরে রাখা বা বাড়াতে অপব্যবহারের প্রমাণ থাকে। **একীভবন:** প্রতিযোগিতা উল্লেখযোগ্যভাবে কমায় এমন আনুভূমিক একীভবন আটকানো — একীভবনের পর হারফিন্ডাল সূচক বেশি (১৮০০-র ওপরে) এবং একীভবনে সূচক ১০০ বা বেশি বাড়লে; বৃহদায়তনের সুবিধা, বিদেশি প্রতিযোগিতা ও নতুনদের প্রবেশের সহজতাও বিবেচ্য। উল্লম্ব একীভবন সাধারণত প্রতিযোগিতা কমায় না, যদি না খুব কেন্দ্রীভূত শিল্পের বড় ফার্ম হয়। কংগ্লোমারেট একীভবন সাধারণত অনুমোদিত।',
        '**স্লাইড ১২:** **দাম ঠিক করা** অবৈধ, কঠোর ব্যবস্থা নেওয়া হয়। **দাম-বৈষম্য** কদাচিৎ প্রতিযোগিতা কমায়, কদাচিৎ চ্যালেঞ্জ হয়। **বাঁধা চুক্তি** নিষিদ্ধ, বিশেষত প্রভাবশালী ফার্ম করলে, যেমন কোডাক ক্যামেরার ফিল্ম শুধু কোডাকেই প্রসেস করাতে বাধ্য করা।',
        '**স্লাইড ১৩:** আইনগতভাবে অভ্যন্তরীণ সম্প্রসারণে গড়ে ওঠা একচেটিয়া বা অলিগোপলি ঠেকাতে বা ভাঙতে তুলনামূলক অকার্যকর। লুণ্ঠনমূলক বা অপব্যবহারকারী একচেটিয়ার বিরুদ্ধে কার্যকর, যদিও ধীর আইনি প্রক্রিয়া ও প্রতিকার বাস্তবায়নে বাধা আছে। স্পষ্ট প্রতিযোগিতাবিরোধী একীভবন আটকাতে এবং দাম ঠিক করা ও বাঁধা চুক্তি শনাক্ত ও বিচারে কার্যকর। সামগ্রিকভাবে প্রতিযোগিতা ও দক্ষতা বাড়ানোর লক্ষ্যে মাঝারি কার্যকর।'],
    ex="""How well do antitrust laws work in each area?

<div class="tbl"><table><thead><tr><th>Area</th><th>Treatment</th></tr></thead><tbody>
<tr><td>Monopoly</td><td>Sued only with very high market share <b>and</b> evidence of abusive conduct</td></tr>
<tr><td>Horizontal mergers</td><td>Blocked if they substantially lessen competition: post-merger HHI &gt; 1,800 and the merger adds ≥ 100 points (scale economies, foreign competition and ease of entry also considered)</td></tr>
<tr><td>Vertical mergers</td><td>Usually allowed, unless large firms in highly concentrated industries</td></tr>
<tr><td>Conglomerate mergers</td><td>Generally permitted</td></tr>
<tr><td>Price-fixing</td><td>Illegal, strict action</td></tr>
<tr><td>Price discrimination</td><td>Rarely challenged</td></tr>
<tr><td>Tying contracts</td><td>Prohibited, especially by dominant firms (e.g. Kodak film processing)</td></tr></tbody></table></div>

**Overall verdict (slide 13):** weak against monopolies built by legal internal growth; effective against abusive monopolies (but slow); effective against blatant anti-competitive mergers, price-fixing and tying → **moderately effective**.""",
    exb="""প্রতিটি ক্ষেত্রে অ্যান্টি-ট্রাস্ট আইন কতটা কাজ করে?

<div class="tbl"><table><thead><tr><th>ক্ষেত্র</th><th>ব্যবস্থা</th></tr></thead><tbody>
<tr><td>একচেটিয়া</td><td>খুব বেশি বাজার-অংশ <b>এবং</b> অপব্যবহারের প্রমাণ থাকলে তবেই মামলা</td></tr>
<tr><td>আনুভূমিক একীভবন</td><td>প্রতিযোগিতা উল্লেখযোগ্যভাবে কমালে আটকানো হয়: একীভবনের পর HHI &gt; ১,৮০০ এবং একীভবনে ≥ ১০০ পয়েন্ট বাড়লে (বৃহদায়তনের সুবিধা, বিদেশি প্রতিযোগিতা, প্রবেশের সহজতাও বিবেচ্য)</td></tr>
<tr><td>উল্লম্ব একীভবন</td><td>সাধারণত অনুমোদিত, যদি না খুব কেন্দ্রীভূত শিল্পের বড় ফার্ম</td></tr>
<tr><td>কংগ্লোমারেট একীভবন</td><td>সাধারণত অনুমোদিত</td></tr>
<tr><td>দাম ঠিক করা</td><td>অবৈধ, কঠোর ব্যবস্থা</td></tr>
<tr><td>দাম-বৈষম্য</td><td>কদাচিৎ চ্যালেঞ্জ</td></tr>
<tr><td>বাঁধা চুক্তি</td><td>নিষিদ্ধ, বিশেষত প্রভাবশালী ফার্মের (যেমন কোডাকের ফিল্ম প্রসেসিং)</td></tr></tbody></table></div>

**সামগ্রিক রায় (স্লাইড ১৩):** আইনসম্মত অভ্যন্তরীণ প্রবৃদ্ধিতে গড়া একচেটিয়ার বিরুদ্ধে দুর্বল; অপব্যবহারকারী একচেটিয়ার বিরুদ্ধে কার্যকর (কিন্তু ধীর); স্পষ্ট প্রতিযোগিতাবিরোধী একীভবন, দাম ঠিক করা ও বাঁধা চুক্তির বিরুদ্ধে কার্যকর → **মাঝারি কার্যকর**।""",
    tip="Q16 \"analyse\": give this table and the slide-13 verdict \"moderately effective\" with reasons.",
    tipb="Q16-এর \"বিশ্লেষণ\": এই ছক আর স্লাইড ১৩-এর রায় \"moderately effective\" কারণসহ লেখো।")

CHECK([
    Q('Government control of electricity prices is an example of…', 'বিদ্যুতের দামের সরকারি নিয়ন্ত্রণ কিসের উদাহরণ?',
      ['Social regulation · সামাজিক নিয়ন্ত্রণ', 'Industrial regulation · শিল্প নিয়ন্ত্রণ', 'Deregulation · বিনিয়ন্ত্রণ', 'Tying contract · বাঁধা চুক্তি'], 1,
      'Industrial regulation = government regulation of firms\' prices (rates) in selected industries.', 'শিল্প নিয়ন্ত্রণ = নির্বাচিত শিল্পে ফার্মের দামের সরকারি নিয়ন্ত্রণ।'),
    Q('Which is most likely to be blocked by antitrust authorities?', 'অ্যান্টি-ট্রাস্ট কর্তৃপক্ষ কোনটি আটকাতে সবচেয়ে বেশি সম্ভাবনা?',
      ['A conglomerate merger · কংগ্লোমারেট একীভবন', 'A horizontal merger raising HHI above 1,800 · HHI ১,৮০০-র ওপরে তোলা আনুভূমিক একীভবন', 'Internal growth · অভ্যন্তরীণ প্রবৃদ্ধি', 'A small vertical merger · ছোট উল্লম্ব একীভবন'], 1,
      'Horizontal mergers that substantially lessen competition (high post-merger HHI) are blocked.', 'প্রতিযোগিতা উল্লেখযোগ্যভাবে কমানো আনুভূমিক একীভবন (একীভবনের পর উচ্চ HHI) আটকানো হয়।'),
])

SLIDE([14, 15, 16], 'Industrial regulation of natural monopoly and its problems', 'প্রাকৃতিক একচেটিয়ার শিল্প নিয়ন্ত্রণ ও সমস্যা',
    bn=['**স্লাইড ১৪:** যখন কোনো শিল্প একচেটিয়াভাবে সংগঠিত হওয়ার অর্থনৈতিক কারণ থাকে — প্রাকৃতিক একচেটিয়া। প্রাকৃতিক একচেটিয়ায় ভালো অর্থনৈতিক ফলের বিকল্প: • সরকারি মালিকানা • সরকারি নিয়ন্ত্রণ — দাম নিয়ন্ত্রণ; জনস্বার্থ তত্ত্ব অনুযায়ী ফার্ম স্বাভাবিক মুনাফা পায়: দাম = ATC।',
        '**স্লাইড ১৫ — শিল্প নিয়ন্ত্রণের সমস্যা:** খরচ ও অদক্ষতা · একচেটিয়া স্থায়ী করা।',
        '**স্লাইড ১৬ — আইনি কার্টেল তত্ত্ব:** এই ফার্মগুলো নিয়ন্ত্রণ চায়, কারণ এতে আইনি একচেটিয়া পায় যা প্রায় মুনাফা নিশ্চিত করে। নিয়ন্ত্রক কমিশন প্রবেশ আটকায়, অবৈধ কার্টেলের মতো বাজার ভাগ করে, দাম ঠিক করে। বেসরকারি কার্টেল অবৈধ ও অস্থির, প্রায়ই ভেঙে পড়ে; কিন্তু নিয়ন্ত্রণের আড়ালে সরকার-সমর্থিত কার্টেল টিকে থাকে — এটাই এর বিশেষ আকর্ষণ।'],
    ex="""**Natural monopoly** (Lecture 9): one firm is cheapest, so breaking it up would raise costs. Two ways to protect the public:
1. **Public ownership** (e.g. Dhaka WASA, Bangladesh Railway).
2. **Public regulation of prices:** under the **public interest theory**, the regulator sets **P = ATC**, so the firm earns only a **normal profit** while consumers get a fair price.

**Problems with regulation:**
- **Costs and inefficiency:** if price is set at ATC, the firm has **no incentive to cut costs** (higher costs → higher allowed price): X-inefficiency.
- **Perpetuating monopoly:** regulation may keep a monopoly alive even after new technology makes competition possible.
- **Legal cartel theory:** firms may actually **want** regulation, because the regulator blocks entry, divides the market and fixes prices like a **legal, government-protected cartel** that, unlike private cartels, does not break down.""",
    exb="""**প্রাকৃতিক একচেটিয়া** (লেকচার ৯): একটি ফার্মই সবচেয়ে সস্তা, তাই ভাঙলে খরচ বাড়বে। জনগণকে রক্ষার দুই উপায়:
1. **সরকারি মালিকানা** (যেমন ঢাকা ওয়াসা, বাংলাদেশ রেলওয়ে)।
2. **সরকারি দাম নিয়ন্ত্রণ:** **জনস্বার্থ তত্ত্ব** অনুযায়ী নিয়ন্ত্রক **P = ATC** ঠিক করে, তাই ফার্ম শুধু **স্বাভাবিক মুনাফা** পায় আর ভোক্তা ন্যায্য দাম পায়।

**নিয়ন্ত্রণের সমস্যা:**
- **খরচ ও অদক্ষতা:** দাম ATC-তে ঠিক হলে ফার্মের **খরচ কমানোর প্রণোদনা থাকে না** (বেশি খরচ → বেশি অনুমোদিত দাম): X-অদক্ষতা।
- **একচেটিয়া স্থায়ী করা:** নতুন প্রযুক্তি প্রতিযোগিতা সম্ভব করার পরও নিয়ন্ত্রণ একচেটিয়াকে বাঁচিয়ে রাখতে পারে।
- **আইনি কার্টেল তত্ত্ব:** ফার্মগুলো আসলে নিয়ন্ত্রণ **চাইতে** পারে, কারণ নিয়ন্ত্রক প্রবেশ আটকায়, বাজার ভাগ করে ও দাম ঠিক করে — যেন একটি **আইনি, সরকার-সুরক্ষিত কার্টেল**, যা বেসরকারি কার্টেলের মতো ভেঙে পড়ে না।""")

SLIDE(17, 'Deregulation', 'বিনিয়ন্ত্রণ',
    bn=['বিনিয়ন্ত্রণ', 'নিয়ম ও বিধিনিষেধ তুলে নেওয়ার প্রক্রিয়া।', 'বেসরকারি ফার্মগুলোকে প্রতিযোগিতা করতে দিয়েছে।', 'সমাজের জন্য বছরে বড় দক্ষতা-লাভ এনেছে।', 'বিনিয়ন্ত্রণকে সফল বা ব্যর্থ বলার সময় এখনো আসেনি।'],
    ex="""**Deregulation** = **removing restrictions** so private firms can enter and compete (e.g. US airlines, trucking, telecoms from the late 1970s). It has brought **large efficiency gains** (lower prices, more choice), but the slide says it is **too soon** to call it a complete success or failure (some deregulated markets, like electricity in some places, had problems).""",
    exb="""**বিনিয়ন্ত্রণ** = বেসরকারি ফার্ম যাতে ঢুকে প্রতিযোগিতা করতে পারে সেজন্য **বিধিনিষেধ তুলে নেওয়া** (যেমন ১৯৭০-এর দশকের শেষ থেকে যুক্তরাষ্ট্রের এয়ারলাইন, ট্রাক পরিবহন, টেলিকম)। এতে **বড় দক্ষতা-লাভ** হয়েছে (কম দাম, বেশি পছন্দ), কিন্তু স্লাইড বলে সম্পূর্ণ সফল বা ব্যর্থ বলার **সময় এখনো আসেনি** (কিছু জায়গায় বিদ্যুতের মতো বিনিয়ন্ত্রিত বাজারে সমস্যা হয়েছে)।""",
    eg="""**Bangladesh:** in the 1990s the government allowed private mobile operators, private TV channels and private airlines. Mobile call prices fell from over Tk 10 a minute to under Tk 1, and users grew to over 180 million connections: deregulation in action.""",
    egb="""**বাংলাদেশ:** ১৯৯০-এর দশকে সরকার বেসরকারি মোবাইল অপারেটর, বেসরকারি টিভি চ্যানেল ও বেসরকারি এয়ারলাইনের অনুমতি দেয়। মোবাইল কলের দাম মিনিটে ১০ টাকার বেশি থেকে ১ টাকার নিচে নামে, সংযোগ ১৮ কোটি ছাড়ায়: কাজে বিনিয়ন্ত্রণ।""")

SLIDE(18, 'Social regulation', 'সামাজিক নিয়ন্ত্রণ',
    bn=['সামাজিক নিয়ন্ত্রণ', 'পণ্য ও সেবা কোন অবস্থায় উৎপাদিত হয়, উৎপাদনের সমাজের ওপর প্রভাব এবং পণ্যের ভৌত গুণাবলি নিয়ে সংশ্লিষ্ট।', 'পার্থক্যসূচক বৈশিষ্ট্য', 'সামাজিক নিয়ন্ত্রণের সর্বোত্তম মাত্রা — • সমর্থন • সমালোচনা', 'দুটি স্মরণীয় কথা — • বিনামূল্যে দুপুরের খাবার বলে কিছু নেই • কম সরকার সবসময় বেশি সরকারের চেয়ে ভালো নয়'],
    ex="""**Social regulation** covers (1) **production conditions** (worker safety), (2) **impact on society** (pollution), (3) **product qualities** (food safety, labelling).

**Distinguishing features (vs industrial regulation):** it applies to **far more firms** across many industries, and it **intervenes in production details** (how goods are made), not just prices.

**Optimal level:** supporters say it saves lives and protects the environment; critics say it raises costs and prices and slows innovation. The right level is where **marginal benefit = marginal cost**.

**Two reminders:** **"There is no free lunch"**: regulation has real costs (higher prices). **"Less government is not always better"**: removing rules can cost lives.""",
    exb="""**সামাজিক নিয়ন্ত্রণ** দেখে (১) **উৎপাদনের অবস্থা** (শ্রমিক নিরাপত্তা), (২) **সমাজে প্রভাব** (দূষণ), (৩) **পণ্যের গুণ** (খাদ্য নিরাপত্তা, লেবেল)।

**পার্থক্য (শিল্প নিয়ন্ত্রণের তুলনায়):** অনেক শিল্পের **অনেক বেশি ফার্মে** প্রযোজ্য, আর শুধু দাম নয়, **উৎপাদনের খুঁটিনাটিতে** (কীভাবে বানানো হয়) হস্তক্ষেপ করে।

**সর্বোত্তম মাত্রা:** সমর্থকেরা বলেন এটা জীবন বাঁচায় ও পরিবেশ রক্ষা করে; সমালোচকেরা বলেন খরচ ও দাম বাড়ায়, উদ্ভাবন ধীর করে। সঠিক মাত্রা যেখানে **প্রান্তিক সুবিধা = প্রান্তিক ব্যয়**।

**দুটি স্মরণীয় কথা:** **"বিনামূল্যে দুপুরের খাবার নেই"**: নিয়ন্ত্রণের বাস্তব খরচ আছে (বেশি দাম)। **"কম সরকার সবসময় ভালো নয়"**: নিয়ম তুলে নিলে জীবনহানি হতে পারে।""",
    eg="""After the Rana Plaza collapse (2013), stronger building and fire-safety rules for garment factories raised costs, but saved lives and protected the industry's export reputation.""",
    egb="""রানা প্লাজা ধসের (২০১৩) পর গার্মেন্টসে কঠোর ভবন ও অগ্নি-নিরাপত্তার নিয়ম খরচ বাড়িয়েছে, কিন্তু জীবন বাঁচিয়েছে ও শিল্পের রপ্তানি সুনাম রক্ষা করেছে।""")

SLIDE(19, 'Summary of Lecture 12', 'লেকচার ১২-এর সারসংক্ষেপ',
    bn=['সারসংক্ষেপ', 'প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ', 'অ্যান্টি-ট্রাস্ট আইন — ব্যাখ্যার সমস্যা · সরকারের প্রয়োগের সমস্যা · কার্যকারিতা', 'শিল্প নিয়ন্ত্রণ ও তার সমস্যা — প্রাকৃতিক একচেটিয়া · আইনি কার্টেল তত্ত্ব', 'বিনিয়ন্ত্রণ', 'সামাজিক নিয়ন্ত্রণ'],
    ex="""This summary is exactly the outline of **Q16**: antitrust (interpretation, enforcement, effectiveness) → industrial regulation (natural monopoly, P = ATC, problems, legal cartel theory) → deregulation → social regulation.""",
    exb="""এই সারসংক্ষেপই হুবহু **Q16**-এর রূপরেখা: অ্যান্টি-ট্রাস্ট (ব্যাখ্যা, প্রয়োগ, কার্যকারিতা) → শিল্প নিয়ন্ত্রণ (প্রাকৃতিক একচেটিয়া, P = ATC, সমস্যা, আইনি কার্টেল তত্ত্ব) → বিনিয়ন্ত্রণ → সামাজিক নিয়ন্ত্রণ।""")

TOGETHER("""
<div class="tbl"><table><thead><tr><th></th><th>Antitrust policy</th><th>Industrial regulation</th><th>Social regulation</th></tr></thead><tbody>
<tr><td>Aim</td><td>Prevent monopoly, promote competition</td><td>Control prices of natural monopolies</td><td>Safety, health, environment</td></tr>
<tr><td>Tools</td><td>Ban abuse, block mergers, punish price-fixing and tying</td><td>Public ownership or P = ATC</td><td>Standards and rules on production and products</td></tr>
<tr><td>Problems</td><td>Interpretation, enforcement, slow courts</td><td>No incentive to cut costs, perpetuates monopoly, legal cartel</td><td>Raises costs; finding the optimal level</td></tr>
<tr><td>Bangladesh</td><td>Competition Commission</td><td>BERC, BTRC, WASA</td><td>BSTI, DIFE, Department of Environment</td></tr></tbody></table></div>
""", """
<div class="tbl"><table><thead><tr><th></th><th>অ্যান্টি-ট্রাস্ট নীতি</th><th>শিল্প নিয়ন্ত্রণ</th><th>সামাজিক নিয়ন্ত্রণ</th></tr></thead><tbody>
<tr><td>লক্ষ্য</td><td>একচেটিয়া ঠেকানো, প্রতিযোগিতা বাড়ানো</td><td>প্রাকৃতিক একচেটিয়ার দাম নিয়ন্ত্রণ</td><td>নিরাপত্তা, স্বাস্থ্য, পরিবেশ</td></tr>
<tr><td>হাতিয়ার</td><td>অপব্যবহার নিষিদ্ধ, একীভবন আটকানো, দাম ঠিক করা ও বাঁধা চুক্তিতে শাস্তি</td><td>সরকারি মালিকানা বা P = ATC</td><td>উৎপাদন ও পণ্যের মান ও নিয়ম</td></tr>
<tr><td>সমস্যা</td><td>ব্যাখ্যা, প্রয়োগ, ধীর আদালত</td><td>খরচ কমানোর প্রণোদনা নেই, একচেটিয়া স্থায়ী, আইনি কার্টেল</td><td>খরচ বাড়ায়; সর্বোত্তম মাত্রা খোঁজা</td></tr>
<tr><td>বাংলাদেশ</td><td>প্রতিযোগিতা কমিশন</td><td>বিইআরসি, বিটিআরসি, ওয়াসা</td><td>বিএসটিআই, ডিআইএফই, পরিবেশ অধিদপ্তর</td></tr></tbody></table></div>
""")

MIDTERM("""
Full card: <a href="#e16">Q16</a>.

### Q16 — Analyse the anti-trust laws, competition policy and the different ways of regulation and deregulation
**Definitions:** **antitrust policy** = laws and government actions to prevent monopoly and promote competition (and allocative efficiency); **industrial regulation** = government regulation of prices in selected industries; **social regulation** = regulation of production conditions, product characteristics and the social impact of production and consumption.
**Antitrust — issues of interpretation:** monopoly behaviour vs structure (courts apply the **rule of reason**: abuse, not size, is illegal); defining the **relevant market** (90-60-30 rule). **Enforcement:** depends heavily on government action; two views: active antitrust vs laissez-faire. **Effectiveness:** monopolies sued only with high share and abusive conduct; horizontal mergers blocked if they substantially lessen competition (post-merger HHI > 1,800 and +100 points); vertical and conglomerate mergers usually allowed; **price-fixing** illegal; price discrimination rarely challenged; **tying contracts** prohibited. Verdict: weak against legally grown monopolies, effective against abusive monopolies, anti-competitive mergers, price-fixing and tying: **moderately effective**.
**Industrial regulation:** for **natural monopolies**, either public ownership or price regulation (public interest theory: **P = ATC**, normal profit). Problems: costs and inefficiency (no incentive to cut costs), perpetuating monopoly, and the **legal cartel theory** (firms seek regulation that blocks entry and fixes prices).
**Deregulation:** removing restrictions so private firms can compete; large efficiency gains, though too soon to judge fully (e.g. Bangladesh telecom liberalisation).
**Social regulation:** applies broadly and to production details; optimal level where marginal benefit = marginal cost; "no free lunch" and "less government is not always better".
""", """
পূর্ণ কার্ড: <a href="#e16">Q16</a>।

### Q16 — অ্যান্টি-ট্রাস্ট আইন, প্রতিযোগিতা নীতি এবং নিয়ন্ত্রণ ও বিনিয়ন্ত্রণের বিভিন্ন উপায় বিশ্লেষণ করো
**সংজ্ঞা:** **অ্যান্টি-ট্রাস্ট নীতি** = একচেটিয়া ঠেকাতে ও প্রতিযোগিতা (ও বণ্টন দক্ষতা) বাড়াতে আইন ও সরকারি পদক্ষেপ; **শিল্প নিয়ন্ত্রণ** = নির্বাচিত শিল্পে দামের সরকারি নিয়ন্ত্রণ; **সামাজিক নিয়ন্ত্রণ** = উৎপাদনের অবস্থা, পণ্যের বৈশিষ্ট্য এবং উৎপাদন ও ভোগের সামাজিক প্রভাবের নিয়ন্ত্রণ।
**অ্যান্টি-ট্রাস্ট — ব্যাখ্যার সমস্যা:** একচেটিয়া আচরণ বনাম কাঠামো (আদালত **যুক্তির নিয়ম** মানে: আকার নয়, অপব্যবহার অবৈধ); **প্রাসঙ্গিক বাজার** নির্ধারণ (৯০-৬০-৩০ নিয়ম)। **প্রয়োগ:** সরকারের পদক্ষেপের ওপর অনেক নির্ভরশীল; দুটি দৃষ্টিভঙ্গি: সক্রিয় অ্যান্টি-ট্রাস্ট বনাম লেসে-ফেয়ার। **কার্যকারিতা:** উচ্চ অংশ ও অপব্যবহার থাকলেই একচেটিয়ার বিরুদ্ধে মামলা; প্রতিযোগিতা উল্লেখযোগ্যভাবে কমালে আনুভূমিক একীভবন আটকানো (একীভবনের পর HHI > ১,৮০০ ও +১০০ পয়েন্ট); উল্লম্ব ও কংগ্লোমারেট সাধারণত অনুমোদিত; **দাম ঠিক করা** অবৈধ; দাম-বৈষম্য কদাচিৎ চ্যালেঞ্জ; **বাঁধা চুক্তি** নিষিদ্ধ। রায়: আইনসম্মতভাবে বেড়ে ওঠা একচেটিয়ার বিরুদ্ধে দুর্বল, অপব্যবহারকারী একচেটিয়া, প্রতিযোগিতাবিরোধী একীভবন, দাম ঠিক করা ও বাঁধা চুক্তির বিরুদ্ধে কার্যকর: **মাঝারি কার্যকর**।
**শিল্প নিয়ন্ত্রণ:** **প্রাকৃতিক একচেটিয়ায়** সরকারি মালিকানা বা দাম নিয়ন্ত্রণ (জনস্বার্থ তত্ত্ব: **P = ATC**, স্বাভাবিক মুনাফা)। সমস্যা: খরচ ও অদক্ষতা (খরচ কমানোর প্রণোদনা নেই), একচেটিয়া স্থায়ী করা, আর **আইনি কার্টেল তত্ত্ব** (ফার্ম এমন নিয়ন্ত্রণ চায় যা প্রবেশ আটকায় ও দাম ঠিক করে)।
**বিনিয়ন্ত্রণ:** বেসরকারি ফার্মের প্রতিযোগিতার জন্য বিধিনিষেধ তুলে নেওয়া; বড় দক্ষতা-লাভ, যদিও পুরো বিচারের সময় আসেনি (যেমন বাংলাদেশের টেলিকম উদারীকরণ)।
**সামাজিক নিয়ন্ত্রণ:** ব্যাপকভাবে ও উৎপাদনের খুঁটিনাটিতে প্রযোজ্য; সর্বোত্তম মাত্রা যেখানে প্রান্তিক সুবিধা = প্রান্তিক ব্যয়; "বিনামূল্যে খাবার নেই" ও "কম সরকার সবসময় ভালো নয়"।
""")

QUIZ([
    Q('Laws designed to prevent monopoly and promote competition are called…', 'একচেটিয়া ঠেকাতে ও প্রতিযোগিতা বাড়াতে তৈরি আইনকে বলে…',
      ['Social regulation · সামাজিক নিয়ন্ত্রণ', 'Antitrust policy · অ্যান্টি-ট্রাস্ট নীতি', 'Deregulation · বিনিয়ন্ত্রণ', 'Legal cartel · আইনি কার্টেল'], 1,
      'Slide 5 definition.', 'স্লাইড ৫-এর সংজ্ঞা।'),
    Q('Under the public interest theory, a regulated natural monopoly is allowed to charge…', 'জনস্বার্থ তত্ত্বে নিয়ন্ত্রিত প্রাকৃতিক একচেটিয়াকে যে দাম নিতে দেওয়া হয়…',
      ['P = ATC (normal profit) · P = ATC (স্বাভাবিক মুনাফা)', 'The monopoly price · একচেটিয়া দাম', 'Zero · শূন্য', 'P = AFC · P = AFC'], 0,
      'Price equals ATC so the firm just earns normal profit.', 'দাম = ATC, তাই ফার্ম শুধু স্বাভাবিক মুনাফা পায়।'),
    Q('The legal cartel theory says…', 'আইনি কার্টেল তত্ত্ব বলে…',
      ['Regulators always help consumers · নিয়ন্ত্রক সবসময় ভোক্তাকে সাহায্য করে', 'Firms may want regulation because it guarantees a protected monopoly · ফার্ম নিয়ন্ত্রণ চাইতে পারে কারণ তা সুরক্ষিত একচেটিয়া নিশ্চিত করে',
       'Cartels are always legal · কার্টেল সবসময় বৈধ', 'Deregulation is a failure · বিনিয়ন্ত্রণ ব্যর্থ'], 1,
      'Regulation can block entry and fix prices like a lasting, legal cartel.', 'নিয়ন্ত্রণ স্থায়ী, আইনি কার্টেলের মতো প্রবেশ আটকাতে ও দাম ঠিক করতে পারে।'),
    Q('Requiring customers to buy film processing only from the camera maker is a…', 'ক্যামেরা নির্মাতার কাছ থেকেই ফিল্ম প্রসেস করাতে বাধ্য করা হলো…',
      ['Tying contract · বাঁধা চুক্তি', 'Price discrimination · দাম-বৈষম্য', 'Conglomerate merger · কংগ্লোমারেট একীভবন', 'Social regulation · সামাজিক নিয়ন্ত্রণ'], 0,
      'Slide 12: tying contracts are prohibited, especially by dominant firms (Kodak example).', 'স্লাইড ১২: বাঁধা চুক্তি নিষিদ্ধ, বিশেষত প্রভাবশালী ফার্মের (কোডাকের উদাহরণ)।'),
    Q('Factory fire-safety rules are an example of…', 'কারখানার অগ্নি-নিরাপত্তার নিয়ম কিসের উদাহরণ?',
      ['Industrial regulation · শিল্প নিয়ন্ত্রণ', 'Social regulation · সামাজিক নিয়ন্ত্রণ', 'Antitrust · অ্যান্টি-ট্রাস্ট', 'Deregulation · বিনিয়ন্ত্রণ'], 1,
      'Social regulation covers the conditions under which goods are produced.', 'সামাজিক নিয়ন্ত্রণ পণ্য উৎপাদনের অবস্থা দেখে।'),
])

SUMMARY("""
- **Antitrust** (prevent monopoly), **industrial regulation** (prices in selected industries), **social regulation** (production conditions, products, social impact).
- Antitrust issues: **behaviour vs structure (rule of reason)**, **relevant market**; enforcement depends on government (active vs laissez-faire view); effectiveness: mergers (HHI > 1,800), price-fixing illegal, tying banned → **moderately effective**.
- **Natural monopoly:** public ownership or **P = ATC** regulation; problems: inefficiency, perpetuating monopoly, **legal cartel theory**.
- **Deregulation:** removing restrictions, efficiency gains. **Social regulation:** MB = MC; no free lunch.

**Next:** Lecture 13: the **labour market** and how **wages** are determined.
""", """
- **অ্যান্টি-ট্রাস্ট** (একচেটিয়া ঠেকানো), **শিল্প নিয়ন্ত্রণ** (নির্বাচিত শিল্পে দাম), **সামাজিক নিয়ন্ত্রণ** (উৎপাদনের অবস্থা, পণ্য, সামাজিক প্রভাব)।
- অ্যান্টি-ট্রাস্টের সমস্যা: **আচরণ বনাম কাঠামো (যুক্তির নিয়ম)**, **প্রাসঙ্গিক বাজার**; প্রয়োগ সরকারের ওপর নির্ভরশীল (সক্রিয় বনাম লেসে-ফেয়ার); কার্যকারিতা: একীভবন (HHI > ১,৮০০), দাম ঠিক করা অবৈধ, বাঁধা চুক্তি নিষিদ্ধ → **মাঝারি কার্যকর**।
- **প্রাকৃতিক একচেটিয়া:** সরকারি মালিকানা বা **P = ATC** নিয়ন্ত্রণ; সমস্যা: অদক্ষতা, একচেটিয়া স্থায়ী করা, **আইনি কার্টেল তত্ত্ব**।
- **বিনিয়ন্ত্রণ:** বিধিনিষেধ তুলে নেওয়া, দক্ষতা-লাভ। **সামাজিক নিয়ন্ত্রণ:** MB = MC; বিনামূল্যে খাবার নেই।

**পরবর্তী:** লেকচার ১৩: **শ্রমবাজার** ও **মজুরি** কীভাবে নির্ধারিত হয়।
""")
