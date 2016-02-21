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

import os, sys, urllib.request, urllib.parse, urllib.error, urllib.parse, json, re

URL_BASE = "http://www.omdbapi.com/"
URL_SEARCH = "%s?s=" % (URL_BASE)
URL_TITLE = "%s?t=" % (URL_BASE)
URL_GETIMDB = "%s?i=" % (URL_BASE)
CHAR_REPLACE = " ._"
CHAR_DELETE = "()"

class omdbapi:

    def FormatInputToQuery(self, moviename) :
        format = moviename
        for c in CHAR_REPLACE :
            format = format.replace(c, "+")
        ret = ""
        year = ""
        for m in format.split("+") :
            if m.isdigit() and len(m) == 4 :
                year = "&y=%s" % (m)
            elif m.isalnum() :
                if len(ret) > 0 :
                    ret += "+"
                ret += m
        return ret + year

    def NormalizeWindowsPath(self, iPath):
        return re.sub('[:/]', '', iPath)

    def RequestMovie(self, moviename) :
        query = self.FormatInputToQuery(moviename)
        print(URL_SEARCH + query)
        movie = json.loads(urllib.request.urlopen(URL_SEARCH + query).readline().decode())
        if "Response" in movie and movie["Response"] == "False" :
            print("        Impossible to retrieve : '%s'" % (moviename))
            print("        Reason         : '%s'" % (movie["Error"]))
            return None
        print("Search results :")
        results = list()
        for res in movie["Search"] :
            results.append(res)
            # Example: 
            #{"Search":[{"Title":"Heaven & Earth","Year":"1993","imdbID":"tt0107096","Type":"movie"}]}
        return results

    def RequestMovieDetails(self, imdbId):
        movie = json.loads(urllib.request.urlopen(URL_GETIMDB + imdbId).readline().decode())
        if movie["Response"] == "False" :
            print("        Impossible to retrieve : '%s'" % (moviename))
            print("        Reason         : '%s'" % (movie["Error"]))
            return None
        
        """
        # Saving data to dir
        jsondatasavepath = os.path.join(MOVIESDATADIR, moviepath) + ".json"
        if not os.path.exists(jsondatasavepath) :
            open(jsondatasavepath, "w").write(json.dumps(movie, sort_keys = False, indent = 4))
            try :
                if movie["Poster"] != "N/A" :
                    self.DownloadPoster(movie["Poster"], os.path.join(MOVIESDATADIR, moviepath))
            except :
                print("Impossible to download poster '%s' in '%s'" % (movie["Poster"], moviepath))
        """
        return movie
    
    """
    def RecurseOverAllMovies(self, iDir, iFunction) :
        r = re.compile("[(-]+")
        l = os.listdir(iDir)
        for m in l :
            moviequery = m.split(" -")[0].replace("(", "")
            print(moviequery)
            if iFunction != None :
                iFunction(moviequery)
            #self.RequestMovie(moviequery)

    def DownloadPoster(self, iURL, iPath) :
        if iURL == "N/A" :
            return
        fileName, fileExtension = os.path.splitext(urllib.parse.urlparse(iURL).path)
        if os.path.exists(iPath + fileExtension) :
            print("%s already exists" % (iPath + fileExtension))
        else :
            urllib.request.urlretrieve(iURL, iPath + fileExtension)

    def RequestPoster(self, moviename, outputdir) :
        query = FormatInputToQuery(moviename)
        print(URL_TITLE + query)
        movie = json.loads(urllib.request.urlopen(URL_TITLE + query).readline().decode())
        if "Poster" in movie and movie["Poster"] != "N/A" :
            moviepath = self.NormalizeWindowsPath("%s (%s - %s) %s" % (movie["Title"], movie["Year"], movie["Director"], movie["Actors"]))
            jsondatasavepath = os.path.join(outputdir, moviepath) + ".json"
            print("Downloading '%s' in '%s'" % (movie["Poster"], moviepath))
            open(jsondatasavepath, "w").write(json.dumps(movie, sort_keys = False, indent = 4))
            self.DownloadPoster(movie["Poster"], os.path.join(outputdir, moviepath))
    """
