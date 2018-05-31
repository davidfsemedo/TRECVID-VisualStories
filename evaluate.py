import numpy
import pandas
import json
import sys

n_args = len(sys.argv)
if n_args != 3 and n_args != 5:
    print("usage:")
    print("python evaluate.py stories_json evaluation_file [relevance_groundtruth] [transitions_groundtruth]")
    exit()

story_path = sys.argv[1]
stories = json.load(open(story_path))["stories"]
to_evaluate_path = sys.argv[2]
to_evaluate = pandas.read_csv(to_evaluate_path, delim_whitespace=True, dtype={"run_id": numpy.str, "query_id": numpy.str, "dummy": numpy.str, "doc_id": numpy.str})
if n_args == 5:
    relevance_gt_path = sys.argv[3]
    transitions_gt_path = sys.argv[4]
    relevance_gt = pandas.read_csv(relevance_gt_path, dtype={"query_id": numpy.str, "doc_id": numpy.str, "rel": numpy.int32})
    transitions_gt = pandas.read_csv(transitions_gt_path, dtype={"query_id": numpy.str, "doc_id1": numpy.str, "doc_id2": numpy.str, "trans": numpy.int32})


def main():
    if n_args == 3:
        test_format()
    else:
        evaluate()


def test_format():
    for story in stories:
        story_id = story["story_id"]
        segments = story["segments"]
        print("Story ", story_id)
        story_ok = True
        for segment in segments:
            segment_id = segment["segment_id"]
            query_id = "{}.{}".format(story_id, segment["segment_id"])
            n_tries = numpy.count_nonzero(to_evaluate["query_id"] == query_id)
            if n_tries == 0:
                print("Missing segment {}".format(segment_id))
            elif n_tries > 1:
                print("More then one attempt for segment {}".format(segment_id))
            if story_ok:
                story_ok = n_tries == 1
        if story_ok:
            print("Ok")

        print()


def evaluate():
    stories = json.load(open(story_path))["stories"]

    scores = []
    relevances = []
    transitions = []
    for story in stories:
        story_id = story["story_id"]
        segment_attempts = []
        segments = story["segments"]
        for segment in segments:
            segment_id = segment["segment_id"]
            query_id = "{}.{}".format(story_id, segment["segment_id"])
            is_attempt = to_evaluate["query_id"] == query_id
            n_tries = numpy.count_nonzero(is_attempt)
            if n_tries == 0:
                segment_attempts = []
                print("Missing segments for story {}, skipping story.".format(story_id))
                print()
                break
            elif n_tries > 1:
                segment_attempts = []
                print("More then one attempt for segment {} of story {}, skipping story.".format(segment_id, story_id))
                print()
                break
            segment_attempts.append((segment_id, to_evaluate[is_attempt].iloc[0]))

        segment_attempts = sorted(segment_attempts, key=lambda x: x[0])
        if len(segment_attempts) > 0:
            relevant_list, transition_list, score = calc_story(story_id, segment_attempts)
            print("story: ", story_id)
            print("relevance:", " ".join(map(str, relevant_list)))
            print("transitions:", " ".join(map(str, transition_list)))
            print("score:", round(score, 3))
            print()
        else:
            score = 0
            relevant_list = list(numpy.zeros(len(segments)))
            transition_list = list(numpy.zeros(len(segments) - 1))

        scores.append(score)
        relevances += relevant_list
        transitions += transition_list

    avg_scores = numpy.array(scores).mean()
    avg_relevances = numpy.array(relevances).mean()
    avg_transitions = numpy.array(transitions).mean()
    print("Average score: ", round(avg_scores, 3))
    print("Relevance precision: ", round(avg_relevances, 3))
    print("Transitions precision: ", round(avg_transitions, 3))


def calc_story(story_id, segment_attempts):
    docs_list = []
    relevant_list = []
    for segment_id, attempt in segment_attempts:
        relevance_query = relevance_gt[
            (relevance_gt["query_id"] == attempt["query_id"]) &
            (relevance_gt["doc_id"] == attempt["doc_id"]) &
            (relevance_gt["rel"] == 1)
            ]
        relevant = int(numpy.count_nonzero(relevance_query) > 0)
        relevant_list.append(relevant)

        docs_list.append(attempt["doc_id"])

    transition_list = []
    doc_pairs = [(docs_list[i - 1], docs_list[i]) for i in range(1, len(docs_list))]
    for pair, segment_id in zip(doc_pairs, range(1, len(doc_pairs) + 1)):
        query_id = "{}.{}".format(story_id, segment_id)
        transition_query = transitions_gt[
            (transitions_gt["query_id"] == query_id) &
            (transitions_gt["doc_id1"] == pair[0]) &
            (transitions_gt["doc_id2"] == pair[1])
            ]
        good_transition = int(numpy.count_nonzero(transition_query) > 0)
        transition_list.append(good_transition)
    score = quality(relevant_list, transition_list)

    return relevant_list, transition_list, score


def quality(relevance, transitions, a=0.1, b=0.6):
    pairwise_quality = 0
    for i in range(1, len(relevance)):
        pairwise_quality += b * (relevance[i] + relevance[i - 1]) + (1 - b) * (relevance[i] * relevance[i - 1] + transitions[i - 1])

    return a * relevance[0] + (1 - a) / (2 * (len(relevance) - 1)) * pairwise_quality


if __name__ == '__main__':
    main()
