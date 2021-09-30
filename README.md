# Clustering-Story-Texts

## To Set Up To Run Code
```
pip install nltk
pip install tabulate
pip install sklearn
pip install matplotlib
pip install pandas
pip install scipy
```
Other libraries used are os, re, heapq, and math

# To Run Code
```
python main.py
```

# To Hand In
Preprocessed Files are found under /processed_docs folder
Resulting output matrix, dendogram, and clusters are under /results folder
Matrix is found as cosine_matrix.txt
Dendogram is found as dendogram.png (for a better view uncomment plt.show() main.py line 58)
List of files found in each cluster is found in clusters.txt

# Incomplete or Not Working Code
My matrix looks pretty different but I'm not sure if that's just different ordering or what? The numbers are a similar size

# Analysis of results
Like the solution desirbed in the assignment description, in one of my clusters I had only k2.txt while in the other I ever other story.
The first pair is t12 and t6 which makes sense since they are both scary stories about babysitters.

There are 2 groups that form initally in the dendogram.
The first: t14, t7, t1, t8, t12, t6, t5, t2, t13, t10, t3
The second: k11, k5, k4, k1, k9, k14, k6, k10, k13, k7, k8, and t14
The last group has one pair (k3 and k12), and beside them each story gets added to the main cluster individually
The last group: t11, k3, k12, t9, t4

The first group is all teen stories: they all have classic horror feels to them, and most take place on Halloween.
The second group is mainly kids stories and like in the solution desirbed in the assignment description we also have t14. t14 does not contain any classic horror language found in the other stories while it does describe severed heads it never refers to them as such just as heads. The other stories are classic fair tails contianing fantasy elements such as magic, and fairies. One of the first pairs is k10 and k13 which are thumbalina and the ugly duckling, both stories focus on beauty and uglyness giving them similar language.
The remaining kids fabels are k3 (little red ridding hood), and k12 (the 3 little pigs) as well as k6 (Jack and the Beanstalk). All of which are the more violant childrens fables. All of which have characters almost dying and being eaten.
Of the last of the teen horror stories t11 is the most similar to the classic horror and is merged in first to the main cluster, then the childrens stories. Followed by t9 then t4 which are both scary but don't feature as much "on screen" violance or gore.

Finally we have k2 on its own. As seen in the assignment description, k2 is Jack and the Beanstalk. This story has a few more scary elements to it then the other kids story while still using the same language as a typical kids story.

I think due to the short nature of some of these stories they were not grouped together the way one might expect. Also the last of the merges are very close. Perhaps if redune with longer stories (such as if we replace the teen horror stories novel length stories such as RL Stiens Goose Bumps and the Kids Fables with the Equivalent novel length version of the story) then the clusters would form more similarily to what was expected.