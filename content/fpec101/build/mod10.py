MOD(qs=[15])

CONCEPT("""
**Concept:** Lecture 10 finishes monopoly and introduces the third market structure.

1. **Price discrimination:** a monopolist charges **different prices to different buyers** for the same product, a higher price where demand is **inelastic** and a lower price where it is **elastic**, to earn more profit.
2. **Public vs private monopoly**, and a full comparison of **perfect competition vs monopoly**.
3. **Monopolistic competition:** many sellers, **differentiated** products, heavy advertising, easy entry. "Competitive" because there are many firms and free entry; "monopolistic" because each firm's product is a little unique, giving it **some** control over price. Short run: profit or loss. Long run: **normal profit**.

**Exam tip:** this lecture gives the **monopolistic competition** part of **Q15** and finishes the monopoly part (price discrimination, comparison table).
""", """
**ধারণা:** লেকচার ১০ একচেটিয়া শেষ করে তৃতীয় বাজার কাঠামো শুরু করে।

1. **দাম-বৈষম্য:** একচেটিয়া ফার্ম একই পণ্যে **বিভিন্ন ক্রেতাকে ভিন্ন দাম** নেয় — যেখানে চাহিদা **অস্থিতিস্থাপক** সেখানে বেশি, যেখানে **স্থিতিস্থাপক** সেখানে কম — বেশি মুনাফার জন্য।
2. **সরকারি বনাম বেসরকারি একচেটিয়া**, আর **পূর্ণ প্রতিযোগিতা বনাম একচেটিয়ার** পূর্ণ তুলনা।
3. **একচেটিয়া প্রতিযোগিতা:** অনেক বিক্রেতা, **পৃথকীকৃত** পণ্য, প্রচুর বিজ্ঞাপন, সহজ প্রবেশ। অনেক ফার্ম ও অবাধ প্রবেশ বলে "প্রতিযোগিতা"; প্রত্যেকের পণ্য একটু অনন্য বলে দামের ওপর **কিছুটা** নিয়ন্ত্রণ, তাই "একচেটিয়া"। স্বল্পমেয়াদে মুনাফা বা লোকসান; দীর্ঘমেয়াদে **স্বাভাবিক মুনাফা**।

**পরীক্ষার টিপস:** এই লেকচার **Q15**-এর **একচেটিয়া প্রতিযোগিতা** অংশ দেয় এবং একচেটিয়া অংশ শেষ করে (দাম-বৈষম্য, তুলনার ছক)।
""", fig='mc_lr')

WORDS([
    ('Price discrimination', 'Charging different prices for the same product to different buyers', 'দাম-বৈষম্য — একই পণ্যে ভিন্ন ক্রেতাকে ভিন্ন দাম', 'Student vs adult bus fare.'),
    ('Market segregation', 'Separating buyers into groups with different elasticities', 'বাজার পৃথকীকরণ — ভিন্ন স্থিতিস্থাপকতার গোষ্ঠীতে ক্রেতা ভাগ', 'Peak and off-peak travellers.'),
    ('Monopolistic competition', 'Many sellers, differentiated products, easy entry', 'একচেটিয়া প্রতিযোগিতা — অনেক বিক্রেতা, পৃথকীকৃত পণ্য, সহজ প্রবেশ', 'Restaurants, salons, boutiques.'),
    ('Product differentiation', 'Making a product different by attributes, service, location, brand', 'পণ্য পৃথকীকরণ — গুণ, সেবা, অবস্থান, ব্র্যান্ড দিয়ে পণ্য আলাদা করা', 'A café\'s special recipe and décor.'),
    ('Non-price competition', 'Competing by quality, design, advertising rather than price', 'অ-দাম প্রতিযোগিতা — দাম নয়, মান, নকশা, বিজ্ঞাপন দিয়ে প্রতিযোগিতা', 'Free delivery, loyalty cards.'),
    ('Consumer sovereignty', 'Consumers decide what is produced', 'ভোক্তার সার্বভৌমত্ব — ভোক্তাই ঠিক করে কী উৎপাদন হবে', '"The customer is king."'),
])

SLIDE([1, 2, 3, 4], 'Title and outline', 'শিরোনাম ও রূপরেখা',
    bn=['**স্লাইড ১–৩:** প্রিন্সিপলস অব ইকোনমিক্স — সালিমাহ মুশাররিফ। FPEC 101 – লেকচার ১০, ইউনিট ২। বাজার কাঠামো — একচেটিয়া, একচেটিয়া প্রতিযোগিতা।',
        '**স্লাইড ৪ — রূপরেখা:** একচেটিয়া (দাম-বৈষম্য) · একচেটিয়া প্রতিযোগিতা'],
    ex="""Two parts: the end of **monopoly** (price discrimination, public vs private, comparison with perfect competition) and **monopolistic competition**. Reading: McConnell & Brue pp. 436–438, 445–448.""",
    exb="""দুটি অংশ: **একচেটিয়ার** শেষ (দাম-বৈষম্য, সরকারি বনাম বেসরকারি, পূর্ণ প্রতিযোগিতার সাথে তুলনা) আর **একচেটিয়া প্রতিযোগিতা**। পড়া: ম্যাককনেল ও ব্রু পৃ. ৪৩৬–৪৩৮, ৪৪৫–৪৪৮।""")

SLIDE(5, 'Price discrimination: meaning and three forms', 'দাম-বৈষম্য: অর্থ ও তিনটি রূপ',
    bn=['দাম-বৈষম্য', 'কিছু শর্তে একচেটিয়া ফার্ম চাহিদার স্থিতিস্থাপকতার ভিত্তিতে ভিন্ন ক্রেতার কাছে ভিন্ন দাম নিয়ে মুনাফা বাড়াতে পারে।',
        '• একটি বাজারে প্রত্যেক ক্রেতার কাছ থেকে সে সর্বোচ্চ যা দিতে রাজি সেই দাম নেওয়া।', '• প্রত্যেক ক্রেতার কাছে প্রথম কয়েক এককের জন্য এক দাম, পরের এককগুলোর জন্য কম দাম।', '• কিছু ক্রেতার কাছে এক দাম, অন্যদের কাছে আরেক দাম।'],
    ex="""**Price discrimination** = selling the **same product** at **different prices** to different buyers, not because costs differ but because **elasticity of demand differs**. Three forms:

1. **Each customer pays the maximum they are willing to pay** (perfect / first-degree), e.g. bargaining in a bazaar.
2. **Different prices for different quantities** (second-degree): first units dear, later units cheaper, e.g. bulk discounts, "buy 2 get 1 free".
3. **Different prices for different groups** (third-degree): e.g. student fares, children's tickets, foreigner vs local entry fees.""",
    exb="""**দাম-বৈষম্য** = **একই পণ্য** বিভিন্ন ক্রেতার কাছে **ভিন্ন দামে** বিক্রি — খরচ আলাদা বলে নয়, **চাহিদার স্থিতিস্থাপকতা আলাদা** বলে। তিনটি রূপ:

1. **প্রত্যেক ক্রেতা সর্বোচ্চ যা দিতে রাজি তা-ই দেয়** (পূর্ণ / প্রথম মাত্রা), যেমন বাজারে দরদাম।
2. **ভিন্ন পরিমাণে ভিন্ন দাম** (দ্বিতীয় মাত্রা): প্রথম এককগুলো দামি, পরেরগুলো সস্তা, যেমন পাইকারি ছাড়, "২টা কিনলে ১টা ফ্রি"।
3. **ভিন্ন গোষ্ঠীর জন্য ভিন্ন দাম** (তৃতীয় মাত্রা): যেমন ছাত্র ভাড়া, শিশুর টিকিট, বিদেশি বনাম দেশি প্রবেশমূল্য।""",
    eg="""Entry to Lalbagh Fort: Bangladeshi visitors pay much less than foreign tourists. Electricity tariffs: households pay less per unit for the first slab than for higher slabs.""",
    egb="""লালবাগ কেল্লায় প্রবেশ: বাংলাদেশি দর্শনার্থী বিদেশি পর্যটকের চেয়ে অনেক কম দেন। বিদ্যুৎ বিল: প্রথম ধাপের ইউনিটে কম, ওপরের ধাপে বেশি দাম।""")

