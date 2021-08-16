<h1> NLP_Project </h1>
<h3> Goal: To create a reddit summary bot that provides summaries of news articles posted in r/singapore </h3>
<h4> Mini-goals </h4> 
<ul>
  <li>-[x] Extraction summary</li>
  <li>-[x] Reddit bot:</li>
  <li>-[x] Abstraction summary</li> 
  <li>-[] Automation Script that checks r/sg for updates</li>
</ul>

<h4>How it works</h4> 
You will need to a config.py file in order to run PRAW
<ol>
  <li> <code>python create-db.py</code> to create the database to store the urls </li>
  <li> <code>python main.py</code> to run the reddit bot to reply to posts in r/articlesgtest </li>
 </ol>
 
 Used the BART Transformer found in <a href= "https://github.com/huggingface">Hugging Face</a>
 
 Link to subreddit: <a href= "https://www.reddit.com/r/articlessgtest/">here</a>
