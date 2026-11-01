MOD(qs=[20, 7])

CONCEPT("""
**Concept:** In Lecture 2 the market economy's weaknesses included "public goods neglected" and "pollution". Lecture 15 names this problem: **market failure** = the market does **not** allocate resources in the way that best satisfies society. It happens through **public goods**, **merit/demerit goods**, **externalities**, **monopoly power**, **inadequate information** and **factor immobility**. Then it shows the solutions: **private bargaining (Coase)** and **government action** (direct controls, taxes, subsidies, provision, pollution permits). This is midterm **Q20**.
""", """
**ধারণা:** লেকচার ২-এ বাজার অর্থনীতির দুর্বলতায় ছিল "জনদ্রব্য অবহেলিত" ও "দূষণ"। লেকচার ১৫ সমস্যাটির নাম দেয়: **বাজার ব্যর্থতা** = বাজার সমাজের সবচেয়ে ভালো চাওয়া মেটানোর মতো করে সম্পদ বণ্টন **করে না**। এটা ঘটে **জনদ্রব্য**, **মেরিট/ডিমেরিট দ্রব্য**, **বাহ্যিকতা**, **একচেটিয়া ক্ষমতা**, **অপর্যাপ্ত তথ্য** ও **উপাদানের অচলতার** মাধ্যমে। তারপর সমাধান দেখায়: **ব্যক্তিগত দর কষাকষি (কোজ)** ও **সরকারি পদক্ষেপ** (সরাসরি নিয়ন্ত্রণ, কর, ভর্তুকি, সরবরাহ, দূষণের অনুমতিপত্র)। এটা মিডটার্ম **Q20**।
""", fig='externality')

WORDS([
    ('Market failure', 'Private markets do not allocate resources in the way that best satisfies society', 'বাজার ব্যর্থতা — বেসরকারি বাজার সমাজের জন্য সর্বোত্তমভাবে সম্পদ বণ্টন করে না', 'Too much pollution, too few street lights.'),
    ('Public good', 'Non-rival and non-excludable good', 'জনদ্রব্য — অপ্রতিদ্বন্দ্বী ও বাদ দেওয়া যায় না এমন দ্রব্য', 'National defence, street lights, flood embankments.'),
    ('Free-rider problem', 'People benefit without paying, so private firms won\'t supply', 'ফ্রি-রাইডার সমস্যা — টাকা না দিয়েই সুবিধা নেওয়া, তাই বেসরকারি ফার্ম সরবরাহ করে না', 'Enjoying a lighthouse without paying.'),
    ('Merit / demerit good', 'Under-consumed beneficial good / over-consumed harmful good', 'মেরিট / ডিমেরিট দ্রব্য — কম ভোগ হওয়া উপকারী / বেশি ভোগ হওয়া ক্ষতিকর পণ্য', 'Vaccines / cigarettes.'),
    ('Externality', 'A cost or benefit to a third party not involved in the transaction', 'বাহ্যিকতা — লেনদেনে জড়িত নয় এমন তৃতীয় পক্ষের ব্যয় বা সুবিধা', 'Factory smoke; a neighbour\'s garden.'),
    ('Social cost', 'Private cost + external cost', 'সামাজিক ব্যয় — ব্যক্তিগত ব্যয় + বাহ্যিক ব্যয়', 'Cost of a brick + cost of its smoke.'),
    ('Asymmetric information', 'One side of a deal knows more than the other', 'অসম তথ্য — লেনদেনের এক পক্ষ অন্যের চেয়ে বেশি জানে', 'A used-car seller knows hidden faults.'),
    ('Coase theorem', 'Private bargaining can solve externalities if property rights are clear, few parties, low bargaining costs', 'কোজ উপপাদ্য — মালিকানা স্পষ্ট, পক্ষ কম, দর কষাকষির খরচ কম হলে ব্যক্তিগত আলোচনায় বাহ্যিকতার সমাধান', 'Two neighbours agree on noise.'),
    ('Pollution permits', 'Tradable rights to emit a fixed amount of pollution', 'দূষণের অনুমতিপত্র — নির্দিষ্ট পরিমাণ দূষণের হস্তান্তরযোগ্য অধিকার', 'Carbon credits.'),
])

SLIDE([1, 2, 3, 4], 'Title and outline', 'শিরোনাম ও রূপরেখা',
    bn=['**স্লাইড ১–৪:** প্রিন্সিপলস অব ইকোনমিক্স — সালিমাহ মুশাররিফ। FPEC 101 – লেকচার ১৫, ইউনিট ২। সরকার ও বাজার ব্যর্থতা। রূপরেখা: বাজার ব্যর্থতা · জনদ্রব্যের সর্বোত্তম পরিমাণ · সরকারের ভূমিকা · বাজারভিত্তিক সমাধান।'],
    ex="""The last lecture for the midterm. Reading: McConnell & Brue pp. 543–559.""",
    exb="""মিডটার্মের শেষ লেকচার। পড়া: ম্যাককনেল ও ব্রু পৃ. ৫৪৩–৫৫৯।""")

SLIDE([5, 6], 'What is market failure? Its forms', 'বাজার ব্যর্থতা কী? এর রূপ',
    bn=['**স্লাইড ৫:** বাজার ব্যর্থতা এমন পরিস্থিতি যেখানে বেসরকারি বাজার সমাজের চাওয়া সবচেয়ে ভালোভাবে মেটানোর মতো সম্পদ বণ্টন আনে না। যেখানে বেসরকারি বাজার ব্যর্থ, সেখানে সরকারের অর্থনৈতিক ভূমিকা আসতে পারে। বাজার ব্যর্থতা ঘটে যখন পণ্যের বাজারদরে বাহ্যিকতার (পণ্যের উৎপাদন, ভোগ বা বণ্টনে ঘটা ক্ষতিকর বা উপকারী পার্শ্বপ্রতিক্রিয়া) ব্যয় বা সুবিধা অন্তর্ভুক্ত থাকে না। তাই বাজার ব্যর্থতার ক্ষেত্রে সরকারি হস্তক্ষেপের প্রয়োজন; সরকার বলতে পারে হস্তক্ষেপ জনস্বার্থে। সহজ কথায়, বাজার সবসময় দুষ্প্রাপ্য সম্পদ এমনভাবে দক্ষতার সাথে বণ্টন করে না যাতে সর্বোচ্চ মোট সামাজিক কল্যাণ হয়।',
        '**স্লাইড ৬:** বাজার ব্যর্থতার রূপ: • জনদ্রব্যের কম সরবরাহ • মেরিট ও ডিমেরিট দ্রব্য • বাহ্যিকতা • অপর্যাপ্ত তথ্য • উপাদানের অচলতা'],
    ex="""**Market failure** = private markets **do not allocate resources** in the way that **best satisfies society's wants** (they do not maximise total social welfare). Often this is because the market price **ignores external costs or benefits** (externalities). Where markets fail, there is a case for **government intervention** "in the public interest".

**Five forms on slide 6** (+ monopoly power, slide 19):
1. Under-provision of **public goods**
2. **Merit and demerit goods**
3. **Externalities**
4. **Inadequate (asymmetric) information**
5. **Factor immobility**""",
    exb="""**বাজার ব্যর্থতা** = বেসরকারি বাজার **সমাজের চাওয়া সবচেয়ে ভালোভাবে মেটানোর** মতো **সম্পদ বণ্টন করে না** (মোট সামাজিক কল্যাণ সর্বোচ্চ করে না)। প্রায়ই কারণ হলো বাজারদর **বাহ্যিক ব্যয় বা সুবিধা উপেক্ষা করে** (বাহ্যিকতা)। বাজার ব্যর্থ হলে "জনস্বার্থে" **সরকারি হস্তক্ষেপের** যুক্তি আসে।

**স্লাইড ৬-এর পাঁচটি রূপ** (+ একচেটিয়া ক্ষমতা, স্লাইড ১৯):
1. **জনদ্রব্যের** কম সরবরাহ
2. **মেরিট ও ডিমেরিট দ্রব্য**
3. **বাহ্যিকতা**
4. **অপর্যাপ্ত (অসম) তথ্য**
5. **উপাদানের অচলতা**""",
    tip="Q20 first lines: the definition + this list. Then explain each form with one example and its government remedy.",
    tipb="Q20-এর প্রথম লাইন: সংজ্ঞা + এই তালিকা। তারপর প্রতিটি রূপ এক উদাহরণ ও সরকারি প্রতিকারসহ ব্যাখ্যা করো।")