SLIDE(6, 'Conditions for price discrimination', 'দাম-বৈষম্যের শর্ত',
    bn=['দাম-বৈষম্য', 'প্রয়োজনীয় শর্ত:', '• একচেটিয়া ক্ষমতা', '• বাজার পৃথকীকরণ', '• পুনর্বিক্রয় নেই'],
    ex="""Three conditions must all hold:

1. **Monopoly power:** the seller must be able to set prices (a price taker cannot).
2. **Market segregation:** it must be able to **separate buyers** into groups with **different elasticities** (by age, time, place, ID card).
3. **No resale:** buyers in the cheap market must not be able to **resell** to buyers in the dear market (otherwise everyone buys cheap). Services (haircuts, travel, medical care) are easy to discriminate because they cannot be resold.""",
    exb="""তিনটি শর্তই থাকতে হবে:

1. **একচেটিয়া ক্ষমতা:** বিক্রেতাকে দাম ঠিক করতে পারতে হবে (দাম গ্রহণকারী পারে না)।
2. **বাজার পৃথকীকরণ:** **ভিন্ন স্থিতিস্থাপকতার** গোষ্ঠীতে **ক্রেতা আলাদা** করতে পারতে হবে (বয়স, সময়, স্থান, পরিচয়পত্র দিয়ে)।
3. **পুনর্বিক্রয় নেই:** সস্তা বাজারের ক্রেতা যেন দামি বাজারের ক্রেতার কাছে **আবার বেচতে** না পারে (নইলে সবাই সস্তায় কিনবে)। সেবায় (চুল কাটা, ভ্রমণ, চিকিৎসা) বৈষম্য সহজ, কারণ আবার বেচা যায় না।""",
    tip="Write the three conditions as a numbered list; they are a classic 3-mark short question.",
    tipb="তিনটি শর্ত নম্বর দিয়ে লেখো; এটা ক্লাসিক ৩ নম্বরের সংক্ষিপ্ত প্রশ্ন।")

SLIDE(7, 'Price and output under price discrimination', 'দাম-বৈষম্যে দাম ও উৎপাদন',
    bn=['দাম-বৈষম্য', 'এরপর ফার্ম প্রতিটি বাজার-অংশে MR = MC উৎপাদন করে বিক্রি করে।', 'ধরা হয় ATC স্থির এবং সব উৎপাদনে MC = ATC।', 'ফার্ম অস্থিতিস্থাপক বাজারে বেশি দাম নেয়', 'আর বেশি স্থিতিস্থাপক বাজারে কম দাম।',
        'বৈষম্য না করে এক দামে যা হতো তার চেয়ে মোট মুনাফা বেশি।', 'ম্যাককনেল ও ব্রু পৃ. ৪৩৮', 'দাম-বৈষম্যকারী একচেটিয়া ফার্ম বাজারকে অস্থিতিস্থাপক ও স্থিতিস্থাপক দুই অংশে ভাগ করে মোট মুনাফা সর্বোচ্চ করে।'],
    fig='price_disc',
    ex="""The firm splits the market in two and applies **MR = MC in each part** (with constant MC = ATC):
- **Inelastic market** (buyers who need it): **higher price**.
- **Elastic market** (price-sensitive buyers): **lower price**.

Total profit is **larger** than with a single price. Lecture 5's "yield management" (airlines, peak/off-peak trains) is exactly this.""",
    exb="""ফার্ম বাজারকে দুই ভাগ করে **প্রতিটি অংশে MR = MC** প্রয়োগ করে (MC = ATC স্থির ধরে):
- **অস্থিতিস্থাপক বাজার** (যাদের লাগবেই): **বেশি দাম**।
- **স্থিতিস্থাপক বাজার** (দাম-সংবেদনশীল ক্রেতা): **কম দাম**।

এক দামের চেয়ে মোট মুনাফা **বেশি**। লেকচার ৫-এর "ইল্ড ম্যানেজমেন্ট" (এয়ারলাইন, ব্যস্ত/অব্যস্ত সময়ের ট্রেন) ঠিক এটাই।""")

SLIDE(8, 'Public vs private monopoly', 'সরকারি বনাম বেসরকারি একচেটিয়া',
    txt=['Public vs Private Monopoly', 'Finance: Public — Government | Private — by selling shares, savings', 'Motive: welfare services, not profit | produce whatever is demanded',
         'Prices: affordable | higher, as profit is the motive', 'Administration: board formed by government ministry | board formed by private investors', 'Investment: greater | lesser',
         'Efficiency: less efficient | greater efficiency', 'Payment: by paying taxes | paying for product bought', 'Functioning: cannot run smoothly for long-run plans because of inflation etc. | runs smoothly',
         'Burden: on taxpayer | on private investors', 'Shut down: supported by government in case of losses | may be shut down or nationalised'],
    bn=['সরকারি বনাম বেসরকারি একচেটিয়া', 'অর্থায়ন: সরকারি — সরকার | বেসরকারি — শেয়ার বিক্রি, সঞ্চয়', 'উদ্দেশ্য: কল্যাণমূলক সেবা, মুনাফা নয় | যা চাওয়া হয় তা উৎপাদন',
        'দাম: সাশ্রয়ী | বেশি, কারণ মুনাফাই উদ্দেশ্য', 'প্রশাসন: মন্ত্রণালয়ের গঠিত বোর্ড | বেসরকারি বিনিয়োগকারীদের গঠিত বোর্ড', 'বিনিয়োগ: বেশি | কম',
        'দক্ষতা: কম দক্ষ | বেশি দক্ষ', 'পরিশোধ: কর দিয়ে | কেনা পণ্যের দাম দিয়ে', 'পরিচালনা: মূল্যস্ফীতি ইত্যাদির কারণে দীর্ঘমেয়াদি পরিকল্পনায় মসৃণ চলে না | মসৃণ চলে',
        'বোঝা: করদাতার ওপর | বেসরকারি বিনিয়োগকারীর ওপর', 'বন্ধ: লোকসানে সরকার সমর্থন দেয় | বন্ধ বা জাতীয়করণ হতে পারে'],
    ex="""A monopoly can be owned by the **state** (public) or by **private investors**. The key contrast: a **public monopoly** aims at **welfare** and **affordable prices**, financed and backed by taxpayers, but tends to be **less efficient**; a **private monopoly** aims at **profit**, charges **higher prices**, but is usually **more efficient** and bears its own losses.""",
    exb="""একচেটিয়ার মালিক হতে পারে **রাষ্ট্র** (সরকারি) বা **বেসরকারি বিনিয়োগকারী**। মূল বৈসাদৃশ্য: **সরকারি একচেটিয়ার** লক্ষ্য **কল্যাণ** ও **সাশ্রয়ী দাম**, করদাতার অর্থে চলে ও সমর্থিত, কিন্তু **কম দক্ষ** হয়; **বেসরকারি একচেটিয়ার** লক্ষ্য **মুনাফা**, **বেশি দাম** নেয়, কিন্তু সাধারণত **বেশি দক্ষ** এবং নিজের লোকসান নিজে বহন করে।""",
    eg="""**Public:** Bangladesh Railway, Dhaka WASA (low fares, losses covered by the budget). **Private (near-monopoly):** a privately owned toll road or port operator under a concession.""",
    egb="""**সরকারি:** বাংলাদেশ রেলওয়ে, ঢাকা ওয়াসা (কম ভাড়া, লোকসান বাজেট থেকে মেটে)। **বেসরকারি (প্রায়-একচেটিয়া):** কনসেশনে বেসরকারি মালিকানার টোল রোড বা বন্দর পরিচালক।""")

