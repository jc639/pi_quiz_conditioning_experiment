#!/usr/bin/env python
# -*- coding: utf-8 -*-

q_a = [('Humans glow in the dark, but it’s too faint to see?', 'T'), ('There are more calories in a single peanut than in an 8oz steak?', 'F'), ('Oxford university has been around longer than the Aztec empire?', 'T'), ('The fax machine was patented in 1843?', 'T'), ('The oldest living organism on earth is a Galapagos tortoise named Harriet?', 'F'), ('The darker the coffee roast, the less caffeine it contains?', 'T'), ('Crocodiles are capable  of ‘negligible senescence’. In the right conditions, they technically have no limit to their life span?', 'T'), ('Male octopuses grow an extra arm in a pouch under their eye which is actually a penis?', 'T'), ('Heavy metal music has existed longer as a genre than blues. Some historians actually believe heavy metal is actually a huge influence on blues?', 'F'), ('The first game of baseball was played with a dried and stitched head of a wombat, rather than a ball?', 'F'), ('As far as has ever been reported, no-one has ever seen an ostrich bury its head in the sand.', 'T'), ('Approximately one quarter of human bones are in the feet.', 'T'), ('Popeye’s nephews were called Peepeye, Poopeye, Pipeye and Pupeye.', 'T'), ('In ancient Rome, a special room called a vomitorium was available for diners to purge food in during meals.', 'F'), ('The average person will shed 10 pounds of skin during their lifetime.', 'F'), ('Sneezes regularly exceed 100 m.p.h.', 'T'), ('A slug’s blood is green.', 'T'), ('The Great Wall Of China is visible from the moon.', 'F'), ('Virtually all\xa0Las Vegas gambling casinos ensure that they have no clocks.', 'T'), ('The total surface area of two human lungs have a surface area of approximately 70 square metres.', 'T'), ('A man from the USA consumed his 26,000th Big Mac on 11th October 2012, after eating at least one a day for forty years.', 'T'), ('The longest distance swam underwater in one breath is 200 metres. (6th November 2008)', 'T'), ('The record for most needles inserted into the head is 15,000.', 'F'), ('The world’s longest legs belong to a Russian lady and measure 132cm', 'T'), ('The heaviest aircraft pulled by a single man weighed 188.83 tonnes and was pulled 8.8 metres.', 'T'), ('The record for the fastest time to solve a Rubik’s Cube one-handed is 37 seconds', 'F'), ('The world’s tallest living man is 251cm / 8 ft 3 in', 'T'), ('The record for the longest rail tunnel is held by the Channel Tunnel between Britain and France?', 'F'), ('There are crystals in your head, and if you knock them loose, you can become dizzy or ill?', 'T'), ('Oreo cookies predate chocolate chip cookies by over 25 years?', 'F'), ('Sir Paul McCartney’s middle name is James?', 'F'), ('Jupiter is the fifth planet from the sun.', 'T'), ('Gillian Anderson was born in Chicago, Illinois.', 'T'), ('Lithium has the atomic number 17.', 'F'), ('The Guinness World Record for most fingers and toes at birth is held by an Indian man born with 14 fingers and 20 toes in total.', 'T'), ('The oldest building in the world is the Pyramid of Djoser in Egypt.', 'F'), ('Engelbert Humperdinck was born in 1928.', 'F'), ('Sir Steve Redgrave is the only rower to have received the award of BBC Sports Personality of the Year.', 'T'), ('Hotmail was launched in 1996.', 'T'), ('From the ground to the torch, the Statue of Liberty is 93 metres high.', 'T'), ('There are some wasps that make honey.', 'T'), ('Marie Curie’s husband was called Pierre.', 'T'), ('The Lutine Bell can be found in Lloyds of London.', 'T'), ('Seoul is the capital of North Korea.', 'F'), ('According to Scottish law, it is illegal to be drunk in charge of a cow.', 'T'), ('The violent gang of youths in ‘A Clockwork Orange’ were called the ‘Groods’.', 'F'), ('Danny Jones is a member of the band McFly.', 'T'), ('In the television series ‘Mork and Mindy’, Mindy was played by Erin Moran.', 'F'), ('Beth Tweddle won a Silver Medal at the 2012 London Olympic Games.', 'F'), ('Marie Antoinette was married to Louis XVI of France.', 'T'), ('UK shops earn more revenue from Halloween than they do from Bonfire Night?', 'T'), ('In the year 2020, Halloween will fall on a Tuesday.', 'F'), ('The Celtic festival of ‘Samhain’ marks the end of the harvest season and takes place from sunset on October 31st until sunset on November 1st.', 'T'), ('Christopher Lee, famous for portraying Count Dracula in Hammer Horror films, was born on Halloween in 1922.', 'F'), ('Michael Keaton was originally offered Johnny Depp’s leading role in the 1990 film ‘Edward Scissorhands.’', 'F'), ('Jack MacGowran and Vasiliki Maliaros both acted in the film ‘The Exorcist’ and died in the same year it was released.', 'T'), ('Stephen King’s ‘The Shining’ was originally called ‘Halloween Hotel’.', 'F'), ('More of the Empire State building in New York is below ground than above ground?', 'F'), ('The national animal of Scotland is the unicorn?', 'T'), ('With 19 company headquarters within the borders of the state, Minnesota is home to more fortune 500 companies than any other state?', 'F'), ('Alliumphobia is a fear of garlic.', 'T'), ('‘Fauntleroy’ is the middle name of Donald Duck.', 'T'), ('Henry VIII had an extra finger on each hand.', 'F'), ('The singer ‘Cher’ was born Cherilyn Sarkisian.', 'T'), ('Alfred Hitchcock had no belly button as it was removed during surgery.', 'T'), ('The ‘black box’ in an aeroplane is black.', 'F'), ('Michael Jackson had a pet python called ‘Crusher’.', 'T'), ('The distance, as the crow flies, from London to Edinburgh, is greater than the distance from London to Glasgow.', 'F'), ('Geri Halliwell named her daughter ‘Bluebell Madonna’.', 'T'), ('Brendan O’Carroll, famous as ‘Mrs Brown’ from ‘Mrs Brown’s Boys’ is the cousin of Kenneth Branagh.', 'F'), ('There are 259 steps up to the ‘Whispering Gallery’ in St Paul’s Cathedral.', 'T'), ('The reverse of the Nobel Peace Prize, shows three naked men, standing with their hands on each other’s shoulders.', 'T'), ('Centipedes always have 100 feet.', 'F'), ('The world record for a human to hold their breath underwater is 8 minutes 27 seconds.', 'F'), ('Olympus Mons, Mount Olympus on Mars, is taller than Mount Everest.', 'T'), ('The world’s oldest known tree is over 9000 years old.', 'T'), ('A cross between a horse and a zebra is called a Hobra.', 'F'), ('111,111,111 x 111,111,111 = 12,345,678,987,654,321', 'T'), ('Muscle turns to fat if you stop exercising.', 'F'), ('The world’s smallest book is 1cm wide, 1cm tall and 4mm deep.', 'F'), ('A ‘cama’ is a hybrid which is a cross between a Camel and llama.', 'T'), ('Chinstrap and Humboldt are both species of Penguin.', 'T'), ('Litmus paper turns blue under acidic conditions?', 'F'), ('The ‘Volga’ is the longest river in Europe?', 'T'), ('Rarefactions is the phenomenon of light changing direction when it passes through another medium?', 'F'), ('Hydrogen has the atomic number 1?', 'T'), ('Zero degrees Celsius is equal to 24 degrees on the Fahrenheit scale?', 'F'), ('The humerus the longest bone in the human body?', 'F'), ('Dogs cannot see colour?', 'F'), ('Abraham Lincoln and Albert Einstein were alive at the same time. Their lives overlapped by 14 years?', 'F'), ('An emu cannot fly?', 'T'), ('A Dowager is the widow of a peer or a baronet?', 'T'), ('Julie Andrews was the original Eliza Doolittle in My Fair lady?', 'T'), ('Fleas are bloodsuckers?', 'T'), ('Wyoming is on the Canadian border of the USA?', 'F'), ('Two is a Prime number?', 'T'), ('Quaker is another name for a Mormon?', 'F'), ('Top Eastenders totty Wendy Richard is the cousin of top religious singing superstar Cliff Richard?', 'F'), ('Silly mid on is a fielding position in cricket?', 'T'), ('Spartacus was a great Roman general?', 'F'), ('Edinburgh is further East than Carlisle?', 'F'), ('Kangaroos are only an inch long at birth?', 'T'), ('Warner Brothers originally wanted Ronald Reagan to play the part of Rick Blaine in Casablanca?', 'T'), ('The most northerly point on the British mainland is actually named after a Dutchman?', 'F'), ('Cary Grant and Noel Coward were both offered the part of James Bond in Dr. No?', 'T'), ("George Washington's body was preserved in a barrel of Whiskey for 32 years?", 'F'), ('Born in Crew in 1837, George Gascoigne was the great-grandfather of Bamber Gascoigne and the great-great-grandfather of Paul Gascoigne?', 'F'), ('The Lascar Parrot of Borneo has a venemous spit that can paralyse small rodents within seconds?', 'F'), ('The can-opener was not invented until 45 years after the tin can?', 'T'), ("President Theodore Roosevelt's son was called Kermit?", 'T'), ('The total weight of termites on earth is much heavier than the total weight of humans on earth?', 'T'), ('The total weight of all the humans on earth is greater than that of all the cows on earth?', 'F'), ('‘La Isla Bonita’, ‘Papa Don’t Preach’ and ‘Open Your Heart’ are all songs by Madonna?', 'T'), ('You can go ice skating on the Eiffel Tower during the Christmas holidays?', 'T'), ('Haem is the iron-containing component that gives blood its red colour?', 'T'), ('Haddock is the most widely-eaten fish by humans?', 'F'), ('Lady Jane Grey was Queen of England for just 9 days in 1553?', 'T'), ('Diurnal is the scientific antonym for nocturnal?', 'T'), ('The Spanish food ‘Tapas’ literally translates to ‘lid’ or ‘cover’?', 'T'), ('‘Crapula’ is the latin word for sickness caused by excessive eating or drinking?', 'T'), ('Onology is the science of making gin?', 'F'), ('Gourde, Lempira, Rial, Ringgit, Togrog and Cordoba are all types of currency?', 'T'), ('The Jabberwocky was slain with a vorpal blade near the Tumtum tree?', 'T'), ('“I’ll have what she’s having” is a quote from the film Casabanca?', 'F'), ('The ‘Discovery’ is an ill fated space ship from the film 2001: A Space Odyssey?', 'T'), ('Putting the spoon handle into the neck of an opened bottle of sparkling wine will help the alcohol retain its fizz?', 'F'), ('The word ‘graffiti’ is derived from the latin word ‘stylus’?', 'T'), ('Corcodile, Alligator, Cayman and Gavial are the only members of the order ‘Crocodilia’?', 'T'), ('In Italy, the number 33 is considered unlucky?', 'F'), ('Charlie Chaplin died on Christmas day, 1977?', 'T'), ('The USSR was officially dissolved in 1989?', 'F'), ('The Shrine of the Three Kings, a reliquary said to contain the bones of the Three Wise Men, can be visited in the cathedral in Cologne?', 'T'), ('‘November Sinterklaas’, the Dutch Father Christmas, is said to arrive in Holland by steamboat from Spain?', 'T'), ('In the 1960’s, the North American Aerospace Defense Command started tracking Santa’s flight path around the world?', 'T'), ('For chips prepared in the home, nearly 60% are over baked?', 'T'), ('Fans of wedges are most likely to dip them in ketchup?', 'F'), ('Valentine Tereshkova was the first woman in space?', 'T'), ('The first recorded valentine was sent in the year 1300?', 'F'), ('Doves mate for life?', 'T'), ("Part of a Valentine's tradition derives from a Roman festival where boys and girls took it in turns to draw names out of a hat and later got married.", 'T'), ('Two is the only even prime number?', 'T'), ('A group of peacocks is called a parliament?', 'F'), ('The African Rhinoceros has two horns on its head?', 'T'), ("In the film Fantasia, the Sorceror's name was Yensid?", 'T'), ('Identical twins have the same fingerprints?', 'F'), ('Elvis Presley was a black belt in Karate?', 'T'), ('A rat can survive longer without water than a camel?', 'T'), ('Charlie Chaplin once won first prize in a Charlie Chaplin look-a-like contest?', 'F'), ('Rubies and Sapphires are exactly alike except in colour?', 'T'), ("Donald Duck's middle name is Fauntelroy?", 'T'), ('Sharks do not blink?', 'T'), ('All polar bears are left-handed?', 'T'), ('Westward Ho! Is the only town/city in the UK with an exclamation mark in its name?', 'T'), ('Approximately 80,000 photographs are taken around the world every second?', 'F'), ('Most Eskimoes have fridges?', 'T'), ('Thomas Edison (who invented the light bulb) was afraid of the dark?', 'T'), ('Metathesiophobia is the fear of hairdressers?', 'F'), ('Mickey Mouse made his on-screen debut in the same cartoon as Minnie Mouse made hers?', 'T'), ('An ostrich’s eye is bigger than its brain?', 'T'), ('In space it’s impossible to cry?', 'T'), ('Slugs don’t have noses?', 'F'), ('Shakespeare’s Macbeth was a real person', 'T'), ('The first Mickey Mouse film was silent?', 'T'), ('`Copyrightable` is the longest word in the English language that can be written without repeating a letter?', 'F'), ('Clinophobia is the fear of beds?', 'T'), ('In America, on 1st January 2001, over 3700 prisoners were sentenced to death', 'F'), ('Taphephobia is the fear of losing your teeth?', 'F'), ('Puff the Magic Dragon played on Cherry Lane?', 'T'), ('The 1945 military operation ‘Manna’ was based in Germany?', 'F'), ('There are 8 countries in the world with nuclear submarines?', 'F'), ('The American inventor of the deep-freezing process was a Mr Birdseye?', 'T'), ('Sideburns were named after a prominant wearer, a General Ambrose E Burnside?', 'T'), ('Scotland Yard was originally the name of a medieval house used by Scots Kings visiting London?', 'T'), ('The Oxford-Cambridge Boat Race has never ended in a dead heat?', 'F'), ('The first non-white British MP was elected over 100 years ago?', 'T'), ('The Queen holds UK Passport No.1?', 'F'), ('3 times more people were killed in the 1906 San Francisco Earthquake than on the Titanic in 1912?', 'F'), ('Humphrey Bogart never said "Play it again Sam" in Casablanca?', 'T'), ('A granny, a sheepshank and a bowline are all parts of chimney?', 'F'), ('You can still be executed for certain crimes in England?', 'F'), ('Pakistan and India are neighbouring countries?', 'T'), ('The 2004 Olympic Games were hosted by Greece?', 'T'), ('The Titanic sank in the year 1932?', 'F'), ("Homer Simpson's mother is called Maria", 'F'), ('An average human heart will have beat approximately 1.5 billion times when it reaches the age of 66 years.', 'F'), ("The author of 'Alice in Wonderland' wrote under the pen-name Lewis Carroll but his real name was Charles Lutwidge Dodgson", 'T'), ('Sound travels much slower through water than through air.', 'F'), ('Murdoc Niccals is the leader of the virtual band Gorillaz.', 'T'), ('Earthworms breathe through their skin.', 'T'), ('During the average life of a Venus Flytrap plant, each separate trap may catch over 500 insects.', 'T'), ('The Great Fire of London swept through the centre of the English city in the year 1466.', 'F'), ('The rock band Snow Patrol were originally called Shrug.', 'T'), ('Some types of seaweed can grow 50 centimetres in a day.', 'T'), ('The correct name for an eagle’s nest is a ‘watch’.', 'F'), ('Walt Disney’s full name was Walter Elias Disney.', 'T'), ('The seahorse is the only fish with a prehensile tail?', 'T'), ('Lassie is a female character but has always been played by a male dog?', 'T'), ('Malta is the nearest commonweath country to the UK?', 'T'), ('‘James’ was the first name of Officer Dibble in Top Cat?', 'F'), ('The bestselling American Author Danielle Steel has over 500 million copies of her books in print?', 'T')]