SLIDE([7, 8], 'Private goods vs public goods; the free-rider problem', 'ব্যক্তিগত বনাম জনদ্রব্য; ফ্রি-রাইডার সমস্যা',
    bn=['**স্লাইড ৭ — ব্যক্তিগত দ্রব্যের বৈশিষ্ট্য:** **প্রতিদ্বন্দ্বিতা (ভোগে)** মানে একজন কিনে ভোগ করলে তা আরেকজনের কেনা ও ভোগের জন্য থাকে না। **বাদ দেওয়ার যোগ্যতা** মানে বিক্রেতা টাকা না দেওয়া মানুষকে পণ্যের সুবিধা থেকে বাদ রাখতে পারে; শুধু বাজারদর দিতে ইচ্ছুক ও সক্ষমরাই পায়। ভোক্তা ব্যক্তিগত দ্রব্য চায়, মুনাফা-সন্ধানী সরবরাহকারী তা উৎপাদন করে। বাজারদর দিতে রাজিরা পায়; যারা দেয় না তারা পায় না। প্রতিযোগিতামূলক বাজার ব্যক্তিগত দ্রব্য সরবরাহ করে এবং সমাজের সম্পদ দক্ষতার সাথে বণ্টন করে — বেশিও না, কমও না।',
        '**স্লাইড ৮ — জনদ্রব্যের বৈশিষ্ট্য:** **অপ্রতিদ্বন্দ্বিতা (ভোগে)** মানে একজনের ভোগ অন্যদের ভোগে বাধা দেয় না; সবাই একসাথে জনদ্রব্যের সুবিধা পায়, যেমন জাতীয় প্রতিরক্ষা, রাস্তার বাতি। **বাদ দেওয়ার অযোগ্যতা** মানে একবার তৈরি হলে কাউকে সুবিধা থেকে বাদ রাখার কার্যকর উপায় নেই। এগুলো ফ্রি-রাইডার সমস্যা তৈরি করে — জনদ্রব্য একবার সরবরাহ হলে টাকা না দেওয়া মানুষসহ সবাই সুবিধা পায়। জনদ্রব্যের চাহিদা বাজারে প্রকাশ পায় না, তাই বেসরকারি উৎপাদক তা বানায় না, সরকারকে সরবরাহ করতে হয়; সরকার কর দিয়ে অর্থায়ন করতে পারে।'],
    ex="""<div class="tbl"><table><thead><tr><th></th><th>Private good</th><th>Public good</th></tr></thead><tbody>
<tr><td>Rivalry</td><td><b>Rival</b>: if I eat the apple, you can't</td><td><b>Non-rival</b>: my use doesn't reduce yours</td></tr>
<tr><td>Excludability</td><td><b>Excludable</b>: no pay, no product</td><td><b>Non-excludable</b>: can't keep non-payers out</td></tr>
<tr><td>Market result</td><td>Provided efficiently by the market</td><td>Not provided by the market (free riders)</td></tr>
<tr><td>Examples</td><td>Food, clothes, phones</td><td>Defence, street lights, flood embankments, lighthouses</td></tr></tbody></table></div>

**Free-rider problem:** since non-payers cannot be excluded, everyone waits for someone else to pay. Demand is never expressed in the market, so private firms do not produce it, and **government must provide it, financed by taxes**.""",
    exb="""<div class="tbl"><table><thead><tr><th></th><th>ব্যক্তিগত দ্রব্য</th><th>জনদ্রব্য</th></tr></thead><tbody>
<tr><td>প্রতিদ্বন্দ্বিতা</td><td><b>প্রতিদ্বন্দ্বী</b>: আমি আপেল খেলে তুমি পারবে না</td><td><b>অপ্রতিদ্বন্দ্বী</b>: আমার ব্যবহারে তোমারটা কমে না</td></tr>
<tr><td>বাদ দেওয়ার যোগ্যতা</td><td><b>বাদ দেওয়া যায়</b>: টাকা নেই তো পণ্য নেই</td><td><b>বাদ দেওয়া যায় না</b>: টাকা না দেওয়াদের ঠেকানো যায় না</td></tr>
<tr><td>বাজারের ফল</td><td>বাজার দক্ষভাবে সরবরাহ করে</td><td>বাজার সরবরাহ করে না (ফ্রি-রাইডার)</td></tr>
<tr><td>উদাহরণ</td><td>খাবার, কাপড়, ফোন</td><td>প্রতিরক্ষা, রাস্তার বাতি, বন্যার বাঁধ, বাতিঘর</td></tr></tbody></table></div>

**ফ্রি-রাইডার সমস্যা:** টাকা না দেওয়াদের বাদ দেওয়া যায় না বলে সবাই অন্য কারো টাকা দেওয়ার অপেক্ষা করে। চাহিদা বাজারে প্রকাশ পায় না, তাই বেসরকারি ফার্ম বানায় না, আর **সরকারকে করের টাকায় সরবরাহ করতে হয়**।""",
    eg="""A coastal embankment protects every household behind it, whether or not they paid. No private company could collect money from all of them, so the Bangladesh Water Development Board builds embankments with tax money.""",
    egb="""উপকূলীয় বাঁধ পেছনের প্রতিটি পরিবারকে রক্ষা করে, টাকা দিক বা না দিক। কোনো বেসরকারি কোম্পানি সবার কাছ থেকে টাকা তুলতে পারবে না, তাই বাংলাদেশ পানি উন্নয়ন বোর্ড করের টাকায় বাঁধ বানায়।""")

