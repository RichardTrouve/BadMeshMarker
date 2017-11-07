# BadMeshMarker
Simple tool for maya to mark Meshes containing the requested type of geometry by coloring them in Red in the outliner.

highly inspired by the work of 
Erik Lehmann : https://gumroad.com/d/a0af2f394f208c5a9dc44b54fe6ad85f

After using sanity checks (for modeling cleanup) on large/complex files, I find it quite redundant to have to check the whole scene again and again just to jump on the next item for cleanup, 

i wrote this tool so i could scan the scene just ones and have a quick overview and quickly select the bad meshes in the outliner. 
For now it's very basic, if i find it usefull i will definetly add other features

**INSTRUCTIONS**
You can just copy/paste the code and run it in the script editor.

1 button to mark the  meshes with ngons in the outliner

1 button to reset the outliner color settings back to default

**NOT WORKING ON VERSIONS PREVIOUS TO MAYA 2016**
**THIS IS UNFINISHED CODE, MIGHT BE BUGGY or INNACCURATE, USE IT AT YOUR OWN RISK**

TO-DO : -Isolate marked meshes on the viewport
        -Display Marked meshes Count (not sure if it's really useful
