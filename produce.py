# importing the required libraries  
from time import sleep  
from json import dumps  
from kafka import KafkaProducer  
import uuid
import json


# initializing the Kafka producer  
tweets_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:29092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )  


if __name__ == "__main__":

    data = [
        {
            "author_id": "833354837383376897",
            "id": "1503056098634665987",
            "text": "RT @Showbiz_IT: #TheKashmirFiles team meets PM #NarendraModi, receives appreciation for film\nhttps://t.co/nTAhHzw8RG"
        },
        {
            "author_id": "1273672259303993344",
            "id": "1503056035116109824",
            "text": "RT @taran_adarsh: 'THE KASHMIR FILES' TEAM MEETS PM MODI... #TheKashmirFiles producers #AbhishekAgarwal, #PallaviJoshi and #VivekRanjanAgni\u2026"
        },
        {
            "author_id": "477725328",
            "id": "1503055971597242379",
            "text": "RT @Showbiz_IT: #TheKashmirFiles team meets PM #NarendraModi, receives appreciation for film\nhttps://t.co/nTAhHzw8RG"
        },
        {
            "author_id": "848066150470746112",
            "id": "1503055909047902208",
            "text": "RT @DhangarRanjan: \u091f\u0942\u0902\u0921\u0932\u093e \u0938\u0947 \u0935\u093f\u0927\u093e\u092f\u0915 \u092e\u093e\u0928\u0928\u0940\u092f @PPSDhangarMLA \u091c\u0940 \u0915\u094b #YogiAdityanath  \u0915\u0947\u092c\u093f\u0928\u0947\u091f \u092e\u0947\u0902 \u091c\u0917\u0939 \u0926\u0940 \u091c\u093e\u090f \u0910\u0938\u0940 \u0905\u092a\u0947\u0915\u094d\u0937\u093e \u0917\u0921\u093c\u0930\u093f\u092f\u093e \u0927\u0928\u0917\u0930 \u0938\u092e\u093e\u091c \u092d\u093e\u091c\u092a\u093e\u2026"
        },
        {
            "author_id": "1066361663866195971",
            "id": "1503055889820921856",
            "text": "RT @Showbiz_IT: #TheKashmirFiles team meets PM #NarendraModi, receives appreciation for film\nhttps://t.co/nTAhHzw8RG"
        },
        {
            "author_id": "1044185709748334598",
            "id": "1503055869541453827",
            "text": "RT @Showbiz_IT: #TheKashmirFiles team meets PM #NarendraModi, receives appreciation for film\nhttps://t.co/nTAhHzw8RG"
        },
        {
            "author_id": "1227248148705267714",
            "id": "1503055849836912642",
            "text": "RT @Shubh1mm: LARGEST POLITICAL PARTY IN THE WORLD \n\nRemember the name, \u092d\u093e\u0930\u0924\u0940\u092f \u091c\u0928\u0924\u093e \u092a\u093e\u0930\u094d\u091f\u0940 \ud83c\uddee\ud83c\uddf3\ud83d\udea9 \n\n#BJP #NarendraModi @BJP4Maharashtra @BJP4I\u2026"
        },
        {
            "author_id": "1131988048046989312",
            "id": "1503055848402145282",
            "text": "RT @PCMohanMP: Shri #YogiAdityanath Ji meets Prime Minister Shri #NarendraModi Ji in #NewDelhi.\n\n@narendramodi @myogiadityanath @myogioffic\u2026"
        },
        {
            "author_id": "1117530919567527936",
            "id": "1503055778139504642",
            "text": "@narendramodi @PMOIndia \nMy kind request to our beloved Prime minister to tweet about this masterpiece #TheKashmiriFiles written and directed by @vivekagnihotri .\nIt will be a great awareness, sir.\nKindly RT, if you want it too.\n#NarendraModi #KashmiriHindus #Kashmir_Files https://t.co/5yROQOJK58"
        },
        {
            "author_id": "1437712249020248212",
            "id": "1503055754109935617",
            "text": "RT @Showbiz_IT: #TheKashmirFiles team meets PM #NarendraModi, receives appreciation for film\nhttps://t.co/nTAhHzw8RG"
        }

]
    
    for item in data:  
        my_data = item  
        tweets_producer.send('tweets', value = my_data)  
        sleep(5)  

