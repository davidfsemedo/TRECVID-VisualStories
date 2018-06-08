
# TRECVID-Social-media Video Storytelling Linking
TRECVID 2018 - Social-media Video Storytelling Linking Development Kit

# Evaluation Script
We provide a command line tool to evaluate runs. The evaluation computes a score that corresponds to the **Quality metric** described in the Guidelines document. Concretely it assesses two criteria: 
* **Relevance** of each assigned image/video to a segment;
* **Quality of transitions** between an assigned image/video of consecutive segments.

For a detailed explanation of the metric, please refer to the Social-media Video Storytelling Linking Task Guidelines (`guidelines.pdf`) document available [here](http://datasets.novasearch.org/trecvid-visualstories/).

To run the script you will need both the Stories/segments queries and both relevance and transitions groundtruth files. These are all available in the [dataset directory](http://datasets.novasearch.org/trecvid-visualstories/).

## Dependencies
The script is implemented in Python. All dependencies are Python libraries that can be installed through `Anaconda` or `pip`. List of dependencies:
* numpy
* pandas
* termcolor
## Usage
```console
foo@bar:~$ python evaluate.py <event_stories.json> <result.run> <event_relevance_groundtruth.csv>  <event_transitions_groundtruth.csv>                                                                                          
```

### Checking submission
You can check your run submission file for issues. Namely, the tool checks for segments without assigned image/videos, multiple images/videos assigned to a single segment. To check your submission run the script as follows: 
```console
foo@bar:~$ python evaluate.py <event_stories.json> <result.run>                                                                                        
```
Note: We provide a set of valid and non-valid sample submission files in the folder `runs`. We advise you to go through all the runs to understand the submission format. Example:
```console
foo@bar:~$ python evaluate.py edfest_2016_stories.json runs/example_incomplete_submission.run                                        
```
### Evaluating submission
Example of submission evaluation:
```console
foo@bar:~$ python evaluate.py edfest_2016_stories.json runs/example_incomplete_submission.run edfest_2016_relevance_groundtruth.csv edfest_2016_transitions_groundtruth.csv                                        
```
Each story will be evaluated individually. At the end, the average score is shown, over all stories.



---
##### Contact:

If you have any question or if you find any issue, please contact:
David Semedo - Email: df.semedo@campus.fct.unl.pt

The NOVASEARCH Team.
