from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig

model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

ARTICLE_TO_SUMMARIZE = ''' A 69-year-old Singaporean man died on Wednesday (Aug 11) from complications due to Covid-19. In a media statement, the Ministry of Health (MOH) said that the man developed symptoms on July 28 and was admitted to Tan Tock Seng Hospital the next day where he tested positive for Covid-19 infection. “He had not been vaccinated against Covid-19, and had a history of stroke, diabetes mellitus, hypertension and hyperlipidaemia,” MOH said. Hyperlipidaemia, a blood condition, is one of the main risk factors for coronary heart disease and stroke. This is the sixth death from Covid-19 this month. The first was a 34-year-old Ukrainian man who died on Aug 1 while the fifth death this month was an 80-year-old Singaporean woman who died on Aug 7. There are now 43 people who have died in Singapore after contracting the coronavirus. On Wednesday, Singapore recorded 63 new Covid-19 cases, bringing the total tally to 65,953 since the outbreak began. '''
inputs = tokenizer([ARTICLE_TO_SUMMARIZE],
                   max_length=1024, return_tensors='pt')

# Generate Summary
summary_ids = model.generate(
    inputs['input_ids'], num_beams=4, max_length=5, early_stopping=True)
print([tokenizer.decode(g, skip_special_tokens=True,
      clean_up_tokenization_spaces=False) for g in summary_ids])
