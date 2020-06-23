[![CircleCI](https://circleci.com/gh/ssghost/My_Att_viewer.svg?style=svg)](https://circleci.com/gh/ssghost/My_Att_Viewer)
# My_Att_Viewer
A visualisation plug-in for illustrating attention in RNN models.
## Usage
First, run `$sh dlmodel.sh` to download RNN models from Github, then run `$python test.py` of downloaded snippets, then `$python run.py --loadpath=[path_for_test_model] --figsize=[output_figsize] --savepath=[output_savepath]` and you can get an attention map for the tested sentence.

All 3 parameters can't be empty.
