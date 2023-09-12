import requests

# Define the sneaker data to be sent in JSON format
sneakers_data = [
    
    {
        "image": "https://images.stockx.com/images/Nike-Air-Force-1-Low-SP-Tiffany-And-Co-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1676727983",
        "name": "Nike Air Force 1 Low Tiffany & Co. 1837",
        "description": "Nike\u2019s first-ever collaboration with Tiffany & Co. comes in the form of a luxurious Air Force 1.\n<br>\n<br>\nThis updated take on the iconic basketball sneaker features elevated details that include a sterling silver piece on the heel, a suede upper, and a signature Tiffany Blue shade on a tumbled suede Swoosh. Additional elements such as a black soft leather lining and \"tiffany\" cursive branding on the tongue make these a rich and subtle pair of Air Force 1s.\n<br>\n<br>\nThe Nike Air Force 1 Tiffany & Co. 1837 released in March of 2023 and retailed for $400.",
        "model": "Nike Air Force 1 Low",
        "brand": "Nike",
        "sku": "DZ1382-001",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Adidas-Pro-Model-II-Big-Sean-Detroit-Player.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1626898870",
        "name": "adidas Pro Model II Big Sean Detroit Player",
        "description": "Designed in collaboration with rapper Big Sean, the adidas Pro Model Promo ‘Detroit Player’ features a luxurious build, highlighted by a red leather upper finished in a subtle reptilian texture. The rubber shell toe is finished in matching red, while distressed tonal suede is used on the signature Three-Stripes, eyestay and heel tab. Metallic gold hardware adds to the shoe’s premium look and feel.",
        "model": "adidas Pro Model II",
        "brand": "adidas",
        "sku": "Q33025",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-Bred-2016-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606318705",
        "name": "Jordan 1 Retro High Bred Banned (2016)",
        "description": "The shoe that started it all. In 1985,  Nike partnered with a young superstar in the making, Michael Jordan, and changed the game by releasing the Air Jordan, now known as the Air Jordan 1. It was rumored that this black and red colorway was banned by the NBA for violating the league's dress code, leading to the shoe's reputation as the banned Jordans. While this story was most likely a marketing move on Nike's part as it has never been confirmed, the legend of the Air Jordan 1 Bred lives on.\n<br>\n<br>\nThe Air Jordan 1 Bred 2016 featured a black and Varsity Red leather upper with Swoosh overlays and Wings logo detailing at the collar. Vintage-styled Nike Swoosh woven tongue tags add a classic feel. From there, a white and red Air sole completes the design.\n<br>\n<br>\nThe Air Jordan 1 Bred 2016 released in September of 2016 and retailed for $160.\n<br>\n<br>\nTo shop all Air Jordan 1 shoes, <a href=\"https://stockx.com/retro-jordans/air-jordan-1\">click here.</a> ",
        "model": "Jordan 1 Retro High",
        "brand": "Jordan",
        "sku": "555088-001",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-3-Retro-A-Ma-Maniere-W-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1619806955",
        "name": "Jordan 3 Retro A Ma Mani\u00e9re (Women's)",
        "description": "After a slew of collaborative releases with adidas and Nike, DC-based sneaker boutique A Ma Mani\u00e9re teamed up with Jordan Brand to release a women\u2019s exclusive Jordan 3 with the Air Jordan 3 A Ma Mani\u00e9re (W). The release aligns with their short film Raised By Women, an ode to the strides and accomplishments of everyday women in urban communities.\n\nThe Air Jordan 3 A Ma Mani\u00e9re arrives featuring a white tumbled leather upper with Medium Grey suede on the toe wrap, eyestay, heel wrap, and ankle. Each panel of leather on the upper has a raw trim, revealing a natural, tan edge. To provide a vintage aesthetic, the eyelets, heel tab, and lower portion of the midsole are yellowed. From there, the tongue on the left sneaker features an embroidered A Ma Mani\u00e9re logo, while the right features a Jumpman logo. Quilted satin lining on the interior of the shoe adds an element of luxury. A white, Violet Ore, and Medium Grey sole with a classic Air unit in the heel completes this retro look.\n\nThe women's Air Jordan 3 A Ma Mani\u00e9re released in April of 2021 and retailed for $200.",
        "model": "Jordan 3 Retro",
        "brand": "Jordan",
        "sku": "DH3434-110",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-White-Cement-2016-Product_V2.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1690294620",
        "name": "Jordan 4 Retro White Cement (2016)",
        "description": "The Air Jordan 4 Retro White Cement 2016 features the classic 1989 colorway White/Fire Red/Black/Tech Gray. Black waffle eyestays and white mesh enhance the white leather upper. \"Cement\" refers to the black-speckled gray accents on the midsole, wings, and heel. A black Nike Air logo and Swoosh appear just below a cement-pattern heel tab. The white tongue features a red Jumpman above \"Flight\" printed in black. The black insole has a red Nike Air logo and Swoosh. The white midsole has visible Air. The rubber outsole includes every color in the colorway.\n<br>\n<br>\nThe Air Jordan 4 Retro White Cement 2016 was released on February 12, 2016, at a retail price of $220.",
        "model": "Jordan 4 Retro",
        "brand": "Jordan",
        "sku": "840606-192",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-Pinnacle-Vachetta-Tan-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1635779837",
        "name": "Jordan 1 Retro Pinnacle Vachetta Tan",
        "description": "The premise for the Nike Air Jordan 1 Pinnacle 'Vachetta Tan' was wear over time. Similar to a baseball glove, the more someone wore it, the more the leather broke in and settled into a well-worn sneaker that conformed to your foot. The shoe also came with two sets of premium waxed laces in two different shades of tan and a dust bag.",
        "model": "Jordan 1 Retro",
        "brand": "Jordan",
        "sku": "705075-201",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-Air-Max-1-Atmos-Animal-Pack-2-2018-Black-Box-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606325108",
        "name": "Nike Air Max 1 Atmos Animal Pack 2.0 (All Black Box) (2018)",
        "description": "The Jungle Book has got nothing on these Nike Air Max 1 Atmos Animal Packs.\nMade in collaboration with Atmos, these are a new take on the classic \"Animal\" AM95, originally released in 2007. Coming in wheat, sport red, bison and classic green, they feature a synthetic tiger, leopard, zebra and pony printed upper. Red accents the \"Swoosh\" on the sides while black detailing on the upper, replacing the ivory found on the OG\u2019s finishes this pair off.  They first dropped on March 2nd, 2018, exclusively via the Nike SNKRS Pass to NYC-based customers via the SNKRS app. A second drop followed on March 17th, 2018, at select Nike Sportswear retailers worldwide. If you want your Air Max collection to have some of that jungle juice, these are a must. Those looking for a pair can buy these Nike Air Max 1 Atmos Animal Pack 2.0 online today by placing a Bid on StockX.",
        "model": "Nike Air Max 1",
        "brand": "Nike",
        "sku": "AQ0928-700",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-3-Retro-Black-Cement-2018-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1609356781",
        "name": "Jordan 3 Retro Black Cement (2018)",
        "description": "One of the most anticipated releases of 2018, the Air Jordan 3 Retro OG marked the first time original \"Nike Air\" branding was featured on the \"Black Cement\" AJ 3 since it's 2001 retro. Jordan stuck to the mantra of \"if it aint broke, don\u2019t fix it,\" on these, staying true to the OG with a black-based leather upper with cement grey, fire red, and white accents, finished off by the iconic elephant print detailing. Their release date was on Michael Jordan's 55th birthday, February 17th, 2018, and went for $200 in mens sizes. The \"Black Cement\" Air Jordan 3 Retro OG is a must-have, and you don't need us to tell you that. They should be in everyone's collection, multiples if possible. If you're on the hunt for a pair, you can buy them online today. Those with a pair to sell can hit up the StockX marketplace and see what they're currently going for.",
        "model": "Jordan 3 Retro",
        "brand": "Jordan",
        "sku": "854262-001",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-Bred-Toe-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606322598",
        "name": "Jordan 1 Retro High Bred Toe",
        "description": "Combining elements of three certified classic AJ1\u2019s, the 2018 Jordan 1 Retro High Bred Toe is like the Coachella lineup of OG 1s. Coming in gym red, black, and summit white, with red on the toe box, outsole, and wrapping around the ankle and heel, white side panels and midsole and black covering the rest of the sneaker, it\u2019s a perfectly balanced mash-up of the Banned, Chicago, and Black Toe all in one. Originally releasing in February of 2018, the Bred toe has been one of the most popular sneakers on StockX since its drop. For fans of the AJ1, this colorway is a must Bid.",
        "model": "Jordan 1 Retro High",
        "brand": "Jordan",
        "sku": "555088-610",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-OG-Essentials-Sail-Product.png?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1686755741",
        "name": "Jordan 1 Retro High OG Sail",
        "description": "The Air Jordan 1 Retro High OG Essentials Sail is a retro-inspired Air Jordan 1 sneaker from the \"Premium Essentials\" pack in a Sail colorway.\n<br>\n<br>\nThis sneaker features a Sail leather upper accented in University Red, visible on the \u2018Nike Air\u2019 tongue tag branding. Other details include a perforated toe box, the \u2018Air Jordan\u2019 Wings logo stamped on the upper collar, and Sail Swooshes on the laterals and medials. Rounding out the design is a tonal midsole and rubber outsole. The sneaker comes with an extra set of University Red laces.\u00a0\n<br>\n<br>\nThe Air Jordan 1 Retro High OG Essentials Sail was released on 20th June 2017, retailing at $160.",
        "model": "Jordan 1 Retro High OG",
        "brand": "Jordan",
        "sku": "555088-114",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-5-Retro-Premium-Wine-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1608520360",
        "name": "Jordan 5 Retro Premium Wine",
        "description": "This Air Jordan 5 Retro is nicknamed the \"Wine\" edition. The fourth \"Premium\" release of 2017, they come in a bordeaux, sail, and elemental gold colorway. Featuring a bordeaux-based premium leather upper with perforated lines on the sides instead of traditional mesh netting. A gold quilted leather collar and sail colored translucent gum hits on the outsole finish things off. Their release date was December 14th, 2017 at select Jordan Brand retailers worldwide. Available in men's sizes only, they retailed for $400 and came in special packaging. If you missed out on the \"Burgundy\" AJ 5 LS from 2006, you need to have the \"Wine\" Air Jordan 5 Retro Premium in your collection. Those looking for a pair can buy the online now. Others that have pairs to sell can unload them via the marketplace.",
        "model": "Jordan 5 Retro Premium",
        "brand": "Jordan",
        "sku": "881432-612",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-OG-Chicago-Reimagined-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1665691099",
        "name": "Jordan 1 Retro High OG Chicago Lost and Found",
        "description": "The original Air Jordan 1 Chicago colorway was first introduced in 1985 and has only been retroed a few times since. But 2022 is the year that the colorway returns with an added vintage look. Pre-yellowed accents and cracked leather uppers showcase a fabricated look of age and wear. The Air Jordan 1 Lost and Found Chicago released in November of 2022 for $180.",
        "model": "Jordan 1 Retro High OG",
        "brand": "Jordan",
        "sku": "DZ5485-612",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-Un-Supreme-Product.png?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1686755754",
        "name": "Jordan 1 Retro Un-Supreme",
        "description": "The Nike Air Jordan 1 Retro High 'Black Elephant' features a black leather and cement grey elephant print upper reminiscent of the iconic 2002 Supreme x Dunk Low Pro SB. Released in January 2016, the look is finished off with Varsity Red accents, a white midsole, and a black outsole.",
        "model": "Jordan 1 Retro",
        "brand": "Jordan",
        "sku": "839115-013",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-Raptors-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606316804",
        "name": "Jordan 4 Retro Raptors (2018)",
        "description": "If you want a pair that feels like some early 2000's Vin-sanity, the Jordan 4 Raptors are exactly what you need. These Toronto-themed Js come in a black, court purple and university red colorway, and sport a black-based suede upper with red and purple accents and paint splatter detailing on the midsole. Their release date was in August 2018, where they were available at select Jordan Brand retailers worldwide for $200. If you\u2019re a fan of the AJ 4, have a \"We The North\" t-shirt in you closet, and are running through the 6 with your woes, you need to own this pair.",
        "model": "Jordan 4 Retro",
        "brand": "Jordan",
        "sku": "AQ3816-065",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-Air-Max-1-SP-Concepts-Denim-Tiger-Camo-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1647032458",
        "name": "Nike Air Max 1 SP Concepts Heavy",
        "description": "PLEASE NOTE: Print Patterns May Vary. Nike and Concepts joined forces once again for the 1970's inspired Nike Air Max 1 SP Concepts Heavy.\n<br>\n<br>\nThe Nike Air Max 1 SP Concepts Heavy nods to youth culture of the 1970's and their style. Bleached denim, bandana, corduroy, and tiger camo M-65 jacket material make up the upper, offering a playful look. On the Swooshes, embroidered flowers add a vintage-inspired styling. From there, a speckled white midsole with a gum outsole completes the design.\n<br>\n<br>\nThe Nike Air Max 1 SP Concepts Heavy released in March of 2022 and retailed for $170.",
        "model": "Nike Air Max 1 SP",
        "brand": "Nike",
        "sku": "DN1803-900",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/New-Balance-997S-Bodega-No-Bad-Days-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607047522",
        "name": "New Balance 997S Bodega No Bad Days",
        "description": "Originally released exclusively at Bodega locations and their online store, the New Balance 997S Bodega No Bad Days is now available to customers around the world on StockX. As part of an ongoing collaboration between these two Boston-born companies, this model of the 997 is a sequel to the previously released No Days Off 997S.\n<br>\n<br>\nThis 997S features rubber and synthetic materials on the tongue and heel, highlighted with aqua, yellow, and red accents on the branding, tongue, and heel. A New Balance signature two-tone ENCAP midsole finalizes this new installment in the extensive history of these two companies. These sneakers released in September of 2019 for $160.",
        "model": "New Balance 997S",
        "brand": "New Balance",
        "sku": "MS997JBG",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-A-Ma-Maniere-Violet-Ore_V2-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1671732043",
        "name": "Jordan 4 Retro A Ma Mani\u00e9re Violet Ore",
        "description": "James Whitner\u2019s A Ma Mani\u00e9re and Jordan Brand partner up for this luxury AJ 4 silhouette. The new Air Jordan 4 A Ma Mani\u00e9re features a deeply rich Violet Ore and vintage cream tones. Sleek metallic pins, tonal mesh detailing and a quilted interior add luxe detailing throughout the silhouette.\n<br>\n<br>\nThe Air Jordan 4 A Ma Mani\u00e9re released in November of 2022 and retailed for $225.",
        "model": "Jordan 4 Retro",
        "brand": "Jordan",
        "sku": "DV6773-220",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-9-Retro-Bred-Patent-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607657108",
        "name": "Jordan 9 Retro Bred Patent",
        "description": "Originally made in 2002 as a PE for Miami Heat legend Eddie Jones, the Air Jordan 9 Bred Patents were never released to the public...until now. In 2018, Jordan Brand busted open the vault for this remastered version, known as the \"Bred Patent\" edition. They come in a black, university red, and anthracite colorway, and sport a black-based leather upper with patent leather detailing. Red branding throughout and a dark grey colored sole finishes things off. These legendary AJ9s released on March 10th, 2018, for $190, and released with full-family sizing, down to toddler. Any fan of the Bred colorway should add these to their collection ASAP.",
        "model": "Jordan 9 Retro",
        "brand": "Jordan",
        "sku": "302370-014",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-Patent-Gold-Toe-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606321591",
        "name": "Jordan 1 Retro High NRG Patent Gold Toe",
        "description": "After the \"Gold Top 3\" AJ1s dropped at ComplexCon in 2017, Nike decided to strike while the gold was hot with the Jordan 1 Retro High NRG Patent Gold Toe. Known as the \"Patent Gold Toe\" edition, these AJ 1\u2019s came in the same black, metallic gold and summit white colorway as the \"Gold Top 3s.\" However, they feature gold toes and tongue tags as well as black tongues on both sneakers. The medial of each shoe is also in black/gold while the lateral in white, black and gold. Their release date was February 16th, 2018, costing the usual $160 in men\u2019s sizes and $120 for grade school sizes. Another must-have for fans of the Air Jordan 1, you can use your \"golden touch\" to buy or sell this Air Jordan 1 Retro High OG online today on StockX.",
        "model": "Jordan 1 Retro High NRG",
        "brand": "Jordan",
        "sku": "861428-007",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-Lebron-12-NSRL-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1614778864",
        "name": "Nike LeBron 12 NSRL",
        "description": "The Nike LeBron 12 ‘NSRL’ released in November 2014 as the lead colorway of the silhouette. The design features a Hyper Turquoise Megafuse upper with Cool Grey Hyperposite wings, supported underfoot by five multicolored, hexagonally shaped Nike Zoom Air bags in the icy translucent outsole. The NSRL color is inspired by the real life Nike Sports Research Lab, where scientific data and analysis helps guide the future of footwear.",
        "model": "Nike LeBron 12",
        "brand": "Nike",
        "sku": "684593-301",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-SB-Lakers-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607649923",
        "name": "Jordan 1 Retro High OG Defiant SB LA to Chicago",
        "description": "Drop some magic on the haters after copping the Jordan 1 Retro High OG Defiant SB Lakers. This AJ 1 SB comes with a white upper plus blue and yellow accents, yellow Nike \"Swoosh\", white midsole, and a black sole. These sneakers released in May 2019 and retailed for $175. Buy these kicks on StockX today.",
        "model": "Jordan 1 Retro High OG Defiant",
        "brand": "Jordan",
        "sku": "CD6578-507",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-6-Retro-Travis-Scott-British-Khaki-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1620406101",
        "name": "Jordan 6 Retro Travis Scott British Khaki",
        "description": "Travis Scott and Jordan Brand teamed up to deliver the Air Jordan 6 Retro Travis Scott British Khaki. The British Khaki marks the second time that Travis has added his touch to the Jordan 6 silhouette, the first being the 2019 Air Jordan 6 Travis Scott.\n<br>\n<br>\nThe upper of the Air Jordan 6 Retro Travis Scott British Khaki is made of British Khaki suede. From there, hits of Bright Crimson appear on the heel and tongue embroidered logos. The upper also has two cargo pockets: one with a snap enclosure on the lateral ankle and one with a zip enclosure on the medial ankle. A translucent tongue, heel tab, and outsole that glows in the dark adds the finishing touches to this latest Travis Scott Jordan. \n<br>\n<br>\nThe Air Jordan 6 Retro Travis Scott British Khaki released in April of 2021 and retailed for $250.",
        "model": "Jordan 6 Retro",
        "brand": "Jordan",
        "sku": "DH0690-200",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-Equality-Product.png?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1686755736",
        "name": "Jordan 1 Retro High Equality Black History Month (2018)",
        "description": "The look of the Air Jordan 1 Retro High Equality Black History Month (2018) is inspired by three primary colors: metallic gold, white, and black.\n<br>\n<br>\nThe leather top of the Retro High Equality Air Jordan 1 features a black and white color scheme. The top half of the upper is divided into two sections, the bottom half being white and the top half being black. A shiny gold dubrae near the toe, Carmelo Anthony's Jordan PE emblem on the tongue patch, and the word \"Equality\" printed on the heel portion of the white midsoles of the shoes are further details.\n<br>\n<br>\nThe Air Jordan 1 Retro High Equality Black History Month (2018) was recommended to retail at $145 during its launch on January 15th, 2018.",
        "model": "Jordan 1 Retro High",
        "brand": "Jordan",
        "sku": "AQ7474-001",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-Winter-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606316899",
        "name": "Jordan 4 Retro Winterized Loyal Blue",
        "description": "Jordan Brand spins an iconic design for winter with the Jordan 4 Retro Winterized Loyal Blue, now available on StockX. Reminiscent of the extremely limited Eminem Encore 4, this release gives many of us the opportunity to own a blue toned Jordan 4 without having to spend more than the cost of a car. The difference between this winterized design and a traditional Jordan 4 lies in the material choices. The Winterized 4 replaces the classic mesh insert panels with a canvas-like material and adopts a fleece lining to retain warmth.\n<br>\n<br>\nThis Jordan 4 Retro is comprised of a loyal blue upper with red accents. Grey and black detailing, a white midsole, and grey outsole completes the design. These sneakers released in December of 2019 for $200.",
        "model": "Jordan 4 Retro",
        "brand": "Jordan",
        "sku": "CQ9597-401",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-RE2PECT-Derek-Jeter-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607048949",
        "name": "Jordan 1 Retro High RE2PECT (Derek Jeter)",
        "description": "The Air Jordan 1 Retro High RE2PECT Derek Jeter is a special iteration of the Air Jordan 1 silhouette paying tribute to baseball legend Derek Jeter in celebration of his successful career with the Yankees.\n<br>\n<br>\nThe shoe features a navy-blue suede and white leather upper, in respect to the Yankees' colors, with the Air Jordan wings logo on the ankle collar and Nike Air branding on the tongue. It also bears special branding on the collar in a tonal text print, with inspirational words such as \"Re2Spect,\" \"Fearless,\" \"Discipline,\" and \"Focus.\"\n<br>\n<br>\nThe Air Jordan 1 Retro High RE2PECT Derek Jeter was released for retail priced at $160 on November 18, 2017.",
        "model": "Jordan 1 Retro High",
        "brand": "Jordan",
        "sku": "555088-008",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-SB-Dunk-Low-Concepts-Orange-Lobster-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1681136628",
        "name": "Nike SB Dunk Low Concepts Orange Lobster",
        "description": "The Nike SB Dunk Low Concepts Orange Lobster\u00a0comes toned in a mixture of three main colors: electro orange, orange frost, and white.\n<br>\n<br>\nThis Low Nike SB Dunk features a nubuck upper with varying orange tones, softly speckled overlays, and a tonal Swoosh accented in white. The interior lining is embellished with a bib-inspired pattern, and the white mesh tongue is embellished with a woven Nike SB tag. The shoe boasts an orange rubber outsole and a cupsole with black sidewalls.\n<br>\n<br>\nThe Nike SB Dunk Low Concepts Orange Lobster was set to retail at $120 at its market launch on December 20th, 2022.",
        "model": "Nike SB Dunk Low",
        "brand": "Nike",
        "sku": "FD8776-800",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-Travis-Scott-Cactus-Jack-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1682532259",
        "name": "Jordan 4 Retro Travis Scott Cactus Jack",
        "description": "The only way to describe the Travis Scott Air Jordan 4 Retros properly would be to use the rappers own adlib: la flame. These Jordan 4s were made in collaboration with rapper, Travis Scott and nicknamed the \"Cactus Jack\" edition. Similar in design to the infamous Eminem pair, these feature a lighter shade of blue suede on the upper. Black accents, a red liner, paint splatter detailing, a white midsole and \"Cactus Jack\" branding on the back heel tab finish things off for this pair. These dropped in June of 2018 for $225 and came exclusively in men\u2019s sizes. If you\u2019re a fan of Travis Scott and the AJ 4, this pair is another must-have. Straight up!",
        "model": "Jordan 4 Retro",
        "brand": "Jordan",
        "sku": "308497-406",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-11-Retro-Low-Derek-Jeter-Re2pect-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607649913",
        "name": "Jordan 11 Retro Low Derek Jeter RE2PECT",
        "description": "Start spreading the news, the Jordan 11 Retro Low Derek Jeter RE2PECT will have you singing \"New York, New York\" in no time. This Air Jordan 11 Retro took the elusive \"Derek Jeter\" premium high-top from 2017 and converted it into low-top in 2018. As the \"Re2pect\" edition, they come in a New York Yankees-themed binary blue and sail colorway and sport a full suede upper with Jeter\u2019s jersey number, \"2\" embroidered on the back heels. A full translucent gum outsole and two sets of laces, rope and leather finish this pair off. These dropped in May of 2018 for a cool $200, but for Yankees fans, they are priceless. If you\u2019re a fan of Derek Jeter, the New York Yankees and the Air Jordan 11, you need to hit that Bid button.",
        "model": "Jordan 11 Retro Low",
        "brand": "Jordan",
        "sku": "AV2187-441",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-13-Retro-He-Got-Game-2018-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606323382",
        "name": "Jordan 13 Retro He Got Game (2018)",
        "description": "Paying homage to the cult-classic movie of the same name, the Jordan 13 Retro \"He Got Game\" is based on the pair Denzel Washington wore in the 1998 film. Directed by Spike Lee, Washington originally wore this pair of classic kicks while playing ball against his basketball prodigy son, Jesus Shuttlesworth (Ray Allen). The shoes feature a buttery leather upper in white and black, a green hologram on the side panel, and a red and white outsole. These dropped in August 2018 for $190. Do the right thing and grab a pair today on StockX.",
        "model": "Jordan 13 Retro",
        "brand": "Jordan",
        "sku": "414571-104",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-5-Retro-P51-Camo-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607650434",
        "name": "Jordan 5 Retro P51 Camo",
        "description": "The Air Jordan 5 Retro P51 Camo arrives in a dark stucco, university red-river rock color scheme.\n<br>\n<br>\nThe Jordan 5 Retro P51 Camo has an upper that features a light grey suede with dark stucco and university red accents, and it also features perforated sides for breathability. The midsole is made of lightweight foam with an air cushioning unit for comfort and responsiveness. The rubber outsole of the shoe is both grippy and long-lasting. The shoe's lace-up tie offers a secure fit, while the cushioned tongue and ankle collar provide both support and comfort. The sneaker features a Jumpman logo on the tongue and \"AIR 23\" branding on the heel.\n<br>\n<br>\nThe Air Jordan 5 Retro P51 Camo was released on September 2, 2017, at a retail price of $190.",
        "model": "Jordan 5 Retro",
        "brand": "Jordan",
        "sku": "136027-051",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-LeBron-7-Florida-A-M-University-Gorge-Green-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1675275027",
        "name": "Nike LeBron 7 FAMU Gorge Green",
        "description": "",
        "model": "Nike LeBron 7",
        "brand": "Nike",
        "sku": "DX8554-300",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/New-Balance-997S-Bodega-Better-Days-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1629134912",
        "name": "New Balance 997S Bodega Better Days",
        "description": "The New Balance 997S Bodega Better Days is a collaboration between New Balance and the Bodega streetwear brand.\n<br>\n<br>\nThe New Balance 997S Bodega Better Days has a gray palette with touches of\u00a0orange,\u00a0red, yellow, and white embellishments. The upper of the shoe is composed of leather, suede, and mesh. The shoe features the trademark \"N\" branding\u00a0of New Balance on the sides and a durable\u00a0rubber outsole for increased traction. This sneaker's midsole is constructed with New Balance's ENCAP technology, which offers lightweight cushioning and stability. The midsole also features the innovative ABZORB cushioning technology developed by New Balance.\n<br>\n<br>\nThe New Balance 997S Bodega Better Days was released on\u00a0September 25th, 2020, for a retail price of $160.",
        "model": "New Balance 997S",
        "brand": "New Balance",
        "sku": "MS997JBO",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-Canyon-Purple-W-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1660285854",
        "name": "Jordan 4 Retro Canyon Purple (Women's)",
        "description": "The Air Jordan 4 Retro Canyon Purple W was inspired by Tinker Hatfield\u2019s 1989 design. This shoe replaces the traditional leather or nubuck build.\n<br>\n<br>\nThis Air Jordan 4 for women has an upper that is crafted from shaggy suede in a vibrant purple color finish. Lime green accents land on the speckled eyelets and midsole, while the signature Jumpman logo graces the woven tongue tag in Safety Orange. The bright hues are offset by contrasting hits of black on the molded wings, Jumpman-embossed heel tab, and herringbone-traction rubber outsole.\n<br>\n<br>\nThe Air Jordan 4 Retro Canyon Purple W was released on the 15th of October 2022, and originally retailed for $200.",
        "model": "Jordan 4 Retro",
        "brand": "Jordan",
        "sku": "AQ9129-500",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-Strap-A-Tribe-Called-Quest-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1646080630",
        "name": "Jordan 1 Retro High Strap A Tribe Called Quest",
        "description": "Inspired by A Tribe Called Quest’s album artwork for Midnight Marauders, the Air Jordan 1 High Strap ‘A Tribe Called Quest’ is embellished with a similar pattern throughout the canvas underlays, while the rest of the upper is fashioned with premium leather panels. Accented with a patent leather Swoosh, the shoe also incorporates an elastic strap around the collar to enhance stability.",
        "model": "Jordan 1 Retro",
        "brand": "Jordan",
        "sku": "342132-062",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-4-Retro-SE-Black-Canvas-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1664433335",
        "name": "Jordan 4 Retro SE Black Canvas",
        "description": "The Air Jordan 4 Retro SE Black Canvas arrives in a neutral color scheming with contrasting touches of crimson red.\n<br>\n<br>\nThis Black Canvas Air Jordan is a mid-top sneaker with a black canvas upper complemented by a gray tonal suede which covers the eyelets and forefoot overlays. A gray Jumpman logo graces the heel and woven tongue tag, with the latter getting a crimson Flight logo. The sneaker also rides on a two-tone polyurethane midsole with visible Air-sole cushioning in the heel.\n<br>\n<br>\nThe Air Jordan 4 Retro SE Black Canvas was released on the 5th of October 2022, and retailed at a price of $210.",
        "model": "Jordan 4 Retro SE",
        "brand": "Jordan",
        "sku": "DH7138-006",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-3-Retro-Tinker-Hatfield-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606315675",
        "name": "Jordan 3 Retro Tinker Hatfield",
        "description": "Coming straight out the legendary Tinker Hatfield\u2019s sketchbook, the Air Jordan 3 Retro Tinker Hatfield is an OG sketch finally come to life. The shoe features a mix of both white cement and black cement hues, with Swoosh logos highlighted on the side and Nike Air branding on the heels. With sketched graphic insoles and Tinker\u2019s personal signature featured on the inside of the tongues, these are a must-own for fans of the 3s. The shoes initially dropped in March of 2018, retailing at a cool $200. If you feel like Tinker, throw up a Bid or an Ask on these icons today.",
        "model": "Jordan 3 Retro",
        "brand": "Jordan",
        "sku": "AQ3835-160",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-5-Retro-DJ-Khaled-We-The-Best-Sail-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1669100641",
        "name": "Jordan 5 Retro DJ Khaled We The Best Sail",
        "description": "The Air Jordan 5 Retro DJ Khaled We The Best Sail comes toned in a mixture of three colors; violet star, washed yellow, and sail.\n<br>\n<br>\nThis collaborative Air Jordan 5 has an off-white leather upper. The shoe also has a quilting lining in powder blue and a midsole made of Violet Star Air-assisted Polyurethane. A vintage Jumpman emblem with the words \"Keep Going\" on the inside and a shiny silver polish on the outside decorates the tongue. On uneven heel overlays, the 'We the Best' branding and the Nike Air insignia are visible.\n<br>\n<br>\nThe Air Jordan 5 Retro DJ Khaled We The Best Sail retailed for $225 on its market debut in November 2022.",
        "model": "Jordan 5 Retro",
        "brand": "Jordan",
        "sku": "DV4982-175",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-OG-A-Ma-Maniere-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1638286909",
        "name": "Jordan 1 Retro High OG A Ma Mani\u00e9re",
        "description": "The Air Jordan 1 A Ma Mani\u00e9re features a premium cracked leather upper with burgundy reptilian-textural leather collars and Swooshes. Silky quilted lining and custom woven tongue and insole labels add a sense of luxury. At the base, a yellowed sole provides a vintage feel to complete the design.\n<br>\n<br>\nThe Air Jordan 1 A Ma Mani\u00e9re released in November of 2021 and retailed for $200.",
        "model": "Jordan 1 Retro High OG",
        "brand": "Jordan",
        "sku": "DO7097-100",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-High-Gatorade-Blue-Lagoon-Product.png?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1686755730",
        "name": "Jordan 1 Retro High Gatorade Blue Lagoon",
        "description": "The Air Jordan 1 Retro High Gatorade Blue Lagoon is dressed in two colors, blue lagoon and yellow hues.\n<br>\n<br>\nThis High Retro Air Jordan 1 shoe's monochrome blue coloring is complemented by orange branding, which includes\u00a0a Nike Air tongue tag\u00a0that has a similar design to a Gatorade bottle cap, as well as a lightning bolt at the heel. The complete the themed-aesthetic, there is a logo visible underneath the translucent outsole. Air units are included on the soles of the sneaker.\n<br>\n<br>\nThe Air Jordan 1 Retro High Gatorade Blue Lagoon was set to sell at $175 during its launch on December 26th, 2017.",
        "model": "Jordan 1 Retro High",
        "brand": "Jordan",
        "sku": "AJ5997-455",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/New-Balance-992-Todd-Snyder-10th-Anniversary-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1641935326",
        "name": "New Balance 992 Todd Snyder 10th Anniversary",
        "description": "To celebrate his 10th anniversary in business, Todd Synder teamed up with New Balance in releasing the New Balance 992 Todd Snyder 10th Anniversary.\u00a0\n<br>\n<br>\nThe sneaker features an upper covered with tanned leather overlays in grey and a breathable meshed vamp, while at the same time presenting a contrast with subtle accents of soft tangerine on eyelets, USA embroidery atop the tongue, and the heel tab. Apart from that, a silver shade can be seen on the N emblem on the side panels and the NB signature brand on the heel stabilizer. Finishing off the shoe is a white stacked cushioning midsole.\u00a0\n<br>\n<br>\nThe New Balance 992 Todd Snyder 10th Anniversary was released on January 12th, 2021, and retailed at a price of $240.",
        "model": "New Balance 992",
        "brand": "New Balance",
        "sku": "M992TA",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/NikeCraft-General-Purpose-Shoe-Tom-Sachs-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1655990902",
        "name": "NikeCraft General Purpose Shoe Tom Sachs",
        "description": "After a brief hiatus following the renowned Mars Yard series, Nike and Tom Sachs joined forces once again in 2022 for the NikeCraft General Purpose Shoe.\n<br>\n<br>\nThe NikeCraft General Purpose Shoe (GPS) is a minimalist, do-everything shoe that will thrive in any possible scenario thrown your way. In a clean styling, the GPS boasts a three-piece molded cup sole, suede mudguards, microfiber collar, and an ultra-breathable knit that is open enough to breathe but tight enough to fend off rain and snow. Touching on Sachs' previous designs, a waffle tread outsole similar to that of the first Nike Moon Shoe and a tongue with exposed foam edges adds a vintage appeal.\n<br>\n<br>\nThe NikeCraft General Purpose Shoe released in June of 2022 and retailed for $110.",
        "model": "NikeCraft General Purpose Shoe",
        "brand": "Nike",
        "sku": "DA6672-200",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-SB-Light-Bone-Black-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607649848",
        "name": "Jordan 1 Retro High OG Defiant SB NYC to Paris",
        "description": "Grab a fresh pair of Nike SB's and cop the Jordan 1 Retro High OG Defiant SB Light Bone. This AJ 1 SB comes with a grey upper plus white and black accents, black Nike \"Swoosh\", white midsole, and a white sole. These sneakers released in May 2019 and retailed for $175. Place a Bid on these sneakers today.",
        "model": "Jordan 1 Retro High OG Defiant",
        "brand": "Jordan",
        "sku": "CD6578-006",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-1-Retro-AJKO-Royal-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1607046696",
        "name": "Jordan 1 Retro AJKO Royal",
        "description": "The Jordan 1 Retro AJKO Royal was released as part of the Jordan 1 collection.\n<br>\n<br> \nThe upper of the Air Jordan 1 Retro AJKO Royal is made from premium quality canvas material, which provides durability and flexibility for long-lasting wear. The Jordan Wings logo is prominently displayed on the side of the shoe, while the Nike logo appears on the tongue. The shoe features a cushioned footbed and a padded tongue and collar to provide superior support and comfort for your feet. The outsole is made from rubber, which provides excellent traction and durability on any surface.\n<br>\n<br> \nThe standout feature of the Jordan 1 Retro AJKO Royal is its bold and unique colorway. The black and blue combination is eye-catching, and makes a statement on the court or in casual settings. Additionally, the canvas material used in the upper of the shoe sets it apart from other Jordan 1 models, making it a standout piece in any sneaker collection. The shoe was released on August 23rd, 2014, at a list price of $140.",
        "model": "Jordan 1 Retro",
        "brand": "Jordan",
        "sku": "638471-007",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-3-Retro-White-Cement-Reimagined-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1678266994",
        "name": "Jordan 3 Retro White Cement Reimagined",
        "description": "Jordan is traveling back in time to 1988 for the next part of their Reimagined series, with the release of the Air Jordan 3 Retro White Cement Reimagined. \n<br>\n<br>\nJordan used the same design and specs as the original 1988 Jordan 3 silhouette to help craft the second model of the Reimagined series. The Air Jordan 3 Retro White Cement is constructed with a white leather upper, and off-white colored midsoles and heel tabs, helping to give the sneaker a vintage design.  \n<br>\n<br>\nThe Air Jordan 3 Retro White Cement Reimagined released March 11, 2023, with a retail price of $210.",
        "model": "Jordan 3 Retro",
        "brand": "Jordan",
        "sku": "DN3707-100",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-Air-Max-1-SP-Concepts-Denim-Paisley-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1685115444",
        "name": "Nike Air Max 1 SP Concepts Far Out (Special Box)",
        "description": "PLEASE NOTE: Print Patterns May Vary. Box color may vary between in-store and online release.",
        "model": "Nike Air Max 1 SP",
        "brand": "Nike",
        "sku": "DN1803-500",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Air-Jordan-5-Retro-What-The-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1609768847",
        "name": "Jordan 5 Retro What The",
        "description": "To honor the 30th Anniversary of the Jordan 5, Jordan Brand added a \"What The?\" treatment to its catalog with the Jordan 5 What The. This design boasts a mix of materials and details from Jumpman\u2019s best Non-OG Jordan 5 colorways, including the Tokyo, Shanghai, Raging Bull, Bel-Air, Laser, Green Bean, Olive, and Quai 54 colorways.\n<br>\n<br>\nIn true mismatched fashion, each foot of the Jordan 5 What The showcases a different look. On the right, yellow suede from the Tokyo 5 smothers the upper atop a purple and blue speckled Belair 5 midsole with a patterned interior pulled from the Jordan 5 Olive. On the left, red suede tributing the Raging Bull Jordan 5 covers the upper atop a black, grey, and lime green sole that references the Quai 54 iteration. Heel embroidery nodding to the Shanghai and Tokyo models, icy translucent outsoles, and 3M reflective tongues complete this scrambled iteration. \n<br>\n<br>\nThe Jordan 5 What The released in November of 2020 and retailed for $220.\n",
        "model": "Jordan 5 Retro",
        "brand": "Jordan",
        "sku": "CZ5725-700",
        "condition": "",
        "size": "",
        "location": ""
    },
    {
        "image": "https://images.stockx.com/images/Nike-LeBron-8-South-Beach-2021-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1622045972",
        "name": "Nike LeBron 8 South Beach (2021)",
        "description": "In 2021, Nike brought back the classic 2010 Nike LeBron 8 South Beach. The upper consists of a mix of Filament Green leather and carbon fiber. From there, hits of Pink Flash appear on the laces and inner lining. Lastly, a lion head is embossed on the tongue to symbolize LeBron\u2019s status as king of the court. \n<br>\n<br>\nThe Nike LeBron 8 South Beach (2021) releases July of 2021 for $200.",
        "model": "Nike LeBron 8",
        "brand": "Nike",
        "sku": "CZ0328-400",
        "condition": "",
        "size": "",
        "location": ""
    }

    
]

# Set the API URL
api_url = "http://localhost:5001/api/add_sneaker"

# Loop through each sneaker data and send POST request
for sneaker_data in sneakers_data:
    sneaker_data
    response = requests.post(api_url, json=sneaker_data, headers={'Content-Type': 'application/json'})

    #Print the API response for each sneaker
    print(f"Adding {sneaker_data['name']}")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")