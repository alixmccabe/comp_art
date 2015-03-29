import random
import string

lev_dis = {}
def levenshtein_distance(s1,s2):
	""" Computes the Levenshtein distance between two input strings """
	if len(s1) == 0:
		return len(s2)

	if len(s2) == 0:
		return len(s1)

	if 's1,s2' in lev_dis:
		return lev_dis[s1,s2]

	else:
		lev_dis[s1,s2] = min([int(s1[0] != s2[0]) + levenshtein_distance(s1[1:],s2[1:]), 1+levenshtein_distance(s1[1:],s2), 1+levenshtein_distance(s1,s2[1:])])

		return lev_dis[s1,s2]

def mutate_text(message, prob_ins=0.05, prob_del=0.05, prob_sub=0.05):
    """
    Given a Message and independent probabilities for each mutation type,
    return a length 1 tuple containing the mutated Message.

    Possible mutations are:
        Insertion:      Insert a random (legal) character somewhere into
                        the Message
        Deletion:       Delete one of the characters from the Message
        Substitution:   Replace one character of the Message with a random
                        (legal) character
    """
    if random.random() < prob_ins:
	    index = random.sample(range(len(message)),1)[0]
	    message = message[0:index] + random.choice(string.letters) + message[index:len(message)]
	    message = message.upper()

    if random.random() < prob_del:
	    index = random.sample(range(len(message)),1)[0]
	    message  = message[0:index] + message[index+1:len(message)]


    if random.random() < prob_sub:
	    index = random.sample(range(len(message)),1)[0]
	    message = message[0:index] + random.choice(string.letters) + message[index+1:len(message)]

    # TODO: Also implement deletion and substitution mutations
    # HINT: Message objects inherit from list, so they also inherit
    #       useful list methods
    # HINT: You probably want to use the VALID_CHARS global variable

    return (str(message), )   # Length 1 tuple, required by DEAP

print mutate_text('POOPY POOPY POOP')