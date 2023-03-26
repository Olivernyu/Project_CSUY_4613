# Project_-CSUY_4613

## Docker setup process
1. followed installation guide form: https://docs.docker.com/desktop/install/mac-install/
2. Learned how to set up basic docker file from these sources:
    -   https://docs.docker.com/language/python/build-images/
    -   https://circleci.com/blog/docker-and-cicd-tutorial-a-deep-dive-into-containers/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--uscan-en-dsa-tROAS-auth-brand&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY0tBlxlcgbYHULtVA6fqVRYjQrvBIs5ZrOI5hLQZv03D1rQPq4_qIAaAmoaEALw_wcB
    - https://www.youtube.com/watch?v=pTFZFxd4hOI
3. built dockerfile with `docker build -t basic-linux-image .`. Run docker with `docker run -it --rm -p 8080:80 basic-linux-image`
4. docker terminal screent shot in file `docker terminal.png`