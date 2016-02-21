#!/usr/bin/python3

if __name__ == "__main__":
    import os, sys, argparse, json
    import omdbapi
    
    api = omdbapi.omdbapi()
    moviedata = None
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to process movies from")
    args = parser.parse_args()
    if (args.directory) :
        # TODO: loop in directory and propose choices to user
        pass
    else :
        print("After one search, say '--print' to display the raw JSON")
        while(True) :
            moviename = ""
            while moviename == "" :
                moviename = input("Movie name> ")
            if moviename == "--print" :
                print(json.dumps(moviedata, sort_keys = False, indent = 4))
            else :
                results = api.RequestMovie(moviename)
                if results == None:
                    print("Bad query has been submitted, please try again")
                    continue
                for i in range(0,len(results)) :
                    r = results[i]
                    print("%d [%s]> %s (%s) [%s]" % (i, r["Type"], r["Title"], r["Year"], r["imdbID"]))
                moviechoice = -1
                while not moviechoice in range(0, len(results)) :
                    moviechoice = input("Movie choice (ENTER to cancel)> ")
                    if moviechoice == "" :
                        break
                    try :   
                        moviechoice = int(moviechoice)
                    except :
                        print("You should input an integer !")
                if moviechoice == "":
                    continue
                moviedata = api.RequestMovieDetails(results[moviechoice]["imdbID"])
                moviepath = api.NormalizeWindowsPath("%s (%s - %s) %s" % (moviedata["Title"], moviedata["Year"], moviedata["Director"], moviedata["Actors"]))
                print(moviepath)
                print("Genre : %s" % (moviedata["Genre"]))
                print("Plot  : %s" % (moviedata["Plot"]))
    