SLIDE([9, 10, 11, 12], 'The optimal amount of a public good; cost-benefit analysis', 'জনদ্রব্যের সর্বোত্তম পরিমাণ; ব্যয়-সুবিধা বিশ্লেষণ',
    bn=['**স্লাইড ৯ ও ১১:** [চিত্র: জনদ্রব্যের সর্বোত্তম পরিমাণ — খাড়াভাবে যোগ করা ব্যক্তিগত চাহিদা (প্রান্তিক সুবিধা) ও S (দ্রব্যের প্রান্তিক ব্যয়); সর্বোত্তম পরিমাণ যেখানে প্রান্তিক সুবিধা = প্রান্তিক ব্যয়]',
        '**স্লাইড ১০:** জনদ্রব্যের চাহিদা — প্রান্তিক সুবিধা। ক্রমহ্রাসমান প্রান্তিক উপযোগের কারণে পরপর এককগুলো ক্রমশ কম বাড়তি সুবিধা দেয়, তাই নিম্নমুখী। দিতে-ইচ্ছুকতার সূচি দিয়ে দেখানো হয়। প্রতিটি দামে চাহিদার পরিমাণ যোগ না করে, প্রতিটি সম্ভাব্য পরিমাণে শেষ এককের জন্য মানুষ যে দাম দিতে রাজি তা যোগ করা হয়। ব্যক্তিগত চাহিদা রেখা খাড়াভাবে যোগ করে জনদ্রব্যের সম্মিলিত চাহিদা পাওয়া যায়। জনদ্রব্যের যোগান — প্রান্তিক ব্যয়। ব্যক্তিগত বা জনদ্রব্য, যেকোনো দ্রব্যের যোগান রেখা হলো তার প্রান্তিক ব্যয় (MC) রেখা। বেশি উৎপাদনে প্রান্তিক ব্যয় বাড়ে — ক্রমহ্রাসমান প্রতিদানের নিয়মে।',
        '**স্লাইড ১২ — ব্যয়-সুবিধা বিশ্লেষণ:** দুষ্প্রাপ্যতার কারণে সরকারি খাতে বেশি সম্পদ মানে বেসরকারি খাতে কম — সুযোগ ব্যয়, আবার সুবিধাও। ব্যয় হলো ব্যক্তিগত দ্রব্যের উৎপাদন কমায় তৃপ্তির ক্ষতি; সুবিধা হলো বেশি জনদ্রব্যের বাড়তি তৃপ্তি। প্রয়োজনীয় সম্পদ কি বেসরকারি থেকে সরকারি খাতে সরানো উচিত? বাড়তি জনদ্রব্যের সুবিধা কম ব্যক্তিগত দ্রব্যের ব্যয়ের চেয়ে বেশি হলে হ্যাঁ: MB > MC। ছেড়ে দেওয়া ব্যক্তিগত দ্রব্যের ব্যয় বাড়তি জনদ্রব্যের সুবিধার চেয়ে বেশি হলে না: MC > MB।'],
    ex="""How much of a public good should the government provide?

- **Demand = marginal benefit (MB):** downward-sloping (diminishing marginal utility). Because everyone consumes the **same** quantity, we add individuals' **willingness to pay** **vertically** (not horizontally as for private goods).
- **Supply = marginal cost (MC):** upward-sloping (diminishing returns).
- **Optimal amount: MB = MC.**

**Cost-benefit analysis:** resources used for public goods are taken from private goods (opportunity cost). Provide **more** if **MB > MC**; **stop** where MB = MC; provide **less** if **MC > MB**.""",
    exb="""সরকার কতটা জনদ্রব্য সরবরাহ করবে?

- **চাহিদা = প্রান্তিক সুবিধা (MB):** নিম্নমুখী (ক্রমহ্রাসমান প্রান্তিক উপযোগ)। সবাই **একই** পরিমাণ ভোগ করে বলে ব্যক্তিদের **দিতে-ইচ্ছুকতা** **খাড়াভাবে** যোগ করা হয় (ব্যক্তিগত দ্রব্যের মতো আনুভূমিকভাবে নয়)।
- **যোগান = প্রান্তিক ব্যয় (MC):** ঊর্ধ্বমুখী (ক্রমহ্রাসমান প্রতিদান)।
- **সর্বোত্তম পরিমাণ: MB = MC।**

**ব্যয়-সুবিধা বিশ্লেষণ:** জনদ্রব্যে ব্যবহৃত সম্পদ ব্যক্তিগত দ্রব্য থেকে আসে (সুযোগ ব্যয়)। **MB > MC** হলে **বেশি** দাও; MB = MC-তে **থামো**; **MC > MB** হলে **কম** দাও।""",
    eg="""Should Dhaka build one more flyover? If the extra benefit (time saved, less pollution) is Tk 900 crore and the cost (including the hospitals or schools that money could have built) is Tk 700 crore, MB > MC: build it.""",
    egb="""ঢাকায় আরেকটি ফ্লাইওভার বানানো উচিত? বাড়তি সুবিধা (সময় বাঁচা, কম দূষণ) ৯০০ কোটি টাকা আর ব্যয় (ওই টাকায় যে হাসপাতাল বা স্কুল হতে পারত তাসহ) ৭০০ কোটি হলে MB > MC: বানাও।""")

SLIDE(13, 'Merit and demerit goods', 'মেরিট ও ডিমেরিট দ্রব্য',
    bn=['মেরিট বনাম ডিমেরিট দ্রব্য', '**মেরিট দ্রব্য:** সামাজিকভাবে কাম্য কিন্তু বাজার প্রক্রিয়ার হাতে ছাড়লে কম সরবরাহ/কম ভোগ হয় — মানুষ এগুলো থেকে প্রাপ্ত পূর্ণ ব্যক্তিগত সুবিধা সম্পর্কে তথ্যের অভাবে থাকে (সাধারণত দীর্ঘমেয়াদি), ফলে কম ভোগ করে।',
        '**ডিমেরিট দ্রব্য:** সামাজিকভাবে অকাম্য কিন্তু বাজার প্রক্রিয়ার হাতে ছাড়লে বেশি সরবরাহ/বেশি ভোগ হয় — মানুষ এগুলো ভোগের পূর্ণ ব্যক্তিগত ব্যয় সম্পর্কে তথ্যের অভাবে থাকে (সাধারণত দীর্ঘমেয়াদি), ফলে বেশি ভোগ করে।'],
    ex="""Both come from **people not knowing the full long-term effects**:

- **Merit goods** (education, vaccines, health check-ups, seat belts): people underestimate the **benefits**, so they consume **too little**. Remedy: subsidies, free provision, compulsion (compulsory primary education, EPI vaccination).
- **Demerit goods** (cigarettes, drugs, alcohol, junk food): people underestimate the **costs**, so they consume **too much**. Remedy: taxes, bans, warnings (graphic health warnings on cigarette packs).""",
    exb="""দুটোই আসে **মানুষ দীর্ঘমেয়াদি পূর্ণ প্রভাব না জানায়**:

- **মেরিট দ্রব্য** (শিক্ষা, টিকা, স্বাস্থ্য পরীক্ষা, সিটবেল্ট): মানুষ **সুবিধা** কম মনে করে, তাই **খুব কম** ভোগ করে। প্রতিকার: ভর্তুকি, বিনামূল্যে সরবরাহ, বাধ্যতামূলক করা (বাধ্যতামূলক প্রাথমিক শিক্ষা, ইপিআই টিকা)।
- **ডিমেরিট দ্রব্য** (সিগারেট, মাদক, অ্যালকোহল, জাংক ফুড): মানুষ **ব্যয়** কম মনে করে, তাই **খুব বেশি** ভোগ করে। প্রতিকার: কর, নিষেধাজ্ঞা, সতর্কবার্তা (সিগারেটের প্যাকেটে ছবিসহ স্বাস্থ্য সতর্কবার্তা)।""")

