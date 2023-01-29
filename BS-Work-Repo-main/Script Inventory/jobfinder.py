# Todo?: Combine linear and thorough search because cannot find "Parking Permit"
# todo: Add delete old databases option (or auto delete)
# todo: Add safety check if person accidentally inputs a single letter character? (they can just restart the script)
#  - Probably not needed since we have C + ENTER already.

import os, re, sqlite3, sys, datetime, time
from pprint import pprint

# The following directories lists use different searching algorithms.

WIP_DIR = r'M:\Printlink Digital'
WIP_DIRS = [
    WIP_DIR,
]

DATA_DIR = r'Y:'
DATA_DIRS = [
    DATA_DIR,
    r"\\jwilliams2021\backups\data",
]

PRODUCTION_DIR = r'Y:\Production'
PRODUCTION_DIRS = [
    PRODUCTION_DIR,
    r'Y:\Development', # has similar structure to Y:\Production
]

RESULTS_PER_PAGE = 10
# For displayXElementsAtATime e.g. How many lines of text/search results to display at a time.

THOROUGH_SEARCH_DEPTH = 5
# Maximum number of directories to go down when running a thorough job search in Production
# Update this to something higher than 5, i.e. 10, to get all of them.


YEAR_REGEX = r'20\d{2}'
JOBID_REGEX = r'(\w)\1{6,7}|\d{6,7}' # Matches XXXXXXX, 0000000 too.
# JOBID_REGEX = r'\d{6,7}'
# the \1 is called a back reference (previous char)
# the | means logical OR

# Reverse the lists so the search results are displayed in the order they are listed above.
# DATA_DIRS       =       DATA_DIRS[::-1]
PRODUCTION_DIRS = PRODUCTION_DIRS[::-1]
WIP_DIRS        =        WIP_DIRS[::-1]
# (Side effect of iterating through search results and using displayXElementsAtATime, reverse=True)


def getJobID(string):
    found = re.search(JOBID_REGEX, string)
    if found is None:
        return None
    else:
        return found.group(0)


def findYearDirectories(path):
    yearDirectories = []
    
    for dirEntry in directoriesInPath(path):
        if re.search(YEAR_REGEX, dirEntry.name, re.IGNORECASE):
            yearDirectories += [dirEntry.path]
    
    yearDirectories.sort()
    
    return yearDirectories


# Unused
def scanDataDirForJob(keyword, dataDir=DATA_DIR, interactive=False):
    '''
    interactive is no longer used.
    '''
    
    if ':' in dataDir and not dataDir.endswith(os.sep):
        dataDir = os.path.join(dataDir, os.sep)
        # os.sep so we have Y:\2021\... instead of Y:2021\... (which is only valid in Python)
    
    yearDirs = findYearDirectories(dataDir)
    keyword = keyword.lower().strip()
    
    found = []
    
    for year in yearDirs:
        year = os.path.join(dataDir, year)
        monthDirs = []
        
        for dirsInYear in os.scandir(year):
            if os.path.isdir(dirsInYear.path):
                monthDirs += [dirsInYear.path]
        
        for monthDir in monthDirs:
            for jobDir in os.scandir(monthDir):
                if keyword not in jobDir.name.lower():
                    continue
                found += [jobDir.path]
                
    return found


def scanDataDirsForJob(keyword, dataDirs=DATA_DIRS, interactive=False):
    '''
    Generator version of scanDataDirForJob function, but takes a list of
    directories (strings) instead. This was implemented because it's much faster
    to display a few addresses at a time instead of scanning the whole list of
    data directories (e.g. backups) before returning the results.
    '''
    
    keyword = keyword.strip().lower()
    
    for dataDir in dataDirs:
        # os.sep so we have Y:\2021\... instead of Y:2021\... (which is only valid in Python)
        if ':' in dataDir and not dataDir.endswith(os.sep):
            dataDir = os.path.join(dataDir, os.sep)
        
        yearDirs = findYearDirectories(dataDir)[::-1] # Most recent first. List of strings
        
        for year in yearDirs:
            monthDirs = getDirectories(year)
            
            # todo: Sort by month?? Then I'll have to sort the other functions too.
            
            for monthDir in monthDirs:
                for sJobDir in os.listdir(monthDir):
                    if keyword not in sJobDir.lower():
                        continue
                    
                    joined = os.path.join(monthDir.path, sJobDir)
                    yield joined



