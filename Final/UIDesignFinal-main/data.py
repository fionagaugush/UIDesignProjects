data = {
    "user": {
        "id": 1,
        "step": 0,  # 0: Haven’t started learning, 1: Clicked on learn button, 2: Started quiz
        "currentQuizQuestion": 0,
        "quizScore": 0
    },
    "birds": {

        "0":{
            "id": 0,
            "name": "Mourning Dove",
            "imageUrl": "birds_image/bird_1.png",
            "soundUrl": "birds_audio/bird_1.mp3",
            "description": "Low mournful coo",
            "call": {
                "sound": "coo-ah, coo, coo",
                "type": ["Hoot"],
                "pattern": ["Falling", "Flat", "Undulating"]
            },
            "spottingLocations": ["The Ramble"]

        },
       "1": {
            "id": 1,
            "name": "Great Blue Heron",
            "imageUrl": "birds_image/BlueHeron.jpeg",
            "soundUrl": "birds_audio/BlueHeron.mp3",
            "description": "Harsh squawk",
            "call": {
                "sound": "roh, roh, roh",
                "type": ["Croak/Quack", "Scream"],
                "pattern": ["Flat", "Simple"]
            },
            "spottingLocations": ["Central Park Lake"]
        },

       "2": {
            "id": 2,
            "name": "Red Tailed Hawk",
            "imageUrl": "birds_image/Hawk.jpeg",
            "soundUrl": "birds_audio/Hawk.mp3",
            "description": "High-pitched descending scream",
            "call": {
                "sound": "keeeer",
                "type": ["Croak/Quack", "Scream"],
                "pattern": ["Falling", "Simple"]
            },
            "spottingLocations": ["west side of Conservatory Water"]
        },


        "3":{
            "id": 3,
            "name": "House Sparrow",
            "imageUrl": "birds_image/Sparrow.jpeg",
            "soundUrl": "birds_audio/Sparrow.mp3",
            "description": "Shrill monotonous, noisy chirping",
            "call": {
                "sound": "Cheep, Cheep",
                "type": ["Chirp/Chip", "Rattle"],
                "pattern": ["Falling/Flat"]
            },
            "spottingLocations": ["Pilgrim Hill"]
        },


        "4":{
            "id": 4,
            "name": "Northern Cardinal",
            "imageUrl": "birds_image/Cardinal.jpeg",
            "soundUrl": "birds_audio/Cardinal.mp3",
            "description": "Metallic chip, repeated whistles",
            "call": {
                "sound": "Cheer, cheer, cheer",
                "type": ["Chirp/Chip", "Whistle"],
                "pattern": ["Falling", "Whistle"]
            },
            "spottingLocations": ["The Ramble"]
        },


        "5":{
            "id": 5,
            "name": "Red Bellied Woodpecker",
            "imageUrl": "birds_image/Woodpecker.jpeg",
            "soundUrl": "birds_audio/Woodpecker.mp3",
            "description": "Shrill rolling churr",
            "call": {
                "sound": "Churrr or chuck, chuck",
                "type": ["Chirp/Chip", "Rattle", "Drum"],
                "pattern": ["Falling", "Flat"]
            },
            "spottingLocations": ["Locust Grove"]
        },


        "6":{
            "id": 6,
            "name": "Tufted Titmouse",
            "imageUrl": "birds_image/Titmouse.jpeg",
            "soundUrl": "birds_audio/Titmouse.mp3",
            "description": "A whistled series",
            "call": {
                "sound": "Peter, Peter, Peter",
                "type": ["Buzz", "Chirp/Chip", "Whistle"],
                "pattern": ["Falling"]
            },
            "spottingLocations": ["Turtle Pond"]
        },


     "7":   {
            "id": 7,
            "name": "Blue Jay",
            "imageUrl": "birds_image/BlueJay.jpg",
            "soundUrl": "birds_audio/BlueJay.mp3",
            "description": "A raucous jay-jay, harsh cries, jeer",
            "call": {
                "sound": "Jay, Jay",
                "type": ["Chirp/Chip", "Rattle", "Scream", "Whistle"],
                "pattern": ["Falling", "Flat"]
            },
            "spottingLocations": ["Belvedere Castle’s"]
        },
    },
    "quizQuestions": [
        {
            "id": 1, 
            "type": "QUIZ_MULTIPLE_CHOICE",
            "questionText": "Which bird's call can be described as a 'low mournful coo'? ",
            "choices": [
                "House Sparrow",
                "Red Bellied Woodpecker",
                "Mourning Dove",
                "None of the Above"
            ],
            "correctAnswer": 2
        },
        {
            "id": 2,
            "type": "QUIZ_MAPPING",
            "questionText": "Listen to the three audio clips and drag them to the correct bird",
            "sounds": [
                "birds_audio/BlueHeron.mp3",
                "birds_audio/Woodpecker.mp3",
                "birds_audio/Hawk.mp3"
            ],
            "images": [
                "birds_image/BlueHeron.jpeg",
                "birds_image/Woodpecker.jpeg",
                "birds_image/Hawk.jpeg"
            ],
            "correctAnswer": [1, 2, 0],
            "birds": ["Great Blue Heron", "Red Bellied Woodpecker", "Red Tailed Hawk"]
        },
        {
            "id": 3, 
            "type": "QUIZ_MULTIPLE_CHOICE",
            "questionText": "True or False: This recording is a house sparrow",
            "audioURL": "birds_audio/Sparrow.mp3",
            "choices": [
                "True",
                "False"
            ],
            "correctAnswer": 0
        },
        {
            "id": 4, 
            "type": "QUIZ_MULTIPLE_CHOICE",
            "questionText": "Which bird makes a 'Peter Peter Peter' noise?",
            "choices": [
                "Tufted Titmouse",
                "Mourning Dove",
                "Great Blue Heron",
                "None of the Above"
            ],
            "correctAnswer": 0
        },
        {
            "id": 5, 
            "type": "QUIZ_MULTIPLE_CHOICE",
            "questionText": "Listen to the audio mashup and identify the two birds in it",
            "audioURL": "birds_audio/MourningDove_and_Cardinal.mp3",
            "choices": [
                "Mourning Dove + Northern Cardinal",
                "Red Tailed Hawk + Northern Cardinal",
                "House Sparrow + Mourning Dove",
                "None of the Above"
            ],
            "correctAnswer": 0
        },
        # {
        #     "id": 6,
        #     "type": "QUIZ_MAPPING",
        #     "questionText": "Listen to the three audio clips and drag them to the correct bird",
        #     "sounds": [
        #         "birds_audio/Sparrow.mp3",
        #         "birds_audio/Cardinal.mp3",
        #         "birds_audio/MourningDove.mp3"
        #     ],
        #     "images": [
        #         "birds_image/Sparrow.jpeg",
        #         "birds_image/Cardinal.jpeg",
        #         "birds_image/MourningDove.jpeg"
        #     ],
        #     "correctAnswer": [1, 2, 0],
        #     "birds": ["House Sparrow", "Northern Cardinal", "Mourning Dove"]
        # },
        {
            "id": 6,
            "type": "QUIZ_MULTIPLE_CHOICE",
            "questionText": "Which bird makes a 'keeeeer' noise?",
            "choices": [
                "Red Bellied Woodpecker",
                "Tufted Titmouse",
                "Red Tailed Hawk",
                "Blue Jay"
            ],
            "correctAnswer": 2,
        }, 
        # {
        #     "id": 8,
        #     "type": "QUIZ_MULTIPLE_CHOICE",
        #     "questionText": "True or False: This recording is a Northern Cardinal",
        #     "audioURL": "birds_audio/Sparrow.mp3",
        #     "choices": [
        #         "True",
        #         "False"
        #     ],
        #     "correctAnswer": 1
        # }
    ]
}