SLIDE([14, 15, 16], 'Externalities: negative and positive', 'বাহ্যিকতা: নেতিবাচক ও ইতিবাচক',
    bn=['**স্লাইড ১৪ — বাহ্যিকতা:** উপচে পড়া প্রভাব — লেনদেনে সরাসরি জড়িত নয় এমন ব্যক্তি বা গোষ্ঠীর (তৃতীয় পক্ষ) ব্যয় বা সুবিধা। ভোগ ও উৎপাদনের বাহ্যিকতা। নেতিবাচক বাহ্যিকতা — বাহ্যিক ব্যয় — পণ্যে অতিরিক্ত উৎপাদন ও সম্পদের অতিরিক্ত বণ্টন। ইতিবাচক বাহ্যিকতা — বাহ্যিক সুবিধা — কম উৎপাদন ও কম বণ্টন। সামাজিক ব্যয় = ব্যক্তিগত ব্যয় + বাহ্যিক ব্যয়। উৎপাদনে নেতিবাচক বাহ্যিকতা: সামাজিক ব্যয় (MSC) > ব্যক্তিগত ব্যয় (MPC); ভোগে নেতিবাচক: ব্যক্তিগত সুবিধা (MPB) > সামাজিক সুবিধা (MSB)। উৎপাদনে ইতিবাচক: MSC < MPC; ভোগে ইতিবাচক: সামাজিক সুবিধা > ব্যক্তিগত সুবিধা।',
        '**স্লাইড ১৫ — নেতিবাচক বাহ্যিকতা:** উৎপাদক কিছু ব্যয় সমাজের ঘাড়ে বাহ্যিক ব্যয় হিসেবে চাপালে তাদের প্রান্তিক ব্যয় কম দেখায়; তাই যোগান রেখায় সব প্রকৃত ব্যয় ধরা থাকে না। ভারসাম্য উৎপাদন Qe সর্বোত্তম Qo-র চেয়ে বেশি। পণ্যে সম্পদ অতিরিক্ত বণ্টিত; অনেক বেশি একক উৎপাদিত।',
        '**স্লাইড ১৬ — ইতিবাচক বাহ্যিকতা:** D-তে পণ্যের বাহ্যিক সুবিধা নেই, Dt-তে আছে। ফলে ভারসাম্য উৎপাদন Qe সর্বোত্তম Qo-র চেয়ে কম। পণ্যে সম্পদ কম বণ্টিত।'],
    fig='externality',
    ex="""**Externality** = a **spillover** cost or benefit to a **third party** who is not part of the deal.

- **Negative externality (external cost):** e.g. factory pollution. **Social cost = private cost + external cost**, so **MSC > MPC**. The market supply S ignores the external cost → output **Qe > Qo**: **overproduction**, too many resources.
- **Positive externality (external benefit):** e.g. vaccination protects others too, education benefits society. **Social benefit > private benefit**. Market demand D ignores it → output **Qe < Qo**: **underproduction**.""",
    exb="""**বাহ্যিকতা** = লেনদেনে জড়িত নয় এমন **তৃতীয় পক্ষের** ওপর **উপচে পড়া** ব্যয় বা সুবিধা।

- **নেতিবাচক বাহ্যিকতা (বাহ্যিক ব্যয়):** যেমন কারখানার দূষণ। **সামাজিক ব্যয় = ব্যক্তিগত ব্যয় + বাহ্যিক ব্যয়**, তাই **MSC > MPC**। বাজারের যোগান S বাহ্যিক ব্যয় উপেক্ষা করে → উৎপাদন **Qe > Qo**: **অতিরিক্ত উৎপাদন**, বেশি সম্পদ।
- **ইতিবাচক বাহ্যিকতা (বাহ্যিক সুবিধা):** যেমন টিকা অন্যদেরও রক্ষা করে, শিক্ষা সমাজের উপকার করে। **সামাজিক সুবিধা > ব্যক্তিগত সুবিধা**। বাজারের চাহিদা D তা উপেক্ষা করে → উৎপাদন **Qe < Qo**: **কম উৎপাদন**।""",
    eg="""**Negative:** tanneries and dyeing factories polluting the Buriganga; brick kilns' smoke around Dhaka. **Positive:** a family planting trees (cleaner air for neighbours); a girl's education (healthier families, lower child mortality).""",
    egb="""**নেতিবাচক:** বুড়িগঙ্গা দূষণকারী ট্যানারি ও ডাইং কারখানা; ঢাকার চারপাশে ইটভাটার ধোঁয়া। **ইতিবাচক:** কোনো পরিবারের গাছ লাগানো (প্রতিবেশীর জন্য পরিষ্কার বাতাস); মেয়ের শিক্ষা (স্বাস্থ্যকর পরিবার, শিশুমৃত্যু কম)।""",
    tip="In Q20 draw both externality diagrams and write: negative → overproduction (Qe > Qo); positive → underproduction (Qe < Qo).",
    tipb="Q20-এ দুটি বাহ্যিকতার চিত্র আঁকো ও লেখো: নেতিবাচক → অতিরিক্ত উৎপাদন (Qe > Qo); ইতিবাচক → কম উৎপাদন (Qe < Qo)।")

SLIDE([17, 18], 'Correcting externalities', 'বাহ্যিকতা সংশোধন',
    bn=['**স্লাইড ১৭ — নেতিবাচক বাহ্যিকতা সংশোধন:** নেতিবাচক বাহ্যিকতায় সম্পদের অতিরিক্ত বণ্টন হয়। সরকার দুইভাবে তা ঠিক করতে পারে: ১) সরাসরি নিয়ন্ত্রণ, যা যোগান রেখা S থেকে St-তে সরিয়ে উৎপাদন Qe থেকে Qo-তে কমায়; ২) নির্দিষ্ট কর T আরোপ, যাও যোগান রেখা S থেকে St-তে সরিয়ে অতিরিক্ত বণ্টন দূর করে।',
        '**স্লাইড ১৮ — ইতিবাচক বাহ্যিকতা সংশোধন:** ইতিবাচক বাহ্যিকতায় সম্পদের কম বণ্টন হয়। ভোক্তাকে ভর্তুকি দিয়ে তা ঠিক করা যায়, যা বাজার চাহিদা D থেকে Dt-তে সরিয়ে উৎপাদন Qe থেকে Qo-তে বাড়ায়। বিকল্পভাবে উৎপাদককে U ভর্তুকি দিয়ে যোগান রেখা St থেকে St′-তে সরিয়ে উৎপাদন Qe থেকে Qo-তে বাড়িয়ে কম বণ্টন দূর করা যায়।'],
    ex="""**Negative externality (too much):** make the polluter **pay the full cost** so supply shifts **left** (S → St) and output falls from Qe to Qo:
1. **Direct controls** (e.g. emission limits, requiring filters), or
2. A **specific tax** per unit (a "Pigouvian" tax equal to the external cost).

**Positive externality (too little):** encourage more output so it rises from Qe to Qo:
1. **Subsidy to consumers** → demand shifts right (D → Dt), or
2. **Subsidy to producers** → supply shifts right, or
3. **Government provides it directly** (slide 25).""",
    exb="""**নেতিবাচক বাহ্যিকতা (খুব বেশি):** দূষণকারীকে **পূর্ণ ব্যয় দিতে** বাধ্য করো, যাতে যোগান **বাঁয়ে** সরে (S → St) আর উৎপাদন Qe থেকে Qo-তে নামে:
1. **সরাসরি নিয়ন্ত্রণ** (যেমন নির্গমনের সীমা, ফিল্টার বাধ্যতামূলক), অথবা
2. এককপ্রতি **নির্দিষ্ট কর** (বাহ্যিক ব্যয়ের সমান "পিগুভিয়ান" কর)।

**ইতিবাচক বাহ্যিকতা (খুব কম):** উৎপাদন বাড়াতে উৎসাহ দাও, যাতে Qe থেকে Qo-তে ওঠে:
1. **ভোক্তাকে ভর্তুকি** → চাহিদা ডানে সরে (D → Dt), অথবা
2. **উৎপাদককে ভর্তুকি** → যোগান ডানে সরে, অথবা
3. **সরকারের সরাসরি সরবরাহ** (স্লাইড ২৫)।""")

SLIDE(19, 'Monopoly power as a market failure', 'বাজার ব্যর্থতা হিসেবে একচেটিয়া ক্ষমতা',
    bn=['• দাম নির্ধারণে ক্ষমতা, অর্থাৎ দাম নির্ধারক', '• খরচ কম রাখার প্রণোদনা কম', '• বিকল্প কম বা নেই — ভোক্তার পছন্দ সীমিত করতে পারে, যেমন পণ্যের খুচরা বিক্রেতার সংখ্যা সীমিত করা', '• প্রবেশ/প্রস্থানে উচ্চ বাধা'],
    ex="""This slide lists **monopoly power** as another source of market failure (Lectures 9–12):
- the firm is a **price maker** (P > MC → too little output);
- **little incentive to keep costs low** (X-inefficiency);
- **few or no substitutes**, so consumer choice is restricted (e.g. limiting which retailers may sell the good);
- **high barriers to entry and exit**.

Remedy: competition policy and regulation (Lecture 12).""",
    exb="""এই স্লাইড **একচেটিয়া ক্ষমতাকে** বাজার ব্যর্থতার আরেক উৎস হিসেবে তালিকাভুক্ত করে (লেকচার ৯–১২):
- ফার্ম **দাম নির্ধারক** (P > MC → খুব কম উৎপাদন);
- **খরচ কম রাখার প্রণোদনা কম** (X-অদক্ষতা);
- **বিকল্প কম বা নেই**, তাই ভোক্তার পছন্দ সীমিত (যেমন কোন খুচরা বিক্রেতা পণ্যটি বেচবে তা সীমিত করা);
- **প্রবেশ ও প্রস্থানে উচ্চ বাধা**।

প্রতিকার: প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ (লেকচার ১২)।""")