MONTHS_ORDER = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
def sortMonths(sList):
    sList_sorted = []
    for month in MONTHS_ORDER:
        for j, s in enumerate(sList):
            if s.lower().startswith(month):
                sList_sorted.append(sList.pop(j))
                break
    
    return sList_sorted


class WIP:
    
    # Unused
    @staticmethod
    def findJobs(wipDir=WIP_DIR):
        '''
        Scans wipDirs for jobs.
        
        This function is a generator.
        Just like Product.findProjects, this yields DirEntry objects
        '''
        
        # Walk through year
        for yearDir in findYearDirectories(wipDir):
            # findYearDirectories returns a list of strings, while directoriesInPath
            # returns a generator object.
        
            # Walk through each month; exclude Dailys, misc
            for month in directoriesInPath(yearDir):
                for dirInMonth in directoriesInPath(month.path):
                    if re.match(JOBID_REGEX, dirInMonth.name):
                        yield dirInMonth
                    
                    # Scan contents of each dir in month
                    for directory in directoriesInPath(dirInMonth.path):
                        if re.match(JOBID_REGEX, directory.name):
                            yield directory
    
    
    @staticmethod
    def findDirectoriesContainingJobs(wipDir=WIP_DIR):
        '''
        Scans wipDirs for directories containing jobs.
        e.g.
        M:\Printlink Digital\2021\April 2021\Jobs - Apr 2021\
        M:\Printlink Digital\2021\April 2021\
        
        This function is a generator.
        Just like Product.findProjects, this yields DirEntry objects
        '''
        
        # Walk through year
        for yearDir in findYearDirectories(wipDir):
            # findYearDirectories returns a list of strings, while directoriesInPath
            # returns a generator object.
        
            # Walk through each month; exclude Dailys, misc
            for month in getDirectories(yearDir):
                monthAlreadyYielded = False
                for dirInMonth in getDirectories(month.path):
                    # Scan contents of each dir in month
                    for directory in getDirectories(dirInMonth.path):
                        if re.match(JOBID_REGEX, directory.name):
                            yield dirInMonth
                            break
                    
                    if monthAlreadyYielded:
                        continue
                    
                    if re.match(JOBID_REGEX, dirInMonth.name):
                        monthAlreadyYielded = True
                        yield month

        #   For each month folder, check for jobs that don't include 'jobs'


class Production:
    
    @staticmethod
    def findProjects(productionDir=PRODUCTION_DIR, batches=True):
        '''
        Scans production (or otherwise) for directories containing a workflow and batches folder.
        - If batches param is False, then only workflow.
        
        
        **Currently doens't scan nested projects under a project folder. e.g. TR Annotations
        in "Thomson Reuters".
        
        Returns: List of DirEntry objects
        '''
        
        def isProjectDir(directory):
            dirContents = os.listdir(directory)
            
            if not keywordInList('workflow', dirContents):
                return False
            if not keywordInList('batches', dirContents) and batches == True:
                return False
            
            return True
        
        # Get all clientdirectories under productionDir
        clientDirs = getDirectories(productionDir)
        
        # Browse all project directories under client dirs for 'Batches' folder.
        projectDirs = []
        for clientDir in clientDirs:
            dirsInClientDir = getDirectories(clientDir)
            
            # Check each directory found for workflow & batches directory
            for directory in dirsInClientDir:
                if isProjectDir(directory):
                    projectDirs += [directory]          
        
        return projectDirs
    
    
    @staticmethod
    def findJobsThoroughly(productionDir=PRODUCTION_DIR, maxdepth=THOROUGH_SEARCH_DEPTH):
        '''
        Returns a dictionary:
        KEY (string) = location/path/directory
        VALUE (list) = list of jobs
        '''
        jobsDict = {}
        
        for dirEntry in rscandir_dirsonly_generator(productionDir, maxdepth):
            for subDirEntry in getDirectories(dirEntry.path):
                if getJobID(subDirEntry.name) is not None:
                    jobsDict.setdefault(dirEntry.path, [])
                    jobsDict[dirEntry.path] += [subDirEntry]
                
        return jobsDict