SLIDE([9, 10, 11, 12], 'Perfect competition vs monopoly: eight comparisons', 'পূর্ণ প্রতিযোগিতা বনাম একচেটিয়া: আটটি তুলনা',
    bn=['**স্লাইড ৯ — দক্ষতা:** পূর্ণ প্রতিযোগিতায় তীব্র প্রতিযোগিতা ও একই এককদামের কারণে ফার্ম যতটা সম্ভব দক্ষভাবে উৎপাদনে বাধ্য; খরচ বেশি কিন্তু দাম বাড়ানো না গেলে উচ্চ-ব্যয়ের উৎপাদক কম মুনাফা পায় ও অদক্ষ ফার্ম বেরিয়ে যায়। একচেটিয়ায় বৃহদায়তনের সুবিধা পেলে তা একচেটিয়া ফার্মের জন্যই সবচেয়ে লাভজনক, কারণ সে যত খুশি দাম নিতে পারে। **দাম:** পূর্ণ প্রতিযোগিতায় ক্রেতা টানতে দাম কম রাখা হয়। একচেটিয়া বড় পরিসরে উৎপাদন করে কম দামেও মুনাফা করতে পারে, যা পূর্ণ প্রতিযোগিতার চেয়েও কম হতে পারে; আবার অদক্ষ হলে খরচ মেটাতে অনেক বেশি দামও নিতে পারে।',
        '**স্লাইড ১০ — সংরক্ষিত মুনাফা:** পূর্ণ প্রতিযোগিতায় বিনিয়োগ ও গবেষণার জন্য মুনাফা বাঁচে না; একচেটিয়ায় বাঁচে। **সরবরাহকারী:** পূর্ণ প্রতিযোগিতায় অসন্তুষ্ট ক্রেতা অন্য সরবরাহকারীর কাছে যেতে পারে; একচেটিয়া একমাত্র সরবরাহকারী, ক্রেতার বিকল্প নেই।',
        '**স্লাইড ১১ — উৎপাদন:** বিপুল বিনিয়োগ ও মূলধনী যন্ত্রের শিল্পে পূর্ণ সক্ষমতায় চলতে পুরো দেশীয় বাজার লাগে; একাধিক ফার্ম থাকলে সক্ষমতার নিচে চলতে হয়, খরচ বাড়ে। একচেটিয়ায় পুরো বাজার নিশ্চিত, তাই বৃহদায়তনের সুবিধায় বিপুল উৎপাদন ও প্রতিযোগিতামূলক দাম সম্ভব। **সাড়া:** পূর্ণ প্রতিযোগিতায় চাহিদা ও দাম বাড়লে সবাই উৎপাদন বাড়ায়, ফলে যোগান চাহিদা ছাড়িয়ে দাম পড়ে যায়, পরের মৌসুমে উৎপাদন কমায় — ওঠানামা চলে। একচেটিয়া একমাত্র সরবরাহকারী বলে বাজারের ধারা ভালো অনুমান করে বেশি কার্যকরভাবে সাড়া দেয়।',
        '**স্লাইড ১২ — দাম:** পূর্ণ প্রতিযোগিতায় সবচেয়ে দক্ষ উৎপাদনের ভিত্তিতে সবাই একই দাম নেয়, যেখানে দাম = গড় ব্যয় = প্রান্তিক ব্যয়। একচেটিয়া উৎপাদন সীমিত করে গড় বা প্রান্তিক ব্যয়ের চেয়ে অনেক বেশি দাম নেয়। **ভোক্তার সার্বভৌমত্ব:** পূর্ণ প্রতিযোগিতায় ভোক্তাই রাজা, যা চায় তা সরবরাহ হয়, বেছে নেওয়ার অনেক বিক্রেতা। একচেটিয়ায় একজনই সরবরাহকারী বলে ভোক্তার সার্বভৌমত্ব কম, উৎপাদক শক্তিশালী অবস্থানে।'],
    ex="""The four slides compare the two extremes under eight headings:

<div class="tbl"><table><thead><tr><th>Heading</th><th>Perfect competition</th><th>Monopoly</th></tr></thead><tbody>
<tr><td>Efficiency</td><td>Forced to be efficient; inefficient firms leave</td><td>Benefits from economies of scale, but no pressure to be efficient</td></tr>
<tr><td>Prices</td><td>Kept low to attract buyers</td><td>Could be lower (scale) or much higher (inefficiency, restricting output)</td></tr>
<tr><td>Retained profit</td><td>None left for investment and research</td><td>Profits available for investment</td></tr>
<tr><td>Supplier choice</td><td>Consumer can switch</td><td>No choice</td></tr>
<tr><td>Production</td><td>Big-capital industries run below capacity if split</td><td>Whole market → large output, economies of scale</td></tr>
<tr><td>Response to change</td><td>Over-reaction, boom-bust cycles</td><td>Better able to estimate market trends</td></tr>
<tr><td>Price vs cost</td><td>P = AC = MC</td><td>P &gt; AC and MC (restricts output)</td></tr>
<tr><td>Consumer sovereignty</td><td>Consumer is king</td><td>Producer is in the stronger position</td></tr></tbody></table></div>

Notice the slides give monopoly some **advantages** too (research funds, scale, stable planning). A balanced exam answer mentions both sides.""",
    exb="""চারটি স্লাইড আটটি শিরোনামে দুই প্রান্তের তুলনা করে:

<div class="tbl"><table><thead><tr><th>শিরোনাম</th><th>পূর্ণ প্রতিযোগিতা</th><th>একচেটিয়া</th></tr></thead><tbody>
<tr><td>দক্ষতা</td><td>দক্ষ হতে বাধ্য; অদক্ষরা বেরিয়ে যায়</td><td>বৃহদায়তনের সুবিধা পায়, কিন্তু দক্ষ হওয়ার চাপ নেই</td></tr>
<tr><td>দাম</td><td>ক্রেতা টানতে কম রাখা হয়</td><td>কম হতে পারে (আকার) বা অনেক বেশি (অদক্ষতা, উৎপাদন সীমিত)</td></tr>
<tr><td>সংরক্ষিত মুনাফা</td><td>বিনিয়োগ ও গবেষণার জন্য বাঁচে না</td><td>বিনিয়োগের জন্য মুনাফা থাকে</td></tr>
<tr><td>সরবরাহকারী বাছাই</td><td>ভোক্তা বদলাতে পারে</td><td>কোনো বিকল্প নেই</td></tr>
<tr><td>উৎপাদন</td><td>বড় মূলধনের শিল্প ভাগ হলে সক্ষমতার নিচে চলে</td><td>পুরো বাজার → বিপুল উৎপাদন, বৃহদায়তনের সুবিধা</td></tr>
<tr><td>পরিবর্তনে সাড়া</td><td>অতিপ্রতিক্রিয়া, তেজি-মন্দার চক্র</td><td>বাজারের ধারা ভালো অনুমান করতে পারে</td></tr>
<tr><td>দাম বনাম ব্যয়</td><td>P = AC = MC</td><td>P &gt; AC ও MC (উৎপাদন সীমিত)</td></tr>
<tr><td>ভোক্তার সার্বভৌমত্ব</td><td>ভোক্তাই রাজা</td><td>উৎপাদক শক্তিশালী অবস্থানে</td></tr></tbody></table></div>

খেয়াল করো, স্লাইড একচেটিয়ার কিছু **সুবিধাও** দেখায় (গবেষণার অর্থ, আকার, স্থিতিশীল পরিকল্পনা)। ভারসাম্যপূর্ণ উত্তরে দুই দিকই লেখো।""",
    tip="This table is ready-made for a \"compare perfect competition and monopoly\" question. Learn the eight headings.",
    tipb="\"পূর্ণ প্রতিযোগিতা ও একচেটিয়ার তুলনা\" প্রশ্নে এই ছক সরাসরি কাজে লাগে। আটটি শিরোনাম শেখো।")