SLIDE([20, 21], 'Information failure and factor immobility', 'তথ্যের ব্যর্থতা ও উপাদানের অচলতা',
    bn=['**স্লাইড ২০ — অপর্যাপ্ত তথ্য — অসম তথ্য:** ক্রেতা বা বিক্রেতার মধ্যে উপযুক্ত তথ্যের অভাবেও বাজার ব্যর্থতা হতে পারে। এর মানে চাহিদা বা যোগানের দাম পণ্যের সব সুবিধা বা সুযোগ ব্যয় প্রতিফলিত করে না। অন্যদিকে বিক্রেতার অপর্যাপ্ত তথ্যে সে পণ্যের প্রকৃত সুযোগ ব্যয়ের চেয়ে বেশি বা কম দাম মেনে নিতে পারে। লেনদেনের এক পক্ষ (ক্রেতা বা বিক্রেতা) অন্যের চেয়ে বেশি তথ্য পায়, ফলে সম্পদের ভুল বণ্টন। এক পক্ষের বেশি তথ্য প্রায়ই "বিরূপ নির্বাচন" আনে (অজ্ঞ পক্ষ প্রায়ই পণ্য/সেবার জন্য খুব বেশি বা খুব কম দাম দেয়)।',
        '**স্লাইড ২১ — উপাদানের অচলতা:** পেশাগত — অন্য কাজের দক্ষতা (ও জ্ঞানের) অভাব, যেমন জাহাজ নির্মাতা আইটির কাজ করার চেষ্টা করছে। ভৌগোলিক — আর্থিক খরচ (বন্ধক ইত্যাদি)/ পরিবার। দুটোই "বাজার ব্যর্থতা" — শ্রমিক কম ব্যবহৃত হয়।'],
    ex="""**Asymmetric information:** one side knows more than the other, so prices do not reflect true benefits and costs:
- Buyers may pay **too much** for poor quality (a used phone with hidden faults, adulterated food, fake medicine).
- This leads to **adverse selection**: the uninformed side pays the wrong price, and good-quality sellers may leave the market.
Remedies: quality standards (BSTI), labelling, licensing, consumer-rights laws.

**Factor immobility:** resources cannot move to where they are most needed:
- **Occupational:** lack of skills for other jobs (a shipbuilder cannot become an IT worker overnight).
- **Geographical:** cost of moving, housing, family ties.
Both leave workers **under-used** (unemployment), a market failure. Remedies: training, relocation support.""",
    exb="""**অসম তথ্য:** এক পক্ষ অন্যের চেয়ে বেশি জানে, তাই দাম প্রকৃত সুবিধা ও ব্যয় প্রতিফলিত করে না:
- ক্রেতা নিম্নমানের জিনিসে **খুব বেশি** দিতে পারে (লুকানো ত্রুটির পুরোনো ফোন, ভেজাল খাবার, নকল ওষুধ)।
- এতে **বিরূপ নির্বাচন** হয়: অজ্ঞ পক্ষ ভুল দাম দেয়, আর ভালো মানের বিক্রেতা বাজার ছাড়তে পারে।
প্রতিকার: মানদণ্ড (বিএসটিআই), লেবেল, লাইসেন্স, ভোক্তা অধিকার আইন।

**উপাদানের অচলতা:** সম্পদ যেখানে সবচেয়ে দরকার সেখানে যেতে পারে না:
- **পেশাগত:** অন্য কাজের দক্ষতার অভাব (জাহাজ নির্মাতা রাতারাতি আইটি কর্মী হতে পারেন না)।
- **ভৌগোলিক:** সরে যাওয়ার খরচ, বাসস্থান, পারিবারিক বন্ধন।
দুটোই শ্রমিককে **কম ব্যবহৃত** রাখে (বেকারত্ব), এটা বাজার ব্যর্থতা। প্রতিকার: প্রশিক্ষণ, স্থানান্তরে সহায়তা।""")

SLIDE(22, 'Non-government correction: Coase theorem and liability', 'সরকারবহির্ভূত সংশোধন: কোজ উপপাদ্য ও দায়',
    bn=['সরকারবহির্ভূত হস্তক্ষেপ — সংশোধন', '**ব্যক্তিগত দর কষাকষি — কোজ উপপাদ্য**', 'বাহ্যিক ব্যয় বা সুবিধা প্রতিকারে সরকার দরকার নেই যেখানে — • সম্পত্তির মালিকানা স্পষ্টভাবে সংজ্ঞায়িত • জড়িত মানুষের সংখ্যা কম • দর কষাকষির খরচ নগণ্য।',
        'এ অবস্থায় সরকারের ভূমিকা ক্ষতিগ্রস্ত ব্যক্তি বা গোষ্ঠীর মধ্যে দর কষাকষিতে উৎসাহ দেওয়ায় সীমিত রাখা উচিত।', 'দুর্ভাগ্যবশত অনেক বাহ্যিকতায় অনেক পক্ষ জড়িত, দর কষাকষির খরচ বেশি, আর বাতাস-পানির মতো সম্মিলিত সম্পত্তি। এসব ক্ষেত্রে ব্যক্তিগত দর কষাকষি প্রতিকার হতে পারে না।',
        'স্পষ্ট সম্পত্তির অধিকার ও সরকারি দায় আইন কিছু বাহ্যিকতার সমস্যায় প্রতিকার দেয় — • সরাসরি, ক্ষতিকর বাহ্যিকতা সৃষ্টিকারীকে ক্ষতিগ্রস্তদের ক্ষতিপূরণ দিতে বাধ্য করে • পরোক্ষভাবে, মামলার ভয়ে ফার্ম ও ব্যক্তিকে নেতিবাচক বাহ্যিকতা তৈরিতে নিরুৎসাহিত করে।'],
    ex="""**Coase theorem:** the government is **not needed** to fix an externality if (1) **property rights are clearly defined**, (2) **few people** are involved, and (3) **bargaining costs are small**. The parties will negotiate a solution themselves; the government should just encourage bargaining.

**Limits:** most big externalities (air and river pollution) involve **many people**, **high bargaining costs** and **common property**, so bargaining fails.

**Liability laws** help: polluters can be **sued for damages** (direct), and the fear of lawsuits **discourages** harmful behaviour (indirect).""",
    exb="""**কোজ উপপাদ্য:** বাহ্যিকতা ঠিক করতে সরকার **দরকার নেই** যদি (১) **সম্পত্তির অধিকার স্পষ্ট**, (২) **কম মানুষ** জড়িত, এবং (৩) **দর কষাকষির খরচ কম**। পক্ষগুলো নিজেরাই সমাধানে আসবে; সরকারের শুধু দর কষাকষিতে উৎসাহ দেওয়া উচিত।

**সীমা:** বেশিরভাগ বড় বাহ্যিকতায় (বায়ু ও নদী দূষণ) **অনেক মানুষ**, **উচ্চ দর কষাকষির খরচ** ও **সম্মিলিত সম্পত্তি**, তাই দর কষাকষি ব্যর্থ হয়।

**দায় আইন** সাহায্য করে: দূষণকারীর বিরুদ্ধে **ক্ষতিপূরণের মামলা** করা যায় (সরাসরি), আর মামলার ভয় ক্ষতিকর আচরণ **নিরুৎসাহিত** করে (পরোক্ষ)।""",
    eg="""Two neighbours in a Dhaka apartment: one plays loud music at night. Ownership is clear and only two people are involved, so they can agree (e.g. music off after 10 pm) without the government. But thousands of people breathing brick-kiln smoke cannot bargain with every kiln: government must act.""",
    egb="""ঢাকার এক অ্যাপার্টমেন্টে দুই প্রতিবেশী: একজন রাতে জোরে গান বাজান। মালিকানা স্পষ্ট, মাত্র দুজন জড়িত, তাই সরকার ছাড়াই একমত হতে পারেন (যেমন রাত ১০টার পর গান বন্ধ)। কিন্তু ইটভাটার ধোঁয়া নেওয়া হাজারো মানুষ প্রতিটি ভাটার সাথে দর কষতে পারে না: সরকারকে পদক্ষেপ নিতে হয়।""")