class JobLocationsDB:
    
    def __init__(self, dbPath, overwrite=False):
        self.dbPath = dbPath
        self.dbConn = None
        self.dbCursor = None
        
        # For new data insert
        self._currentLocationID = 0
        self._currentFolderID   = 0
    
    @property
    def currentLocationID(self):
        return self._currentLocationID
    
    @property
    def currentFolderID(self):
        return self._currentFolderID
    
    def create(self, overwrite=False):
        if os.path.exists(self.dbPath):
            if overwrite == False:
                raise FileExistsError(f'{self.dbPath} already exists. Will not overwrite as overwrite flag is set to False.')
            os.remove(self.dbPath)
        
        con = sqlite3.connect(self.dbPath)
        
        cur = con.cursor()
        
        cur.execute('''CREATE TABLE locations (
            location_id INTEGER PRIMARY KEY,
            path VARCHAR(480) UNIQUE);''')
        
        cur.execute('''CREATE TABLE job_locations
            (job_location_id INTEGER PRIMARY KEY AUTOINCREMENT,
            folder VARCHAR(240),
            location_id INTEGER,
            FOREIGN KEY(location_id) REFERENCES locations(location_id));''')
        
        cur.execute('''CREATE VIEW jobs AS
            SELECT folder, path
            FROM job_locations NATURAL
            JOIN locations;''')
        
        con.commit()
        
        self.dbConn = con
        self.dbCursor = cur
    
    def getNextLocationID(self):
        self._currentLocationID += 1
        return self._currentLocationID
    
    def getNextFolderID(self):
        self._currentFolderID += 1
        return self._currentFolderID
    
    def insertLocation(self, path):
        '''
        This does not verify whether locations inserted exist or not.
        '''
        
        self.dbCursor.execute('INSERT INTO locations(location_ID, path) VALUES (?, ?)',
                              (self.getNextLocationID(), path))
        
        return self.currentLocationID
    
    
    def insertJobsByLocationID(self, jobDirEntries, locationID):
        entriesToAdd = ((self.getNextFolderID(), jobDirEntry.name, locationID) for jobDirEntry in jobDirEntries)        
        self.dbCursor.executemany('INSERT INTO job_locations(job_location_id, folder, location_id) VALUES (?, ?, ?)',
                        entriesToAdd)
        return self.currentFolderID
    
    
    def fetchAll(self):
        self.dbCursor.execute('SELECT * FROM jobs;')
        return self.dbCursor.fetchall()
    
    
    def searchJob(self, searchKeyword):
        #self.dbCursor.execute("SELECT * FROM jobs WHERE folder LIKE (?);", [f'%{searchKeyword}%',])
        self.dbCursor.execute("SELECT * FROM jobs WHERE folder LIKE :pattern;",
                              {'pattern': f'%{searchKeyword}%'})
        '''
        sqlite pattern can consite of wildwards. e.g.
        % - Matches any sequence of zero or more characters
        _ - Matches any single character
        
        Source: https://www.sqlitetutorial.net/sqlite-like/
        '''
        return self.dbCursor.fetchall()
    
    
    def searchForLocation(self, searchKeyword):
        self.dbCursor.execute("SELECT path FROM locations WHERE path LIKE :pattern;",
                              {'pattern': f'%{searchKeyword}%'})
        return self.dbCursor.fetchall()
    
    
    def generateIndexes(self):
        '''
        Indexes make DB access/search faster after you've inserted all locations
        and made commits.
        '''
        
        # 'folder' column index
#         self.dbCursor.commit()
        self.dbCursor.execute('CREATE INDEX job_locations_folder_idx ON job_locations(folder);')
        self.dbCursor.execute('CREATE INDEX locations_path_idx ON locations(path);')
        self.dbConn.commit() # save index
    
    def openDB(self):
        self.dbConn = sqlite3.connect(self.dbPath)
        self.dbCursor = self.dbConn.cursor()
    
    def retrieveLocation(self, sLocation):
        """
        Returns a location tuple: (location_id, path)
        Useful for retrieving ID of a location string.
        """
        
        results = self.dbCursor.execute(r'SELECT location_id, path FROM locations WHERE path=:path LIMIT 1;', {
            'path': sLocation,
        })
        
        return results.fetchone()
        

def keywordInList(keyword, sList, matchCase=False):
    '''
    Returns True if the keyword is found inside the contents of the list.
    
    Should return list of indexes instead?
    '''
    
    def stringList(sList):
        for string in sList:
            if matchCase:
                yield string
            else:
                yield string.lower()
    
    keyword = keyword.lower() if not matchCase else keyword
    
    for string in stringList(sList):
        if keyword in string:
            return True
    
    return False


