from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for

app = Flask(__name__)
valid = 1
current_id = 10
data = {
    "1":
        {   "id": "1",
            "name": "Sun Ra",
            "image": "https://media.npr.org/assets/img/2014/05/21/sun-ra-in-text1-cb4036fa5068a4f9afd4b56bf6c55bb176415eaf-s1100-c50.jpg",
            'biography': "Bandleader, composer, arranger, keyboard player, poet, philosopher, and cosmonaut Sun Ra advanced jazz into the space age. Through his elaborate concerts, films, and countless recordings, he fused imagery and mythology related to ancient Egypt as well as science fiction, planting the seeds for what would eventually be referred to as Afrofuturism. Ras music encompassed nearly every style of jazz, with roots in ragtime and swing, bebop and avant-garde jazz. nitially active as a blues pianist, he worked with swing musicians such as Coleman Hawkins during the 1940s, then established his own trajectory during the 50s, when he founded the ever-changing ensemble known as the Arkestra. - Scott Yanow & Paul Simpson, Rovi",
            "year": "1977",
            "notable_works": ["Tapestry from an Asteroid", "Hour of Parting", "Springtime Again", "Door to the Cosmos", "When There Is No Sun"],
            "genre": ["Jazz"],
            "department":"Jazz",
            "performance": "https://sunramusic.bandcamp.com/album/solo-piano-at-wkcr-1977",
            "notes":"",
            "alt": "Sun Ra concealing face with art piece"

            },

    "2":
        {    "id": "2",
             "name": "MF DOOM",
             "image": "https://miro.medium.com/v2/resize:fit:480/0*Adq1bLS83sjgPXvW.jpg",
             'biography': 'Daniel Dumil, also known by his stage name MF DOOM or simply DOOM, was a British-American rapper and record producer. Noted for his intricate wordplay, signature metal mask, and "supervillain" stage persona, Dumile became a major figure of underground hip hop and alternative hip hop in the 2000s. After his death, Variety described him as one of the scene\'s "most celebrated, unpredictable and enigmatic figures" According to an obituary in The Ringer, his flow was "loose and conversational, but delivered with technical precision", and his use of rhyme and meter eclipsed that of Big Pun and Eminem. Dumile\'s production work frequently incorporated samples and quotations from film.- Wikipedia ',
             "year": "1997",
             "notable_works": ["Rapp Snitch Knishes", "Doomsday", "One Beer", "All Caps", "Meat Grinder"],
             "genre": ["Rap", "Hip Hop"],
             "department": "American",
             "performance": "https://www.youtube.com/watch?v=0mAoW4nVLYA",
             "notes":"",
             "alt":"MF DOOM with his famous mask on"
             },
    "3":
        {    "id": "3",
            "name": "John Cage",
            "image": "https://media.newyorker.com/photos/59096d672179605b11ad7235/master/pass/101004_r20053_p886.jpg",
            'biography':'The most influential and controversial American experimental composer of the 20th century, John Cage was the father of indeterminism, a Zen-inspired aesthetic which expelled all notions of choice from the creative process. Rejecting the most deeply held compositional principles of the past -- logical consequence, vertical sensitivity, and tonality among them -- Cage created a groundbreaking alternative to the serialist method, deconstructing traditions established hundreds and even thousands of years earlier; the end result was a radical new artistic approach which impacted all of the music composed in its wake, forever altering not only the ways in which sounds are created but also how they\'re absorbed by audiences. Indeed, it\'s often been suggested that he did to music what Karl Marx did to government -- he leveled it. - Jason Ankeny, Rovi',
            "year": "1987",
            "notable_works": ['4\'33"', "In a Landscape", "Sonatas and Interludes", "First Construction (in Metal)", "String Quartet in Four Parts "],
            "genre": ["avant-garde", "electronic", "classical"],
            "department": "New Music",
            "performance": "https://en.wikipedia.org/wiki/Europeras",
             "notes":'Within "Europera 1 & 2" there is a 3 minute sound loop, "Truckera" that was recorded live on air at WKCR',
             "alt": "John Cage playing a string instrument "
        },
    "4":
        {
            "id": "4",
            "name": "Willie Nelson",
            "image": "https://cmhof.imgix.net/wp-content/uploads/2022/05/09110126/Nelson_Willie.jpg",
            'biography':'As a songwriter and performer, Willie Nelson has played a vital role in post-rock & roll country music. Although he didn\'t become a star until the mid-\'70s, he spent the 1960s writing songs that became hits for stars like Ray Price, Patsy Cline, Faron Young, andn Billy Walker, as well as releasing a series of records on Liberty and RCA that earned him a small but devoted cult following. During the early \'70s, Willie abandoned Nashville for his native Texas, setting up shop with the redneck hippies in Austin and taking control of his music on the landmark Shotgun Willie (1973) and Phases & Stages (1974). Nelson found a kindred spirit in  Waylong Jennings and, together, they spearheaded the outlaw country movement that finally made him a star by 1975. Following the crossover success of that year\'s Red Headed Stranger and "Blue Eyes Crying in the Rain," Nelson became a genuine success, as recognizable in pop circles as he was to country audiences; in addition to recording, he also launched an acting career in the early \'80s. Even when he was a star, he never played it safe musically. Instead, he borrowed from a wide variety of styles, including traditional pop -- his biggest album was 1978\'s Stardust, a collection of interpretations of the Great American Songbook -- Western swing, jazz, traditional country, cowboy songs, honky tonk, rock & roll, folk, and the blues, creating a distinctive, elastic hybrid. Nelson remained at the top of the country charts until the mid-\'80s, when his lifestyle -- which had always been close to the outlaw clichés with which his music flirted -- began to spiral out of control, culminating in an infamous battle with the IRS in the late \'80s. Nelson\'s hit singles dried up by the early \'90s, but he kept performing and recording at a prodigious pace, both on his own and in a variety of collaborative settings, including the country supergroup the Highwaymen. - Stephen Thomas Erlewine & Steve Leggett, Rovi',
            "year": "1996",
            "notable_works": ["Mammas Don't Let Your Babies Grow Up to Be Cowboys", "Good Hearted Woman","Always on My Mind", "Beer For My Horses", "To All The Girls I've Loved Before"],
            "genre": ["Country", "Blues", "Folk"],
            "department": "American",
            "performance": "https://www.cc-seas.columbia.edu/wkcr/archives/American%20Archive/artist/Willie%20Nelson",
            "notes":"",
            "alt":" Willie Nelson playing the guitar"


        },
    "5":{
        "id": "5",
        "name": "Nas",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Nas-04.jpg/220px-Nas-04.jpg",
        'biography':'Beginning with his classic debut, Illmatic (1994), Nas has stood tall as one of New York City\'s leading rap voices, outspokenly expressing a righteous, self-empowered swagger that has endeared him to critics and hip-hop purists. Whether proclaiming himself "Nasty Nas" or "Nas Escobar" or "Nastradamus" or "God\'s Son," the self-appointed King of New York has battled numerous adversaries, none more challenging than Jay-Z , who vied with Nas for the throne left in the wake of the Notorious B.I.G.\'s 1997 assassination. Such headline-worthy drama has informed his provocative rhymes, delivered with a masterful flow and a wise perspective over beats by a range of producers, from DJ Premier and Pete Rock  to the Alchemist and Kanye West. Nas has continually matured as an artist, evolving from a young street disciple to a vain, all-knowing sage and humbled godly teacher, as illustrated through Hip Hop Is Dead (2006), Nas (2008), and Life Is Good (2012), all of which were Grammy nominated. Since relaunching and expanding the multimedia hip-hop company Mass Appeal , he\'s continued to build his deep discography with releases such as Nasir (2018), and a string of collaborations with producer Hit-Boy that includes the Grammy-winning King\'s Disease (2020), King\'s Disease II (2021) and III (2022) as well as a trilogy of releases in the Magic series, ending with 2023\'s Magic 3, the sixth consecutive and final Nas/Hit-Boy team-up.- Jason Birchmeier',
        "year": "1993",
        "notable_works": ["N.Y. State of Mind", "Made You Look", "The World Is Yours", "Hate Me Now", "If I Ruled the World" ],
        "genre": ["Rap", "Hip Hop"],
        "department": "American",
        "performance": "https://www.youtube.com/watch?v=veeqDywIQoQ",
        "alt":"Nas with beanie on looking at camera"
    },

    "6":{
        "id": "6",
        "name": "Vernon Reid",
        "image": "https://www.innerviews.org/inner/reid2/reidheader2.jpg",
        'biography':'As the lead guitarist of  and a co-founder of the Black Rock Coalition, Vernon Reid has done a great deal to undermine stereotypical expectations of what music black artists ought to play; his rampant eclecticism encompasses everything from hard rock and punk to funk, R&B and avant-garde jazz, and his anarchic, lightning-fast solos have become something of a hallmark as well. Born in London, Reid and his family emigrated to Brooklyn while he was a child; he began playing guitar at age 15, initially studying jazz and progressing quickly. In 1980, he joined drummer Ronald Shannon Jackson\'s Decoding Society, a cutting-edge jazz group with whom he appeared on six albums; over the course of the decade, Reid went on to work with a wide variety of experimental musicians- Defunkt, Bill Frisell, John Zorn, Arto Lindsay, and Public Enemy, among others. -  Steve Huey and Thom Jurek, Rovi',
        "year": "2006",
        "notable_works": ["World in My Eyes", "Low Rider", "The Unforgiven", "Mistaken Identity", "Cp Time"],
        "genre": ["Metal", "Rock", "Funk"],
        "department": "New Music",
        "performance": 'https://www.youtube.com/watch?v=Yh5nymGcatU',
        "alt":"Vernon Reid holding guitar looking at camera"
    },
    "7":{
        "id": "7",
        "name": "The Notorious B.I.G.",
        "image": "https://images.radio.com/aiu-media/BIG052022-9378c6c1-4309-4c01-affb-c1b09c8205fe.jpg?width=800",
        'biography':'In just a few short years, the Notorious B.I.G. went from a Brooklyn street hustler to the savior of East Coast hip-hop to a tragic victim of the culture of violence he depicted so realistically on his records. His all-too-brief odyssey almost immediately took on mythic proportions, especially since his murder followed the shooting of rival Tupac Shakur by only six months. In death, the man also known as Biggie Smalls became a symbol of the senseless violence that plagued inner-city America in the waning years of the 20th century. Whether or not his death was really the result of a much-publicized feud between the East and West Coast hip-hop scenes, it did mark the point where both sides stepped back from a rivalry that had gone too far. Hip-hop\'s self-image would never quite be the same, and neither would public perception. The aura of martyrdom that surrounds the Notorious B.I.G. sometimes threatens to overshadow his musical legacy, which was actually quite significant. Aided by Sean "Puffy" Combs\' radio-friendly sensibility, Biggie reestablished East Coast rap\'s viability by leading it into the post-Dr. Dre gangsta age. Where fellow East Coasters the Wu-Tang Clan slowly built an underground following, Biggie crashed onto the charts and became a star right out of the box. In the process, he helped Combs\' Bad Boy label supplant Death Row  as the biggest hip-hop imprint in America, and also paved the way to popular success for other East Coast talents like Jay-Z and Nas. Biggie was a gifted storyteller with a sense of humor and an eye for detail, and his narratives about the often-violent life of the streets were rarely romanticized; instead, they were told with a gritty, objective realism that won him enormous respect and credibility. The general consensus in the rap community was that when his life was cut short, Biggie was just getting started.',
        "year": "1992",
        "notable_works": ["Hypnotize", "Big Poppa", "Juicy", "Mo Money Mo Problems", "Party And Bullshi "],
        "genre": ["Rap", "Hip Hop"],
        "department": "American",
        "performance": "https://www.youtube.com/watch?v=PZTFtRyafjw",
        "alt":"Biggie with finger on ear and sunglasses and hat on "

    },
    "8":{
        "id": "8",
        "name": "Sonny Sharrock",
        "image": "https://g123-media.sos-ch-gva-2.exoscale-cdn.com/filer_public_thumbnails/filer_public/78/59/7859c43a-59a0-4d66-b5f9-57840feee4c5/sonny-sharrock-zurich-53595-guitar-original-photograph.jpg__960x0_q85_subsampling-2_upscale.jpg",
        'biography':'Of the electric guitar\'s few proponents in avant-garde jazz, Sonny Sharrock is easily the most influential; he was one of the earliest guitarists to even attempt free playing, along with Derek Bailey and Sonny Greenwich . Sharrock\'s visceral aggression and monolithic sheets of noise were influenced by the screaming overtones of saxophonists like Coltrane, Sanders, and Ayler, and his experiments with distortion and feedback predated even Jimi Hendrix. Naturally, he provoked much hostility among traditionalists, but once his innovations were assimilated, he enjoyed wide renown in avant-garde circles. -  Steve Huey, Rovi',
        "year": "1974",
        "notable_works": ["Blind Willie", "Who Does She Hope To Be?", "Improvised Music #1", "Black Woman", "Peanut"],
        "genre": ["Jazz", "Experimental", "Rock"],
        "department": "New Music",
        "performance": "https://www.youtube.com/watch?v=7rgNQGce1vU",
        "alt":"Sonny Sharrock playing guitar smiling"
    },
    "9":{
        "id": "9",
        "name": "Jay-Z",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Jay-Z-02-mika.jpg/220px-Jay-Z-02-mika.jpg",
        'biography':'From the projects to the throne, New York rapper, producer, and entrepreneur Jay-Z embodied the quintessential rags-to-riches dream, becoming one of the most successful MCs of his generation while creating an empire that made him one of the richest artists of the era. After debuting in the late \'90s with Reasonable Doubt and In My Lifetime, Vol 1, he began a chart run that notched over a dozen number one albums spread over two decades, including the multi-platinum, Grammy-winning Vol. 2...Hard Knock Life (1999), the Blueprint series (2001, 2002, 2009), and The Black Album (2003). In addition to his solo work, Jay-Z also found mainstream crossover success with pop, R&B, and rock artists, notably collaborating with protege Rihanna on their Grammy-winning "Umbrella" (2008); alternative metal outfit Linkin Park  on 2004\'s genre mash-up Collision Course; Alicia Keys on New York City\'s unofficial anthem, the chart-topping "Empire State of Mind" (2011); frequent foil Kanye West on Watch the Throne (2012); and wife Beyonce on numerous hit singles, international tours, and the joint album Everything Is Love (2018). He also contributed the song "What It Feels Like" to the soundtrack of the Oscar-nominated 2021 drama Judas and The Black Messiah. In addition to rapping, Jay-Z has also served as a label head, team owner (NBA\'s Brooklyn Nets), real-estate mogul, and fashion designer. -  Jason Birchmeier & Andy Kellman, Rovi',
        "year": "1995",
        "notable_works": ["Empire State of Mind", "4:44", "Run This Town", "Why I Love You", "99 Problems" ],

        "genre": ["Hip Hop", "Rap"],
        "department": "American",
        "performance": "https://www.youtube.com/watch?v=ssKbzld-5yU",
        "alt":"Jay-Z sitting looking down at camera"
    },
    "10":{
        "id": "10",
        "name": "Wu-Tang Clan",
        "image": "https://www.ascap.com/~/media/site-pages/news-and-events/events/2019/sundance/composerspotlight-square/wutangclan.jpg",
        'biography':'Emerging in 1993, when \'s G-funk had overtaken the hip-hop world, the Staten Island, New York-based Wu-Tang Clan proved to be the most revolutionary rap group of the \'90s -- and only partially because of their music. Turning the standard concept of a hip-hop crew inside out, the Wu-Tang Clan were assembled as a loose congregation of nine MCs, almost as a support group. Instead of releasing one album after another, the Clan were designed to overtake the record industry in as profitable a fashion as possible, the idea being to establish themselves as a force with their debut album and then spin off into as many side projects as possible. In the process, the members would all become individual stars as well as receive individual royalty checks. - Stephen Thomas Erlewine & Steve Huey, Rovi',
        "year": "1992",
        "notable_works": ["Protect Ya Neck", "C.R.E.A.M.", "Triumph", "Wu-Tang Clan Ain’t Nuthing Ta F’ Wi", "Method Man" ],
        "genre": ["Hip Hop", "Rap"],
        "department": "American",
        "performance": "https://www.youtube.com/watch?v=kVXyy7R02iM",
        "alt":"Members of Wu-Tang Clan all sitting on ground looking at camera"

    }

}