CHECK([
    Q('Which is NOT a condition for price discrimination?', 'কোনটি দাম-বৈষম্যের শর্ত নয়?',
      ['Monopoly power · একচেটিয়া ক্ষমতা', 'Market segregation · বাজার পৃথকীকরণ', 'Easy resale between buyers · ক্রেতাদের মধ্যে সহজ পুনর্বিক্রয়', 'Different elasticities · ভিন্ন স্থিতিস্থাপকতা'], 2,
      'If buyers could resell, the cheap group would resell to the dear group and discrimination would fail.', 'ক্রেতারা আবার বেচতে পারলে সস্তা গোষ্ঠী দামি গোষ্ঠীর কাছে বেচবে, বৈষম্য ব্যর্থ হবে।'),
    Q('A price-discriminating monopolist charges the higher price in the market where demand is…', 'দাম-বৈষম্যকারী একচেটিয়া বেশি দাম নেয় যে বাজারে চাহিদা…',
      ['More elastic · বেশি স্থিতিস্থাপক', 'Inelastic · অস্থিতিস্থাপক', 'Perfectly elastic · পূর্ণ স্থিতিস্থাপক', 'Zero · শূন্য'], 1,
      'Buyers with inelastic demand keep buying even at a high price.', 'অস্থিতিস্থাপক চাহিদার ক্রেতা বেশি দামেও কিনতে থাকে।'),
])

SLIDE([13, 14], 'Monopolistic competition: definition', 'একচেটিয়া প্রতিযোগিতা: সংজ্ঞা',
    bn=['**স্লাইড ১৩:** একচেটিয়া প্রতিযোগিতা', '**স্লাইড ১৪:** এমন একটি বাজার কাঠামো যার বৈশিষ্ট্য — তুলনামূলক বেশি সংখ্যক বিক্রেতা; পৃথকীকৃত পণ্য (প্রায়ই প্রচুর বিজ্ঞাপনে প্রচারিত); শিল্পে সহজ প্রবেশ ও প্রস্থান। প্রথম ও তৃতীয় বৈশিষ্ট্য একচেটিয়া প্রতিযোগিতার "প্রতিযোগিতামূলক" দিক; দ্বিতীয়টি "একচেটিয়া" দিক।'],
    ex="""**Monopolistic competition** = (1) a **relatively large number of sellers**, (2) **differentiated products** (often heavily advertised), (3) **easy entry and exit**.

The name explains itself: features **1 and 3** make it **competitive**; feature **2** (each product is slightly unique) gives each firm a little **monopoly** power.""",
    exb="""**একচেটিয়া প্রতিযোগিতা** = (১) **তুলনামূলক বেশি সংখ্যক বিক্রেতা**, (২) **পৃথকীকৃত পণ্য** (প্রায়ই প্রচুর বিজ্ঞাপিত), (৩) **সহজ প্রবেশ ও প্রস্থান**।

নামটাই ব্যাখ্যা: বৈশিষ্ট্য **১ ও ৩** একে **প্রতিযোগিতামূলক** করে; বৈশিষ্ট্য **২** (প্রতিটি পণ্য একটু অনন্য) প্রত্যেক ফার্মকে একটু **একচেটিয়া** ক্ষমতা দেয়।""",
    eg="""Fast-food shops on Satmasjid Road, beauty salons, tailors, bakeries, clothing brands like Yellow, Ecstasy, Sailor: many sellers, each a bit different, and a new one opens every month.""",
    egb="""সাতমসজিদ রোডের ফাস্টফুড দোকান, বিউটি পার্লার, দর্জি, বেকারি, ইয়েলো, এক্সট্যাসি, সেইলরের মতো পোশাক ব্র্যান্ড: অনেক বিক্রেতা, প্রত্যেকে একটু আলাদা, প্রতি মাসে নতুন একটা খোলে।""")

