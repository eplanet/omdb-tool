#!/usr/bin/python3

"""
    This file is part of omdb-tool.

    omdb-tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    omdb-tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with omdb-tool.  If not, see <http://www.gnu.org/licenses/>.
"""


def displayMovieChoice(results):
    for i in range(0,len(results)) :
        r = results[i]
        print("%d [%s - %s]> %s [%s]" % (i, r["Type"], r["Year"], r["Title"], r["imdbID"]))
    moviechoice = -1
    if len(results) == 1:
        return 0
    while not moviechoice in range(0, len(results)) :
        moviechoice = input("Movie choice (ENTER to cancel)> ")
        if moviechoice == "" :
            break
        try :
            moviechoice = int(moviechoice)
        except :
            print("You should input an integer !")
    return moviechoice

def displayMovieName(movieId):
    moviedata = api.RequestMovieDetails(movieId)
    moviepath = api.NormalizeWindowsPath("%s (%s - %s) %s" % (moviedata["Title"], moviedata["Year"], moviedata["Director"], moviedata["Actors"]))
    print(moviepath)
    print("Genre : %s" % (moviedata["Genre"]))
    print("Plot  : %s" % (moviedata["Plot"]))
    return moviedata

def processMovieQuery(moviename):
    results = api.RequestMovie(moviename)
    if results == None:
        print("Bad query has been submitted, please try again")
        return None
    moviechoice = displayMovieChoice(results)
    if moviechoice == "":
        return None
    return displayMovieName(results[moviechoice]["imdbID"])

if __name__ == "__main__":
    import os, sys, argparse, json
    import omdbapi
    
    api = omdbapi.omdbapi()
    moviedata = None
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to process movies from")
    args = parser.parse_args()
    if (args.directory) :
        if(not os.path.exists(args.directory)) :
            parser.print_help()
            sys.exit(1)
        else :
            for f in os.listdir(args.directory):
                path = os.path.join(args.directory,f)
                if os.path.isdir(path):
                    continue
                print("Processing: ", os.path.splitext(f)[0])
                moviedata = processMovieQuery(os.path.splitext(f)[0])
    else :
        print("After one search, say '--print' to display the raw JSON")
        while(True) :
            moviename = ""
            while moviename == "" :
                moviename = input("Movie name> ")
            if moviename == "--print" :
                print(json.dumps(moviedata, sort_keys = False, indent = 4))
            else :
                movidedata = processMovieQuery(moviename)
