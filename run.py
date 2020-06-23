import getopt, sys
from attview import Visualizer

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'l:f:s:', ['modelpath=','figsize=','savepath='])
    except getopt.GetoptError as err:
        print(err) 
        sys.exit()

    loadpath, figsize, savepath = '', 0, ''
    
    for o, a in opts:
        if o in ('-l', '--modelpath') and type(a)==str:
            loadpath = a
        elif o in ('-f', '--figsize') and type(a)==int:
            figsize = a 
        elif o in ('-s', '--savepath') and type(a)==str:
            savepath = a
        else:
            assert False, 'unhandled option'    
    
    vis = Visualizer()
    vis.read(loadpath)
    vis.create_map(figsize, savepath)
    
if __name__ == "__main__":
    main()