def searchKeywordInList(keyword, sList, matchCase=False):
    '''
    Returns a list of matching elements in sList.
    '''
    
    matches = []
    
    keyword = keyword.lower() if not matchCase else keyword
    
    for i, string in enumerate(sList):
        string = string.lower() if not matchCase else string
        
        if keyword in string:
            matches += [sList[i]]
    
    return matches


def rscandir_dirsonly(path='.', maxdepth=-1):
    currentDirs = [] # Current directories in this path
    
    for dirEntry in os.scandir(path):
        
        if dirEntry.is_dir():
            currentDirs.append(dirEntry)
            
            if maxdepth != 0:
                currentDirs.extend(rscandir_dirsonly(dirEntry.path, maxdepth=maxdepth - 1))

    return currentDirs


def rscandir_dirsonly_generator(path='.', maxdepth=-1):
    # Memory efficient, but expense of CPU processing and disk time
    
    for dirEntry in os.scandir(path):
        
        if dirEntry.is_dir():
            yield dirEntry
            
            if maxdepth != 0:
                for dirEntry in rscandir_dirsonly_generator(dirEntry.path, maxdepth=maxdepth - 1):
                    yield dirEntry


def getDirectories(dirPath):
    '''
    Returns directories as DirEntry objects:
    https://docs.python.org/3.6/library/os.html#os.DirEntry
    '''
    
    directories = []
    
    for entry in os.scandir(dirPath):
        if entry.is_dir():
#             yield entry
            directories += [entry]
    
    return directories
    
    
def directoriesInPath(dirPath):
    '''
    Slightly more memory efficient version of getDirectories.
    
    Downsides:
    * You cannot re-iterated over the returned variable/generator unless
    you copy it to another array i.e. wrap it in list(...) and store in another variable
    before the initial iteration.
    * Freeing scandir's resources can be tricky (I don't know enough about yield/generators).
    
    e.g.    
    myVar = list(directoriesInPath(path))
    '''
#     return (dirEntry for dirEntry in os.scandir(dirPath) if os.path.isdir(dirEntry.path))
    for dirEntry in os.scandir(dirPath):
        if os.path.isdir(dirEntry.path):
            yield dirEntry


def generateProductionJobLocationsDB(jldb, productionPaths=PRODUCTION_DIRS, thorough=False):
    if not thorough:
        for productionPath in productionPaths:
            for projDirEntry in Production.findProjects(productionPath):
                # make the file/dir contents of the DirEntry into a list:
                sProjDirDirs = [de.path for de in getDirectories(projDirEntry.path)]
                batchesDirs = searchKeywordInList('batches', sProjDirDirs) # strings
                
                for batchesDir in batchesDirs:            
                    locID = jldb.insertLocation(batchesDir)
                    jobDirEntries = (d for d in os.scandir(batchesDir) if os.path.isdir(d))
                    jldb.insertJobsByLocationID(jobDirEntries, locID)

    else:
        for productionPath in productionPaths:
            for path, jobDirEntries in Production.findJobsThoroughly(productionPath).items():
                locID = jldb.insertLocation(path)
                jldb.insertJobsByLocationID(jobDirEntries, locID)

#     productionProjects = Production.findProjects(PRODUCTION_DIR)
#     for projDirEntry in productionProjects:
#         batchesDir = os.path.join(projDirEntry, 'Batches')
#         jobDirs = (entry for entry in os.scandir(batchesDir) if entry.is_dir()) # Generator = Less memory
#         for jobDir in jobDirs:
#             if searchKeyword in jobDir.name:
#                 print(jobDir.path)

    return jldb


def generateWIPJobLocationsDB(jldb, wipPaths=WIP_DIRS):
    
    for wipPath in wipPaths:
        for jobDirEntry in WIP.findDirectoriesContainingJobs(wipPath):
            locID = jldb.insertLocation(jobDirEntry.path)
            jobDirEntries = (d for d in os.scandir(jobDirEntry.path) if os.path.isdir(d))
            jldb.insertJobsByLocationID(jobDirEntries, locID)
    
    return jldb


def generateDBFilename():
    now = datetime.datetime.now()
    sDate = f'{now.year:04d}{now.month:02d}{now.day:02d}-{now.hour:02d}{now.minute:02d}'
    filename = f'jobs_{sDate}.sqlite3'
    return filename


