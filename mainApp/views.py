from django.shortcuts import render
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False
    )
    page = await browser.newPage()
    await page.goto('http://127.0.0.1:8000/pdf')
    await page.pdf({'path': 'static/reports/report.pdf', 'format': 'A4'})
    await browser.close()

def generatepdf(request):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    return render(request, "index.html")

def index(request):
    return render(request, "index.html", context={"greetings": "Hello Working...."})