SLIDE([15, 16], 'Features of monopolistic competition', 'একচেটিয়া প্রতিযোগিতার বৈশিষ্ট্য',
    bn=['**স্লাইড ১৫:** তুলনামূলক বেশি সংখ্যক বিক্রেতা — ছোট বাজার-অংশ · যোগসাজশ নেই · স্বাধীন সিদ্ধান্ত। পৃথকীকৃত পণ্য (প্রায়ই প্রচুর বিজ্ঞাপনে প্রচারিত) — পণ্যের গুণাবলি · সেবা · অবস্থান · ব্র্যান্ড নাম ও প্যাকেজিং · দামের ওপর কিছু নিয়ন্ত্রণ। শিল্পে সহজ প্রবেশ ও প্রস্থান।',
        '**স্লাইড ১৬ — প্রচুর বিজ্ঞাপন:** সফল পণ্য পৃথকীকরণের জন্য একচেটিয়া প্রতিযোগীরা প্রায়ই প্রচুর বিজ্ঞাপন দেয়। পৃথকীকরণ ও বিজ্ঞাপনের লক্ষ্য — অ-দাম প্রতিযোগিতা — পণ্যের আকর্ষণ বাড়ানো এবং ক্রেতার কাছে দামকে কম গুরুত্বপূর্ণ করা। সফল হলে চাহিদা বাড়ে, ডানে সরে এবং তুলনামূলক কম স্থিতিস্থাপক হয়।'],
    ex="""**1. Many sellers:** each has a **small market share**, so there is **no collusion** and each firm acts **independently**.

**2. Differentiated products**, by: **attributes** (quality, design), **service** (friendly staff, delivery), **location** (the shop near you), **brand names and packaging**. This gives **some control over price**.

**3. Easy entry and exit.**

**4. Heavy advertising (non-price competition):** the aim is to make the product more appealing so that **price matters less**: demand **shifts right** and becomes **less elastic**.""",
    exb="""**১. অনেক বিক্রেতা:** প্রত্যেকের **ছোট বাজার-অংশ**, তাই **যোগসাজশ নেই**, প্রত্যেকে **স্বাধীনভাবে** চলে।

**২. পৃথকীকৃত পণ্য**, যেভাবে: **গুণাবলি** (মান, নকশা), **সেবা** (আন্তরিক কর্মী, ডেলিভারি), **অবস্থান** (তোমার কাছের দোকান), **ব্র্যান্ড নাম ও প্যাকেজিং**। এতে **দামের ওপর কিছু নিয়ন্ত্রণ** আসে।

**৩. সহজ প্রবেশ ও প্রস্থান।**

**৪. প্রচুর বিজ্ঞাপন (অ-দাম প্রতিযোগিতা):** লক্ষ্য পণ্যকে আকর্ষণীয় করা যাতে **দাম কম গুরুত্বপূর্ণ** হয়: চাহিদা **ডানে সরে** এবং **কম স্থিতিস্থাপক** হয়।""")

SLIDE(17, 'Demand: highly elastic; short run vs long run', 'চাহিদা: খুব স্থিতিস্থাপক; স্বল্প বনাম দীর্ঘমেয়াদ',
    bn=['দাম ও উৎপাদন নির্ধারণ', '**খুব স্থিতিস্থাপক চাহিদা রেখা** — পূর্ণ প্রতিযোগিতা ও একচেটিয়া থেকে পার্থক্য। একচেটিয়া প্রতিযোগীর চাহিদা বিশুদ্ধ একচেটিয়ার চেয়ে বেশি স্থিতিস্থাপক, কারণ তার অনেক প্রতিযোগী আছে যারা কাছাকাছি বিকল্প দেয়; কিন্তু পূর্ণ প্রতিযোগিতার মতো পূর্ণ স্থিতিস্থাপক নয়, কারণ পণ্য পৃথকীকৃত।',
        'চাহিদার স্থিতিস্থাপকতা নির্ভর করে প্রতিদ্বন্দ্বীর সংখ্যা ও পৃথকীকরণের মাত্রার ওপর। প্রতিদ্বন্দ্বী যত বেশি ও পৃথকীকরণ যত দুর্বল, স্থিতিস্থাপকতা তত বেশি।', 'স্বল্পমেয়াদে মুনাফা ও লোকসান', 'দীর্ঘমেয়াদে মুনাফা বা লোকসান — স্বাভাবিক মুনাফা'],
    ex="""The firm's demand curve slopes down but is **highly elastic**:
- **More elastic than a monopolist's**, because there are many close substitutes.
- **Not perfectly elastic** like perfect competition, because products are differentiated.

Elasticity depends on the **number of rivals** and the **degree of differentiation**: more rivals and weaker differentiation → more elastic.

Output rule: **MR = MC** (like any firm). **Short run:** profit or loss. **Long run:** normal profit (next slides).""",
    exb="""ফার্মের চাহিদা রেখা নিচে নামে কিন্তু **খুব স্থিতিস্থাপক**:
- **একচেটিয়ার চেয়ে বেশি স্থিতিস্থাপক**, কারণ অনেক কাছাকাছি বিকল্প আছে।
- পূর্ণ প্রতিযোগিতার মতো **পূর্ণ স্থিতিস্থাপক নয়**, কারণ পণ্য পৃথকীকৃত।

স্থিতিস্থাপকতা নির্ভর করে **প্রতিদ্বন্দ্বীর সংখ্যা** ও **পৃথকীকরণের মাত্রার** ওপর: বেশি প্রতিদ্বন্দ্বী ও দুর্বল পৃথকীকরণ → বেশি স্থিতিস্থাপক।

উৎপাদনের নিয়ম: **MR = MC** (যেকোনো ফার্মের মতো)। **স্বল্পমেয়াদ:** মুনাফা বা লোকসান। **দীর্ঘমেয়াদ:** স্বাভাবিক মুনাফা (পরের স্লাইড)।""")