def processCommandLineArguments(argv):
    print(sys.argv)
    
    if 'regendb' == sys.argv[1]:
        generateJobsDB()
        sys.exit(0)
    elif 'regendbx' == sys.argv[1]:
        generateJobsDB(deepscan=True)
        sys.exit(0)


def getLatestDatabaseFile(path):
    dbFiles = []
    
    for dirEntry in os.scandir(path):
        if not os.path.isfile(dirEntry):
            continue
        if not dirEntry.name.startswith('jobs_'):
            continue
        if not dirEntry.name.endswith('sqlite3'):
            continue
        dbFiles += [dirEntry.path]
    
    if len(dbFiles) == 0:
        return None
    
    dbFiles.sort(reverse=True)
    return dbFiles[0]


CHOICE_SEARCH_IN_DATA = 0
CHOICE_SEARCH_IN_DATA_INTERACTIVE = 1
CHOICE_SEARCH_IN_DB = 10
CHOICE_UPDATE_DB = 20
CHOICE_UPDATE_DB_THOROUGH = 21
CHOICE_SEARCH_IN_LOCATIONS = 30
CHOICE_HELP = 40
CHOICE_QUIT = 1000

def mainLoopPrompt():
    sPrompt = \
'''
What do you want to do?
 (a) Search for jobs in the data directories
 (b) Search for jobs in the production/WIP directories
     (uses generated database)
 (l) Search for locations in the database e.g. "Thomson Reuters"
 (u) Regenerate jobs database (linear search, takes ~5 minutes)
 (g) Regenerate jobs database (thorough search, ~30 minutes) 
 (h) Help
 (q) Quit
'''
    print(sPrompt)
    choice = input('Enter choice (a/b/u/q/etc.): ')

    while (choice not in 'abhuglq') or len(choice.strip()) == 0:
        print("Invalid option. Please try again.")
        choice = input('Enter choice (a/b/c/q/etc.):')
    
    # Map the choice
    if choice == 'a':
        return CHOICE_SEARCH_IN_DATA
    elif choice == 'b':
        return CHOICE_SEARCH_IN_DB
    elif choice == 'u':
        return CHOICE_UPDATE_DB
    elif choice == 'g':
        return CHOICE_UPDATE_DB_THOROUGH
    elif choice == 'l':
        return CHOICE_SEARCH_IN_LOCATIONS
    elif choice == 'h':
        return CHOICE_HELP
    elif choice == 'q':
        return CHOICE_QUIT
    
    print('Something went wrong with mainLoopPrompt')
    return CHOICE_QUIT


def promptReturnToMainMenu():
    input('\nPress ENTER to go back to the main menu.')


def ProcessChoice_searchInData(interactive=False):
    promptMsg = 'Enter a search keyword, or leave blank then press ENTER to return to main menu:\n>'
    searchKeyword = input(promptMsg).strip()
    
    while len(searchKeyword) != 0:
        try:
            found = scanDataDirsForJob(searchKeyword, DATA_DIRS)

            displayXElementsAtATime_generator(RESULTS_PER_PAGE, found)
            
        except FileNotFoundError as ex:
            print("Unable to access some drives (backups?). Maybe Jordan's computer is off? Turn it on if that's the case; IT might have turned it off for updates.")
            input("Press ENTER to continue.")
        else:
            print('\nSearch finished.', end=' ')
                
        searchKeyword = input(promptMsg).strip()
        

def ProcessChoice_searchInData_old(interactive=False):
    '''
    ProcessChoice_searchInData, but retrieves all results before displaying (slower).
    '''
    
    promptMsg = 'Enter a search keyword, or leave blank then press ENTER to return to main menu:\n>'
    searchKeyword = input(promptMsg).strip()
    
    while len(searchKeyword) != 0:
        found = []
        for dataDir in DATA_DIRS:
            searchResults = scanDataDirForJob(searchKeyword, dataDir, interactive)       
            found.extend(searchResults)
        
        displayXElementsAtATime(RESULTS_PER_PAGE, found, reversed=True)
        
        print('\nSearch finished.', end=' ')
        
        if len(found) == 0:
            print(f'No job name containing "{searchKeyword}" found.')
        
        searchKeyword = input(promptMsg).strip()