SLIDE([23, 24, 25], 'Government intervention: direct controls, taxes, subsidies, provision', 'সরকারি হস্তক্ষেপ: সরাসরি নিয়ন্ত্রণ, কর, ভর্তুকি, সরবরাহ',
    bn=['**স্লাইড ২৩ — সরাসরি নিয়ন্ত্রণ:** কার্যক্রম সীমিত করার আইন। এমন সরাসরি নিয়ন্ত্রণ অপরাধী ফার্মকে ক্ষতিকর কার্যক্রমের প্রকৃত খরচ বহনে বাধ্য করে। ঐতিহাসিকভাবে অভিন্ন নির্গমন মানদণ্ড — অনুমোদিত দূষণের সীমা — এভাবে ব্যবহৃত হয়েছে। সরাসরি নিয়ন্ত্রণ উৎপাদনের প্রান্তিক ব্যয় বাড়ায়, কারণ ফার্মকে দূষণ নিয়ন্ত্রণ যন্ত্র চালাতে ও রক্ষণাবেক্ষণ করতে হয়। ভারসাম্য দাম বাড়ে, উৎপাদন কমে। অতিরিক্ত বণ্টন সংশোধন হয়।',
        '**স্লাইড ২৪ — নির্দিষ্ট কর:** উৎপাদককে ঠিক করতে হয় কর দেবে নাকি বিকল্প পণ্য কিনতে বা বানাতে বাড়তি খরচ করবে। কর উৎপাদনের প্রান্তিক ব্যয় বাড়িয়ে পণ্যের ব্যক্তিগত যোগান রেখা বাঁয়ে সরায়। ভারসাম্য দাম বাড়ে, উৎপাদন কমে। কর প্রাথমিক অতিরিক্ত বণ্টন দূর করে।',
        '**স্লাইড ২৫ — ভর্তুকি ও সরকারি সরবরাহ:** উৎপাদককে ভর্তুকি — যোগান বাড়ে, প্রান্তিক ব্যয় কমে, উৎপাদন বাড়ে, কম বণ্টন দূর হয়। ভোক্তাকে ভর্তুকি — চাহিদা বাড়ে, দাম কমে, উৎপাদন বাড়ে, কম বণ্টন দূর হয়। সরাসরি সরবরাহ — পণ্যটি জনদ্রব্য হিসেবে সরাসরি সরবরাহ।'],
    ex="""<div class="tbl"><table><thead><tr><th>Tool</th><th>Used for</th><th>Effect</th><th>Example (Bangladesh)</th></tr></thead><tbody>
<tr><td>Direct controls (laws, emission standards)</td><td>Negative externalities</td><td>MC ↑, price ↑, output ↓ to Qo</td><td>Banning polythene bags; brick-kiln rules; mandatory effluent treatment plants (ETPs)</td></tr>
<tr><td>Specific tax</td><td>Negative externalities, demerit goods</td><td>Supply shifts left, price ↑, output ↓</td><td>High supplementary duty on cigarettes</td></tr>
<tr><td>Subsidy to producers</td><td>Positive externalities, merit goods</td><td>Supply ↑, MC ↓, output ↑</td><td>Fertiliser subsidy; solar-home-system support</td></tr>
<tr><td>Subsidy to consumers</td><td>Positive externalities, merit goods</td><td>Demand ↑, output ↑</td><td>Stipends for schoolgirls</td></tr>
<tr><td>Direct provision</td><td>Public goods, merit goods</td><td>Government supplies it</td><td>Free primary schools, EPI vaccines, roads, embankments</td></tr></tbody></table></div>""",
    exb="""<div class="tbl"><table><thead><tr><th>হাতিয়ার</th><th>কিসের জন্য</th><th>প্রভাব</th><th>উদাহরণ (বাংলাদেশ)</th></tr></thead><tbody>
<tr><td>সরাসরি নিয়ন্ত্রণ (আইন, নির্গমন মানদণ্ড)</td><td>নেতিবাচক বাহ্যিকতা</td><td>MC ↑, দাম ↑, উৎপাদন ↓ Qo পর্যন্ত</td><td>পলিথিন নিষিদ্ধ; ইটভাটার নিয়ম; বাধ্যতামূলক বর্জ্য শোধনাগার (ইটিপি)</td></tr>
<tr><td>নির্দিষ্ট কর</td><td>নেতিবাচক বাহ্যিকতা, ডিমেরিট দ্রব্য</td><td>যোগান বাঁয়ে, দাম ↑, উৎপাদন ↓</td><td>সিগারেটে উচ্চ সম্পূরক শুল্ক</td></tr>
<tr><td>উৎপাদককে ভর্তুকি</td><td>ইতিবাচক বাহ্যিকতা, মেরিট দ্রব্য</td><td>যোগান ↑, MC ↓, উৎপাদন ↑</td><td>সারে ভর্তুকি; সোলার হোম সিস্টেমে সহায়তা</td></tr>
<tr><td>ভোক্তাকে ভর্তুকি</td><td>ইতিবাচক বাহ্যিকতা, মেরিট দ্রব্য</td><td>চাহিদা ↑, উৎপাদন ↑</td><td>স্কুলছাত্রীদের উপবৃত্তি</td></tr>
<tr><td>সরাসরি সরবরাহ</td><td>জনদ্রব্য, মেরিট দ্রব্য</td><td>সরকার সরবরাহ করে</td><td>বিনামূল্যে প্রাথমিক বিদ্যালয়, ইপিআই টিকা, রাস্তা, বাঁধ</td></tr></tbody></table></div>""",
    tip="This table is the \"how does the government regulate it\" half of Q20. Learn one Bangladesh example per tool.",
    tipb="এই ছকই Q20-এর \"সরকার কীভাবে নিয়ন্ত্রণ করে\" অর্ধেক। প্রতিটি হাতিয়ারের একটি বাংলাদেশি উদাহরণ শেখো।")

SLIDE(26, 'Market-based approach: pollution permits', 'বাজারভিত্তিক পদ্ধতি: দূষণের অনুমতিপত্র',
    bn=['নেতিবাচক বাহ্যিকতায় বাজারভিত্তিক পদ্ধতি', 'দূষণের অনুমতিপত্র', 'দূষণের নির্দিষ্ট সীমা', 'অনুমতিপত্র না থাকলে দূষণ অনেক বেশি হতো এবং তা সমাজের ওপর পুরো অপরিশোধিত খরচ হতো',
        'অনুমতিপত্র থাকলে দূষণের চাহিদা বাড়লে (উৎপাদনের প্রয়োজন বাড়লে) অনুমতিপত্রের দাম বাড়ে।', 'সমাজের খরচ ফার্মের ভেতরে অন্তর্ভুক্ত হয়', 'ফার্মগুলো অনুমতিপত্র কেনাবেচা করতে পারে, কিন্তু দূষণ-অধিকারের (অনুমতিপত্রের) যোগান পূর্ণ অস্থিতিস্থাপক'],
    ex="""**Pollution permits (cap and trade):**
1. The government sets a **fixed limit (cap)** on total pollution and issues that many **permits**; the supply of permits is **perfectly inelastic** (vertical).
2. Firms must hold a permit for each unit they pollute, and can **buy and sell** permits.
3. As demand to pollute rises (more production), the **price of permits rises**.

**Why it works:** pollution is limited to the cap, and each firm now pays for its pollution, so the **social cost is internalised**. Firms that can cut pollution cheaply do so and sell spare permits; the pollution is reduced at the **lowest total cost**.""",
    exb="""**দূষণের অনুমতিপত্র (ক্যাপ অ্যান্ড ট্রেড):**
1. সরকার মোট দূষণের **নির্দিষ্ট সীমা (ক্যাপ)** ঠিক করে ঠিক ততগুলো **অনুমতিপত্র** দেয়; অনুমতিপত্রের যোগান **পূর্ণ অস্থিতিস্থাপক** (খাড়া)।
2. ফার্মকে প্রতিটি দূষণ এককের জন্য অনুমতিপত্র রাখতে হয়, আর অনুমতিপত্র **কেনাবেচা** করা যায়।
3. দূষণের চাহিদা বাড়লে (বেশি উৎপাদন), **অনুমতিপত্রের দাম বাড়ে**।

**কেন কাজ করে:** দূষণ সীমার মধ্যে থাকে, আর প্রতিটি ফার্ম এখন নিজের দূষণের দাম দেয়, তাই **সামাজিক ব্যয় অন্তর্ভুক্ত** হয়। যে ফার্ম সস্তায় দূষণ কমাতে পারে সে কমায় ও বাড়তি অনুমতিপত্র বেচে; ফলে **সবচেয়ে কম মোট খরচে** দূষণ কমে।""",
    eg="""The EU Emissions Trading System and carbon-credit markets work this way. Bangladesh benefits from carbon-credit projects such as solar home systems and improved cook stoves.""",
    egb="""ইইউ নির্গমন বাণিজ্য ব্যবস্থা ও কার্বন ক্রেডিট বাজার এভাবে কাজ করে। সোলার হোম সিস্টেম ও উন্নত চুলার মতো কার্বন ক্রেডিট প্রকল্পে বাংলাদেশ লাভবান হয়।""")

