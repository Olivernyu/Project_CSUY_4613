# Project_-CSUY_4613

## Docker setup process
1. followed installation guide form: https://docs.docker.com/desktop/install/mac-install/
2. Learned how to set up basic docker file from these sources:
    -   https://docs.docker.com/language/python/build-images/
    -   https://circleci.com/blog/docker-and-cicd-tutorial-a-deep-dive-into-containers/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--uscan-en-dsa-tROAS-auth-brand&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY0tBlxlcgbYHULtVA6fqVRYjQrvBIs5ZrOI5hLQZv03D1rQPq4_qIAaAmoaEALw_wcB
    - https://www.youtube.com/watch?v=pTFZFxd4hOI
3. built dockerfile with `docker build -t basic-linux-image .`. Run docker with `docker run -it --rm -p 8080:80 basic-linux-image`
4. docker terminal screent shot in file `docker terminal.png`


## Huggingface sentiment analysis app
Link to hugging face page: https://huggingface.co/spaces/Olivernyu/sentiment_analysis_app


## Milestone 3: finetuning language model
1. I am finetuning the bert-base-uncased pre-trained model
2. The training process and code is in the FinetuneLM.ipynb notebook in this repo
3. I uploaded the finetuned model to hugging face at: https://huggingface.co/Olivernyu/finetuned_bert_base_uncased
4. The finetuned model is added to my sentiment analysis app, which can found here: https://huggingface.co/spaces/Olivernyu/sentiment_analysis_app.

I had and overcame an issue where the toxic category dominates the probability. It is usually the highest, with the second highest probablity category is usually consistent with the text. For example, if there is a text that contains a threat, the probability of the toxic category will be highest, followed by threat. The same goes for text that corresponds to any other category like obscene, insult, or identity hate. I looked into the dataset and found that nearly all positive occurences for categories that are not toxic also have positive for toxic. I mitigated this through using a weighted binary cross entropy loss and saw improvements in the performance of the model. It now does fairly well on categorizing `insult` and `obscene` in addition to `toxic`, but is still not ideal for `threat` and `identity_hate` due to the small number of training samples.