def ProcessChoice_searchInDB():
    latestDB_filename = getLatestDatabaseFile('.')
    if latestDB_filename is None:
        print('No job databases found e.g. jobs_#####.splite3')
        promptReturnToMainMenu()
        return
    
    print(f'Opening \"{latestDB_filename}\" database.')
    jldb = JobLocationsDB(latestDB_filename)
    jldb.openDB()

    promptMsg = 'Please enter a search keyword (or press ENTER to return to main menu):\n>'
    searchKeyword = input(promptMsg).strip()

    while len(searchKeyword) != 0:
        searchResults = jldb.searchJob(searchKeyword)
        resultsList = [os.path.join(found[1], found[0]) for found in searchResults]
        displayXElementsAtATime(RESULTS_PER_PAGE, resultsList, reversed=True)
        
        print('Search finished.', end=' ')
        
        if len(searchResults) == 0:
            print(f'No job name containing "{searchKeyword}" found.')
        
        searchKeyword = input(promptMsg).strip()
    
#     promptReturnToMainMenu()


def ProcessChoice_generateDB():
    print('This will regenerate the job database for production and WIP, which could take ~5 minutes to complete. Do you want to continue?')
    choice = input('y/n: ').lower()

    if choice != 'y':
        return False
    
    generateJobsDB()
    promptReturnToMainMenu()
    
    return True


def ProcessChoice_generateDB_thorough():
    print('''
You are about to perform a thorough job search in the Production directorie(s) and a normal scan of the WIP directories to rebuild the jobs database.
This could take ~30 minutes to complete.
Do you want to continue?
''')
    choice = input('y/n: ').lower()

    if choice != 'y':
        return False
    
    generateJobsDB(deepscan=True)
    promptReturnToMainMenu()
    
    return True

    
def generateJobsDB(deepscan=False):
    est = 5 if deepscan == False else 30
    print(f'<< This might take ~{est} minutes to complete >>')
    
    dbFilename = generateDBFilename()
    jldb = JobLocationsDB(dbFilename)
    jldb.create()

    startTime = time.time()
    
    print('Inserting production jobs to the DB...', end=' ')
    generateProductionJobLocationsDB(jldb, thorough=deepscan)
    print('Done.')
    
    print('Inserting WIP jobs to the DB...', end=' ')
    generateWIPJobLocationsDB(jldb)
    print('Done.')
    
    jldb.generateIndexes() # Commits changes to db.

    endTime = time.time()
    elapsedTime = endTime - startTime
    
    print('Done. Time elapsed: {}m {}s'.format(int(elapsedTime / 60), int(elapsedTime % 60)))
    print(f'DB generated: {dbFilename}')


def ProcessChoice_searchInLocations():
    latestDB_filename = getLatestDatabaseFile('.')
    if latestDB_filename is None:
        print('No job databases found e.g. jobs_#####.splite3')
        promptReturnToMainMenu()
        return
    
    print(f'Opening \"{latestDB_filename}\" database.')
    jldb = JobLocationsDB(latestDB_filename)
    jldb.openDB()

    promptMsg = 'Please enter a search keyword (or press ENTER to return to main menu):\n>'
    searchKeyword = input(promptMsg).strip()

    while len(searchKeyword) != 0:
        searchResults = jldb.searchForLocation(searchKeyword) # list of tuples: (id, path)
        resultsList = [found[0] for found in searchResults]
        displayXElementsAtATime(RESULTS_PER_PAGE, resultsList, reversed=True)
        
        print('Search finished.', end=' ')
        
        if len(searchResults) == 0:
            print(f'No job name containing "{searchKeyword}" found.')
        
        searchKeyword = input(promptMsg).strip()
    
#     promptReturnToMainMenu()