SLIDE([18, 19, 20, 21, 22], 'From short-run profit/loss to long-run normal profit', 'স্বল্পমেয়াদি মুনাফা/লোকসান থেকে দীর্ঘমেয়াদি স্বাভাবিক মুনাফা',
    txt={18: ['Profits: in the short term, if profit, other firms are attracted and enter; demand for each business falls (shifts left); each firm has a smaller share of total demand and faces more close substitutes; economic profit is reduced until it disappears.',
              'Loss: with short-term losses, firms leave; the survivors face fewer substitutes and a bigger share of demand; their demand curves shift right; losses disappear and give way to normal profits in the long run.'],
         19: ['[Diagram: elastic demand curve above ATC: economic profit → competitors enter]'], 20: ['[Diagram: demand curve shifts left; economic profits decrease; in the long run, profits are zero]'],
         21: ['[Diagram: demand below ATC: loss → competitors leave]'], 22: ['[Diagram: some firms exit; D shifts right; losses get smaller; in the long run, profits are zero]']},
    bn=['**স্লাইড ১৮ — মুনাফা:** স্বল্পমেয়াদে মুনাফা হলে অন্য ফার্ম আকৃষ্ট হয়ে ঢোকে; প্রতিটি ব্যবসার চাহিদা কমে (বাঁয়ে সরে); প্রত্যেকের মোট চাহিদার অংশ ছোট হয়, কাছাকাছি বিকল্প বাড়ে; অর্থনৈতিক মুনাফা কমতে কমতে শেষ হয়। **লোকসান:** স্বল্পমেয়াদে লোকসান হলে ফার্ম চলে যায়; টিকে থাকা ফার্মের বিকল্প কমে, চাহিদার অংশ বাড়ে, চাহিদা রেখা ডানে সরে; দীর্ঘমেয়াদে লোকসান দূর হয়ে স্বাভাবিক মুনাফা আসে।',
        '**স্লাইড ১৯–২২:** [চিত্র: ATC-র ওপরে স্থিতিস্থাপক চাহিদা → অর্থনৈতিক মুনাফা → প্রতিযোগী ঢোকে → চাহিদা বাঁয়ে সরে, দীর্ঘমেয়াদে মুনাফা শূন্য। ATC-র নিচে চাহিদা → লোকসান → প্রতিযোগী চলে যায় → চাহিদা ডানে সরে, লোকসান কমে, দীর্ঘমেয়াদে মুনাফা শূন্য]'],
    fig='mc_lr',
    ex="""The same entry/exit logic as perfect competition, but now it works by **shifting each firm's demand curve**:

- **Short-run profit** (P > ATC) → new firms enter with similar products → each firm loses customers → its **demand shifts left** → profit shrinks until demand just **touches (is tangent to) ATC**: **P = ATC, normal profit**.
- **Short-run loss** (P < ATC) → some firms leave → survivors gain customers → **demand shifts right** → losses disappear → **normal profit**.

**Long-run equilibrium:** P = ATC (normal profit), but **P > MC** and P is **above minimum ATC**: firms have **excess capacity** (they could produce more at lower cost). That is the "cost" of product variety.""",
    exb="""পূর্ণ প্রতিযোগিতার মতো একই প্রবেশ/প্রস্থানের যুক্তি, তবে এবার কাজ করে **প্রতিটি ফার্মের চাহিদা রেখা সরিয়ে**:

- **স্বল্পমেয়াদি মুনাফা** (P > ATC) → অনুরূপ পণ্য নিয়ে নতুন ফার্ম ঢোকে → প্রতিটি ফার্ম ক্রেতা হারায় → **চাহিদা বাঁয়ে সরে** → মুনাফা কমে, যতক্ষণ না চাহিদা ATC-কে **শুধু ছোঁয় (স্পর্শক হয়)**: **P = ATC, স্বাভাবিক মুনাফা**।
- **স্বল্পমেয়াদি লোকসান** (P < ATC) → কিছু ফার্ম চলে যায় → টিকে থাকারা ক্রেতা পায় → **চাহিদা ডানে সরে** → লোকসান দূর হয় → **স্বাভাবিক মুনাফা**।

**দীর্ঘমেয়াদি ভারসাম্য:** P = ATC (স্বাভাবিক মুনাফা), কিন্তু **P > MC** আর P **সর্বনিম্ন ATC-র ওপরে**: ফার্মের **অতিরিক্ত সক্ষমতা** থাকে (কম খরচে বেশি উৎপাদন করতে পারত)। এটা পণ্য-বৈচিত্র্যের "মূল্য"।""",
    eg="""A new style of "tehari" shop becomes popular in Mohammadpur and makes big profits. Within a year, five similar shops open nearby; each one's customers fall, and soon they all earn just normal profit.""",
    egb="""মোহাম্মদপুরে নতুন ধরনের "তেহারি" দোকান জনপ্রিয় হয়ে বড় মুনাফা করল। এক বছরে কাছাকাছি পাঁচটি একই রকম দোকান খুলল; প্রত্যেকের ক্রেতা কমল, শিগগিরই সবাই শুধু স্বাভাবিক মুনাফা পায়।""",
    tip="In Q15 draw the two-panel diagram: short-run profit, then long-run tangency (D touches ATC).",
    tipb="Q15-এ দুই-প্যানেলের চিত্র আঁকো: স্বল্পমেয়াদি মুনাফা, তারপর দীর্ঘমেয়াদি স্পর্শবিন্দু (D, ATC-কে ছোঁয়)।")

SLIDE(23, 'Exceptions to normal profit in the long run', 'দীর্ঘমেয়াদে স্বাভাবিক মুনাফার ব্যতিক্রম',
    bn=['দীর্ঘমেয়াদে স্বাভাবিক মুনাফার ব্যতিক্রম', '• এমন পণ্য পৃথকীকরণ যা অন্য ফার্ম সময় পেলেও নকল করতে পারে না।',
        '• পণ্য পৃথকীকরণে বড় অর্থ লাগলে তা প্রবেশে বাধা হয়ে যায়, প্রমিত পণ্যের তুলনায়। এতে কিছু একচেটিয়া ক্ষমতা বোঝায়, ফলে দীর্ঘমেয়াদেও ছোট অর্থনৈতিক মুনাফা থাকতে পারে।'],
    ex="""Two cases where a firm can keep a **small economic profit** even in the long run:
1. Its differentiation **cannot be copied** (a secret recipe, a famous brand, the best location).
2. Differentiating is **expensive** (advertising, design), which acts as a **barrier to entry**, giving the firm a little monopoly power.""",
    exb="""দুটি ক্ষেত্রে ফার্ম দীর্ঘমেয়াদেও **ছোট অর্থনৈতিক মুনাফা** রাখতে পারে:
1. এর পৃথকীকরণ **নকল করা যায় না** (গোপন রেসিপি, বিখ্যাত ব্র্যান্ড, সেরা অবস্থান)।
2. পৃথকীকরণ **ব্যয়বহুল** (বিজ্ঞাপন, নকশা), যা **প্রবেশে বাধা** হয়ে ফার্মকে একটু একচেটিয়া ক্ষমতা দেয়।""",
    eg="""Old Dhaka's famous biryani houses (e.g. a decades-old brand name) keep long queues and good profits: newcomers cannot copy the reputation.""",
    egb="""পুরান ঢাকার বিখ্যাত বিরিয়ানির দোকান (যেমন কয়েক দশকের পুরোনো ব্র্যান্ড) লম্বা লাইন ও ভালো মুনাফা ধরে রাখে: নবাগতরা সুনাম নকল করতে পারে না।""")

SLIDE(24, 'Summary of Lecture 10', 'লেকচার ১০-এর সারসংক্ষেপ',
    bn=['সারসংক্ষেপ', 'একচেটিয়া — দাম-বৈষম্য (শর্ত, উৎপাদন নির্ধারণ), সরকারি বনাম বেসরকারি একচেটিয়া', 'পূর্ণ প্রতিযোগিতা বনাম একচেটিয়া', 'একচেটিয়া প্রতিযোগিতা — সংজ্ঞা, বৈশিষ্ট্য, দাম-উৎপাদন নির্ধারণ, দীর্ঘমেয়াদে স্বাভাবিক মুনাফার ব্যতিক্রম'],
    ex="""Revision checklist: price discrimination (3 forms, 3 conditions, higher price in the inelastic market); public vs private monopoly; 8-point comparison of perfect competition and monopoly; monopolistic competition (definition, features, elastic demand, short-run profit/loss, long-run normal profit, exceptions).""",
    exb="""রিভিশন চেকলিস্ট: দাম-বৈষম্য (৩ রূপ, ৩ শর্ত, অস্থিতিস্থাপক বাজারে বেশি দাম); সরকারি বনাম বেসরকারি একচেটিয়া; পূর্ণ প্রতিযোগিতা ও একচেটিয়ার ৮-দফা তুলনা; একচেটিয়া প্রতিযোগিতা (সংজ্ঞা, বৈশিষ্ট্য, স্থিতিস্থাপক চাহিদা, স্বল্পমেয়াদি মুনাফা/লোকসান, দীর্ঘমেয়াদি স্বাভাবিক মুনাফা, ব্যতিক্রম)।""")

