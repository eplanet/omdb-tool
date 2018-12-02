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

def run():
    import os, sys, argparse, json
    import omdbtool
    
    moviedata = None
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apikey", required=True,
        help="API key to use OMDb API")
    parser.add_argument("-d", "--directory",
        help="Directory to process movies from")
    args = parser.parse_args()
    api = omdbtool.omdbapi(args.apikey)
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
                moviedata = api.process_movie_query(os.path.splitext(f)[0])
    else :
        print("After one search, say '--print' to display the raw JSON")
        while(True) :
            moviename = ""
            while moviename == "" :
                moviename = input("Movie name> ")
            if moviename == "--print" :
                print(json.dumps(moviedata, sort_keys = False, indent = 4))
            else :
                movidedata = api.process_movie_query(moviename)

if __name__ == "__main__":
    run()
