Sentiment-Driven Video Recommender – Deployment (GCP)
====================================================

FastAPI service that serves a pre-computed recommendation similarity matrix plus aggregated emotion (sentiment) scores. Frontend (single page) is rendered from a Jinja2 template and calls JSON endpoints.

Artifacts required inside the image (placed in ``docker_app/`` before build):
 - ``final_score_matrix.joblib`` (DataFrame of final recommendation scores)
 - ``df_avg_emotions.csv`` (Per-video aggregated emotion scores; must contain ``video_id`` column)

Endpoints:
 - ``/`` UI (embedded JS)
 - ``/api/recommendations/?video_id=<optional>``
 - ``/api/emotion_scores/<video_id>``
 - ``/health`` (status + artifact load info)

Quick Local Run
---------------
.. code-block:: bash

    cd docker_app
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn main_app:app --reload --host 0.0.0.0 --port 8000

Navigate to http://127.0.0.1:8000

Docker Local
------------
.. code-block:: bash

    cd docker_app
    docker build -t vidrec:local .
    docker run -p 8000:8000 vidrec:local

GCP Manual Deployment (Artifact Registry + Cloud Run)
----------------------------------------------------
**Prerequisites**: gcloud CLI authenticated (``gcloud auth login``) and a project selected.

1. Set environment variables
   .. code-block:: bash

       export PROJECT_ID=YOUR_PROJECT_ID
       export REGION=europe-west1
       export REPO=vidrec
       export SERVICE=vidrec-service
       gcloud config set project $PROJECT_ID

2. Enable APIs (once)
   .. code-block:: bash

       gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com

3. Create Artifact Registry repo (once)
   .. code-block:: bash

       gcloud artifacts repositories create $REPO \
         --repository-format=docker \
         --location=$REGION \
         --description="VidRec images" || echo "Repo exists"

4. Build & Push (local Docker)
   .. code-block:: bash

       cd docker_app
       gcloud auth configure-docker ${REGION}-docker.pkg.dev
       IMAGE=${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/vidrec:$(git rev-parse --short HEAD)
       docker build -t $IMAGE .
       docker push $IMAGE

5. Deploy to Cloud Run
   .. code-block:: bash

       gcloud run deploy $SERVICE \
         --image $IMAGE \
         --region $REGION \
         --platform managed \
         --allow-unauthenticated \
         --port 8000 \
         --memory 512Mi \
         --concurrency 80

6. Verify
   .. code-block:: bash

       curl -s https://<CLOUD-RUN-URL>/health | jq

   Open the root URL in a browser to see the interface.

Optional: Cloud Build CI
------------------------
``cloudbuild.yaml`` (in ``docker_app/``) supports automated build & deploy. Create a trigger:
.. code-block:: bash

    gcloud builds triggers create github \
      --name=vidrec-trigger \
      --repo-name=VidRecEngine \
      --repo-owner=ivanseldas \
      --branch-pattern=^main$ \
      --build-config=docker_app/cloudbuild.yaml \
      --substitutions=_REGION=$REGION,_REPO=$REPO

Troubleshooting
---------------
* ``status=degraded`` in /health: artifact missing – ensure files exist prior to build.
* 404 /health: service not deployed / wrong URL.
* Slow first request: Cloud Run cold start (optionally set ``--min-instances=1``).
* Permission denied on push: re-run ``gcloud auth configure-docker``.

License
-------
MIT (see root LICENSE file).