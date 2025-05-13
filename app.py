import streamlit as st

st.title("Tripteller: A Personal Vacation Matchmaker")
st.subheader("Find your perfect getaway with just a few questions!")

# Questions to ask: 
questions = [
    {"question": "What kind of surroundings would you like?", 
     "options": ["Beach/Tropical", "Desert", "Mountains/Forest", "City"]},
    
    {"question": "What is your total budget?", 
     "options": ["<$3000", "$3-5k", "$5-7k", "$8k+"]},
    
    {"question": "What kind of accommodation would you prefer?", 
     "options": ["Hotel", "Hostel", "Airbnb/Villa", "All-Inclusive Resort"]},
    
    {"question": "Are you bringing kids along?", 
     "options": ["Yes", "No"]}
]

# Vacation Suggestions Dictionary
vacation_suggestions = {
    ("Beach/Tropical", "<$3000", "Hotel", "Yes"): "Visit coastal Mexico or Sri Lanka — great value hotels with easy access to beaches.",
    ("Beach/Tropical", "<$3000", "Hotel", "No"): "Visit coastal Mexico or Sri Lanka — great value hotels with easy access to beaches.",
    ("Beach/Tropical", "<$3000", "Hostel", "Yes"): "Try Thailand or the Philippines — these backpacker favorites offer tropical beauty and cheap stays perfect for solo or social travel.",
    ("Beach/Tropical", "<$3000", "Hostel", "No"): "Try Thailand or the Philippines — these backpacker favorites offer tropical beauty and cheap stays perfect for solo or social travel.",
    ("Beach/Tropical", "<$3000", "Airbnb/Villa", "Yes"): "Check out Bali or coastal Colombia! You’ll find charming beachfront villas and vibrant local culture on a budget.",
    ("Beach/Tropical", "<$3000", "Airbnb/Villa", "No"): "Check out Bali or coastal Colombia! You’ll find charming beachfront villas and vibrant local culture on a budget.",
    ("Beach/Tropical", "<$3000", "All-Inclusive Resort", "Yes"): "I suggest going to Mexico, El Salvador, or Costa Rica — they offer affordable flights, warm beaches, and family-friendly all-inclusive resorts.",
    ("Beach/Tropical", "<$3000", "All-Inclusive Resort", "No"): "Try Dominican Republic or Panama for budget-friendly all-inclusives and beach vibes.",
    ("Beach/Tropical", "$3-5k", "Hotel", "Yes"): "Consider Belize, Hawaii, or southern Italy for a balanced budget and gorgeous coastline.",
    ("Beach/Tropical", "$3-5k", "Hotel", "No"): "Consider Belize, Hawaii, or southern Italy for a balanced budget and gorgeous coastline.",
    ("Beach/Tropical", "$3-5k", "Hostel", "Yes"): "Consider Belize, Hawaii, or southern Italy for a balanced budget and gorgeous coastline.",
    ("Beach/Tropical", "$3-5k", "Hostel", "No"): "Consider Belize, Hawaii, or southern Italy for a balanced budget and gorgeous coastline.",
    ("Beach/Tropical", "$3-5k", "Airbnb/Villa", "Yes"): "Consider Belize, Hawaii, or southern Italy for a balanced budget and gorgeous coastline.",
    ("Beach/Tropical", "$3-5k", "Airbnb/Villa", "No"): "Consider Belize, Hawaii, or southern Italy for a balanced budget and gorgeous coastline.",
    ("Beach/Tropical", "$3-5k", "All-Inclusive Resort", "Yes"): "The Caribbean or the Maldives are perfect for a comfortable beach getaway with options for both families and adults.",
    ("Beach/Tropical", "$3-5k", "All-Inclusive Resort", "No"): "The Caribbean or the Maldives are perfect for a comfortable beach getaway with options for both families and adults.",
    ("Beach/Tropical", "$5-7k", "Hotel", "Yes"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "Hotel", "No"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "Hostel", "Yes"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "Hostel", "No"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "Airbnb/Villa", "Yes"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "Airbnb/Villa", "No"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "All-Inclusive Resort", "Yes"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$5-7k", "All-Inclusive Resort", "No"): "Consider Bora Bora, Fiji, or Turks and Caicos — luxurious stays with unmatched tropical beauty.",
    ("Beach/Tropical", "$8k+", "Hotel", "Yes"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "Hotel", "No"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "Hostel", "Yes"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "Hostel", "No"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "Airbnb/Villa", "Yes"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "Airbnb/Villa", "No"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "All-Inclusive Resort", "Yes"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",
    ("Beach/Tropical", "$8k+", "All-Inclusive Resort", "No"): "Splurge in the Seychelles or the Maldives — elite tropical destinations with luxury everything.",

    ("Desert", "<$3000", "Hotel", "Yes"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "Hotel", "No"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "Hostel", "Yes"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "Hostel", "No"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "Airbnb/Villa", "Yes"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "Airbnb/Villa", "No"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "All-Inclusive Resort", "Yes"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",
    ("Desert", "<$3000", "All-Inclusive Resort", "No"): "Head to Arizona or Southern Utah — scenic parks, warm sun, and desert charm, great for budget-conscious travelers.",

    ("Desert", "$3-5k", "Hotel", "Yes"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "Hotel", "No"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "Hostel", "Yes"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "Hostel", "No"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "Airbnb/Villa", "Yes"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "Airbnb/Villa", "No"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "All-Inclusive Resort", "Yes"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Desert", "$3-5k", "All-Inclusive Resort", "No"): "Explore Morocco or Palm Springs — a perfect blend of exotic desert charm and stylish resorts.",
    ("Mountains/Forest", "<$3000", "Hotel", "Yes"): "Try the Smoky Mountains or Canadian Rockies — affordable scenic escapes with family-friendly lodging.",
    ("Mountains/Forest", "<$3000", "Hotel", "No"): "Try the Smoky Mountains or Canadian Rockies — affordable scenic escapes with family-friendly lodging.",
    ("Mountains/Forest", "<$3000", "Hostel", "Yes"): "Visit the Appalachian Trail or parts of Patagonia for rugged adventure and social accommodations.",
    ("Mountains/Forest", "<$3000", "Hostel", "No"): "Visit the Appalachian Trail or parts of Patagonia for rugged adventure and social accommodations.",
    ("Mountains/Forest", "<$3000", "Airbnb/Villa", "Yes"): "Look into North Carolina or upstate New York — private cabins surrounded by nature on a budget.",
    ("Mountains/Forest", "<$3000", "Airbnb/Villa", "No"): "Look into North Carolina or upstate New York — private cabins surrounded by nature on a budget.",
    ("Mountains/Forest", "<$3000", "All-Inclusive Resort", "Yes"): "Check out family-friendly mountain resorts in Colorado or Chile that offer bundled deals.",
    ("Mountains/Forest", "<$3000", "All-Inclusive Resort", "No"): "Check out adventure resorts in Colorado or Chile that offer bundled nature excursions.",

    ("Mountains/Forest", "$3-5k", "Hotel", "Yes"): "Try Switzerland or northern California — scenic stays with quality family lodging.",
    ("Mountains/Forest", "$3-5k", "Hotel", "No"): "Try Switzerland or northern California — scenic stays with quality family lodging.",
    ("Mountains/Forest", "$3-5k", "Hostel", "Yes"): "Try Switzerland or northern California — scenic stays with quality family lodging.",
    ("Mountains/Forest", "$3-5k", "Hostel", "No"): "Try Switzerland or northern California — scenic stays with quality family lodging.",
    ("Mountains/Forest", "$3-5k", "Airbnb/Villa", "Yes"): "Rent a cozy cabin in the Alps or Pacific Northwest — perfect for families who love the outdoors.",
    ("Mountains/Forest", "$3-5k", "Airbnb/Villa", "No"): "Rent a cozy cabin in the Alps or Pacific Northwest — perfect for couples or solo nature lovers.",
    ("Mountains/Forest", "$3-5k", "All-Inclusive Resort", "Yes"): "Try eco-resorts in Costa Rica or British Columbia — tailored for nature-loving families.",
    ("Mountains/Forest", "$3-5k", "All-Inclusive Resort", "No"): "Try eco-resorts in Costa Rica or British Columbia — tailored for nature-loving travelers.",

    ("City", "<$3000", "Hotel", "Yes"): "Consider cities like Lisbon, Buenos Aires, or Montreal — exciting urban vibes without breaking the bank.",
    ("City", "<$3000", "Hotel", "No"): "Consider cities like Lisbon, Buenos Aires, or Montreal — exciting urban vibes without breaking the bank.",
    ("City", "<$3000", "Hostel", "Yes"): "Look into hostels in Barcelona or Prague — family-friendly ones do exist, and they’re affordable!",
    ("City", "<$3000", "Hostel", "No"): "Look into hostels in Barcelona or Prague — social, central, and easy on the wallet.",
    ("City", "<$3000", "Airbnb/Villa", "Yes"): "Try a city stay in Athens or Mexico City — lively, cultural, and plenty of family Airbnbs.",
    ("City", "<$3000", "Airbnb/Villa", "No"): "Try a city stay in Athens or Mexico City — lively, cultural, and plenty of cool Airbnbs.",
    ("City", "<$3000", "All-Inclusive Resort", "Yes"): "Look at urban-style resorts in places like Istanbul or Dubai that cater to all ages.",
    ("City", "<$3000", "All-Inclusive Resort", "No"): "Look at urban-style resorts in places like Istanbul or Dubai with rich history and great dining.",

    ("City", "$3-5k", "Hotel", "Yes"): "Paris, Tokyo, or New York — plan ahead for deals and kid-friendly city fun.",
    ("City", "$3-5k", "Hotel", "No"): "Paris, Tokyo, or New York — plan ahead for deals and high-end experiences.",
    ("City", "$3-5k", "Hostel", "Yes"): "Consider Berlin or Seoul — vibrant urban areas with safe, fun hostels and great food.",
    ("City", "$3-5k", "Hostel", "No"): "Consider Berlin or Seoul — vibrant urban areas with safe, fun hostels and great food.",
    ("City", "$3-5k", "Airbnb/Villa", "Yes"): "Rent in central Barcelona or Rome — immersive, walkable, and fun for the family.",
    ("City", "$3-5k", "Airbnb/Villa", "No"): "Rent in central Barcelona or Rome — immersive, walkable, and great for couples or solo travel.",
    ("City", "$3-5k", "All-Inclusive Resort", "Yes"): "Look for city-style resorts in Kuala Lumpur or Singapore with built-in entertainment for families.",
    ("City", "$3-5k", "All-Inclusive Resort", "No"): "Look for city-style resorts in Kuala Lumpur or Singapore with built-in entertainment and cuisine.",
    ("Mountains/Forest", "$5-7k", "Hotel", "Yes"): "Stay in luxury lodges in Banff or the Dolomites — nature, comfort, and adventure for all ages.",
    ("Mountains/Forest", "$5-7k", "Hotel", "No"): "Stay in luxury lodges in Banff or the Dolomites — nature, comfort, and adventure await.",
    ("Mountains/Forest", "$5-7k", "Hostel", "Yes"): "Explore the Pyrenees or Rockies — family-friendly adventure hostels with amazing views.",
    ("Mountains/Forest", "$5-7k", "Hostel", "No"): "Explore the Pyrenees or Rockies — affordable social stays with access to outdoor activities.",
    ("Mountains/Forest", "$5-7k", "Airbnb/Villa", "Yes"): "Go for a scenic getaway in Lake Tahoe or Bavaria — cozy forest homes with family-friendly vibes.",
    ("Mountains/Forest", "$5-7k", "Airbnb/Villa", "No"): "Go for a scenic getaway in Lake Tahoe or Bavaria — perfect for a quiet or romantic escape.",
    ("Mountains/Forest", "$5-7k", "All-Inclusive Resort", "Yes"): "Choose upscale eco-lodges in New Zealand or Costa Rica — nature plus luxury for the whole crew.",
    ("Mountains/Forest", "$5-7k", "All-Inclusive Resort", "No"): "Choose upscale eco-lodges in New Zealand or Costa Rica — perfect for nature-loving travelers.",

    ("Mountains/Forest", "$8k+", "Hotel", "Yes"): "Luxury mountain retreats in the Swiss Alps or Aspen — full-service, kid-friendly, and stunning.",
    ("Mountains/Forest", "$8k+", "Hotel", "No"): "Luxury mountain retreats in the Swiss Alps or Aspen — high-end relaxation in stunning scenery.",
    ("Mountains/Forest", "$8k+", "Hostel", "Yes"): "Try private hostel suites in the Dolomites or Alps — social settings in luxury areas for adventurous families.",
    ("Mountains/Forest", "$8k+", "Hostel", "No"): "Try premium hostels in the Dolomites or Alps — great for solo or group travelers who love the outdoors.",
    ("Mountains/Forest", "$8k+", "Airbnb/Villa", "Yes"): "Rent a high-end chalet in Switzerland or Norway — full amenities with incredible views for the family.",
    ("Mountains/Forest", "$8k+", "Airbnb/Villa", "No"): "Rent a high-end chalet in Switzerland or Norway — private, peaceful, and scenic.",
    ("Mountains/Forest", "$8k+", "All-Inclusive Resort", "Yes"): "Go all-in at mountain resorts in Canada or New Zealand — luxury lodging meets family adventure.",
    ("Mountains/Forest", "$8k+", "All-Inclusive Resort", "No"): "Go all-in at mountain resorts in Canada or New Zealand — luxury meets wilderness escape.",

    ("City", "$5-7k", "Hotel", "Yes"): "Explore London, Dubai, or Hong Kong — family-friendly hotels in world-class cities with lots to do.",
    ("City", "$5-7k", "Hotel", "No"): "Explore London, Dubai, or Hong Kong — world-class cities with exciting hotels and nightlife.",
    ("City", "$5-7k", "Hostel", "Yes"): "Go urban adventuring in Tokyo or Amsterdam — modern hostels with family amenities are popping up!",
    ("City", "$5-7k", "Hostel", "No"): "Go urban adventuring in Tokyo or Amsterdam — modern hostels in the heart of the action.",
    ("City", "$5-7k", "Airbnb/Villa", "Yes"): "Try lofts in Seoul or Milan — stylish city stays with room for the family.",
    ("City", "$5-7k", "Airbnb/Villa", "No"): "Try lofts in Seoul or Milan — stylish city stays in buzzing neighborhoods.",
    ("City", "$5-7k", "All-Inclusive Resort", "Yes"): "Look into luxury city-based resorts in Singapore or Dubai — great dining and activities for families.",
    ("City", "$5-7k", "All-Inclusive Resort", "No"): "Look into luxury city-based resorts in Singapore or Dubai — convenience, cuisine, and comfort.",

    ("City", "$8k+", "Hotel", "Yes"): "Go all-out in cities like Tokyo, Paris, or NYC — 5-star family hotels with tailored experiences.",
    ("City", "$8k+", "Hotel", "No"): "Go all-out in cities like Tokyo, Paris, or NYC — 5-star hotels and unforgettable dining, art, and culture.",
    ("City", "$8k+", "Hostel", "Yes"): "Try upscale hostels in Berlin or Sydney with private family rooms — modern and centrally located.",
    ("City", "$8k+", "Hostel", "No"): "Try upscale hostels in Berlin or Sydney — chic, social, and surprisingly high-end.",
    ("City", "$8k+", "Airbnb/Villa", "Yes"): "Book luxury apartments in Manhattan, London, or Tokyo — space, comfort, and a city view.",
    ("City", "$8k+", "Airbnb/Villa", "No"): "Book luxury apartments in Manhattan, London, or Tokyo — sleek, stylish, and central.",
    ("City", "$8k+", "All-Inclusive Resort", "Yes"): "Opt for elite all-inclusive urban resorts in Singapore or Abu Dhabi — family luxury at its peak.",
    ("City", "$8k+", "All-Inclusive Resort", "No"): "Opt for elite all-inclusive urban resorts in Singapore or Abu Dhabi — luxury redefined in the city.",
}

# For collecting User Answers
user_answers = {}

for q in questions:
    answer = st.selectbox(q["question"], q["options"])
    user_answers[q["question"]] = answer

# This is for making the match button
if st.button("Find My Perfect Trip"):
    st.balloons()

    # Selections
    surroundings = user_answers['What kind of surroundings would you like?']
    budget = user_answers['What is your total budget?']
    accommodations = user_answers['What kind of accommodation would you prefer?']
    kids = user_answers['Are you bringing kids along?']

    user_key = (surroundings, budget, accommodations, kids)

    # Look up suggestion
    suggestion = vacation_suggestions.get(user_key, "Sorry, no suggestions available for your selected options.")

    st.success("Here is your personalized vacation match!")
    st.write(f"Surroundings: {surroundings}")
    st.write(f"Budget: {budget}")
    st.write(f"Accommodation: {accommodations}")
    st.write(f"Bringing kids: {kids}")
    st.markdown(f"Recommendation: {suggestion}")

# Country Itinerary Section
st.markdown("---")
st.markdown("Get Sample Itineraries by Country")

# List of countries
country_options = [
    "Select a country...",
    "Mexico", "El Salvador", "Costa Rica", "Philippines", "Thailand", "Indonesia",
    "Maldives", "French Polynesia", "Morocco", "United States", "Egypt", "Jordan",
    "United Arab Emirates", "Oman", "Chile", "Namibia", "Peru", "Canada", "Switzerland",
    "Italy", "Germany", "Norway", "New Zealand", "Argentina", "France", "Austria",
    "Spain", "Portugal", "Czech Republic", "Greece", "Turkey", "Japan", "South Korea",
    "Malaysia", "Singapore", "United Kingdom", "Netherlands", "Australia"
]

# Itineraries dictionary
itineraries = {
    "Mexico": [
        "Day 1: Explore Mexico City — visit the Zócalo, Frida Kahlo Museum, and Teotihuacan pyramids.",
        "Day 2: Head to Cancún — enjoy the beaches and explore the Mayan ruins at Tulum.",
        "Day 3: Relax at Playa del Carmen or take a day trip to Isla Cozumel."
    ],
    "El Salvador": [
        "Day 1: Visit San Salvador — explore the National Palace, El Boquerón National Park, and the Metropolitan Cathedral.",
        "Day 2: Head to Suchitoto — enjoy colonial architecture and visit the beautiful Lake Suchitlán.",
        "Day 3: Explore the Ruta de Las Flores — a scenic route with waterfalls, coffee farms, and charming towns."
    ],
    "Costa Rica": [
        "Day 1: Visit San José and take a tour of the National Museum and Central Market.",
        "Day 2: Head to Arenal Volcano for hiking and hot springs relaxation.",
        "Day 3: Explore Manuel Antonio National Park, enjoy the beaches, and spot local wildlife."
    ],
    "Philippines": [
        "Day 1: Explore Manila — visit the Intramuros, Rizal Park, and Manila Ocean Park.",
        "Day 2: Go island hopping in Palawan — visit the stunning beaches and lagoons of El Nido.",
        "Day 3: Relax at Boracay Island — known for its white sand beaches and vibrant nightlife."
    ],
    "Thailand": [
        "Day 1: Visit Bangkok — explore the Grand Palace, Wat Arun, and the floating market.",
        "Day 2: Take a day trip to Ayutthaya to see the ancient temples and historical ruins.",
        "Day 3: Head to Phuket for beautiful beaches and explore Phi Phi Islands."
    ],
    "Indonesia": [
        "Day 1: Explore Bali — visit Uluwatu Temple and Tanah Lot Temple.",
        "Day 2: Visit Ubud — explore the Monkey Forest, rice terraces, and the Sacred Water Temple.",
        "Day 3: Go to Gili Islands for snorkeling and relaxing on white sand beaches."
    ],
    "Maldives": [
        "Day 1: Arrive in Malé and take a scenic boat ride to your luxury resort.",
        "Day 2: Enjoy snorkeling, diving, and underwater experiences.",
        "Day 3: Relax at a private overwater villa and enjoy a sunset cruise."
    ],
    "French Polynesia": [
        "Day 1: Visit Tahiti — explore the lush valleys and waterfalls.",
        "Day 2: Head to Bora Bora for water activities like snorkeling and diving.",
        "Day 3: Explore Moorea Island's beaches and enjoy local Polynesian culture."
    ],
    "Morocco": [
        "Day 1: Explore Marrakesh — visit Jardin Majorelle, the Medina, and the Saadian Tombs.",
        "Day 2: Take a trip to the Atlas Mountains and visit a Berber village.",
        "Day 3: Visit the Sahara Desert — ride camels and watch the sunset over the dunes."
    ],
    "United States": [
        "Day 1: Explore New York City — visit Times Square, Central Park, and the Statue of Liberty.",
        "Day 2: Visit Washington D.C. — see the White House, Lincoln Memorial, and the Smithsonian Museums.",
        "Day 3: Head to California for a day in Los Angeles — visit Hollywood, Venice Beach, and Santa Monica."
    ],
    "Egypt": [
        "Day 1: Visit Cairo — explore the Pyramids of Giza, the Sphinx, and the Egyptian Museum.",
        "Day 2: Take a Nile River cruise to Luxor — visit the Valley of the Kings and Karnak Temple.",
        "Day 3: Head to Sharm El Sheikh for relaxing beaches and water sports."
    ],
    "Jordan": [
        "Day 1: Visit Amman — explore the Roman Theater, Citadel, and the Jordan Museum.",
        "Day 2: Visit Petra — explore the ancient Nabatean city and the Treasury.",
        "Day 3: Go to the Dead Sea — relax in the mineral-rich waters and mud."
    ],
    "United Arab Emirates": [
        "Day 1: Explore Dubai — visit the Burj Khalifa, Dubai Mall, and Palm Jumeirah.",
        "Day 2: Head to Abu Dhabi — visit Sheikh Zayed Grand Mosque and Ferrari World.",
        "Day 3: Go to the desert for a safari and stargazing."
    ],
    "Oman": [
        "Day 1: Visit Muscat — explore the Sultan Qaboos Grand Mosque, Al Jalali and Al Mirani forts.",
        "Day 2: Take a trip to Nizwa to visit Nizwa Fort and the traditional souk.",
        "Day 3: Explore the Wahiba Sands desert and Wadi Shab."
    ],
    "Chile": [
        "Day 1: Visit Santiago — explore Plaza de Armas, the Museum of Memory and Human Rights.",
        "Day 2: Head to Valparaíso — explore the colorful city, street art, and beaches.",
        "Day 3: Visit the Atacama Desert — see the Valle de la Luna and salt flats."
    ],
    "Namibia": [
        "Day 1: Visit Windhoek — explore the city and the Independence Memorial Museum.",
        "Day 2: Go to Sossusvlei — explore the stunning red sand dunes and Dead Vlei.",
        "Day 3: Visit Etosha National Park for a safari to spot wildlife."
    ],
    "Peru": [
        "Day 1: Visit Lima — explore the Miraflores district, the historic center, and museums.",
        "Day 2: Head to Cusco — explore the Sacred Valley and the Temple of the Sun.",
        "Day 3: Take a day trip to Machu Picchu — hike to the ancient Inca citadel."
    ],
    "Canada": [
        "Day 1: Visit Toronto — explore the CN Tower, Ripley’s Aquarium, and the Royal Ontario Museum.",
        "Day 2: Head to Niagara Falls — enjoy the views and take a boat ride to the base of the falls.",
        "Day 3: Explore Vancouver — visit Stanley Park, Granville Island, and Grouse Mountain."
    ],
    "Switzerland": [
        "Day 1: Visit Zurich — explore the Old Town, Lake Zurich, and the Swiss National Museum.",
        "Day 2: Head to Lucerne — visit the Chapel Bridge, Lion Monument, and take a boat cruise on Lake Lucerne.",
        "Day 3: Explore the Swiss Alps and enjoy a day of skiing or hiking in Zermatt."
    ],
    "Italy": [
        "Day 1: Explore Rome — visit the Colosseum, Roman Forum, and Vatican City.",
        "Day 2: Head to Florence for art and culture — visit Uffizi Gallery and climb the Duomo.",
        "Day 3: Visit Venice — take a gondola ride along the canals and explore St. Mark's Square."
    ],
    "Germany": [
        "Day 1: Visit Berlin — explore the Brandenburg Gate, Berlin Wall, and Museum Island.",
        "Day 2: Take a trip to Bavaria — visit Neuschwanstein Castle and the picturesque town of Füssen.",
        "Day 3: Explore Munich — visit Marienplatz, the English Garden, and Hofbräuhaus."
    ],
    "Norway": [
        "Day 1: Visit Oslo — explore the Royal Palace, Akershus Fortress, and the Viking Ship Museum.",
        "Day 2: Take a scenic drive to Bergen — explore Bryggen and take a funicular ride to Mount Fløyen.",
        "Day 3: Visit the Geirangerfjord for a stunning boat tour of the fjords."
    ],
    "New Zealand": [
        "Day 1: Explore Auckland — visit the Sky Tower, Auckland War Memorial Museum, and Waiheke Island.",
        "Day 2: Head to Rotorua for geothermal parks, hot springs, and Maori cultural experiences.",
        "Day 3: Visit Queenstown for adventure activities like bungee jumping, hiking, and scenic cruises."
    ],
    "Argentina": [
        "Day 1: Visit Buenos Aires — explore the colorful La Boca, Recoleta Cemetery, and Plaza de Mayo.",
        "Day 2: Head to Mendoza — visit wineries and enjoy wine tastings in Argentina's wine region.",
        "Day 3: Explore Patagonia — visit the Perito Moreno Glacier and Los Glaciares National Park."
    ],
    "France": [
        "Day 1: Visit Paris — explore the Eiffel Tower, Louvre Museum, and Montmartre.",
        "Day 2: Take a day trip to Versailles to see the Château de Versailles and its gardens.",
        "Day 3: Visit the French Riviera — enjoy Nice, Cannes, and the stunning Mediterranean coastline."
    ],
    "Austria": [
        "Day 1: Visit Vienna — explore the Schönbrunn Palace, St. Stephen's Cathedral, and the Belvedere Palace.",
        "Day 2: Head to Salzburg — visit Mozart's birthplace, Hohensalzburg Fortress, and Mirabell Gardens.",
        "Day 3: Explore the Austrian Alps — enjoy skiing, hiking, or a scenic drive through the mountains."
    ],
    "Spain": [
        "Day 1: Visit Madrid — explore the Royal Palace, Prado Museum, and Retiro Park.",
        "Day 2: Head to Seville — visit the Alcázar Palace, Seville Cathedral, and Plaza de España.",
        "Day 3: Visit Barcelona — explore La Sagrada Familia, Park Güell, and the Gothic Quarter."
    ],
    "Portugal": [
        "Day 1: Visit Lisbon — explore the Belém Tower, Jerónimos Monastery, and Alfama district.",
        "Day 2: Head to Porto — visit the Ribeira district, Livraria Lello, and enjoy wine tastings.",
        "Day 3: Explore Sintra — visit the Pena Palace and Quinta da Regaleira."
    ],
    "Czech Republic": [
        "Day 1: Explore Prague — visit Prague Castle, Charles Bridge, and Old Town Square.",
        "Day 2: Visit Český Krumlov — explore the historic town center and the beautiful castle.",
        "Day 3: Visit Kutná Hora — see the famous Sedlec Ossuary and St. Barbara's Church."
    ],
    "Greece": [
        "Day 1: Explore Athens — visit the Acropolis, Parthenon, and the Temple of Olympian Zeus.",
        "Day 2: Visit Santorini — enjoy the breathtaking views, relax on the black sand beaches, and explore Oia.",
        "Day 3: Visit Mykonos — experience the vibrant nightlife and stunning beaches."
    ],
    "Turkey": [
        "Day 1: Visit Istanbul — explore the Hagia Sophia, Blue Mosque, and Topkapi Palace.",
        "Day 2: Head to Cappadocia for a hot air balloon ride and explore the rock formations.",
        "Day 3: Visit Pamukkale for the famous thermal springs and white terraces."
    ],
    "Japan": [
        "Day 1: Visit Tokyo — explore Shibuya Crossing, Meiji Shrine, and the Imperial Palace.",
        "Day 2: Take a bullet train to Kyoto — see the Golden Pavilion, Fushimi Inari Shrine, and Kiyomizu-dera.",
        "Day 3: Visit Osaka — enjoy the bustling Dotonbori, Osaka Castle, and the Universal Studios Japan theme park."
    ],
    "South Korea": [
        "Day 1: Visit Seoul — explore Gyeongbokgung Palace, Bukchon Hanok Village, and Myeongdong.",
        "Day 2: Take a trip to Jeonju for traditional Korean food and culture.",
        "Day 3: Visit Busan — relax at Haeundae Beach, visit Gamcheon Culture Village, and see the Beomeosa Temple."
    ],
    "Malaysia": [
        "Day 1: Explore Kuala Lumpur — visit the Petronas Towers, Batu Caves, and Merdeka Square.",
        "Day 2: Head to Penang — explore George Town, Kek Lok Si Temple, and enjoy local street food.",
        "Day 3: Visit Langkawi — relax on the beaches and take a cable car ride to the top of Gunung Mat Cincang."
    ],
    "Singapore": [
        "Day 1: Visit Marina Bay — explore the Gardens by the Bay, Marina Bay Sands, and the Merlion.",
        "Day 2: Visit Sentosa Island — enjoy Universal Studios, S.E.A. Aquarium, and the beaches.",
        "Day 3: Explore Chinatown, Little India, and Kampong Glam for cultural experiences."
    ],
    "United Kingdom": [
        "Day 1: Explore London — visit Buckingham Palace, Tower of London, and the British Museum.",
        "Day 2: Take a trip to Bath — visit the Roman Baths and explore the Georgian architecture.",
        "Day 3: Visit Edinburgh — explore the Royal Mile, Edinburgh Castle, and Arthur's Seat."
    ],
    "Netherlands": [
        "Day 1: Explore Amsterdam — visit the Rijksmuseum, Anne Frank House, and canal tours.",
        "Day 2: Visit Keukenhof Gardens during tulip season and Zaanse Schans for windmills.",
        "Day 3: Visit Rotterdam for modern architecture and the Maritime Museum."
    ],
    "Australia": [
        "Day 1: Explore Sydney — visit the Opera House, Bondi Beach, and the Sydney Harbour Bridge.",
        "Day 2: Head to the Great Barrier Reef — take a snorkeling or diving tour.",
        "Day 3: Visit Melbourne — explore Federation Square, the Royal Botanic Gardens, and take a road trip along the Great Ocean Road."
    ]
}

selected_country = st.selectbox("Choose a Country for Itinerary:", country_options)

if st.button("Show Itinerary Plan"):
    if selected_country == "Select a country...":
        st.warning("Please select a valid country.")
    else:
        st.markdown(f"Itinerary for {selected_country}:")
        if selected_country in itineraries:
            for day in itineraries[selected_country]:
                st.write(day)
        else:
            st.info(f"Sorry, no itinerary available for {selected_country} yet.")

# Adding this footer for writing our names
st.markdown("---")
st.caption("Made by Natalie and Cici from CMSI1010! | The Tripteller 2025 Edition")