import os
import sys
file_path = os.path.join(os.path.dirname(__file__), '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, os.path.abspath(file_path))

encuesta = os.path.join(file_dir, 'encuesta.csv')
notfollowers = os.path.join(file_dir, 'notfollowers.csv')
vaicommunityfollowers = os.path.join(file_dir, 'vai.community-followers.csv')
followers = os.path.join(file_dir, 'followers.csv')

