# Solution Design

## Background

Croud account managers have to proactively review the comments that are left on the clients posts.

This task is time consuming for the following reason:
1. Gathering of comments
2. Analysing the sentiment of comments

The analysing of the comments is also subjective. 

We are aiming to create a technical solution that will scrape and analyse the sentiment of all comments left on a clients post.


## Goals

We are trying to get a solution in front of the account managers as soon as possible.

Because of this we will develop iteratively and go live with the minimum viable product (MVP). We require a roadmap for the potential changes we will make.

What optimisations could happen if the product is adopted.

## Requirements

The system will scrape and analyse the comments from a clients post (YouTube/Instagram/TikTok). To which it will save them to a database before the account manager can download them as a CSV.

The output must include the following: 
1. Sentiment score, a value between -1 and 1.
2. Label, a string which is either Negative, Neutral or Positive.

Other requirements to note are:
1. No fixed SLI/SLOs
2. No predefined usage patterns. App can be used at any time
3. Go-live with 2->10 users and random bursts of activity
4. Lightweight UI for account managers to use
5. Authentication done via Croud OIDC

## Assumptions

1. Use of Google Cloud Platform, assumption made due to job spec.
2. Use of 3rd party models are okay as the data sent is available to anyone. Less security risks

## High Level Architecture Diagram

(![alt text](<High Level Architecture Diagram.png>))

### Frontend UI

This can be a very simple UI, personally aim to go with React with Next JS, but that is as I have prior experience. Would rely on other engineers opinions here.

Initial design would look be a simple form that would publish message to a topic for the backend to consume. The frontend will create a UUID that can be tracked between the services and ensure that the status of the scrape can be checked.

Once submitted it will poll the backend /status every n minutes to check the status.

Once the /status is ready to download the user can click confirm download etc.

### PubSub

We require a way for the Frontend UI to not be locked to the Backend Service whilst the scraping is commencing as it could take time.

A simple solution would be to have a PubSub topic that the FE publishes too before a push subscription initiates a request to the backend.

### Backend 

#### Endpoint: /scraper
Scraper endpoint will be triggered via a PubSub Message. The request will be written to the DB before a scrape will be commenced.
Once scraped all comments will be written to the DB and status updated.

#### Endpoint: /status?job_id={uuid}
GET endpoint that takes the UUID of a scrape job request
Checks the DB to see where the request is at. This could be, pre-scrape, scraping, scraped etc.

#### Endpoint: /download_csv?job_id={uuid}
GET endpoint that takes the UUID of a scrape job request
Returns a csv of the comments that have been analysed

### Terraform
All of these resources can be easily created and maintained using terraform, would be a sensible solution to maintain different environments

#### IAP & Firewall

Preference would be to use GCP inhouse security, so only allowing users who are a part of specific google group.
Firewall set up to only allow requests to set domains.

## Deployment Plan

Aim to get the MVP out as quick as possible.

MVP: 
1. Frontend UI
2. Backend Service with only one domain being scraped. Could see creating the scrapers being a time consuming event.
3. DB setup - keep it simple, BQ
4. IAP/Firewall
5. Monitoring & Oberservability


## Monitoring & Observability

Easily setup via TF. We want this done before go-live as it means we can track adoption and identify potential bugs etc


## Scalability

By utilising Cloud Run services increasing scalability would be incredibly simple. The tool would require the initial users request id to be stored in the frontend UI. Which would be okay for an initial release, however on refresh this id could be lost and the user would not be able to download.

Due to the way the IAP/Brand would be setup we could easily add the functionality of listing a selection of requests (last 5 etc) that the user has made irrelevant of refreshing pages. 


## CI/CD

As we are deploying Cloud Run services I would strive to use cloud build to deploy our services to the GCP project.


## Feedback & talking points for the interview:

1. Sarcasm & Emojis in comments
2. Utilising different models, switching out the model is incredibly easy, would like to spend more time researching to find an optimum model.
3. Optimisations to the service, potential pitfalls e.g. location of loading the model, should likely be done via the lifespan of the service. 
4. DB -> assuming the account managers don't have technical ability would alter the way I would recommend storing the data.
5. Some sites e.g. YouTube have likes/dislike counts on the comments, this should be utilised in the analysis.

I would generally be comfortable with the majority of this project, especially the scraper & API service. I would want support on the frontend UI which I would look for in the other engineers, as well as getting feedback from the users for how they want the page to look. I would also want other engineers opinions on which models to use, a poor choice in model would quickly make this project redundant.
