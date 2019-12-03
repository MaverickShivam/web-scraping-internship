import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
number=0
with open("speakers.csv","w",newline="",encoding="utf-8")as fp:
  fieldnames=["Names","Image","Designation","Company","Bio","Country","Website","Facebook","Instagram","LinkedIn","YouTube"]
  j=csv.DictWriter(fp,fieldnames=fieldnames)
  j.writeheader()
  for n in range(1,540):#there are about 540 pages so we can change it accordingly.
    profiles=[]
    ol=("https://speakerhub.com/speakers?page=")
    html =urlopen(ol+str(n))
    bsObj = BeautifulSoup(html,"lxml")
    total=bsObj.findAll("li")
    for i in range(106,118):
      names=[]
      images=[]
      designations=[]
      companies=[]
      countries=[]
      swebsites=[]
      fbs=[]
      instas=[]
      yts=[]
      bios=[]
      lins=[]
      k1=total[i].findAll("a",{"class":"user-link hidden"})[0]
      profile=k1.get("href")
      profile=("https://speakerhub.com"+str(profile))
      profiles.append(profile)
      maindata=BeautifulSoup(urlopen(profiles[i-106]),"lxml")
      print((n-1)*12+i-105)
      try:
        name=str(maindata.find_all("div", itemprop="givenName")[0])
        name=name.replace('<div class="field-item odd m3-1 m4-1" itemprop="givenName">',' ')
        name=name.replace("</div>","")
        names.append(name)
        image=maindata.findAll("img", typeof="foaf:Image")[0]
        link=image.get("src")
        images.append(link)
        designation=str(maindata.findAll("span",{"class":"job"})[0])
        designation=designation.replace('<span class="job" itemprop="jobTitle">',"")
        designation=designation.replace("</span>","")
        designations.append(designation)
        company=maindata.findAll("meta",itemprop="name")[0]
        company=company.get("content")
        companies.append(company)
        country=maindata.findAll("div",{"class":"field field-name-field-country field-type-taxonomy-term-reference field-label-inline clearfix"})[0]
        country=country.findAll("div",{"class":"field-item odd m3-1 m4-1"})[0]
        country=country.get_text()
        countries.append(country)
        bio=maindata.findAll("div",{"class":"panel-body"})[0]
        bio=bio.get_text()
        bio=bio.replace("\n","")
        bio=bio.replace("\r","")
        bios.append(bio)
        try:
          swebsite=maindata.findAll("div",{"class":"field field-name-social simple-border simple-shadow bg-white profile-radius"})[0]
          
          try:
            fb=swebsite.findAll("a",{"title":"Facebook"})[0]
            fb=fb.get("href")
            fbs.append(fb)
          except:
            fbs.append("NA")


          try:
            insta=swebsite.findAll("a",{"title":"Instagram"})[0]
            insta=insta.get("href")
            instas.append(insta)
          except:
            instas.append("NA")

          try:
            yt=swebsite.findAll("a",{"title":"Youtube channel"})[0]
            yt=yt.get("href")
            yts.append(yt)
          except:
            yts.append("NA")

          try:
            lin=swebsite.findAll("a",{"title":"LinkedIn"})[0]
            lin=lin.get("href")
            lins.append(lin)
          except:
            lins.append("NA")

          try:
            swebsite=swebsite.findAll("a",{"title":"Website"})[0]
            swebsite=swebsite.get("href")
            swebsites.append(swebsite)
          except:
            swebsites.append("NA")
          
        except:
          fbs.append("NA")
          instas.append("NA")
          swebsites.append("NA")
          lins.append("NA")
          yts.append("NA")
          
        j.writerow({"Names":names[0],"Image":images[0],"Designation":designations[0],"Company":companies[0],"Bio":bios[0],"Country":countries[0],"Website":swebsites[0],"Facebook":fbs[0],"Instagram":instas[0],"LinkedIn":lins[0],"YouTube":yts[0]})
      except:
        number=number
print("Data Saved")
close = input("press enter to close")    