TOGETHER("""
### Monopolistic competition vs the other two structures
<div class="tbl"><table><thead><tr><th></th><th>Perfect competition</th><th>Monopolistic competition</th><th>Monopoly</th></tr></thead><tbody>
<tr><td>Sellers</td><td>Very many</td><td>Relatively many</td><td>One</td></tr>
<tr><td>Product</td><td>Identical</td><td>Differentiated</td><td>Unique</td></tr>
<tr><td>Demand facing firm</td><td>Perfectly elastic</td><td>Highly elastic, downward</td><td>Market demand, less elastic</td></tr>
<tr><td>Entry</td><td>Free</td><td>Easy</td><td>Blocked</td></tr>
<tr><td>Advertising</td><td>None</td><td>Heavy</td><td>Public relations</td></tr>
<tr><td>Long-run profit</td><td>Normal</td><td>Normal (with exceptions)</td><td>Abnormal</td></tr>
<tr><td>Long-run efficiency</td><td>P = MC = min ATC</td><td>P = ATC but &gt; MC and &gt; min ATC (excess capacity)</td><td>P &gt; MC, P &gt; min ATC</td></tr></tbody></table></div>
""", """
### একচেটিয়া প্রতিযোগিতা বনাম অন্য দুটি কাঠামো
<div class="tbl"><table><thead><tr><th></th><th>পূর্ণ প্রতিযোগিতা</th><th>একচেটিয়া প্রতিযোগিতা</th><th>একচেটিয়া</th></tr></thead><tbody>
<tr><td>বিক্রেতা</td><td>অসংখ্য</td><td>তুলনামূলক অনেক</td><td>একজন</td></tr>
<tr><td>পণ্য</td><td>একই রকম</td><td>পৃথকীকৃত</td><td>অনন্য</td></tr>
<tr><td>ফার্মের চাহিদা</td><td>পূর্ণ স্থিতিস্থাপক</td><td>খুব স্থিতিস্থাপক, নিম্নমুখী</td><td>বাজার চাহিদা, কম স্থিতিস্থাপক</td></tr>
<tr><td>প্রবেশ</td><td>অবাধ</td><td>সহজ</td><td>বন্ধ</td></tr>
<tr><td>বিজ্ঞাপন</td><td>নেই</td><td>প্রচুর</td><td>জনসংযোগ</td></tr>
<tr><td>দীর্ঘমেয়াদি মুনাফা</td><td>স্বাভাবিক</td><td>স্বাভাবিক (ব্যতিক্রমসহ)</td><td>অস্বাভাবিক</td></tr>
<tr><td>দীর্ঘমেয়াদি দক্ষতা</td><td>P = MC = সর্বনিম্ন ATC</td><td>P = ATC কিন্তু &gt; MC ও &gt; সর্বনিম্ন ATC (অতিরিক্ত সক্ষমতা)</td><td>P &gt; MC, P &gt; সর্বনিম্ন ATC</td></tr></tbody></table></div>
""", fig='price_disc')

MIDTERM("""
Full card: <a href="#e15">Q15</a>.

### Q15 (part 3) — Monopolistic competition (+ monopoly additions)
**Monopolistic competition** is a market structure with a relatively large number of sellers, differentiated products (often heavily advertised) and easy entry and exit. **Features:** small market shares, no collusion, independent action; differentiation by attributes, service, location, brand and packaging, giving some control over price; heavy advertising (non-price competition) to shift demand right and make it less elastic. **Demand:** downward-sloping and highly elastic (more elastic than monopoly, not perfectly elastic); elasticity rises with the number of rivals and weaker differentiation. **Short run:** produce where MR = MC; economic profit or loss. **Long run:** profits attract entry, each firm's demand shifts left until P = ATC (tangency): **normal profit**; losses cause exit, demand shifts right until normal profit. At long-run equilibrium P > MC and P > min ATC (excess capacity). **Exceptions:** differentiation that cannot be copied, or costly differentiation that acts as a barrier, may allow small long-run profits. **Barriers:** low.

**Monopoly additions:** **price discrimination** — charging different prices to different buyers (each buyer's maximum; quantity-based; group-based), requiring monopoly power, market segregation and no resale; the firm sets MR = MC in each market and charges more in the inelastic market, raising total profit. **Public vs private monopoly** (welfare and affordable prices vs profit and efficiency). **Perfect competition vs monopoly:** efficiency, prices, retained profit, supplier choice, production scale, response to change, P = AC = MC vs P > AC, consumer sovereignty.
""", """
পূর্ণ কার্ড: <a href="#e15">Q15</a>।

### Q15 (অংশ ৩) — একচেটিয়া প্রতিযোগিতা (+ একচেটিয়ার সংযোজন)
**একচেটিয়া প্রতিযোগিতা** এমন বাজার কাঠামো যেখানে তুলনামূলক বেশি বিক্রেতা, পৃথকীকৃত পণ্য (প্রায়ই প্রচুর বিজ্ঞাপিত) ও সহজ প্রবেশ-প্রস্থান। **বৈশিষ্ট্য:** ছোট বাজার-অংশ, যোগসাজশ নেই, স্বাধীন সিদ্ধান্ত; গুণ, সেবা, অবস্থান, ব্র্যান্ড ও প্যাকেজিং দিয়ে পৃথকীকরণ, যা দামের ওপর কিছু নিয়ন্ত্রণ দেয়; চাহিদা ডানে সরাতে ও কম স্থিতিস্থাপক করতে প্রচুর বিজ্ঞাপন (অ-দাম প্রতিযোগিতা)। **চাহিদা:** নিম্নমুখী ও খুব স্থিতিস্থাপক (একচেটিয়ার চেয়ে বেশি, পূর্ণ নয়); প্রতিদ্বন্দ্বী বেশি ও পৃথকীকরণ দুর্বল হলে আরও স্থিতিস্থাপক। **স্বল্পমেয়াদ:** MR = MC-তে উৎপাদন; অর্থনৈতিক মুনাফা বা লোকসান। **দীর্ঘমেয়াদ:** মুনাফা প্রবেশ টানে, প্রতিটি ফার্মের চাহিদা বাঁয়ে সরে P = ATC (স্পর্শ) পর্যন্ত: **স্বাভাবিক মুনাফা**; লোকসানে প্রস্থান, চাহিদা ডানে সরে স্বাভাবিক মুনাফা পর্যন্ত। দীর্ঘমেয়াদি ভারসাম্যে P > MC ও P > সর্বনিম্ন ATC (অতিরিক্ত সক্ষমতা)। **ব্যতিক্রম:** নকল-অযোগ্য পৃথকীকরণ, বা বাধা হয়ে দাঁড়ানো ব্যয়বহুল পৃথকীকরণে দীর্ঘমেয়াদেও ছোট মুনাফা থাকতে পারে। **বাধা:** কম।

**একচেটিয়ার সংযোজন:** **দাম-বৈষম্য** — বিভিন্ন ক্রেতাকে ভিন্ন দাম (প্রত্যেকের সর্বোচ্চ; পরিমাণভিত্তিক; গোষ্ঠীভিত্তিক); শর্ত: একচেটিয়া ক্ষমতা, বাজার পৃথকীকরণ, পুনর্বিক্রয় নেই; প্রতিটি বাজারে MR = MC, অস্থিতিস্থাপক বাজারে বেশি দাম, মোট মুনাফা বাড়ে। **সরকারি বনাম বেসরকারি একচেটিয়া** (কল্যাণ ও সাশ্রয়ী দাম বনাম মুনাফা ও দক্ষতা)। **পূর্ণ প্রতিযোগিতা বনাম একচেটিয়া:** দক্ষতা, দাম, সংরক্ষিত মুনাফা, সরবরাহকারী বাছাই, উৎপাদনের আকার, পরিবর্তনে সাড়া, P = AC = MC বনাম P > AC, ভোক্তার সার্বভৌমত্ব।
""")

