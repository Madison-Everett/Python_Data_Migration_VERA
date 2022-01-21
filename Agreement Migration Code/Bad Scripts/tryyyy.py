import requests



def pdfDownload(url):
    response=requests.get(url)
    expdf=response.content
    egpdf=open('ex.pdf','wb')
    egpdf.write(expdf)
    egpdf.close()


    print(expdf)

pdfDownload('https://journals.sagepub.com/doi/pdf/10.1177/0956797614553009')