SLIDE(27, 'Summary of Lecture 15', 'লেকচার ১৫-এর সারসংক্ষেপ',
    bn=['সারসংক্ষেপ', 'বাজার ব্যর্থতা · ব্যক্তিগত বনাম জনদ্রব্য (জনদ্রব্যের সর্বোত্তম পরিমাণ, চাহিদা, যোগান, ব্যয়-সুবিধা বিশ্লেষণ, কম ভোগ ও সরবরাহ) · ডিমেরিট দ্রব্য (বেশি ভোগ ও সরবরাহ) · বাহ্যিকতা (নেতিবাচক, ইতিবাচক, সংশোধন) · তথ্যের ব্যর্থতা · উপাদানের অচলতা · সরকারবহির্ভূত হস্তক্ষেপ (ব্যক্তিগত দর কষাকষি — কোজ উপপাদ্য) · সরকারি হস্তক্ষেপ (সরাসরি নিয়ন্ত্রণ, নির্দিষ্ট কর, ভর্তুকি ও সরকারি সরবরাহ) · নেতিবাচক বাহ্যিকতায় বাজারভিত্তিক পদ্ধতি'],
    ex="""The summary is the plan for **Q20**: define market failure → forms (public goods, merit/demerit, externalities, monopoly, information, immobility) → remedies (Coase bargaining and liability; direct controls, taxes, subsidies, provision; pollution permits). **Congratulations: you have finished all 15 lectures for the midterm!**""",
    exb="""সারসংক্ষেপটাই **Q20**-এর পরিকল্পনা: বাজার ব্যর্থতার সংজ্ঞা → রূপ (জনদ্রব্য, মেরিট/ডিমেরিট, বাহ্যিকতা, একচেটিয়া, তথ্য, অচলতা) → প্রতিকার (কোজ দর কষাকষি ও দায়; সরাসরি নিয়ন্ত্রণ, কর, ভর্তুকি, সরবরাহ; দূষণের অনুমতিপত্র)। **অভিনন্দন: মিডটার্মের ১৫টি লেকচারই শেষ!**""")

TOGETHER("""
<div class="tbl"><table><thead><tr><th>Form of market failure</th><th>Result</th><th>Remedy</th></tr></thead><tbody>
<tr><td>Public goods (non-rival, non-excludable)</td><td>Not provided (free riders)</td><td>Government provides; amount where MB = MC</td></tr>
<tr><td>Merit goods</td><td>Under-consumed</td><td>Subsidies, free provision, compulsion</td></tr>
<tr><td>Demerit goods</td><td>Over-consumed</td><td>Taxes, bans, warnings</td></tr>
<tr><td>Negative externality</td><td>Overproduction (Qe &gt; Qo)</td><td>Direct controls, specific tax, permits, liability</td></tr>
<tr><td>Positive externality</td><td>Underproduction (Qe &lt; Qo)</td><td>Subsidies to consumers/producers, provision</td></tr>
<tr><td>Monopoly power</td><td>P &gt; MC, too little output</td><td>Competition policy, regulation</td></tr>
<tr><td>Asymmetric information</td><td>Wrong prices, adverse selection</td><td>Standards, labelling, consumer laws</td></tr>
<tr><td>Factor immobility</td><td>Under-used workers</td><td>Training, relocation help</td></tr></tbody></table></div>
""", """
<div class="tbl"><table><thead><tr><th>বাজার ব্যর্থতার রূপ</th><th>ফল</th><th>প্রতিকার</th></tr></thead><tbody>
<tr><td>জনদ্রব্য (অপ্রতিদ্বন্দ্বী, বাদ দেওয়া যায় না)</td><td>সরবরাহ হয় না (ফ্রি-রাইডার)</td><td>সরকার সরবরাহ করে; পরিমাণ যেখানে MB = MC</td></tr>
<tr><td>মেরিট দ্রব্য</td><td>কম ভোগ</td><td>ভর্তুকি, বিনামূল্যে সরবরাহ, বাধ্যতামূলক</td></tr>
<tr><td>ডিমেরিট দ্রব্য</td><td>বেশি ভোগ</td><td>কর, নিষেধাজ্ঞা, সতর্কবার্তা</td></tr>
<tr><td>নেতিবাচক বাহ্যিকতা</td><td>অতিরিক্ত উৎপাদন (Qe &gt; Qo)</td><td>সরাসরি নিয়ন্ত্রণ, নির্দিষ্ট কর, অনুমতিপত্র, দায়</td></tr>
<tr><td>ইতিবাচক বাহ্যিকতা</td><td>কম উৎপাদন (Qe &lt; Qo)</td><td>ভোক্তা/উৎপাদককে ভর্তুকি, সরবরাহ</td></tr>
<tr><td>একচেটিয়া ক্ষমতা</td><td>P &gt; MC, খুব কম উৎপাদন</td><td>প্রতিযোগিতা নীতি, নিয়ন্ত্রণ</td></tr>
<tr><td>অসম তথ্য</td><td>ভুল দাম, বিরূপ নির্বাচন</td><td>মানদণ্ড, লেবেল, ভোক্তা আইন</td></tr>
<tr><td>উপাদানের অচলতা</td><td>কম ব্যবহৃত শ্রমিক</td><td>প্রশিক্ষণ, স্থানান্তরে সহায়তা</td></tr></tbody></table></div>
""")

