import json
from tweetgraph import UserGraph,User
tweet_file="/home/ksb/Documents/thesis/tweet_data/trans_mtf_ftm_genderqueer_nb_july1.txt" # in the future this will be part of a loop but hardcoded for now
def main():
    tweet_graph=UserGraph()
    print "*** Going to analyze %s***"%tweet_file
    success=0
    failure=0
    tfile=open(tweet_file,'r')
    topics=""
    for line in tfile:
        if topics=="":
            for l in line:
                if l != "{":
                    topics+=l
                else:
                    break
            line=line[len(topics):]
        try:
            if success<5: # remove in the future, just keeping it reasonable for now 
                tf=json.loads(line)
                if is_english(tf):
                    if calculate_hostility(extract_text(tf))<0:
                        success=5
                        print "success: %d"%success
                        print "end"
                    success+=1
                    print "\n\n"
            else:
                break
        except:
            failure+=1
            pass
    tfile.close()    
    print "Success: %d\nFailure: %d"%(success,failure)

def add_to_graph(handle,graph):
    graph.add_vertex(handle)
    
def add_interaction(handle,otherhandle,graph):
    graph.add_edge(handle,otherhandle)
    
def calculate_hostility(text):
    # who knows how this will work
    
    return hostility 
    
def extract_user(tweet):
    try:
        print tweet['user']['screen_name']
        return True
    except:
        return False

def is_english(tweet):
    return tweet['lang']=="en"
        
def extract_hashtags(tweet):
    return tweet['entities']['hashtags']

def extract_text(tweet):
    return tweet['text']

def extract_umentions(tweet):
    return tweet['user_mentions']
    
def is_retweet(tweet):
    return 'RT' in tweet

main()