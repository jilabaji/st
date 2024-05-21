from textblob import TextBlob

testimonial = TextBlob("I bought this case for 299 under pre order. The price increased later. I have tried and returned 5 junk cases so far. Finally I got this one and my search is over. Amazing quality and superb finish. Memory card feature is too god to believe. Surprisingly light weight for an armour case that is truly protective in all sense.  Just go for it if you find it around 299 again.")
print (testimonial.sentiment)

testimonial = TextBlob("After eight months my smartwatch's internal display is damaged. Though it is warranty period fireboltt refused to repair or replace the watch. This is very bad services I have received. Please don't buy fireboltt ")
print (testimonial.sentiment)
