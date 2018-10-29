import shutil

filenames = ['negex_combined.txt','ts_negex_357072.txt']
with open('out/negex_all.txt','wb') as wfd:
    for f in filenames:
        with open('output/{0}'.format(f),'rb') as fd:
            shutil.copyfileobj(fd, wfd)
