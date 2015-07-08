"""
This code is part of my (Katherine Sittig-Boyd's) senior thesis project, which investigates the way 
gender is discussed in a microblogging context, since many prior studies have focused on gender expression
and patterns used in speech in other online communication contexts, such as forums, email conversations, and the like.

This is all interesting and all, but what I'm particularly interested in is delving into how Twitter users discuss gender,
specifically in the context of nonbinary, trans, and genderqueer/nonconforming individuals. Since many Twitter users do not
gender themselves in their profiles, I will not be analyzing the gender of the speakers as a primary focus of this project,
and am instead going to focus on the ideas perpetuated by these users and what kind of message they send.

For instance, there are already means to determine whether a given trending hashtag, used collectively by Twitter users site-,
nation-, and worldwide, is trending with positive or negative sentiment (for instance, individuals celebrating a sports win
might create a positively trending hashtag, while people angry with a political debate might cause an associated hashtag to 
trend negatively). However, with hashtags that are not widely used, or "trending," eg those related to trans/nb/gq identities,
it is valuable to identify certain patterns that exist within the nature of these posts.

There are a few approaches I will likely begin to take on this project, and they are as follows:

1. Identify sentiment of tweets associated with a specific hashtag or set of hashtags, for instance #TransIsBeautiful, 


"""

class User:
    def __init__(self,h=None,uid=None):
        self.handle=h # CAN CHANGE so is this even relevant tbh
        self.user_id=h
        
        # both of these are dictionaries that keep a tally of how many times these users have interacted (mutually?)
        self.tweeted_to={}
        self.tweeted_at={} 
        self.hostility=0 # be generous to start!
        self.positivity=0 # I guess less generous?
        
    def __print__(self):
        """ 
        This method displays the user's current handle, their id, and how many people they share mutual relationships with 
        """
        dis_string="Handle: %s\n Number of relationships: %d\n Positivity: %d\n Hostility: %d"%(self.handle,self.find_num_mutuals(),self.positivity,self.hostility)
        return dis_string
        
    def is_mutual(self,other_user):
        """
        This method will determine whether or not two users have each tweeted at one another.
        For a 
        """
        if self.tweeted_to.keys().contains(other_user.user_id):
            if other_user.tweeted_to.keys().contains(self.user_id):
                return True
        return False
        
    def find_num_mutuals(self):
        """
        This method will use a simple intersection method. I'm gonna write it for now because I'm on a plane & can't look up the syntax haha
        """
        mutuals=0 
        received=self.tweeted_at.keys()
        for u in self.tweeted_to.keys():
            if u in received:
                mutuals+=1
        return mutuals
        
    def increase_hostility(self):
        self.hostility+=1
        
    def increase_positivity(self):
        self.positivity+=1
        
    def get_hostility(self):
        return self.hostility
        
    def get_positivity(self):
        return self.positivity
        
        
#    def add_tweeted_to(self,user):
#        if 
        
    def increase_interactions(self,uid):
        self.tweeted_to[uid]+=1
        
    
    
    
    
class UserGraph:
    users=0
    
    def __init__(self):
        self.__class__.users+=1
        # the keys to vertices are uids (strings), which can be used to get more information about a user
        self.vertices={} # so vertices[v] is a list of vertices connected to v FROM v
        self.edges=0 # no edges to start
        # idk what else actually
    
    def add_vertex(self,v):        
        self.vertices[v]=set()
    
    def add_edge(self, v, w):
        """
        Given vertices v and w, create an edge between them
        """
        #self.vertices.append(v) # this is such a terrible idea lol there is no structure whatsoever 
        if self.vertices.has_key(v)==False:
            self.vertices[v]=set()
        if self.vertices.has_key(w)==False:
            self.vertices[w]=set()
        self.vertices[v].add(w)
        self.edges+=1
        
    def adj(self,v):
        # return any vertex connected to vertex V where v --> other vertex
        return self.vertices[v]
        
    def has_path_to(self,v,w):
        # returns a boolean that signifies whether or not there exists a path between v and w
        ver=self.dfs(v)
        return w in ver 
        
    def dfs(self,v,visited=None):
        if visited==None:
            visited=set()
        visited.add(v) 
        for ver in self.vertices[v]-visited:
            self.dfs(ver,visited)
        return visited
        
    def find_hostility_between(self,v,w):
        """
        write this doc
        """
        vhost=v.get_hostility()
        whost=w.get_hostility()
                
    def v(self):
        return len(self.vertices.keys())

    def e(self):
        return (self.edges) # ??
        
        
def main():
    katie=User(h="katiegoogling")
    jillie=User(h="bean_jillie")
    
    ug=UserGraph()
    ug.add_vertex("katiegoogling")
    ug.add_edge("katiegoogling","bean_jillie")
    print ug.v()
    #print "blah blah it's 12 am"
    print "the following vertices are adjacent to katiegoogling: " 
    print ug.adj("katiegoogling")
    print ug.has_path_to("katiegoogling","xer")
    
def calc_hostility(tweet):
    # this is the part that will get fun!! 
    
    return None
    
def read_tweet_data(filepath):
    data=""
    form_ugraph(data)
    
def form_ugraph(data):
    users=UserGraph()
    
    
    
#main()