def ProcessChoice_help():
    displayXElementsAtATime(RESULTS_PER_PAGE, '''
Regenerating jobs database/cache
--------------------------------
Only Production and WIP directories are stored. The data directories aren't cached as they're reasonably quick to access (linear directory structure).


[Searching for jobs in the database]
------------------------------------
If you used the first "update database" option, you may notice that some production folders aren't cached. This is because they don't contain a 'Batches' and 'Workflow' directory using the following directory structure:
<Production dir>\<Client dir>\<Project dir>\<'Batches' and 'Workflow' dirs>

e.g. "TR Annotations" isn't cached because it doesn't have an immediate 'Batches' and 'Workflow' directory despite having two subfolders (Galleys and Booklets) each containing these directories.

This rule-based approach is done to speed up the database creation signficantly (linear vs. exponential # of directories to search as you go down a level). If you want to get almost all (or all of them), you can use the second database update option - to get all of them, just update the THOROUGH_SEARCH_DEPTH variable whithin this file then restart this script before selecting the command.


[ Building database via commandline ]
-------------------------------------
py jobfinder.py regendb
(Fast)

py jobfinder.py regendbx
(Slow, but thorough)

Both options automatically quit the program when done.

Don't forget the "py" part to run the program. If you do, it will run the script with no arguments even if there are some passed.


[Searching for locations in the database]
-----------------------------------------
A search function that searches for locations/directory paths stored in the database. This may be useful if the job folder names mostly contain numbers. e.g. "2020884  - Run 72" from "ANZ Home_Buyers_Welcome_Packs".
'''.split('\n'))
    promptReturnToMainMenu()


def displayXElementsAtATime(numToDisplay, elements, reversed=False):
    numElements = len(elements)
    i = 1
    while i <= numElements:
        element = elements[i - 1] if not reversed else elements[numElements - i]
        print(element)
        
        if i % numToDisplay == 0:
            numRemaining = numElements - i
            x = min(numRemaining, numToDisplay)
            
            key = ""
            if numRemaining > numToDisplay:
                key = input(f'-- Press ENTER to display {x} more ({numRemaining} remaining). C + ENTER to cancel.')
            elif numRemaining > 0:
                key = input(f'-- Press ENTER to display the last {numRemaining}. C + ENTER to cancel.')
            
            if key.lower().strip() == 'c':
                return
        
        i += 1


def displayXElementsAtATime_generator(numToDisplay, elements):
    # elements is a generator, in which case, reversed flag doesn't apply and numRemaining isn't displayed
    # Still works with normal iterables (i.e. lists/tuples)

    # This function was made for scanDataDirsForJob (With an 's' in Dirs) to emulate
    # the original job finder script. i.e. show X at a time realtime, without retrieving
    # all results before displaying.

    for i, element in enumerate(elements):
        j = i + 1
        print(element)
        
        if j % numToDisplay == 0:
            key = input(f'-- Press ENTER to display more. C + ENTER to cancel.')
            
            if key.lower().strip() == 'c':
                return


def main():
    jldb = None
    
    if len(sys.argv) > 1:
        processCommandLineArguments(sys.argv)
    
    # Open latest DB
    # --------------   
    latestDB_filename = getLatestDatabaseFile('.')
    if latestDB_filename is None:
        print('No jobs databases found.')
        ProcessChoice_generateDB()

    # Test - no need to enter input
#     print("""
# Use '%' or '_' wildcards. e.g. '2016142%' to find jobs containing this ID e.g.
# 2017142_TR_Financial Markets Law 21-07-21 + Tab
# """)
# #     searchKeyword = '2017142%'
#     searchKeyword = '%2016529%'
#     for found in jldb.searchJob(searchKeyword):
#         print(os.path.join(found[1], found[0]))
#     
#     print('\nDone.')
#     jldb = None # Free resources


    print('----------------')
    print('  JOBFINDER.PY  ')
    print('----------------')

    
    # Command loop
    # ------------
    choice = mainLoopPrompt()
    while choice != CHOICE_QUIT:
        
        if choice == CHOICE_SEARCH_IN_DATA or choice == CHOICE_SEARCH_IN_DATA_INTERACTIVE:
            interactive = (choice == CHOICE_SEARCH_IN_DATA_INTERACTIVE)
            ProcessChoice_searchInData(interactive)
        
        elif choice == CHOICE_SEARCH_IN_DB:
            ProcessChoice_searchInDB()
    
        elif choice == CHOICE_UPDATE_DB:
            ProcessChoice_generateDB()
        
        elif choice == CHOICE_UPDATE_DB_THOROUGH:
            ProcessChoice_generateDB_thorough()
    
        elif choice == CHOICE_SEARCH_IN_LOCATIONS:
            ProcessChoice_searchInLocations()
        
        elif choice == CHOICE_HELP:
            ProcessChoice_help()   
        
#         print('\nIs there anything else?\n')
        choice = mainLoopPrompt()
    
    print('Goodbye.')
    
    
if __name__ == '__main__':
    main()