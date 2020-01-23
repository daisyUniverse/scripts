import sys
movie = sys.argv[1]
movie = movie.split('CREATE',1)
sys.stdout.write("Now ripping: " + movie[1].replace('.m4v',''))