QUIZ([
    Q('Student discounts on bus tickets are an example of…', 'বাসের টিকিটে ছাত্র ছাড় কিসের উদাহরণ?',
      ['Perfect competition · পূর্ণ প্রতিযোগিতা', 'Price discrimination · দাম-বৈষম্য', 'Predatory pricing · লুণ্ঠনমূলক দাম', 'Collusion · যোগসাজশ'], 1,
      'Different prices for the same service to groups with different elasticities.', 'ভিন্ন স্থিতিস্থাপকতার গোষ্ঠীকে একই সেবায় ভিন্ন দাম।'),
    Q('Which feature makes monopolistic competition "monopolistic"?', 'কোন বৈশিষ্ট্য একচেটিয়া প্রতিযোগিতাকে "একচেটিয়া" করে?',
      ['Many sellers · অনেক বিক্রেতা', 'Easy entry · সহজ প্রবেশ', 'Differentiated products · পৃথকীকৃত পণ্য', 'No advertising · বিজ্ঞাপন নেই'], 2,
      'Each slightly unique product gives the firm some control over its price.', 'প্রতিটি একটু অনন্য পণ্য ফার্মকে দামের ওপর কিছু নিয়ন্ত্রণ দেয়।'),
    Q('In long-run equilibrium, a monopolistically competitive firm earns…', 'দীর্ঘমেয়াদি ভারসাম্যে একচেটিয়া প্রতিযোগী ফার্ম পায়…',
      ['Large economic profit · বড় অর্থনৈতিক মুনাফা', 'Normal profit (P = ATC) · স্বাভাবিক মুনাফা (P = ATC)', 'Continuous losses · অবিরাম লোকসান', 'Zero revenue · শূন্য আয়'], 1,
      'Entry shifts each firm\'s demand left until it is tangent to ATC.', 'প্রবেশে প্রতিটি ফার্মের চাহিদা বাঁয়ে সরে ATC-র স্পর্শক হওয়া পর্যন্ত।'),
    Q('A public monopoly differs from a private one mainly in that it…', 'সরকারি একচেটিয়া বেসরকারি থেকে মূলত আলাদা কারণ এটি…',
      ['Aims at welfare and affordable prices · কল্যাণ ও সাশ্রয়ী দাম লক্ষ্য করে', 'Always makes profit · সবসময় মুনাফা করে', 'Has no costs · কোনো খরচ নেই', 'Sells shares to the public · জনসাধারণের কাছে শেয়ার বেচে'], 0,
      'Slide 8: public monopolies provide welfare services, not profit, financed by government.', 'স্লাইড ৮: সরকারি একচেটিয়া মুনাফা নয়, কল্যাণমূলক সেবা দেয়, সরকারি অর্থায়নে।'),
    Q('The demand curve of a monopolistically competitive firm is more elastic when…', 'একচেটিয়া প্রতিযোগী ফার্মের চাহিদা বেশি স্থিতিস্থাপক হয় যখন…',
      ['There are fewer rivals · প্রতিদ্বন্দ্বী কম', 'Differentiation is strong · পৃথকীকরণ শক্ত', 'There are more rivals and weaker differentiation · প্রতিদ্বন্দ্বী বেশি ও পৃথকীকরণ দুর্বল', 'Advertising is heavy · বিজ্ঞাপন বেশি'], 2,
      'More close substitutes make buyers more price-sensitive.', 'বেশি কাছাকাছি বিকল্প ক্রেতাকে দামের প্রতি বেশি সংবেদনশীল করে।'),
])

SUMMARY("""
- **Price discrimination:** different prices to different buyers; needs monopoly power, market segregation, no resale; higher price in the inelastic market; more total profit.
- **Public vs private monopoly:** welfare, affordable, taxpayer-backed, less efficient vs profit, higher prices, more efficient.
- **PC vs monopoly:** efficiency, price, retained profit, choice, scale, response, P = AC = MC vs P > AC, consumer sovereignty.
- **Monopolistic competition:** many sellers, differentiated products, heavy advertising, easy entry; highly elastic demand; short-run profit/loss; long-run **normal profit** (P = ATC) with excess capacity; exceptions when differentiation can't be copied.

**Next:** Lecture 11: **oligopoly**, a market of a few big firms.
""", """
- **দাম-বৈষম্য:** ভিন্ন ক্রেতাকে ভিন্ন দাম; শর্ত একচেটিয়া ক্ষমতা, বাজার পৃথকীকরণ, পুনর্বিক্রয় নেই; অস্থিতিস্থাপক বাজারে বেশি দাম; মোট মুনাফা বেশি।
- **সরকারি বনাম বেসরকারি একচেটিয়া:** কল্যাণ, সাশ্রয়ী, করদাতা-সমর্থিত, কম দক্ষ বনাম মুনাফা, বেশি দাম, বেশি দক্ষ।
- **পূর্ণ প্রতিযোগিতা বনাম একচেটিয়া:** দক্ষতা, দাম, সংরক্ষিত মুনাফা, বাছাই, আকার, সাড়া, P = AC = MC বনাম P > AC, ভোক্তার সার্বভৌমত্ব।
- **একচেটিয়া প্রতিযোগিতা:** অনেক বিক্রেতা, পৃথকীকৃত পণ্য, প্রচুর বিজ্ঞাপন, সহজ প্রবেশ; খুব স্থিতিস্থাপক চাহিদা; স্বল্পমেয়াদে মুনাফা/লোকসান; দীর্ঘমেয়াদে **স্বাভাবিক মুনাফা** (P = ATC), অতিরিক্ত সক্ষমতাসহ; নকল-অযোগ্য পৃথকীকরণে ব্যতিক্রম।

**পরবর্তী:** লেকচার ১১: **অলিগোপলি**, কয়েকটি বড় ফার্মের বাজার।
""")
