import getopt, sys
from attview import Visualizer
from seqnet import Seqnet

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:o:l:f:s:', ['text=','outpath=','modelpath=','figsize=','savepath='])
    except getopt.GetoptError as err:
        print(err) 
        sys.exit()

    tpath, opath, loadpath = '','',''
    
    for o, a in opts:
        if o in ('-t', '--text') and type(a)==str:
            tpath = a
        elif o in ('-o', '--outpath') and type(a)==str:
            opath = a 
        elif o in ('-l', '--modelpath') and type(a)==str:
            loadpath = a
        elif o in ('-f', '--figsize') and type(a)==int:
            figsize = a 
        elif o in ('-s', '--savepath') and type(a)==str:
            savepath = a
        else:
            assert False, 'unhandled option'    
    
    seq = Seqnet()
    vis = Visualizer()

    if loadpath != None:
        seq.load_model(loadpath)
        
    seq.test(tpath=tpath,opath=opath)
    vis.read(loadpath)
    vis.create_map(figsize, savepath)
    
if __name__ == "__main__":
    main()