MIDTERM("""
Full card: <a href="#e20">Q20</a>.

### Q20 — Explain market failure and the various ways it occurs. How does the government regulate it?
**Market failure** is a circumstance in which private markets do not bring about the allocation of resources that best satisfies society's wants (total social welfare is not maximised), often because market prices do not include external costs or benefits. It justifies government intervention in the public interest.
**Ways it occurs:** (1) **Public goods** are non-rival and non-excludable, causing the **free-rider problem**; the market does not supply them, so government provides them (optimal amount where marginal benefit = marginal cost; demand found by adding willingness to pay vertically; cost-benefit analysis: provide more if MB > MC). (2) **Merit goods** (education, vaccines) are under-consumed and **demerit goods** (cigarettes) over-consumed because people lack information about long-run benefits/costs. (3) **Externalities**: third-party costs or benefits; social cost = private cost + external cost; **negative** externalities cause overproduction (Qe > Qo), **positive** ones underproduction (Qe < Qo). _(Draw.)_ (4) **Monopoly power**: price maker, little incentive to cut costs, restricted choice, barriers. (5) **Asymmetric information**: one party knows more, leading to misallocation and adverse selection. (6) **Factor immobility**: occupational and geographical, leaving workers under-used.
**Correction:** **non-government**: private bargaining under the **Coase theorem** (clear property rights, few parties, low bargaining costs) and liability laws. **Government**: **direct controls** (emission standards) and **specific taxes** for negative externalities (supply shifts left, price up, output down to Qo); **subsidies** to producers or consumers and **direct provision** for positive externalities, merit and public goods; **market-based pollution permits** (fixed cap, tradable permits, cost internalised by firms).
""", """
পূর্ণ কার্ড: <a href="#e20">Q20</a>।

### Q20 — বাজার ব্যর্থতার ধারণা ও এটি কীভাবে ঘটে ব্যাখ্যা করো। সরকার কীভাবে এটি নিয়ন্ত্রণ করে?
**বাজার ব্যর্থতা** এমন পরিস্থিতি যেখানে বেসরকারি বাজার সমাজের চাওয়া সবচেয়ে ভালোভাবে মেটানোর মতো সম্পদ বণ্টন আনে না (মোট সামাজিক কল্যাণ সর্বোচ্চ হয় না), প্রায়ই কারণ বাজারদরে বাহ্যিক ব্যয় বা সুবিধা থাকে না। এটা জনস্বার্থে সরকারি হস্তক্ষেপের যুক্তি দেয়।
**কীভাবে ঘটে:** (১) **জনদ্রব্য** অপ্রতিদ্বন্দ্বী ও বাদ দেওয়া যায় না, তাই **ফ্রি-রাইডার সমস্যা**; বাজার সরবরাহ করে না, সরকার করে (সর্বোত্তম পরিমাণ যেখানে প্রান্তিক সুবিধা = প্রান্তিক ব্যয়; দিতে-ইচ্ছুকতা খাড়াভাবে যোগ করে চাহিদা; ব্যয়-সুবিধা বিশ্লেষণ: MB > MC হলে বেশি দাও)। (২) দীর্ঘমেয়াদি সুবিধা/ব্যয় সম্পর্কে তথ্যের অভাবে **মেরিট দ্রব্য** (শিক্ষা, টিকা) কম আর **ডিমেরিট দ্রব্য** (সিগারেট) বেশি ভোগ হয়। (৩) **বাহ্যিকতা**: তৃতীয় পক্ষের ব্যয় বা সুবিধা; সামাজিক ব্যয় = ব্যক্তিগত ব্যয় + বাহ্যিক ব্যয়; **নেতিবাচক** বাহ্যিকতায় অতিরিক্ত উৎপাদন (Qe > Qo), **ইতিবাচকে** কম উৎপাদন (Qe < Qo)। _(আঁকো।)_ (৪) **একচেটিয়া ক্ষমতা**: দাম নির্ধারক, খরচ কমানোর প্রণোদনা কম, সীমিত পছন্দ, বাধা। (৫) **অসম তথ্য**: এক পক্ষ বেশি জানে, ভুল বণ্টন ও বিরূপ নির্বাচন। (৬) **উপাদানের অচলতা**: পেশাগত ও ভৌগোলিক, শ্রমিক কম ব্যবহৃত।
**সংশোধন:** **সরকারবহির্ভূত**: **কোজ উপপাদ্য** অনুযায়ী ব্যক্তিগত দর কষাকষি (স্পষ্ট সম্পত্তির অধিকার, কম পক্ষ, কম খরচ) ও দায় আইন। **সরকার**: নেতিবাচক বাহ্যিকতায় **সরাসরি নিয়ন্ত্রণ** (নির্গমন মানদণ্ড) ও **নির্দিষ্ট কর** (যোগান বাঁয়ে, দাম ওপরে, উৎপাদন Qo পর্যন্ত কমে); ইতিবাচক বাহ্যিকতা, মেরিট ও জনদ্রব্যে উৎপাদক বা ভোক্তাকে **ভর্তুকি** ও **সরাসরি সরবরাহ**; **বাজারভিত্তিক দূষণের অনুমতিপত্র** (নির্দিষ্ট সীমা, কেনাবেচাযোগ্য অনুমতিপত্র, ফার্ম নিজে খরচ বহন করে)।
""")

QUIZ([
    Q('A good that is non-rival and non-excludable is a…', 'অপ্রতিদ্বন্দ্বী ও বাদ দেওয়া যায় না এমন দ্রব্য হলো…',
      ['Private good · ব্যক্তিগত দ্রব্য', 'Public good · জনদ্রব্য', 'Demerit good · ডিমেরিট দ্রব্য', 'Inferior good · নিকৃষ্ট পণ্য'], 1,
      'Public goods: everyone can benefit at once and non-payers cannot be excluded.', 'জনদ্রব্য: সবাই একসাথে সুবিধা পায়, টাকা না দেওয়াদের বাদ দেওয়া যায় না।'),
    Q('With a negative production externality, the market output is…', 'উৎপাদনে নেতিবাচক বাহ্যিকতায় বাজারের উৎপাদন…',
      ['Less than optimal · সর্বোত্তমের চেয়ে কম', 'Greater than optimal · সর্বোত্তমের চেয়ে বেশি', 'Exactly optimal · ঠিক সর্বোত্তম', 'Zero · শূন্য'], 1,
      'Producers ignore external costs, so supply is too high: Qe > Qo.', 'উৎপাদক বাহ্যিক ব্যয় উপেক্ষা করে, তাই যোগান খুব বেশি: Qe > Qo।'),
    Q('Social cost equals…', 'সামাজিক ব্যয় সমান…',
      ['Private cost − external cost · ব্যক্তিগত ব্যয় − বাহ্যিক ব্যয়', 'Private cost + external cost · ব্যক্তিগত ব্যয় + বাহ্যিক ব্যয়', 'External cost only · শুধু বাহ্যিক ব্যয়', 'Private benefit · ব্যক্তিগত সুবিধা'], 1,
      'Slide 14: social cost = private cost + external cost.', 'স্লাইড ১৪: সামাজিক ব্যয় = ব্যক্তিগত ব্যয় + বাহ্যিক ব্যয়।'),
    Q('The Coase theorem works best when…', 'কোজ উপপাদ্য সবচেয়ে ভালো কাজ করে যখন…',
      ['Many people are affected · অনেক মানুষ ক্ষতিগ্রস্ত', 'Property rights are clear, few parties, low bargaining costs · সম্পত্তির অধিকার স্পষ্ট, কম পক্ষ, কম দর কষাকষির খরচ',
       'Air is polluted · বাতাস দূষিত', 'The government owns everything · সরকার সব কিছুর মালিক'], 1,
      'Then the affected parties can bargain to a solution without government.', 'তখন ক্ষতিগ্রস্ত পক্ষগুলো সরকার ছাড়াই দর কষে সমাধানে আসতে পারে।'),
    Q('To correct a positive externality like vaccination, the government should…', 'টিকার মতো ইতিবাচক বাহ্যিকতা ঠিক করতে সরকারের উচিত…',
      ['Tax it · কর বসানো', 'Ban it · নিষিদ্ধ করা', 'Subsidise or provide it · ভর্তুকি দেওয়া বা সরবরাহ করা', 'Issue pollution permits · দূষণের অনুমতিপত্র দেওয়া'], 2,
      'Positive externalities are underproduced; subsidies or direct provision raise output to the optimum.', 'ইতিবাচক বাহ্যিকতা কম উৎপাদিত হয়; ভর্তুকি বা সরাসরি সরবরাহ উৎপাদনকে সর্বোত্তমে তোলে।'),
])

SUMMARY("""
- **Market failure:** markets don't allocate resources to best satisfy society; external costs/benefits are ignored.
- **Forms:** public goods (free riders), merit/demerit goods, externalities (negative → too much, positive → too little), monopoly power, asymmetric information, factor immobility.
- **Public goods:** optimal where MB = MC (add willingness to pay vertically); cost-benefit analysis.
- **Fixes:** Coase bargaining and liability laws; direct controls, specific taxes, subsidies, direct provision; tradable **pollution permits**.

**You have finished Modules 1–15.** Revise with the Midterm Q&A, the module quizzes and the summary steps.
""", """
- **বাজার ব্যর্থতা:** বাজার সমাজের জন্য সর্বোত্তমভাবে সম্পদ বণ্টন করে না; বাহ্যিক ব্যয়/সুবিধা উপেক্ষিত।
- **রূপ:** জনদ্রব্য (ফ্রি-রাইডার), মেরিট/ডিমেরিট দ্রব্য, বাহ্যিকতা (নেতিবাচক → খুব বেশি, ইতিবাচক → খুব কম), একচেটিয়া ক্ষমতা, অসম তথ্য, উপাদানের অচলতা।
- **জনদ্রব্য:** সর্বোত্তম যেখানে MB = MC (দিতে-ইচ্ছুকতা খাড়াভাবে যোগ); ব্যয়-সুবিধা বিশ্লেষণ।
- **সমাধান:** কোজ দর কষাকষি ও দায় আইন; সরাসরি নিয়ন্ত্রণ, নির্দিষ্ট কর, ভর্তুকি, সরাসরি সরবরাহ; কেনাবেচাযোগ্য **দূষণের অনুমতিপত্র**।

**তুমি মডিউল ১–১৫ শেষ করেছ।** মিডটার্ম প্রশ্নোত্তর, মডিউল কুইজ ও সারসংক্ষেপ ধাপ দিয়ে রিভিশন দাও।
""")