@app.route('/')
def homepage():
    return render_template('homepage.html', data=data,valid=valid)


@app.route('/search', methods = ['GET', 'POST'])
def search_results():
    global data
    query = request.args.get('query', '')
    list = [entry for entry in data.values() if entry['name'].lower().startswith(query.lower()) or entry['department'].lower().startswith(query.lower()) or entry['year'].startswith(query)]

    return render_template('searchresults.html', query= query, list = list, data=data,valid=valid)



@app.route('/view/<id>')
def view(id=None):
    return render_template("view.html", id=id, data=data,valid=valid)
@app.route('/add',methods = ['GET', 'POST'])
def entry():
    id='0';
    return render_template("entry.html", data=data, id=id,valid=valid)
@app.route('/edit/<id>',methods = ['GET', 'POST'])
def edit(id=None):
    return render_template("edit.html", data=data, id=id,valid=valid)

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    global data;
    global current_id;


    json_data = request.get_json()
    new_id = json_data["id"]

    if new_id == '0':
        current_id +=1
        new_id = str(current_id)

    new_name  = json_data["name"]
    new_image = json_data["image"]
    new_bio = json_data["biography"]
    new_year = json_data["year"]
    new_works = json_data["notable_works"]
    new_genre = json_data["genre"]
    new_department = json_data["department"]
    new_performance=json_data["performance"]
    new_notes= json_data["notes"]
    new_alt = json_data["alt"]

    new_artist={
        "id": new_id,
        "name": new_name,
        "image": new_image,
        "biography": new_bio,
        "year": new_year,
        "notable_works": new_works,
        "genre": new_genre,
        "department": new_department,
        "performance": new_performance,
        "notes": new_notes,
        "alt": new_alt
    }

    data[new_id] = new_artist

    return jsonify(new_artist=new_artist, valid=valid)


if __name__ == '__main__':
    app.run(debug=True)
