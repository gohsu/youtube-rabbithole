# YouTube RabbitHole Explorer

A web app to explore the rabbit hole of YouTube's suggested "Up Next" videos. 

Coded for me to learn web scraping, flask and some front-end. 

### Required

* Selenium WebDriver
* Flask

### How to run

```bash
cd <projectdirectory>
export FLASK_APP=app.py
flask run
```

### Current issues/to do

* scraper does not handle youtube ads well
* for some reason, it can loop between 2-3 video links although the up next algo does not really repeat videos (I suspect this is because of the ads)
* not sure how to host this, hmm...
* design a pretty front-end and write some accompanying text

### Inspired by:

* [All of YouTube, Not Just the Algorithm, is a Far-Right Propaganda Machine](https://ffwd.medium.com/all-of-youtube-not-just-the-algorithm-is-a-far-right-propaganda-machine-29b07b12430)
* [The Making of a YouTube Radical](https://www.nytimes.com/interactive/2019/06/08/technology/youtube-radical.html)
* [The Most Measured Person in Tech Is Running the Most Chaotic Place on the Internet](https://www.nytimes.com/2019/04/17/business/youtube-ceo-susan-wojcicki.html)
* ['Fiction is outperforming reality'](https://www.theguardian.com/technology/2018/feb/02/how-youtubes-algorithm-distorts-truth)
* [Your Undivided Attention Ep 4: Down the Rabbit Hole by Design](http://humanetech.com/wp-content/uploads/2019/07/CHT-Undivided-Attention-Podcast-Ep.4-Down-the-Rabbit-Hole.pdf)



