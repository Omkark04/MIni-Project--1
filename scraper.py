from selenium import webdriver
import time 
import os
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=United%20States&geoId=&trk=public_jobs_jobs-search-bar_search-submit&original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DUnited%2520States%26geoId%3D103644278%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26position%3D1%26pageNum%3D0&position=1&pageNum=0')
search = driver.find_element(By.ID, "job-search-bar-keywords")
driver.implicitly_wait(10)
print(search.text)
search.clear()
search.send_keys("Data Scientists")
html_doc="""
<!DOCTYPE html>

    
    
    
    
    
    

    
    
    
    

    
    
    
    

    
    <html lang="en">
      <head>
        <meta name="pageKey" content="d_jobs_guest_search">
          
    <meta name="robots" content="max-image-preview:large, noarchive">
    <meta name="bingbot" content="max-image-preview:large, archive">
  
<!---->          <meta name="linkedin:pageTag" content="urlType=jserp_custom;emptyResult=false">
        <meta name="locale" content="en_US">
<!---->        <meta id="config" data-app-version="2.0.2607" data-call-tree-id="AAZCM1NNba2Ymq4u6fZ3Pw==" data-multiproduct-name="jobs-guest-frontend" data-service-name="jobs-guest-frontend" data-browser-id="62261486-b63d-497c-8ff0-d0a2fc17c1f0" data-enable-page-view-heartbeat-tracking data-page-instance="urn:li:page:d_jobs_guest_search;tc9wkweBTq+WsIq21Bpu8g==" data-disable-jsbeacon-pagekey-suffix="false" data-member-id="0" data-should-use-full-url-in-pve-path="true" data-dna-member-lix-treatment="enabled" data-human-member-lix-treatment="enabled" data-dfp-member-lix-treatment="control" data-sync-apfc-headers-lix-treatment="control" data-sync-apfc-cb-lix-treatment="control" data-recaptcha-v3-integration-lix-value="control" data-network-interceptor-lix-value="control" data-is-epd-audit-event-enabled="false">

        <link rel="canonical" href="https://www.linkedin.com/jobs/data-analyst-jobs">
<!----><!---->
<!---->
<!---->
<!---->
          <link rel="manifest" href="/homepage-guest/manifest.json" crossorigin="use-credentials">

          <link rel="icon" href="https://static.licdn.com/aero-v1/sc/h/al2o9zrvru7aqj8e1x2rzsrca">


        <script>
          function getDfd() {let yFn,nFn;const p=new Promise(function(y, n){yFn=y;nFn=n;});p.resolve=yFn;p.reject=nFn;return p;}
          window.lazyloader = getDfd();
          window.tracking = getDfd();
          window.impressionTracking = getDfd();
          window.ingraphTracking = getDfd();
          window.appDetection = getDfd();
          window.pemTracking = getDfd();
        </script>

<!---->
        
        
    <title>151,000+ Data Analyst jobs in United States</title>
    <meta name="description" content="Today&amp;#39;s top 151,000+ Data Analyst jobs in United States. Leverage your professional network, and get hired. New Data Analyst jobs added daily.">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="litmsProfileName" content="jobs-guest-frontend">
    <meta name="clientSideIngraphs" content="1" data-gauge-metric-endpoint="/jobs-guest/api/ingraphs/gauge" data-counter-metric-endpoint="/jobs-guest/api/ingraphs/counter">
    <meta charset="utf-8">

    <meta property="og:type" content="website">
    <meta property="og:title" content="151,000+ Data Analyst jobs in United States">
    <meta property="og:url" content="https://www.linkedin.com/jobs/data-analyst-jobs">
    <meta property="og:description" content="Today&amp;#39;s top 151,000+ Data Analyst jobs in United States. Leverage your professional network, and get hired. New Data Analyst jobs added daily.">
<!---->    <meta name="twitter:title" content="151,000+ Data Analyst jobs in United States">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@LinkedIn">
    <meta name="twitter:description" content="Today&amp;#39;s top 151,000+ Data Analyst jobs in United States. Leverage your professional network, and get hired. New Data Analyst jobs added daily.">
  

            <meta property="lnkd:url" content="https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&amp;location=United%20States&amp;geoId=&amp;trk=public_jobs_jobs-search-bar_search-submit&amp;original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DUnited%2520States%26geoId%3D103644278%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26position%3D1%26pageNum%3D0&amp;position=1&amp;pageNum=0">

        <link rel="stylesheet" href="https://static.licdn.com/aero-v1/sc/h/63ndp9jq73n53trr0c7pxthhm">
      
<!---->      </head>
      <body dir="ltr">
<!----><!----><!---->
        
<!---->          
    
    
    
    

    

    
    <div class="base-serp-page">
        
    

    <a href="#main-content" class="skip-link btn-md btn-primary absolute z-11 -top-[100vh] focus:top-0">
      Skip to main content
    </a>
  
      <header class="base-serp-page__header global-alert-offset">
          

    
    
    
    

    <nav class="nav pt-1.5 pb-2 flex items-center justify-between relative flex-nowrap babymamabear:py-1.5
        
         babymamabear:flex-wrap 
        " aria-label="Primary">

      <a href="/?trk=public_jobs_nav-header-logo" class="nav__logo-link link-no-visited-state z-1 mr-auto min-h-[52px] flex items-center babybear:z-0 hover:no-underline focus:no-underline active:no-underline
          " data-tracking-control-name="public_jobs_nav-header-logo" data-tracking-will-navigate>
          
                
          
    
    <span class="sr-only">LinkedIn</span>
<!---->      <icon class="block text-color-brand w-[102px] h-[26px] " data-test-id="nav-logo" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8fkga714vy9b2wk5auqo5reeb"></icon>
  
      
            
      </a>

        

    
    
    
    
    

    <section class="search-bar relative flex flex-grow h-[40px] bg-cool-gray-20 min-w-0 max-w-full mx-4 rounded-sm babymamabear:mx-0 babymamabear:mb-1.5 babymamabear:bg-color-transparent babymamabear:w-full babymamabear:flex babymamabear:flex-wrap
        " data-current-search-type="JOBS">
      <button class="search-bar__placeholder papabear:hidden text-input w-full mt-1.5 !pl-[14px] border-1 border-solid border-color-border-faint rounded-[2px] h-[40px] max-h-[40px] flex items-center overflow-hidden cursor-text" data-tracking-control-name="public_jobs_search-switcher-opener">
        <icon class="text-color-icon w-3 h-3 mr-1" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/397vrsk6op88l4981ji1xe1qt"></icon>
        <div class="search-bar__full-placeholder font-sans text-md text-color-text max-w-[calc(100%-40px)] text-left whitespace-nowrap overflow-hidden text-ellipsis">
<!---->              Data Analyst in United States
<!----><!---->        </div>
        <span class="sr-only">Expand search</span>
      </button>
      
    

      
        

    
    
    
    
    
    
    

    <div class="switcher-tabs__trigger-and-tabs babymamabear:flex">
        <button aria-expanded="false" class="switcher-tabs__placeholder flex !h-full !py-0 !pl-2 !pr-1.5 border-r-1 border-solid border-r-color-border-faint babymamabear:hidden
            tab-md papabear:tab-vertical papabear:justify-start cursor-pointer" data-tracking-control-name="public_jobs_switcher-tabs-placeholder" aria-describedby="switcher-description">
          <span class="switcher-tabs__placeholder-text m-auto"></span>
          <icon class="switcher-tabs__caret-down-filled onload pointer-events-none block my-auto min-h-[24px] min-w-[24px] h-[24px] babymamabear:hidden" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx"></icon>
        </button>
        <div id="switcher-description" class="hidden">This button displays the currently selected search type. When expanded it provides a list of search options that will switch the search inputs to match the current selection. </div>
<!---->        <div class="switcher-tabs hidden z-[1] w-auto min-w-[160px] mb-1.5 py-1 absolute top-[48px] left-0 border-solid border-1 border-color-border-faint papabear:container-raised babymamabear:static babymamabear:w-[100vw] babymamabear:h-[48px] babymamabear:p-0 overflow-y-hidden overflow-x-auto md:overflow-x-hidden">
          <ul class="switcher-tabs__list flex flex-1 items-stretch papabear:flex-col" role="tablist">
                  <li class="switcher-tabs__tab h-[44px] babymamabear:basis-1/2" role="presentation">
                    <button aria-controls="jobs-search-panel" aria-selected="true" class="switcher-tabs__button w-full h-full
                        tab-md papabear:tab-vertical papabear:justify-start cursor-pointer
                        tab-selected" data-switcher-type="JOBS" data-tracking-control-name="public_jobs_switcher-tabs-jobs-search-switcher" id="job-switcher-tab" role="tab">
                        Jobs
                    </button>
                  </li>
                  <li class="switcher-tabs__tab h-[44px] babymamabear:basis-1/2" role="presentation">
                    <button aria-controls="people-search-panel" aria-selected="false" class="switcher-tabs__button w-full h-full
                        tab-md papabear:tab-vertical papabear:justify-start cursor-pointer
                        " data-switcher-type="PEOPLE" data-tracking-control-name="public_jobs_switcher-tabs-people-search-switcher" id="people-switcher-tab" role="tab">
                        People
                    </button>
                  </li>
                  <li class="switcher-tabs__tab h-[44px] babymamabear:basis-1/2" role="presentation">
                    <button aria-controls="learning-search-panel" aria-selected="false" class="switcher-tabs__button w-full h-full
                        tab-md papabear:tab-vertical papabear:justify-start cursor-pointer
                        " data-switcher-type="LEARNING" data-tracking-control-name="public_jobs_switcher-tabs-learning-search-switcher" id="learning-switcher-tab" role="tab">
                        Learning
                    </button>
                  </li>
          </ul>

            <button aria-label="Close" class="switcher-tabs__cancel-btn papabear:hidden block w-6 h-6 m-auto text-color-text-low-emphasis" data-tracking-control-name="public_jobs_switcher-tabs-cancel-search-switcher" type="button">
              <icon class="switcher-tabs__cancel-icon block w-3 h-3 m-auto onload" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
            </button>
        </div>
    </div>
  

        

    
    
    
    

    

    

    <section class="base-search-bar w-full h-full" data-searchbar-type="PEOPLE" aria-labelledby="people-switcher-tab" id="people-search-panel" role="tabpanel">
      <form class="base-search-bar__form w-full flex babymamabear:mx-mobile-container-padding babymamabear:flex-col" role="search" action="/pub/dir" data-tracking-control-name="public_jobs_people-search-bar_base-search-bar-form">
        
          
      
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 search-input">
      <input aria-label="First Name" autocomplete="on" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_people-search-bar_first-name_dismissable-input" maxlength="500" name="firstName" placeholder="First Name" type="search">
      
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_people-search-bar_first-name_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
          
      
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 search-input">
      <input aria-label="Last Name" autocomplete="on" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_people-search-bar_last-name_dismissable-input" maxlength="500" name="lastName" placeholder="Last Name" type="search">
      
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_people-search-bar_last-name_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
      
        <input name="trk" value="public_jobs_people-search-bar_search-submit" type="hidden">
        <button class="base-search-bar__submit-btn block basis-[40px] flex-shrink-0 cursor-pointer babymamabear:invisible babymamabear:ml-[-9999px] babymamabear:w-[1px] babymamabear:h-[1px]" aria-label="Search" data-tracking-control-name="public_jobs_people-search-bar_base-search-bar-search-submit" type="submit">
          <icon class="base-search-bar__search-icon onload mx-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cb5bsr4tsn2r4sjg9e3ls4tjl"></icon>
        </button>
      </form>
    </section>
  
  

        

    
    
    
    

    

    

    <section class="base-search-bar w-full h-full" data-searchbar-type="JOBS" aria-labelledby="job-switcher-tab" id="jobs-search-panel" role="tabpanel">
      <form class="base-search-bar__form w-full flex babymamabear:mx-mobile-container-padding babymamabear:flex-col" role="search" action="/jobs/search" data-tracking-control-name="public_jobs_jobs-search-bar_base-search-bar-form">
        
        

    
    
    

    <code id="i18n_aria_live_text_no-suggestions" style="display: none"><!--"No suggestions found"--></code>
    <code id="i18n_aria_live_text_one-suggestion" style="display: none"><!--"One Suggestion. Use up and down keys to navigate"--></code>
    <code id="i18n_aria_live_text_multiple-suggestions" style="display: none"><!--"Multiple Suggestions. Use up and down keys to navigate"--></code>

    
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 typeahead-input keywords-typeahead-input text-input">
      <input aria-autocomplete="list" aria-controls="job-search-bar-keywords-typeahead-list" aria-haspopup="listbox" aria-label="Search job titles or companies" autocomplete="off" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_dismissable-input" id="job-search-bar-keywords" maxlength="500" name="keywords" placeholder="Search job titles or companies" role="combobox" value="Data Analyst" type="search">
      
<!---->      <div class="typeahead-input__dropdown container-lined absolute top-[calc(100%+3px)] left-0 w-full rounded-b-md rounded-t-none z-[10] overflow-hidden max-w-none babybear:min-w-full babybear:bottom-0 babybear:overflow-y-auto">
        <template class="typeahead-item-template">
          <li class="typeahead-input__dropdown-item py-1.5 px-2 hover:cursor-pointer hover:bg-color-surface-new-hover hover:border-y-2 hover:border-solid hover:border-color-container-primary" role="option">
            <span class="typeahead-input__dropdown-text font-sans text-sm font-bold text-color-text"></span>
          </li>
        </template>

        <ul class="typeahead-input__dropdown-list w-full" id="job-search-bar-keywords-typeahead-list" role="listbox"></ul>
      </div>
<!---->    
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
<!---->        

    
    
    

    <code id="i18n_aria_live_text_no-suggestions" style="display: none"><!--"No suggestions found"--></code>
    <code id="i18n_aria_live_text_one-suggestion" style="display: none"><!--"One Suggestion. Use up and down keys to navigate"--></code>
    <code id="i18n_aria_live_text_multiple-suggestions" style="display: none"><!--"Multiple Suggestions. Use up and down keys to navigate"--></code>

    
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 typeahead-input location-typeahead-input">
      <input aria-autocomplete="list" aria-controls="job-search-bar-location-typeahead-list" aria-haspopup="listbox" aria-label="Location" autocomplete="off" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_dismissable-input" id="job-search-bar-location" maxlength="500" name="location" placeholder="Location" role="combobox" value="United States" type="search">
      
<!---->      <div class="typeahead-input__dropdown container-lined absolute top-[calc(100%+3px)] left-0 w-full rounded-b-md rounded-t-none z-[10] overflow-hidden max-w-none babybear:min-w-full babybear:bottom-0 babybear:overflow-y-auto">
        <template class="typeahead-item-template">
          <li class="typeahead-input__dropdown-item py-1.5 px-2 hover:cursor-pointer hover:bg-color-surface-new-hover hover:border-y-2 hover:border-solid hover:border-color-container-primary" role="option">
            <span class="typeahead-input__dropdown-text font-sans text-sm font-bold text-color-text"></span>
          </li>
        </template>

        <ul class="typeahead-input__dropdown-list w-full" id="job-search-bar-location-typeahead-list" role="listbox"></ul>
      </div>
<!---->    
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
        <input name="geoId" value="103644278" type="hidden">
      
        <input name="trk" value="public_jobs_jobs-search-bar_search-submit" type="hidden">
        <button class="base-search-bar__submit-btn block basis-[40px] flex-shrink-0 cursor-pointer babymamabear:invisible babymamabear:ml-[-9999px] babymamabear:w-[1px] babymamabear:h-[1px]" aria-label="Search" data-tracking-control-name="public_jobs_jobs-search-bar_base-search-bar-search-submit" type="submit">
          <icon class="base-search-bar__search-icon onload mx-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cb5bsr4tsn2r4sjg9e3ls4tjl"></icon>
        </button>
      </form>
    </section>
  
  

        
    
    

    

    

    <section class="base-search-bar w-full h-full" data-searchbar-type="LEARNING" aria-labelledby="learning-switcher-tab" id="learning-search-panel" role="tabpanel">
      <form class="base-search-bar__form w-full flex babymamabear:mx-mobile-container-padding babymamabear:flex-col" role="search" action="/learning/search" data-tracking-control-name="public_jobs_learning-search-bar_base-search-bar-form">
        
        
      
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 search-input">
      <input aria-label="Search skills, subjects, or software" autocomplete="on" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_learning-search-bar_keywords_dismissable-input" maxlength="500" name="keywords" placeholder="Search skills, subjects, or software" value="Data Analyst" type="search">
      
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_learning-search-bar_keywords_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
        <input class="nav__search-uoo" name="upsellOrderOrigin" type="hidden">
        
      
        <input name="trk" value="public_jobs_learning-search-bar_search-submit" type="hidden">
        <button class="base-search-bar__submit-btn block basis-[40px] flex-shrink-0 cursor-pointer babymamabear:invisible babymamabear:ml-[-9999px] babymamabear:w-[1px] babymamabear:h-[1px]" aria-label="Search" data-tracking-control-name="public_jobs_learning-search-bar_base-search-bar-search-submit" type="submit">
          <icon class="base-search-bar__search-icon onload mx-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cb5bsr4tsn2r4sjg9e3ls4tjl"></icon>
        </button>
      </form>
    </section>
  
  

        <div aria-live="polite" class="search-bar__live-text sr-only" role="status"></div>
      
  
    </section>
  

<!---->
      <div class="nav__cta-container order-3 flex gap-x-1 justify-end min-w-[100px] flex-nowrap flex-shrink-0 babybear:flex-wrap flex-2
          ">
          
  
  

      
      <a class="nav__button-secondary btn-md btn-secondary-emphasis ml-3" href="https://www.linkedin.com/login?emailAddress=&amp;fromSignIn=&amp;fromSignIn=true&amp;session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3DData%2520Analyst%26location%3DUnited%2520States%26geoId%3D%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26original_referer%3Dhttps%253A%252F%252Fwww.linkedin.com%252Fjobs%252Fsearch%253Fkeywords%253D%2526location%253DUnited%252520States%2526geoId%253D103644278%2526trk%253Dpublic_jobs_jobs-search-bar_search-submit%2526position%253D1%2526pageNum%253D0%26position%3D1%26pageNum%3D0&amp;trk=public_jobs_nav-header-signin" data-tracking-control-name="public_jobs_nav-header-signin" data-tracking-will-navigate data-tracking-client-ingraph>
          Sign in
      </a>


        
    
    <a class="nav__button-tertiary btn-md btn-primary" href="https://www.linkedin.com/signup/cold-join?source=jobs_registration&amp;session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3DData%2520Analyst%26location%3DUnited%2520States%26geoId%3D%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26original_referer%3Dhttps%253A%252F%252Fwww.linkedin.com%252Fjobs%252Fsearch%253Fkeywords%253D%2526location%253DUnited%252520States%2526geoId%253D103644278%2526trk%253Dpublic_jobs_jobs-search-bar_search-submit%2526position%253D1%2526pageNum%253D0%26position%3D1%26pageNum%3D0&amp;trk=public_jobs_nav-header-join" data-tracking-control-name="public_jobs_nav-header-join" data-test-live-nav-primary-cta data-tracking-will-navigate data-tracking-client-ingraph>
      Join now
<!---->    </a>


<!---->
<!---->      </div>

<!---->
<!---->    </nav>
  
      </header>

        <section class="base-serp-page__filters-bar">
          <div class="base-serp-page__filters">
            
        
        
      <div class="search-filters search-filters--carousel">
        
    
    

    <div class="filters filters--desktop">
      <form class="filters__form" id="jserp-filters" action="https://www.linkedin.com/jobs/search" data-tracking-control-name="public_jobs_filters">
        
              <input name="keywords" value="Data Analyst" type="hidden">
              <input name="location" value="United States" type="hidden">
              <input name="geoId" value="103644278" type="hidden">
          
        <ul class="filters__list">
<!---->            
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter-button--selected pill-checked filter__dropdown-to-modal-trigger" aria-label="Date posted filter. Any time filter is currently applied. Clicking this button displays all Date posted filter options." data-tracking-control-name="public_jobs_f_TPR" aria-expanded="false" type="button">
        
        Any time
      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
<!---->            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Date posted filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_TPR-0" form="jserp-filters" name="f_TPR" checked value type="radio">
    <label for="f_TPR-0">
        Any time (150,797)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_TPR-1" form="jserp-filters" name="f_TPR" value="r2592000" type="radio">
    <label for="f_TPR-1">
        Past month (124,626)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_TPR-2" form="jserp-filters" name="f_TPR" value="r604800" type="radio">
    <label for="f_TPR-2">
        Past week (56,062)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_TPR-3" form="jserp-filters" name="f_TPR" value="r86400" type="radio">
    <label for="f_TPR-3">
        Past 24 hours (9,616)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_TPR" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter__dropdown-to-modal-trigger" aria-label="Company filter. Clicking this button displays all Company filter options." data-tracking-control-name="public_jobs_f_C" aria-expanded="false" type="button">
        Company
<!---->      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
              

    
    
    

    <code id="i18n_aria_live_text_no-suggestions" style="display: none"><!--"No suggestions found"--></code>
    <code id="i18n_aria_live_text_one-suggestion" style="display: none"><!--"One Suggestion. Use up and down keys to navigate"--></code>
    <code id="i18n_aria_live_text_multiple-suggestions" style="display: none"><!--"Multiple Suggestions. Use up and down keys to navigate"--></code>

    
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 typeahead-input filter__typeahead" data-base-api-url="/jobs-guest/api/typeaheadHits?typeaheadType=COMPANY" aria-label="Add a filter for Company">
      <input aria-autocomplete="list" aria-controls="f_C-typeahead-list" aria-haspopup="listbox" aria-label="Add a filter" autocomplete="off" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_f_C_dismissable-input" id="f_C" maxlength="500" placeholder="Add a filter" role="combobox" type="text">
      
        <div aria-live="polite" class="typeahead-live-text sr-only" role="status"></div>
      <div class="typeahead-input__dropdown container-lined absolute top-[calc(100%+3px)] left-0 w-full rounded-b-md rounded-t-none z-[10] overflow-hidden max-w-none babybear:min-w-full babybear:bottom-0 babybear:overflow-y-auto">
        <template class="typeahead-item-template">
          <li class="typeahead-input__dropdown-item py-1.5 px-2 hover:cursor-pointer hover:bg-color-surface-new-hover hover:border-y-2 hover:border-solid hover:border-color-container-primary" role="option">
            <span class="typeahead-input__dropdown-text font-sans text-sm font-bold text-color-text"></span>
          </li>
        </template>

        <ul class="typeahead-input__dropdown-list w-full" id="f_C-typeahead-list" role="listbox"></ul>
      </div>
<!---->    
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_f_C_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Company filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_C-0" form="jserp-filters" name="f_C" value="3076" type="checkbox">
    <label for="f_C-0">
        Kforce Inc (400)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_C-1" form="jserp-filters" name="f_C" value="68313053" type="checkbox">
    <label for="f_C-1">
        Royal Caribbean Group (42)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_C-2" form="jserp-filters" name="f_C" value="115116" type="checkbox">
    <label for="f_C-2">
        ECLARO (25)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_C-3" form="jserp-filters" name="f_C" value="431105" type="checkbox">
    <label for="f_C-3">
        SeatGeek (22)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_C-4" form="jserp-filters" name="f_C" value="105584369" type="checkbox">
    <label for="f_C-4">
        AARATECH (21)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_C" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter__dropdown-to-modal-trigger" aria-label="Job type filter. Clicking this button displays all Job type filter options." data-tracking-control-name="public_jobs_f_JT" aria-expanded="false" type="button">
        Job type
<!---->      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
<!---->            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Job type filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_JT-0" form="jserp-filters" name="f_JT" value="F" type="checkbox">
    <label for="f_JT-0">
        Full-time (135,628)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_JT-1" form="jserp-filters" name="f_JT" value="P" type="checkbox">
    <label for="f_JT-1">
        Part-time (2,763)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_JT-2" form="jserp-filters" name="f_JT" value="C" type="checkbox">
    <label for="f_JT-2">
        Contract (11,498)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_JT-3" form="jserp-filters" name="f_JT" value="T" type="checkbox">
    <label for="f_JT-3">
        Temporary (492)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_JT-4" form="jserp-filters" name="f_JT" value="V" type="checkbox">
    <label for="f_JT-4">
        Volunteer (69)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_JT" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter__dropdown-to-modal-trigger" aria-label="Experience level filter. Clicking this button displays all Experience level filter options." data-tracking-control-name="public_jobs_f_E" aria-expanded="false" type="button">
        Experience level
<!---->      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
<!---->            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Experience level filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_E-0" form="jserp-filters" name="f_E" value="1" type="checkbox">
    <label for="f_E-0">
        Internship (5,530)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_E-1" form="jserp-filters" name="f_E" value="2" type="checkbox">
    <label for="f_E-1">
        Entry level (23,418)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_E-2" form="jserp-filters" name="f_E" value="3" type="checkbox">
    <label for="f_E-2">
        Associate (6,199)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_E-3" form="jserp-filters" name="f_E" value="4" type="checkbox">
    <label for="f_E-3">
        Mid-Senior level (94,823)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_E-4" form="jserp-filters" name="f_E" value="5" type="checkbox">
    <label for="f_E-4">
        Director (2,393)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_E" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter__dropdown-to-modal-trigger" aria-label="Location filter. Clicking this button displays all Location filter options." data-tracking-control-name="public_jobs_f_PP" aria-expanded="false" type="button">
        Location
<!---->      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
              

    
    
    

    <code id="i18n_aria_live_text_no-suggestions" style="display: none"><!--"No suggestions found"--></code>
    <code id="i18n_aria_live_text_one-suggestion" style="display: none"><!--"One Suggestion. Use up and down keys to navigate"--></code>
    <code id="i18n_aria_live_text_multiple-suggestions" style="display: none"><!--"Multiple Suggestions. Use up and down keys to navigate"--></code>

    
    

    <section class="dismissable-input text-input !pr-3 bg-color-transparent flex items-center h-[40px] min-w-0 relative babybear:w-full babybear:mb-1 typeahead-input filter__typeahead" data-base-api-url="/jobs-guest/api/typeaheadHits?origin=jserp&amp;typeaheadType=GEO&amp;geoTypes=POPULATED_PLACE" aria-label="Add a filter for Location">
      <input aria-autocomplete="list" aria-controls="f_PP-typeahead-list" aria-haspopup="listbox" aria-label="Add a filter" autocomplete="off" class="dismissable-input__input font-sans text-md text-color-text bg-color-transparent flex items-center flex-1 focus:outline-none placeholder:text-color-text-secondary" data-tracking-control-name="public_jobs_f_PP_dismissable-input" id="f_PP" maxlength="500" placeholder="Add a filter" role="combobox" type="text">
      
        <div aria-live="polite" class="typeahead-live-text sr-only" role="status"></div>
      <div class="typeahead-input__dropdown container-lined absolute top-[calc(100%+3px)] left-0 w-full rounded-b-md rounded-t-none z-[10] overflow-hidden max-w-none babybear:min-w-full babybear:bottom-0 babybear:overflow-y-auto">
        <template class="typeahead-item-template">
          <li class="typeahead-input__dropdown-item py-1.5 px-2 hover:cursor-pointer hover:bg-color-surface-new-hover hover:border-y-2 hover:border-solid hover:border-color-container-primary" role="option">
            <span class="typeahead-input__dropdown-text font-sans text-sm font-bold text-color-text"></span>
          </li>
        </template>

        <ul class="typeahead-input__dropdown-list w-full" id="f_PP-typeahead-list" role="listbox"></ul>
      </div>
<!---->    
        <button class="dismissable-input__button text-color-text h-[40px] min-w-[24px] w-[24px] -mr-2 opacity-0 transition-opacity duration-[0.1s] disabled:invisible focus:opacity-100" data-tracking-control-name="public_jobs_f_PP_dismissable-input-clear" type="button">
          <label class="sr-only">Clear text</label>
          <icon class="dismissable-input__button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cs55jggk4p3uqh9ozxdmpvjg7"></icon>
        </button>
    </section>
  
  
            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Location filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_PP-0" form="jserp-filters" name="f_PP" value="102571732" type="checkbox">
    <label for="f_PP-0">
        New York, NY (7,070)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_PP-1" form="jserp-filters" name="f_PP" value="102277331" type="checkbox">
    <label for="f_PP-1">
        San Francisco, CA (5,163)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_PP-2" form="jserp-filters" name="f_PP" value="104472865" type="checkbox">
    <label for="f_PP-2">
        Austin, TX (2,964)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_PP-3" form="jserp-filters" name="f_PP" value="102448103" type="checkbox">
    <label for="f_PP-3">
        Los Angeles, CA (1,568)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_PP-4" form="jserp-filters" name="f_PP" value="105573479" type="checkbox">
    <label for="f_PP-4">
        Nashville, TN (909)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_PP" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter__dropdown-to-modal-trigger" aria-label="Salary filter. Clicking this button displays all Salary filter options." data-tracking-control-name="public_jobs_f_SB2" aria-expanded="false" type="button">
        Salary
<!---->      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
<!---->            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Salary filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_SB2-0" form="jserp-filters" name="f_SB2" value="1" type="radio">
    <label for="f_SB2-0">
        $40,000+ (18,148)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_SB2-1" form="jserp-filters" name="f_SB2" value="2" type="radio">
    <label for="f_SB2-1">
        $60,000+ (17,966)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_SB2-2" form="jserp-filters" name="f_SB2" value="3" type="radio">
    <label for="f_SB2-2">
        $80,000+ (17,538)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_SB2-3" form="jserp-filters" name="f_SB2" value="4" type="radio">
    <label for="f_SB2-3">
        $100,000+ (16,562)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_SB2-4" form="jserp-filters" name="f_SB2" value="5" type="radio">
    <label for="f_SB2-4">
        $120,000+ (15,392)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_SB2" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
                
    
    
    

      <li class="filter">
        
    <div class="dropdown-to-modal filter__dropdown-to-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
            
    
    
    

    <button class="filter-button pill flex items-center !min-h-0
         filter__dropdown-to-modal-trigger" aria-label="Remote filter. Clicking this button displays all Remote filter options." data-tracking-control-name="public_jobs_f_WT" aria-expanded="false" type="button">
        Remote
<!---->      <icon data-delayed-url="https://static.licdn.com/aero-v1/sc/h/1mbz49mpng9yvv8gqs11n7dkx" class="filter-button__icon h-3 w-3"></icon>
    </button>
  
          
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-auto top-[100%]" tabindex="-1">
          
            
<!---->            
    

    <div class="filter-values-container">
      <div class="filter-values-container__filter-values" aria-label="Remote filter options" role="group">
          
  

  <div class="filter-values-container__filter-value">
    <input id="f_WT-0" form="jserp-filters" name="f_WT" value="1" type="checkbox">
    <label for="f_WT-0">
        On-site (84,317)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_WT-1" form="jserp-filters" name="f_WT" value="3" type="checkbox">
    <label for="f_WT-1">
        Hybrid (36,402)
    </label>
  </div>

          
  

  <div class="filter-values-container__filter-value">
    <input id="f_WT-2" form="jserp-filters" name="f_WT" value="2" type="checkbox">
    <label for="f_WT-2">
        Remote (34,659)
    </label>
  </div>

      </div>
    </div>
  
              
  <button class="filter__submit-button" form="jserp-filters" data-tracking-control-name="public_jobs_f_WT" type="submit">
    Done
  </button>

          
          
        </div>

<!---->    </div>
  
    </div>
  
      </li>
  
          
        </ul>
      </form>

<!---->    </div>
  
      </div>
  
      
      
          </div>
        </section>

      
        
<!---->      
      

      <div class="base-serp-page__content">
        
        <main id="main-content" class="two-pane-serp-page__results" role="main">
            <section class="two-pane-serp-page__search-header">
              
<!---->
          
    
    

    
    
    

      <section class="job-alert-redirect-section job-alert-redirect-section--jserp">
        <icon class="job-alert-redirect-section__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/dd4yq8pu9gycnw9c7p5uro8qn"></icon>
        <div class="job-alert-redirect-section__container">
          <p>
            Get notified about new <span class="break-words t-bold">Data Analyst</span> jobs in <strong>United States</strong>.
          </p>

          <a class="job-alert-redirect-section__cta" href="https://www.linkedin.com/login?emailAddress=&amp;fromSignIn=&amp;session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3DData%2520Analyst%26location%3DUnited%2520States%26geoId%3D%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26original_referer%3Dhttps%253A%252F%252Fwww.linkedin.com%252Fjobs%252Fsearch%253Fkeywords%253D%2526location%253DUnited%252520States%2526geoId%253D103644278%2526trk%253Dpublic_jobs_jobs-search-bar_search-submit%2526position%253D1%2526pageNum%253D0%26position%3D1%26pageNum%3D0&amp;trk=public_jobs_job-alert-guest-redirect-cta" data-impression-id="public_jobs_job-alert-guest-redirect-cta" data-tracking-control-name="public_jobs_job-alert-guest-redirect-cta" data-tracking-will-navigate>
            Sign in to create job alert
          </a>
        </div>
      </section>
  
      
            </section>

              
<!---->
        
    
    

          
    
    

    <div class="results-context-header">
      <h1 class="results-context-header__context">
          <span class="results-context-header__job-count">151,000+</span> <span class="results-context-header__query-search">Data Analyst Jobs in United States</span>
      </h1>
      
    </div>
  
  
      
            <section class="two-pane-serp-page__results-list">
              
            <ul class="jobs-search__results-list">
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4297713391" data-impression-id="jobs-search-desktop-0" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="zeYVlAICUDjBPth0vg0tJw==" data-column="1" data-row="1">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-vivint-4297713391?position=1&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=zeYVlAICUDjBPth0vg0tJw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQETYb3kvfmOrA/company-logo_100_100/B56Zagg2q8G4AU-/0/1746449689597/vivint_logo?e=2147483647&amp;v=beta&amp;t=E6qwj2zJPWSB2LB-N2YzqWVzxpHKrBXvnAkMA7sUSwc" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/vivint?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Vivint
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Lindon, UT
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4307571880" data-impression-id="jobs-search-desktop-1" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="UwqoZovke/sr3JR0hWZG6A==" data-column="1" data-row="2">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-internship-at-seatgeek-4307571880?position=2&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=UwqoZovke%2Fsr3JR0hWZG6A%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst - Internship
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4E0BAQHsVXif6p-JmA/company-logo_100_100/company-logo_100_100/0/1630619803078/seatgeek_logo?e=2147483647&amp;v=beta&amp;t=dyIZhwTvBV7o_R5MJEcUCVMyX6xpwWfT2SPCCEFIzsk" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst - Internship
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/seatgeek?trk=public_jobs_jserp-result_job-search-card-subtitle">
            SeatGeek
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            New York, NY
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-25">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      2 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4285808234" data-impression-id="jobs-search-desktop-2" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="uxuU/1G7JWmk1UgmQqfvtQ==" data-column="1" data-row="3">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/sr-data-analyst-at-vivint-4285808234?position=3&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=uxuU%2F1G7JWmk1UgmQqfvtQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Sr. Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQETYb3kvfmOrA/company-logo_100_100/B56Zagg2q8G4AU-/0/1746449689597/vivint_logo?e=2147483647&amp;v=beta&amp;t=E6qwj2zJPWSB2LB-N2YzqWVzxpHKrBXvnAkMA7sUSwc" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Sr. Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/vivint?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Vivint
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Lindon, UT
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4308606755" data-impression-id="jobs-search-desktop-3" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="CxH35B7SiukvlwCS6rMfkQ==" data-column="1" data-row="4">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/business-data-analyst-at-kforce-inc-4308606755?position=4&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=CxH35B7SiukvlwCS6rMfkQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Business Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4D0BAQEtonVHDHqAZQ/company-logo_100_100/company-logo_100_100/0/1639415775313/kforce_logo?e=2147483647&amp;v=beta&amp;t=NL8XuPikJ6Xfi1MKQk9TVePX6KdLB4m5KQFZdiHD8IA" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Business Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/kforce?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Kforce Inc
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Nashville, TN
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4274385912" data-impression-id="jobs-search-desktop-4" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="ci4lemYdX+LwRW/wB64enQ==" data-column="1" data-row="5">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/business-intelligence-data-analyst-at-simplepractice-4274385912?position=5&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=ci4lemYdX%2BLwRW%2FwB64enQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Business Intelligence Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQGxKueaCm_03g/company-logo_100_100/company-logo_100_100/0/1727465541512/simplepractice_logo?e=2147483647&amp;v=beta&amp;t=mviCamVQqHRsy_rxU2ciT5pCYqiB5LrQksg0vs_GzQ0" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Business Intelligence Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/simplepractice?trk=public_jobs_jserp-result_job-search-card-subtitle">
            SimplePractice
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4300062927" data-impression-id="jobs-search-desktop-5" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="LdJf3e5OEluARSrrHW9dWQ==" data-column="1" data-row="6">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-measurement-science-at-samba-tv-4300062927?position=6&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=LdJf3e5OEluARSrrHW9dWQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst, Measurement Science
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQE85AyIsz5gHw/company-logo_100_100/company-logo_100_100/0/1719850769441/sambatv_logo?e=2147483647&amp;v=beta&amp;t=HaI0GLSpLU-qyB9WVJ2Jj2oUcjOMxsMueZ6T-qaFlMo" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst, Measurement Science
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/sambatv?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Samba TV
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            New York, NY
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-25">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      2 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4241077472" data-impression-id="jobs-search-desktop-6" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="DZFFdD969Gx/+Qqly0hImw==" data-column="1" data-row="7">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/analyst-data-visualization-business-intelligence-at-royal-caribbean-group-4241077472?position=7&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=DZFFdD969Gx%2F%2BQqly0hImw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Analyst, Data Visualization &amp; Business Intelligence
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQEIwbQ-yw0fKA/company-logo_100_100/company-logo_100_100/0/1686667044701/royal_caribbean_group_logo?e=2147483647&amp;v=beta&amp;t=o4pDXgis4Tke5bzKHs9eGNZn1bfJK138-3mMBnYJSeM" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Analyst, Data Visualization &amp; Business Intelligence
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/royal-caribbean-group?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Royal Caribbean Group
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Miami, FL
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4317975045" data-impression-id="jobs-search-desktop-7" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="3P6Et10djfl2JxtdDwnNyg==" data-column="1" data-row="8">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-sports-research-4317975045?position=8&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=3P6Et10djfl2JxtdDwnNyg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQG0FFrOd8x57A/company-logo_100_100/company-logo_100_100/0/1681943910136/sports_research_corp_logo?e=2147483647&amp;v=beta&amp;t=Xhu3Hgq-q3EitFzXAEa0iKV7gObApsZXTbAHaRSf7tM" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/sports-research-corp-?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Sports Research
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            San Pedro, CA
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/a0d85elrpgg38lskvq1kvzb3" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Medical insurance
             +4&nbsp;benefits
        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-23">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      4 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4300063862" data-impression-id="jobs-search-desktop-8" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="pGF8Xqfb5DoSB04EtcFACg==" data-column="1" data-row="9">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-measurement-science-at-samba-tv-4300063862?position=9&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=pGF8Xqfb5DoSB04EtcFACg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst, Measurement Science
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQE85AyIsz5gHw/company-logo_100_100/company-logo_100_100/0/1719850769441/sambatv_logo?e=2147483647&amp;v=beta&amp;t=HaI0GLSpLU-qyB9WVJ2Jj2oUcjOMxsMueZ6T-qaFlMo" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst, Measurement Science
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/sambatv?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Samba TV
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            San Francisco, CA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4317232336" data-impression-id="jobs-search-desktop-9" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="+FBBVMbakul6hYFaYH95Pw==" data-column="1" data-row="10">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-eclaro-4317232336?position=10&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=%2BFBBVMbakul6hYFaYH95Pw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4D0BAQFAwhBV3KXS_Q/company-logo_100_100/company-logo_100_100/0/1630456986815/eclaro_logo?e=2147483647&amp;v=beta&amp;t=KV2JqBSPdORsOAAQWa4Qvuc7F11lD7KWiVDVh88jRJ4" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/eclaro?trk=public_jobs_jserp-result_job-search-card-subtitle">
            ECLARO
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            New York, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4317218194" data-impression-id="jobs-search-desktop-10" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="zXGXyseWV/sdNLIb7zS9cQ==" data-column="1" data-row="11">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-eclaro-4317218194?position=11&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=zXGXyseWV%2FsdNLIb7zS9cQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4D0BAQFAwhBV3KXS_Q/company-logo_100_100/company-logo_100_100/0/1630456986815/eclaro_logo?e=2147483647&amp;v=beta&amp;t=KV2JqBSPdORsOAAQWa4Qvuc7F11lD7KWiVDVh88jRJ4" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/eclaro?trk=public_jobs_jserp-result_job-search-card-subtitle">
            ECLARO
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Texas, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319204032" data-impression-id="jobs-search-desktop-11" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="2Q6YoWBLh4vly6dnyN+ryQ==" data-column="1" data-row="12">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-salas-o-brien-4319204032?position=12&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=2Q6YoWBLh4vly6dnyN%2BryQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C560BAQG_72A8burDdQ/company-logo_100_100/company-logo_100_100/0/1678813550001/salasobrien_logo?e=2147483647&amp;v=beta&amp;t=ka7VK4_6VxTSp2I7mz1f898cRaJoOs-uX2pP_MvA0zw" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/salasobrien?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Salas O'Brien
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/a0d85elrpgg38lskvq1kvzb3" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Medical insurance
             +3&nbsp;benefits
        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      14 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319195319" data-impression-id="jobs-search-desktop-12" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="+DaL/+bEGXUwDGktSoW6BQ==" data-column="1" data-row="13">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/senior-data-analyst-at-realtor-com-4319195319?position=13&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=%2BDaL%2F%2BbEGXUwDGktSoW6BQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Senior Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C560BAQHvBS3hOf83gQ/company-logo_100_100/company-logo_100_100/0/1630657231725/realtor_com_logo?e=2147483647&amp;v=beta&amp;t=Mjivvu178YRjEgy0jH4_XFAWNu2plAjHp4gToQ47Xyc" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Senior Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/realtor-com?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Realtor.com
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Austin, TX
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      10 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4318386291" data-impression-id="jobs-search-desktop-13" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="vZ32AdfV0UC5WfmeQvBGYA==" data-column="1" data-row="14">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-world-insurance-associates-llc-4318386291?position=14&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=vZ32AdfV0UC5WfmeQvBGYA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQFCPHJ_Bu-PSA/company-logo_100_100/B4EZbp2P7HGUAQ-/0/1747680035321/world_insurance_associates_llc_logo?e=2147483647&amp;v=beta&amp;t=LWs60E7fXX45ECVclHLWeZy-bvA08F6lSAfGy__LgPY" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/world-insurance-associates-llc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            World Insurance Associates LLC
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Iselin, NJ
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319144842" data-impression-id="jobs-search-desktop-14" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="teOWetd4kEg0KAtWOFW2dg==" data-column="1" data-row="15">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-helic-co-4319144842?position=15&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=teOWetd4kEg0KAtWOFW2dg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQGBNZ-3rShTEw/company-logo_100_100/company-logo_100_100/0/1734174956627?e=2147483647&amp;v=beta&amp;t=yBKRJCP06tg-_JXcdL3oS8uaRy34EMTcNXRcbej4a04" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://ca.linkedin.com/company/helicco?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Helic &amp; Co.
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      14 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331140009" data-impression-id="jobs-search-desktop-15" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="O8hgpMqDkNyDBZppUHk1Ug==" data-column="1" data-row="16">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/analytics-reporting-analyst-at-the-walt-disney-company-4331140009?position=16&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=O8hgpMqDkNyDBZppUHk1Ug%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Analytics &amp; Reporting Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQHScKuaJ_0-WA/company-logo_100_100/company-logo_100_100/0/1712695425017/the_walt_disney_company_logo?e=2147483647&amp;v=beta&amp;t=RNCX8SOfIyb101EpcMeT_VYVIEv4nLPFUGLsBZ8WEjg" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Analytics &amp; Reporting Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/the-walt-disney-company?trk=public_jobs_jserp-result_job-search-card-subtitle">
            The Walt Disney Company
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            New York, NY
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4287291751" data-impression-id="jobs-search-desktop-16" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="QuErMvsIzKsbbU3/OE+75g==" data-column="1" data-row="17">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-i-at-lensa-4287291751?position=17&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=QuErMvsIzKsbbU3%2FOE%2B75g%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst I
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4D0BAQEkHa-0Aki9XQ/company-logo_100_100/B4DZaKylu7GsAQ-/0/1746085240184/lensa_logo?e=2147483647&amp;v=beta&amp;t=vxuqQreX_wx1J2lugCeUKuGGZtbGyjhRRFeWyrBMnFQ" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst I
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/lensa?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Lensa
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Rochester, NY
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4300074490" data-impression-id="jobs-search-desktop-17" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="XCsluPhzZWypwkdSkkWo8w==" data-column="1" data-row="18">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-measurement-science-at-samba-tv-4300074490?position=18&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=XCsluPhzZWypwkdSkkWo8w%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst, Measurement Science
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQE85AyIsz5gHw/company-logo_100_100/company-logo_100_100/0/1719850769441/sambatv_logo?e=2147483647&amp;v=beta&amp;t=HaI0GLSpLU-qyB9WVJ2Jj2oUcjOMxsMueZ6T-qaFlMo" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst, Measurement Science
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/sambatv?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Samba TV
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Los Angeles, CA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-25">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      2 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319192020" data-impression-id="jobs-search-desktop-18" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="Zo9/C5kRNGso/n6wVGsZIQ==" data-column="1" data-row="19">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aaratech-4319192020?position=19&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=Zo9%2FC5kRNGso%2Fn6wVGsZIQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQHa_a_VlxuW4A/company-logo_100_100/company-logo_100_100/0/1736445912510?e=2147483647&amp;v=beta&amp;t=W5mlp-Y_2InApg4L2Npkvtarkp9vX-8tzA2GO6I8iPE" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aaratechinc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            AARATECH
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            San Francisco Bay Area
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      19 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4297701547" data-impression-id="jobs-search-desktop-19" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="UBIKgSRB3BBEcnBXiysdPw==" data-column="1" data-row="20">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-betterment-4297701547?position=20&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=UBIKgSRB3BBEcnBXiysdPw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4D0BAQHD-kRGjmwQtQ/company-logo_100_100/company-logo_100_100/0/1637070868010/betterment_logo?e=2147483647&amp;v=beta&amp;t=TGSCwkj7gOLGu1fVTbrZ4IEBHGn7TFLK4oPw5t63HYY" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/betterment?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Betterment
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            New York, NY
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319291921" data-impression-id="jobs-search-desktop-20" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="e9QnrsiTQC7n2dh6W8YzcQ==" data-column="1" data-row="21">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aaratech-4319291921?position=21&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=e9QnrsiTQC7n2dh6W8YzcQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQHa_a_VlxuW4A/company-logo_100_100/company-logo_100_100/0/1736445912510?e=2147483647&amp;v=beta&amp;t=W5mlp-Y_2InApg4L2Npkvtarkp9vX-8tzA2GO6I8iPE" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aaratechinc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            AARATECH
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Austin, TX
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      18 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331851395" data-impression-id="jobs-search-desktop-21" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="Ea0lLlEOrWINf8ICOOKimA==" data-column="1" data-row="22">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331851395?position=22&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=Ea0lLlEOrWINf8ICOOKimA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319281892" data-impression-id="jobs-search-desktop-22" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="ciiMxvQBjXc2wdFkgZflmw==" data-column="1" data-row="23">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aaratech-4319281892?position=23&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=ciiMxvQBjXc2wdFkgZflmw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQHa_a_VlxuW4A/company-logo_100_100/company-logo_100_100/0/1736445912510?e=2147483647&amp;v=beta&amp;t=W5mlp-Y_2InApg4L2Npkvtarkp9vX-8tzA2GO6I8iPE" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aaratechinc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            AARATECH
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Los Angeles Metropolitan Area
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      18 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319192008" data-impression-id="jobs-search-desktop-23" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="tg8G1oB9u6VW2wex19biBw==" data-column="1" data-row="24">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aaratech-4319192008?position=24&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=tg8G1oB9u6VW2wex19biBw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQHa_a_VlxuW4A/company-logo_100_100/company-logo_100_100/0/1736445912510?e=2147483647&amp;v=beta&amp;t=W5mlp-Y_2InApg4L2Npkvtarkp9vX-8tzA2GO6I8iPE" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aaratechinc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            AARATECH
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Dallas-Fort Worth Metroplex
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      19 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331319636" data-impression-id="jobs-search-desktop-24" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="Y/+hfbUW08CkEQZSgm3wvQ==" data-column="1" data-row="25">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-ii-at-kforce-inc-4331319636?position=25&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=Y%2F%2BhfbUW08CkEQZSgm3wvQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst II
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4D0BAQEtonVHDHqAZQ/company-logo_100_100/company-logo_100_100/0/1639415775313/kforce_logo?e=2147483647&amp;v=beta&amp;t=NL8XuPikJ6Xfi1MKQk9TVePX6KdLB4m5KQFZdiHD8IA" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst II
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/kforce?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Kforce Inc
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Mountain View, CA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319172017" data-impression-id="jobs-search-desktop-25" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="KIt6ieSLD4hAOjugAhHmsg==" data-column="1" data-row="26">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aaratech-4319172017?position=26&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=KIt6ieSLD4hAOjugAhHmsg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQHa_a_VlxuW4A/company-logo_100_100/company-logo_100_100/0/1736445912510?e=2147483647&amp;v=beta&amp;t=W5mlp-Y_2InApg4L2Npkvtarkp9vX-8tzA2GO6I8iPE" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aaratechinc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            AARATECH
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Greater Chicago Area
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      18 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331830620" data-impression-id="jobs-search-desktop-26" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="SNLJJ31T4DcbgD0P6+vYLw==" data-column="1" data-row="27">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331830620?position=27&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=SNLJJ31T4DcbgD0P6%2BvYLw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Texas, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331847694" data-impression-id="jobs-search-desktop-27" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="jdsJ1BP3Yky+Rh6qIPZ43A==" data-column="1" data-row="28">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331847694?position=28&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=jdsJ1BP3Yky%2BRh6qIPZ43A%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331362381" data-impression-id="jobs-search-desktop-28" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="12oZ8bOGaKpQflBXWr7xQQ==" data-column="1" data-row="29">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aditi-consulting-4331362381?position=29&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=12oZ8bOGaKpQflBXWr7xQQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C560BAQFhSuWL16cn7A/company-logo_100_100/company-logo_100_100/0/1655498607143/aditiconsulting_logo?e=2147483647&amp;v=beta&amp;t=It4-tJV5B__QI2CpigNjluWwi6a7TieFq3intjkuAoA" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aditiconsulting?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Aditi Consulting
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            San Francisco, CA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-25">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4318087637" data-impression-id="jobs-search-desktop-29" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="4gHMn1qXVtv125iDq2ZZmg==" data-column="1" data-row="30">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-sunderstorm-inc-4318087637?position=30&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=4gHMn1qXVtv125iDq2ZZmg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C560BAQHi55cDD-uFUw/company-logo_100_100/company-logo_100_100/0/1630614921771/sunderstorm_logo?e=2147483647&amp;v=beta&amp;t=6zgMr3FZp3WEU4VeLVavgFqESo_6Ep-73Z4Ucr3EZm4" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/sunderstorm?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Sunderstorm Inc.
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Los Angeles, CA
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/a0d85elrpgg38lskvq1kvzb3" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Medical insurance
             +4&nbsp;benefits
        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      12 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4319122798" data-impression-id="jobs-search-desktop-30" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="GkPdr4K2CnbwgY20KnLk+g==" data-column="1" data-row="31">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-aaratech-4319122798?position=31&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=GkPdr4K2CnbwgY20KnLk%2Bg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D560BAQHa_a_VlxuW4A/company-logo_100_100/company-logo_100_100/0/1736445912510?e=2147483647&amp;v=beta&amp;t=W5mlp-Y_2InApg4L2Npkvtarkp9vX-8tzA2GO6I8iPE" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/aaratechinc?trk=public_jobs_jserp-result_job-search-card-subtitle">
            AARATECH
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Washington DC-Baltimore Area
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      19 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331853011" data-impression-id="jobs-search-desktop-31" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="Ymp7ZIAh3x7z1xTIAUC3OA==" data-column="1" data-row="32">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331853011?position=32&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=Ymp7ZIAh3x7z1xTIAUC3OA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Texas, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4209335393" data-impression-id="jobs-search-desktop-32" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="LIwT/aQCSYHbe1fo+SC4AA==" data-column="1" data-row="33">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-govini-4209335393?position=33&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=LIwT%2FaQCSYHbe1fo%2BSC4AA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C560BAQECNp0SwQ4fMw/company-logo_100_100/company-logo_100_100/0/1675873354237/govini_logo?e=2147483647&amp;v=beta&amp;t=ENXQOko0w-qYrdW8FjC82kJiJGQrLRVgUs3l6GZ_LrY" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/govini?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Govini
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Arlington, VA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331840577" data-impression-id="jobs-search-desktop-33" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="sLnAbDaOQdC9sLZz57PLEQ==" data-column="1" data-row="34">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331840577?position=34&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=sLnAbDaOQdC9sLZz57PLEQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4310125051" data-impression-id="jobs-search-desktop-34" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="WMY7x6V2yGqaw+4ryRH3OQ==" data-column="1" data-row="35">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-healthcare-preferred-remote-at-lensa-4310125051?position=35&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=WMY7x6V2yGqaw%2B4ryRH3OQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst (Healthcare Preferred) - Remote
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4D0BAQEkHa-0Aki9XQ/company-logo_100_100/B4DZaKylu7GsAQ-/0/1746085240184/lensa_logo?e=2147483647&amp;v=beta&amp;t=vxuqQreX_wx1J2lugCeUKuGGZtbGyjhRRFeWyrBMnFQ" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst (Healthcare Preferred) - Remote
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/lensa?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Lensa
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4318613264" data-impression-id="jobs-search-desktop-35" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="58WsYnOgbll7k++8nREDTw==" data-column="1" data-row="36">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-ubs-4318613264?position=36&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=58WsYnOgbll7k%2B%2B8nREDTw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C560BAQEshkSDzwMJ4g/company-logo_100_100/company-logo_100_100/0/1630584313976/ubs_logo?e=2147483647&amp;v=beta&amp;t=SZvIblKcvXSWhllPIuz-m1f4hUwFscfZ-QKdShtwMFI" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://ch.linkedin.com/company/ubs?trk=public_jobs_jserp-result_job-search-card-subtitle">
            UBS
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Raleigh, NC
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331824529" data-impression-id="jobs-search-desktop-36" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="KPtkMdw1B/55hl0tVJdopg==" data-column="1" data-row="37">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-emk-consultoria-4331824529?position=37&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=KPtkMdw1B%2F55hl0tVJdopg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      2 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332320961" data-impression-id="jobs-search-desktop-37" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="j63gmdjnisRKiEaM53k5HA==" data-column="1" data-row="38">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-rexel-usa-4332320961?position=38&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=j63gmdjnisRKiEaM53k5HA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQHb3Zrhg4pgeQ/company-logo_100_100/B4EZne5tOYKgAQ-/0/1760381293743/rexelusa_logo?e=2147483647&amp;v=beta&amp;t=7aX8rvMCboUREtcTXxRQXnr9qPWKsO2SNZe2hAoJN8s" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/rexelusa?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Rexel USA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Carrollton, TX
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-28">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4318060565" data-impression-id="jobs-search-desktop-38" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="YidS2kykrIRQFOGK4Uuu+g==" data-column="1" data-row="39">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-powerfront-4318060565?position=39&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=YidS2kykrIRQFOGK4Uuu%2Bg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4E0BAQGRtYWEHTtWCw/company-logo_100_100/company-logo_100_100/0/1653581944539/powerfront_logo?e=2147483647&amp;v=beta&amp;t=2lxtzzfz-BJCBFUSJ2KOeHOj5UluQf4fmKmLY03hvQQ" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/powerfront?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Powerfront
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Nevada, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/a0d85elrpgg38lskvq1kvzb3" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Medical insurance
             +3&nbsp;benefits
        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      16 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4318308045" data-impression-id="jobs-search-desktop-39" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="hBGJ9rNgOANFGkZTISuzUA==" data-column="1" data-row="40">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-impetusit-4318308045?position=40&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=hBGJ9rNgOANFGkZTISuzUA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/C4E0BAQGw27X_Tw38gw/company-logo_100_100/company-logo_100_100/0/1630630668960/impetusit_logo?e=2147483647&amp;v=beta&amp;t=waPgoyG6aR6WQAdyLrY2bZw9Ro4SnLG2o6Zaz3c9olA" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/impetusit?trk=public_jobs_jserp-result_job-search-card-subtitle">
            ImpetusIT
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Minneapolis, MN
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      4 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331828405" data-impression-id="jobs-search-desktop-40" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="afckG5PVtsLewgAmdb7Y6g==" data-column="1" data-row="41">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331828405?position=41&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=afckG5PVtsLewgAmdb7Y6g%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      2 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331851426" data-impression-id="jobs-search-desktop-41" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="ji436DsotuEJoqpM6zUrLg==" data-column="1" data-row="42">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331851426?position=42&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=ji436DsotuEJoqpM6zUrLg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst - Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst - Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332005751" data-impression-id="jobs-search-desktop-42" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="1p7rsA32HPhyfGniLq0N4Q==" data-column="1" data-row="43">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332005751?position=43&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=1p7rsA32HPhyfGniLq0N4Q%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Texas, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332014243" data-impression-id="jobs-search-desktop-43" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="P34m4f14Pv4wqu813ySFhA==" data-column="1" data-row="44">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-emk-consultoria-4332014243?position=44&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=P34m4f14Pv4wqu813ySFhA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331851384" data-impression-id="jobs-search-desktop-44" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="QnoW7upDlNUS9sfbxf5K+g==" data-column="1" data-row="45">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331851384?position=45&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=QnoW7upDlNUS9sfbxf5K%2Bg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst - Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst - Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332023050" data-impression-id="jobs-search-desktop-45" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="xnpf/iAjC5AZXYYYhs16Ow==" data-column="1" data-row="46">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332023050?position=46&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=xnpf%2FiAjC5AZXYYYhs16Ow%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331842741" data-impression-id="jobs-search-desktop-46" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="/5ea9k7vtyGSnQBoR8BnaA==" data-column="1" data-row="47">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-emk-consultoria-4331842741?position=47&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=%2F5ea9k7vtyGSnQBoR8BnaA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332009514" data-impression-id="jobs-search-desktop-47" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="L//P3biAk2N7MSHzWLp7Eg==" data-column="1" data-row="48">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-emk-consultoria-4332009514?position=48&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=L%2F%2FP3biAk2N7MSHzWLp7Eg%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332002575" data-impression-id="jobs-search-desktop-48" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="ehjBoyGHFZk2D/ssT27F7A==" data-column="1" data-row="49">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332002575?position=49&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=ehjBoyGHFZk2D%2FssT27F7A%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4323994430" data-impression-id="jobs-search-desktop-49" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="9TSvmEhuEEUZySiS2ElwaQ==" data-column="1" data-row="50">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-intern-at-lensa-4323994430?position=50&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=9TSvmEhuEEUZySiS2ElwaQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst Intern
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4D0BAQEkHa-0Aki9XQ/company-logo_100_100/B4DZaKylu7GsAQ-/0/1746085240184/lensa_logo?e=2147483647&amp;v=beta&amp;t=vxuqQreX_wx1J2lugCeUKuGGZtbGyjhRRFeWyrBMnFQ" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst Intern
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/lensa?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Lensa
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Atlanta, GA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      4 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4318073320" data-impression-id="jobs-search-desktop-50" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="pJLj4Mku651BCH1xY5rAFA==" data-column="1" data-row="51">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-air-apps-4318073320?position=51&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=pJLj4Mku651BCH1xY5rAFA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4D0BAQGsf8xDO35hvA/company-logo_100_100/company-logo_100_100/0/1707529392169/airapps_logo?e=2147483647&amp;v=beta&amp;t=pMhs74F1luDbY0hRBDh8Yw5UXFvAkDVGaWe6yo1ra88" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/airapps?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Air Apps
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            San Francisco, CA
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      14 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332009356" data-impression-id="jobs-search-desktop-51" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="iZwNiSHNbYNWXvEa0ajfrQ==" data-column="1" data-row="52">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332009356?position=52&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=iZwNiSHNbYNWXvEa0ajfrQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331842553" data-impression-id="jobs-search-desktop-52" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="JwX7Jf4RCnS95T9bvb97fw==" data-column="1" data-row="53">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331842553?position=53&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=JwX7Jf4RCnS95T9bvb97fw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst - Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst - Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331316745" data-impression-id="jobs-search-desktop-53" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="hN6aelpT7eThyLradnEq4w==" data-column="1" data-row="54">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-motion-recruitment-4331316745?position=54&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=hN6aelpT7eThyLradnEq4w%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          " data-delayed-url="https://media.licdn.com/dms/image/v2/D4E0BAQEOI9UbrI7HpA/company-logo_100_100/company-logo_100_100/0/1736875834564/motion_recruitment_partners_logo?e=2147483647&amp;v=beta&amp;t=cAJhKf-ksoMCYg-vgX8pSr-XEHDZCLymI7uO2Tpn0Uk" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/motion-recruitment-partners?trk=public_jobs_jserp-result_job-search-card-subtitle">
            Motion Recruitment
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            Santa Monica, CA
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/813wpbk0cze9hmkln1auifzbd" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          401(k)
             +2&nbsp;benefits
        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-24">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      3 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331845613" data-impression-id="jobs-search-desktop-54" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="oX7+DzTFw3u0cytXmcwUNw==" data-column="1" data-row="55">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331845613?position=55&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=oX7%2BDzTFw3u0cytXmcwUNw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst - Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst - Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332019532" data-impression-id="jobs-search-desktop-55" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="FZOAYe1nNdIi9YWUJBmS0w==" data-column="1" data-row="56">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/data-analyst-at-emk-consultoria-4332019532?position=56&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=FZOAYe1nNdIi9YWUJBmS0w%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Data Analyst
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Data Analyst
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            California, United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4331814802" data-impression-id="jobs-search-desktop-56" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="ePc2LBHFvTgNmOK8x9ONVw==" data-column="1" data-row="57">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4331814802?position=57&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=ePc2LBHFvTgNmOK8x9ONVw%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-26">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      2 days ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332017389" data-impression-id="jobs-search-desktop-57" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="GbGAba5NLjA6pNoNqePlbQ==" data-column="1" data-row="58">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332017389?position=58&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=GbGAba5NLjA6pNoNqePlbQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

<!---->  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332015183" data-impression-id="jobs-search-desktop-58" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="u7UZfbmt98z2dNYUI0aJQQ==" data-column="1" data-row="59">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332015183?position=59&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=u7UZfbmt98z2dNYUI0aJQQ%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      1 day ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
                <li>
                  
  
    

    
    
    
      <div class="base-card relative w-full hover:no-underline focus:no-underline
        base-card--link
         base-search-card base-search-card--link job-search-card" data-entity-urn="urn:li:jobPosting:4332010595" data-impression-id="jobs-search-desktop-59" data-reference-id="DDdnuKLvZknVutnJguZdFQ==" data-tracking-id="bkyWg7t9TEX8vy41+Nd7NA==" data-column="1" data-row="60">
        

        <a class="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]" href="https://www.linkedin.com/jobs/view/virtual-data-analyst-full-time-100%25-remote-at-emk-consultoria-4332010595?position=60&amp;pageNum=0&amp;refId=DDdnuKLvZknVutnJguZdFQ%3D%3D&amp;trackingId=bkyWg7t9TEX8vy41%2BNd7NA%3D%3D" data-tracking-control-name="public_jobs_jserp-result_search-card" data-tracking-client-ingraph data-tracking-will-navigate>
          
          <span class="sr-only">
              
        
        Virtual Data Analyst Full Time (100% Remote)
      
      
          </span>
        </a>

      
        
    <div class="search-entity-media">
        
      <img class="artdeco-entity-image artdeco-entity-image--square-4
          artdeco-entity-image--ghost" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" data-ghost-classes="artdeco-entity-image--ghost" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/6puxblwmhnodu6fjircz4dn4h" alt>
  
    </div>
  

        <div class="base-search-card__info">
          <h3 class="base-search-card__title">
            
        Virtual Data Analyst Full Time (100% Remote)
      
          </h3>

            <h4 class="base-search-card__subtitle">
              
          <a class="hidden-nested-link" data-tracking-client-ingraph data-tracking-control-name="public_jobs_jserp-result_job-search-card-subtitle" data-tracking-will-navigate href="https://www.linkedin.com/company/emk-consultoria?trk=public_jobs_jserp-result_job-search-card-subtitle">
            EMK CONSULTORIA
          </a>
      
            </h4>

<!---->
            <div class="base-search-card__metadata">
              
          <span class="job-search-card__location">
            United States
          </span>

        
    
    
    
    

      <div class="job-posting-benefits text-sm">
        <icon class="job-posting-benefits__icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8zmuwb93gzlb935fk4ao4z779" data-svg-class-name="job-posting-benefits__icon-svg"></icon>
        <span class="job-posting-benefits__text">
          Be an early applicant
<!---->        </span>
      </div>
  

          <time class="job-search-card__listdate--new" datetime="2025-10-27">
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

      23 hours ago
  
          </time>

<!---->      
            </div>
        </div>
<!---->      
    
      </div>
  
  
  
  

                </li>
            </ul>

            
    
    

    

    
    <div class="loader">
      <div class="loader__container mb-2 overflow-hidden">
        <icon class="loader__icon inline-block loader__icon--default text-color-progress-loading" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/ddi43qwelxeqjxdd45pe3fvs1" data-svg-class-name="loader__icon-svg--small fill-currentColor h-[30px] min-h-[30px] w-[30px] min-w-[30px]"></icon>
      </div>
    </div>
  

      <button aria-label="See more jobs" class="infinite-scroller__show-more-button" data-tracking-control-name="infinite-scroller_show-more">

          
                See more jobs
              
      </button>
  

            
    <div class="px-1.5 flex inline-notification hidden text-color-signal-positive see-more-jobs__viewed-all" role="alert" type="success">
      <icon class="inline-notification__icon w-[20px] h-[20px] shrink-0 mr-[10px] inline-block" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/9zhm3eh2dq7vh2muo8xnfikxh"></icon>
      <p class="inline-notification__text text-sm leading-regular">
        You&#39;ve viewed all jobs for this search
<!---->      </p>
    </div>
  

          
    

      <section class="similar-titles">
        <h3 class="similar-titles__heading">
          Search similar titles
        </h3>

        <ul class="similar-titles__list">
            <li class="similar-titles__title">
              <a class="similar-titles__link" data-tracking-control-name="public_jobs_similar-title" data-tracking-will-navigate href="https://www.linkedin.com/jobs/analyst-jobs?trk=public_jobs_similar-title">
                Analyst jobs
              </a>
            </li>
            <li class="similar-titles__title">
              <a class="similar-titles__link" data-tracking-control-name="public_jobs_similar-title" data-tracking-will-navigate href="https://www.linkedin.com/jobs/skagit-county-jobs?trk=public_jobs_similar-title">
                Skagit County jobs
              </a>
            </li>
            <li class="similar-titles__title">
              <a class="similar-titles__link" data-tracking-control-name="public_jobs_similar-title" data-tracking-will-navigate href="https://www.linkedin.com/jobs/data-science-specialist-jobs?trk=public_jobs_similar-title">
                Data Science Specialist jobs
              </a>
            </li>
        </ul>
      </section>
  
      
            </section>
        </main>
        <section class="two-pane-serp-page__detail-view">
          
        <div class="details-pane__loader details-pane__loader--hide">
          
    <div class="loader">
      <div class="loader__container mb-2 overflow-hidden">
        <icon class="loader__icon inline-block loader__icon--default text-color-progress-loading" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/ddi43qwelxeqjxdd45pe3fvs1" data-svg-class-name="loader__icon-svg--large fill-currentColor h-[60px] min-h-[60px] w-[60px] min-w-[60px]"></icon>
      </div>
    </div>
  
        </div>
        <div class="details-pane__content"></div>
      
        </section>
      
      </div>

      
        
        
      <section class="related-jserps">
        
    

    <section class="tw-expandable-linkster" data-js-module-id="expandable-linkster">
      
    
    

      <div class="show-more-less">
            <button class="show-more-less__button show-more-less__more-button show-more-less-button
                " aria-expanded="false" data-tracking-control-name="public_jobs_show_more">
                
          
            More searches
        
              <icon class="show-more-less__button--chevron show-more-less-button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cyolgscd0imw2ldqppkrb84vo"></icon>
            </button>

            <button class="show-more-less__button show-more-less__less-button show-more-less-button
                show-more-less__button--hide" aria-expanded="false" data-tracking-control-name="public_jobs_show_more">
                
          
            More searches
        
              <icon class="show-more-less__button--chevron show-more-less-button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/4chtt12k98xwnba1nimld2oyg"></icon>
            </button>

        <ul data-max-num-to-show="0" class="show-more-less__list show-more-less__list--hide-after-0" data-impression-id="public_jobs_show-more-less">
          
          
            <li>
              
    <section class="tw-linkster " data-impression-id="public_jobs_linkster" data-module-name="jserp_links" data-js-module-id="linkster">
      <div class="max-w-screen-content-max-w w-full flex justify-between my-0 mx-auto mamabear:px-3 babybear:px-2 babybear:flex-col">
            

    

      <div class="flex-1 w-1/2 pt-2 pr-4 pb-4 pl-0 babybear:pb-2 babybear:w-full babybear:border-b-1 babybear:border-solid babybear:border-color-border-low-emphasis babybear:last:border-b-0">
<!---->        <ul class="my-1">
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/skagit-county-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Skagit County jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-science-specialist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Science Specialist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-scientist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Scientist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-intelligence-intern-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Intelligence Intern jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/startups%2Ecom-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Startups.com jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-assistant-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Assistant jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/clinical-data-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Clinical Data Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-intelligence-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Intelligence Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-intelligence-developer-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Intelligence Developer jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/junior-scientist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Junior Scientist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-engineer-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Engineer jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/boerne-isd-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Boerne ISD jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/scientist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Scientist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/web-marketing-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Web Marketing Analyst jobs
              </a>
            </li>
        </ul>

<!---->      </div>
  
            

    

      <div class="flex-1 w-1/2 pt-2 pr-4 pb-4 pl-0 babybear:pb-2 babybear:w-full babybear:border-b-1 babybear:border-solid babybear:border-color-border-low-emphasis babybear:last:border-b-0">
<!---->        <ul class="my-1">
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/senior-data-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Senior Data Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-data-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Data Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/analyst-internship-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Analyst Internship jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-analyst-intern-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Analyst Intern jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/marketing-data-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Marketing Data Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-intelligence-specialist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Intelligence Specialist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/senior-integration-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Senior Integration Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/sql-developer-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                SQL Developer jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/financial-services-officer-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Financial Services Officer jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/financial-data-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Financial Data Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/staff-chemist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Staff Chemist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/reachire-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                reacHIRE jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/healthcare-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Healthcare Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-reporting-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Reporting Analyst jobs
              </a>
            </li>
        </ul>

<!---->      </div>
  
            

    

      <div class="flex-1 w-1/2 pt-2 pr-4 pb-4 pl-0 babybear:pb-2 babybear:w-full babybear:border-b-1 babybear:border-solid babybear:border-color-border-low-emphasis babybear:last:border-b-0">
<!---->        <ul class="my-1">
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-specialist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Specialist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-research-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Research Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/peoplesoft-financial-consultant-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Peoplesoft Financial Consultant jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-quality-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Quality Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-conversion-specialist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Conversion Specialist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/director-of-student-financial-services-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Director of Student Financial Services jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/lead-data-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Lead Data Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/providence-health-plan-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Providence Health Plan jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/samaritan-hospital-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Samaritan Hospital jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/mail-administrator-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Mail Administrator jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/insurance-counselor-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Insurance Counselor jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/bureau-of-economic-analysis-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Bureau of Economic Analysis jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-intelligence-engineer-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Intelligence Engineer jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/development-database-administrator-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Development Database Administrator jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/biostatistician-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Biostatistician jobs
              </a>
            </li>
        </ul>

<!---->      </div>
  
            

    

      <div class="flex-1 w-1/2 pt-2 pr-4 pb-4 pl-0 babybear:pb-2 babybear:w-full babybear:border-b-1 babybear:border-solid babybear:border-color-border-low-emphasis babybear:last:border-b-0">
<!---->        <ul class="my-1">
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/statistical-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Statistical Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-associate-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Associate jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/graduate-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Graduate Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/statistician-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Statistician jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/optima-health-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Optima Health jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/payroll-tax-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Payroll Tax Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-system-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data System Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-processing-specialist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Processing Specialist jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/junior-business-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Junior Business Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/junior-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Junior Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/business-intelligence-consultant-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Business Intelligence Consultant jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/report-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Report Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-consultant-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Consultant jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/web-analyst-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Web Analyst jobs
              </a>
            </li>
            <li class="tw-link-column-item">
              
              
              <a class="link tw-linkster-link" href="https://www.linkedin.com/jobs/data-mining-specialist-jobs?trk=public_jobs_linkster_link" data-js-module-id="link-column-link" data-tracking-control-name="public_jobs_linkster_link" data-tracking-will-navigate>
                Data Mining Specialist jobs
              </a>
            </li>
        </ul>

<!---->      </div>
  
      </div>
    </section>
  
            </li>
        
        </ul>

<!---->      </div>
  
    </section>
  
      </section>
  
      
      

      

    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    

    
    
    
    

    <footer class="li-footer bg-transparent w-full ">
      <ul class="li-footer__list flex flex-wrap flex-row items-start justify-start w-full h-auto min-h-[50px] my-[0px] mx-auto py-3 px-2 papabear:p-0">
        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        
          <span class="sr-only">LinkedIn</span>
          <icon class="li-footer__copy-logo text-color-logo-brand-alt inline-block self-center h-[14px] w-[56px] mr-1" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/5mebydpuuijm3uhv1q375inqh"></icon>
          <span class="li-footer__copy-text flex items-center">&copy; 2025</span>
        
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://about.linkedin.com?trk=public_jobs_footer-about" data-tracking-control-name="public_jobs_footer-about" data-tracking-will-navigate>
          
          About
        
        </a>
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/accessibility?trk=public_jobs_footer-accessibility" data-tracking-control-name="public_jobs_footer-accessibility" data-tracking-will-navigate>
          
          Accessibility
        
        </a>
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/legal/user-agreement?trk=public_jobs_footer-user-agreement" data-tracking-control-name="public_jobs_footer-user-agreement" data-tracking-will-navigate>
          
          User Agreement
        
        </a>
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/legal/privacy-policy?trk=public_jobs_footer-privacy-policy" data-tracking-control-name="public_jobs_footer-privacy-policy" data-tracking-will-navigate>
          
          Privacy Policy
        
        </a>
  </li>

<!---->        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/legal/cookie-policy?trk=public_jobs_footer-cookie-policy" data-tracking-control-name="public_jobs_footer-cookie-policy" data-tracking-will-navigate>
          
          Cookie Policy
        
        </a>
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/legal/copyright-policy?trk=public_jobs_footer-copyright-policy" data-tracking-control-name="public_jobs_footer-copyright-policy" data-tracking-will-navigate>
          
          Copyright Policy
        
        </a>
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://brand.linkedin.com/policies?trk=public_jobs_footer-brand-policy" data-tracking-control-name="public_jobs_footer-brand-policy" data-tracking-will-navigate>
          
          Brand Policy
        
        </a>
  </li>

          
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/psettings/guest-controls?trk=public_jobs_footer-guest-controls" data-tracking-control-name="public_jobs_footer-guest-controls" data-tracking-will-navigate>
          
            Guest Controls
          
        </a>
  </li>

        
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        <a class="li-footer__item-link flex items-center font-sans text-xs font-bold text-color-text-solid-secondary hover:text-color-link-hover focus:text-color-link-focus" href="https://www.linkedin.com/legal/professional-community-policies?trk=public_jobs_footer-community-guide" data-tracking-control-name="public_jobs_footer-community-guide" data-tracking-will-navigate>
          
          Community Guidelines
        
        </a>
  </li>

        
<!---->
          
          
  <li class="li-footer__item font-sans text-xs text-color-text-solid-secondary flex flex-shrink-0 justify-start p-1 relative w-50% papabear:justify-center papabear:w-auto">
        
              

    
    

    

    

    <div class="collapsible-dropdown collapsible-dropdown--footer collapsible-dropdown--up flex items-center relative hyphens-auto language-selector z-2">
<!---->
        <ul class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-[9999] bottom-[100%] top-auto" role="menu" tabindex="-1">
          
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="العربية (Arabic)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-ar_AE" data-locale="ar_AE" role="menuitem" lang="ar_AE">
                العربية (Arabic)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="বাংলা (Bangla)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-bn_IN" data-locale="bn_IN" role="menuitem" lang="bn_IN">
                বাংলা (Bangla)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Čeština (Czech)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-cs_CZ" data-locale="cs_CZ" role="menuitem" lang="cs_CZ">
                Čeština (Czech)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Dansk (Danish)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-da_DK" data-locale="da_DK" role="menuitem" lang="da_DK">
                Dansk (Danish)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Deutsch (German)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-de_DE" data-locale="de_DE" role="menuitem" lang="de_DE">
                Deutsch (German)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Ελληνικά (Greek)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-el_GR" data-locale="el_GR" role="menuitem" lang="el_GR">
                Ελληνικά (Greek)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="English (English) selected" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link--selected" data-tracking-control-name="language-selector-en_US" data-locale="en_US" role="menuitem" lang="en_US">
                <strong>English (English)</strong>
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Español (Spanish)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-es_ES" data-locale="es_ES" role="menuitem" lang="es_ES">
                Español (Spanish)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="فارسی (Persian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-fa_IR" data-locale="fa_IR" role="menuitem" lang="fa_IR">
                فارسی (Persian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Suomi (Finnish)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-fi_FI" data-locale="fi_FI" role="menuitem" lang="fi_FI">
                Suomi (Finnish)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Français (French)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-fr_FR" data-locale="fr_FR" role="menuitem" lang="fr_FR">
                Français (French)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="हिंदी (Hindi)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-hi_IN" data-locale="hi_IN" role="menuitem" lang="hi_IN">
                हिंदी (Hindi)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Magyar (Hungarian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-hu_HU" data-locale="hu_HU" role="menuitem" lang="hu_HU">
                Magyar (Hungarian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Bahasa Indonesia (Indonesian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-in_ID" data-locale="in_ID" role="menuitem" lang="in_ID">
                Bahasa Indonesia (Indonesian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Italiano (Italian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-it_IT" data-locale="it_IT" role="menuitem" lang="it_IT">
                Italiano (Italian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="עברית (Hebrew)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-iw_IL" data-locale="iw_IL" role="menuitem" lang="iw_IL">
                עברית (Hebrew)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="日本語 (Japanese)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-ja_JP" data-locale="ja_JP" role="menuitem" lang="ja_JP">
                日本語 (Japanese)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="한국어 (Korean)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-ko_KR" data-locale="ko_KR" role="menuitem" lang="ko_KR">
                한국어 (Korean)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="मराठी (Marathi)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-mr_IN" data-locale="mr_IN" role="menuitem" lang="mr_IN">
                मराठी (Marathi)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Bahasa Malaysia (Malay)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-ms_MY" data-locale="ms_MY" role="menuitem" lang="ms_MY">
                Bahasa Malaysia (Malay)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Nederlands (Dutch)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-nl_NL" data-locale="nl_NL" role="menuitem" lang="nl_NL">
                Nederlands (Dutch)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Norsk (Norwegian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-no_NO" data-locale="no_NO" role="menuitem" lang="no_NO">
                Norsk (Norwegian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="ਪੰਜਾਬੀ (Punjabi)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-pa_IN" data-locale="pa_IN" role="menuitem" lang="pa_IN">
                ਪੰਜਾਬੀ (Punjabi)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Polski (Polish)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-pl_PL" data-locale="pl_PL" role="menuitem" lang="pl_PL">
                Polski (Polish)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Português (Portuguese)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-pt_BR" data-locale="pt_BR" role="menuitem" lang="pt_BR">
                Português (Portuguese)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Română (Romanian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-ro_RO" data-locale="ro_RO" role="menuitem" lang="ro_RO">
                Română (Romanian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Русский (Russian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-ru_RU" data-locale="ru_RU" role="menuitem" lang="ru_RU">
                Русский (Russian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Svenska (Swedish)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-sv_SE" data-locale="sv_SE" role="menuitem" lang="sv_SE">
                Svenska (Swedish)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="తెలుగు (Telugu)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-te_IN" data-locale="te_IN" role="menuitem" lang="te_IN">
                తెలుగు (Telugu)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="ภาษาไทย (Thai)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-th_TH" data-locale="th_TH" role="menuitem" lang="th_TH">
                ภาษาไทย (Thai)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Tagalog (Tagalog)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-tl_PH" data-locale="tl_PH" role="menuitem" lang="tl_PH">
                Tagalog (Tagalog)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Türkçe (Turkish)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-tr_TR" data-locale="tr_TR" role="menuitem" lang="tr_TR">
                Türkçe (Turkish)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Українська (Ukrainian)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-uk_UA" data-locale="uk_UA" role="menuitem" lang="uk_UA">
                Українська (Ukrainian)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="Tiếng Việt (Vietnamese)" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-vi_VN" data-locale="vi_VN" role="menuitem" lang="vi_VN">
                Tiếng Việt (Vietnamese)
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="简体中文 (Chinese (Simplified))" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-zh_CN" data-locale="zh_CN" role="menuitem" lang="zh_CN">
                简体中文 (Chinese (Simplified))
            </button>
          </li>
          <li class="language-selector__item" role="presentation">
            <!-- Adding aria-label to both the li and the button because screen reader focus goes to button on desktop and li on mobile-->
            <button aria-label="正體中文 (Chinese (Traditional))" class="font-sans text-xs link block py-[5px] px-2 w-full hover:cursor-pointer hover:bg-color-action hover:text-color-text-on-dark focus:bg-color-action focus:text-color-text-on-dark
                language-selector__link !font-regular" data-tracking-control-name="language-selector-zh_TW" data-locale="zh_TW" role="menuitem" lang="zh_TW">
                正體中文 (Chinese (Traditional))
            </button>
          </li>
<!---->      
        </ul>

          
        <button class="language-selector__button select-none relative pr-2 font-sans text-xs font-bold text-color-text-low-emphasis hover:text-color-link-hover hover:cursor-pointer focus:text-color-link-focus focus:outline-dotted focus:outline-1" aria-expanded="false" data-tracking-control-name="footer-lang-dropdown_trigger">
          <span class="language-selector__label-text mr-0.5 break-words">
            Language
          </span>
          <icon class="language-selector__label-chevron w-2 h-2 absolute top-0 right-0" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cyolgscd0imw2ldqppkrb84vo"></icon>
        </button>
      
    </div>
  
  
          
  </li>

      </ul>

<!---->    </footer>
  
    </div>
  
  
  




          
    <div class="guest-upsells">
        
    
    
    
    <form class="google-auth base-google-auth" action="https://www.linkedin.com/uas/login-submit" method="post">
      <input name="loginCsrfParam" value="62261486-b63d-497c-8ff0-d0a2fc17c1f0" type="hidden">
        <input name="session_redirect" value="https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&amp;location=United%20States&amp;geoId=&amp;trk=public_jobs_jobs-search-bar_search-submit&amp;original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DUnited%2520States%26geoId%3D103644278%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26position%3D1%26pageNum%3D0&amp;position=1&amp;pageNum=0" type="hidden">
      <input name="trk" value="public_jobs_google-one-tap-submit" type="hidden">
        <div class="google-one-tap__module hidden fixed flex flex-col items-center top-[20px] right-[20px] z-[9999]">
          <div class="google-auth__tnc-container hidden relative top-2 bg-color-background-container-tint pl-2 pr-1 pt-2 pb-3 w-[375px] rounded-md shadow-2xl">
            <p class="text-md font-bold text-color-text">
              Agree & Join LinkedIn
            </p>
            
    
    
    <p class="linkedin-tc__text text-color-text-low-emphasis text-xs pb-2 !text-sm !text-color-text" data-impression-id="public_jobs_one-tap-skip-tc-text">
      By clicking Continue to join or sign in, you agree to LinkedIn’s <a href="/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement" target="_blank" data-tracking-control-name="linkedin-tc_auth-button_user-agreement" data-tracking-will-navigate="true">User Agreement</a>, <a href="/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy" target="_blank" data-tracking-control-name="linkedin-tc_auth-button_privacy-policy" data-tracking-will-navigate="true">Privacy Policy</a>, and <a href="/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy" target="_blank" data-tracking-control-name="linkedin-tc_auth-button_cookie-policy" data-tracking-will-navigate="true">Cookie Policy</a>.
    </p>
  
          </div>
          <div data-tracking-control-name="public_jobs_google-one-tap" id="google-one-tap__container"></div>
        </div>
      
    <div class="loader loader--full-screen">
      <div class="loader__container mb-2 overflow-hidden">
        <icon class="loader__icon inline-block loader__icon--default text-color-progress-loading" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/ddi43qwelxeqjxdd45pe3fvs1" data-svg-class-name="loader__icon-svg--large fill-currentColor h-[60px] min-h-[60px] w-[60px] min-w-[60px]"></icon>
      </div>
    </div>
  
    </form>
    <script data-delayed-url="https://static.licdn.com/aero-v1/sc/h/29rdkxlvag0d3cpj96fiilbju" data-module-id="google-gsi-lib"></script>
    <code id="isLinkedInAppWebView" style="display: none"><!--false--></code>
    <code id="shouldRemoveUndefinedValues" style="display: none"><!--false--></code>
    <code id="isItpSupportEnabled" style="display: none"><!--false--></code>
    <code id="tncFlow" style="display: none"><!--"control"--></code>
      <code id="isGoogleAuthButtonLocaleSupportEnabled" style="display: none"><!--true--></code>
      <code id="gsiLocale" style="display: none"><!--"en_US"--></code>
  

        
    
    
    
    
    
    

    <div class="contextual-sign-in-modal base-contextual-sign-in-modal" data-impression-id="public_jobs_contextual-sign-in-modal" data-cool-off-enabled data-show-on-page-load>
<!---->
        

    
    <div class>
<!---->
      <div id="base-contextual-sign-in-modal" class="modal modal--contextual-sign-in" data-outlet="base-contextual-sign-in-modal">
<!---->        <div class="modal__overlay flex items-center bg-color-background-scrim justify-center fixed bottom-0 left-0 right-0 top-0 opacity-0 invisible pointer-events-none z-[1000] transition-[opacity] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.17s]
            py-4
            " aria-hidden="true">
          <section aria-modal="true" role="dialog" aria-labelledby="base-contextual-sign-in-modal-modal-header" tabindex="-1" class="max-h-full modal__wrapper overflow-auto p-0 bg-color-surface max-w-[1128px] min-h-[160px] relative scale-[0.25] shadow-sm shadow-color-border-faint transition-[transform] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.33s] focus:outline-0
              
              w-[1128px] mamabear:w-[744px] babybear:w-[360px]
              
              rounded-md">
              
              <button class="modal__dismiss btn-tertiary h-[40px] w-[40px] p-0 rounded-full indent-0
                  contextual-sign-in-modal__modal-dismiss absolute right-0 m-[20px] cursor-pointer" aria-label="Dismiss" data-tracking-control-name="public_jobs_contextual-sign-in-modal_modal_dismiss">
                <icon class="contextual-sign-in-modal__modal-dismiss-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/gs508lg3t2o81tq7pmcgn6m2"></icon>
              </button>
          
            <div class="modal__main w-full">
              
              <div class="contextual-sign-in-modal__screen contextual-sign-in-modal__context-screen flex flex-col my-4 mx-3">
                  
                  
      <img class="inline-block relative
          
          w-16 h-16
           contextual-sign-in-modal__img m-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/7e5r1tyag1womwdkqzon9r2ib" data-ghost-classes="bg-color-entity-ghost-background" data-ghost-url="https://static.licdn.com/aero-v1/sc/h/cs8pjfgyw96g44ln9r7tct85f" alt>
      
                <h2 class="contextual-sign-in-modal__context-screen-title font-bold font-sans text-xl text-color-text my-2 mx-4 text-center" id="base-contextual-sign-in-modal-modal-header">
                  Sign in to view more jobs
                </h2>
<!----><!---->                <div class="contextual-sign-in-modal__btn-container m-auto w-[320px] babybear:w-full">
<!---->                  
    
                        <div class="w-full max-w-[400px] mx-auto">
                          
    

    <div class="google-auth-button">
<!---->      <div class="google-auth-button__placeholder mx-auto
          " data-theme="filled_blue" data-logo-alignment="center" data-locale="en_US" role="button" aria-label="Continue with google"></div>
<!---->    </div>
  
                        </div>
                    
    
                      
    
    
    
    
    
    
    

    <div class="sign-in-modal" data-impression-id="public_jobs_contextual-sign-in-modal_sign-in-modal">
        
    
    
      
          <button class="sign-in-modal__outlet-btn cursor-pointer btn-md btn-primary btn-secondary" data-tracking-client-ingraph data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_outlet-button" data-modal="base-sign-in-modal">
<!---->              Sign in
          </button>
        
  

      

    
    <div class>
<!---->
      <div id="base-sign-in-modal" class="modal modal--sign-in" data-outlet="base-sign-in-modal">
<!---->        <div class="modal__overlay flex items-center bg-color-background-scrim justify-center fixed bottom-0 left-0 right-0 top-0 opacity-0 invisible pointer-events-none z-[1000] transition-[opacity] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.17s]
            py-4
            " aria-hidden="true">
          <section aria-modal="true" role="dialog" aria-labelledby="base-sign-in-modal-modal-header" tabindex="-1" class="max-h-full modal__wrapper overflow-auto p-0 bg-color-surface max-w-[1128px] min-h-[160px] relative scale-[0.25] shadow-sm shadow-color-border-faint transition-[transform] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.33s] focus:outline-0
              
              w-[1128px] mamabear:w-[744px] babybear:w-[360px]
              
              rounded-md">
              
            <button class="modal__dismiss btn-tertiary h-[40px] w-[40px] p-0 rounded-full indent-0 sign-in-modal__dismiss absolute right-0 cursor-pointer m-[20px]" aria-label="Dismiss" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_dismiss">
              <icon class="sign-in-modal__dismiss-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/gs508lg3t2o81tq7pmcgn6m2"></icon>
            </button>
        
            <div class="modal__main w-full">
              
          <div class="sign-in-modal__screen flex flex-col py-4 w-[513px] babybear:w-full
              px-3">
            <h2 class="sign-in-modal__header font-sans text-display-md text-color-text
                ">
                Welcome back
                          </h2>
            
    
    
    
    
    
    
    
    
    
    

    <code id="i18n_sign_in_form_show_text" style="display: none"><!--"Show"--></code>
    <code id="i18n_sign_in_form_show_label" style="display: none"><!--"Show your LinkedIn password"--></code>
    <code id="i18n_sign_in_form_hide_text" style="display: none"><!--"Hide"--></code>
    <code id="i18n_sign_in_form_hide_label" style="display: none"><!--"Hide your LinkedIn password"--></code>

    
    <code id="i18n_username_error_empty" style="display: none"><!--"Please enter an email address or phone number"--></code>
    
    <code id="i18n_username_error_too_long" style="display: none"><!--"Email or phone number must be between 3 to 128 characters"--></code>
    <code id="i18n_username_error_too_short" style="display: none"><!--"Email or phone number must be between 3 to 128 characters"--></code>

    
    <code id="i18n_password_error_empty" style="display: none"><!--"Please enter a password"--></code>
    
    <code id="i18n_password_error_too_short" style="display: none"><!--"The password you provided must have at least 6 characters"--></code>
    
    <code id="i18n_password_error_too_long" style="display: none"><!--"The password you provided must have at most 400 characters"--></code>

<!---->    <form data-id="sign-in-form" action="https://www.linkedin.com/uas/login-submit" method="post" novalidate class="mt-1.5 mb-2">
      <input name="loginCsrfParam" value="62261486-b63d-497c-8ff0-d0a2fc17c1f0" type="hidden">

      <div class="flex flex-col">
        
    <div class="mt-1.5" data-js-module-id="guest-input">
      <div class="flex flex-col">
        <label class="input-label mb-1" for="base-sign-in-modal_session_key">
          Email or phone
        </label>
        <div class="text-input flex">
          <input class="text-color-text font-sans text-md outline-0 bg-color-transparent w-full" autocomplete="username" id="base-sign-in-modal_session_key" name="session_key" required data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_sign-in-session-key" data-tracking-client-ingraph type="text">
          
        </div>
      </div>

      <p class="input-helper mt-1.5" for="base-sign-in-modal_session_key" role="alert" data-js-module-id="guest-input__message"></p>
    </div>
  

        
    <div class="mt-1.5" data-js-module-id="guest-input">
      <div class="flex flex-col">
        <label class="input-label mb-1" for="base-sign-in-modal_session_password">
          Password
        </label>
        <div class="text-input flex">
          <input class="text-color-text font-sans text-md outline-0 bg-color-transparent w-full" autocomplete="current-password" id="base-sign-in-modal_session_password" name="session_password" required data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_sign-in-password" data-tracking-client-ingraph type="password">
          
            <button aria-live="assertive" aria-relevant="text" data-id="sign-in-form__password-visibility-toggle" class="font-sans text-md font-bold text-color-action z-10 ml-[12px] hover:cursor-pointer" aria-label="Show your LinkedIn password" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_sign-in-password-visibility-toggle-btn" type="button">Show</button>
          
        </div>
      </div>

      <p class="input-helper mt-1.5" for="base-sign-in-modal_session_password" role="alert" data-js-module-id="guest-input__message"></p>
    </div>
  

        <input name="session_redirect" value="https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&amp;location=United%20States&amp;geoId=&amp;trk=public_jobs_jobs-search-bar_search-submit&amp;original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DUnited%2520States%26geoId%3D103644278%26trk%3Dpublic_jobs_jobs-search-bar_search-submit%26position%3D1%26pageNum%3D0&amp;position=1&amp;pageNum=0" type="hidden">

<!---->      </div>

      <div data-id="sign-in-form__footer" class="flex justify-between
          sign-in-form__footer--full-width">
        <a data-id="sign-in-form__forgot-password" class="font-sans text-md font-bold link leading-regular
            sign-in-form__forgot-password--full-width" href="https://www.linkedin.com/uas/request-password-reset?trk=public_jobs_contextual-sign-in-modal_sign-in-modal_forgot_password" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_forgot_password" data-tracking-will-navigate>Forgot password?</a>

<!---->
        <input name="trk" value="public_jobs_contextual-sign-in-modal_sign-in-modal_sign-in-submit" type="hidden">
        <button class="btn-md btn-primary flex-shrink-0 cursor-pointer
            sign-in-form__submit-btn--full-width" data-id="sign-in-form__submit-btn" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_sign-in-submit-btn" data-tracking-client-ingraph data-tracking-litms type="submit">
          Sign in
        </button>
      </div>
          <div class="sign-in-form__divider left-right-divider pt-2 pb-3">
            <p class="sign-in-form__divider-text font-sans text-sm text-color-text px-2">
              or
            </p>
          </div>
    </form>
        <div class="w-full max-w-[400px] mx-auto">
          
    

    <div class="google-auth-button" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_google-auth-button" data-tracking-client-ingraph>
        
    
    
    <p class="linkedin-tc__text text-color-text-low-emphasis text-xs pb-2" data-impression-id="public_jobs_contextual-sign-in-modal_sign-in-modal__button-skip-tc-text">
      By clicking Continue to join or sign in, you agree to LinkedIn’s <a href="/legal/user-agreement?trk=public_jobs_contextual-sign-in-modal_sign-in-modal_auth-button_user-agreement" target="_blank" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_auth-button_user-agreement" data-tracking-will-navigate="true">User Agreement</a>, <a href="/legal/privacy-policy?trk=public_jobs_contextual-sign-in-modal_sign-in-modal_auth-button_privacy-policy" target="_blank" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_auth-button_privacy-policy" data-tracking-will-navigate="true">Privacy Policy</a>, and <a href="/legal/cookie-policy?trk=public_jobs_contextual-sign-in-modal_sign-in-modal_auth-button_cookie-policy" target="_blank" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_auth-button_cookie-policy" data-tracking-will-navigate="true">Cookie Policy</a>.
    </p>
  
      <div class="google-auth-button__placeholder mx-auto
          google-auth-button__placeholder--black-border" data-theme="outline" data-logo-alignment="center" data-locale="en_US" role="button" aria-label="Continue with google" data-safe-to-skip-tnc-redirect></div>
<!---->    </div>
  
        </div>
<!---->  
              <p class="sign-in-modal__join-now m-auto font-sans text-md text-color-text
                  mt-2">
                New to LinkedIn? <a href="https://www.linkedin.com/signup/cold-join?source=jobs_registration&trk=public_jobs_contextual-sign-in-modal_sign-in-modal_join-link" data-tracking-control-name="public_jobs_contextual-sign-in-modal_sign-in-modal_join-link" data-tracking-will-navigate="true" class="sign-in-modal__join-link">Join now</a>
              </p>
          </div>
        
            </div>

<!---->          </section>
        </div>
      </div>
    </div>
  
<!---->    </div>
  
                    
    
                      <div class="contextual-sign-in-modal__divider left-right-divider">
                        <p class="contextual-sign-in-modal__divider-text font-sans text-sm text-color-text px-2">
                          or
                        </p>
                      </div>
                    

                </div>
                  <p class="contextual-sign-in-modal__join-now m-auto font-sans text-md text-color-text my-1">
                    New to LinkedIn? <a href="https://www.linkedin.com/signup/cold-join?source=jobs_registration&trk=public_jobs_contextual-sign-in-modal_join-link" data-tracking-control-name="public_jobs_contextual-sign-in-modal_join-link" data-tracking-will-navigate="true" class="contextual-sign-in-modal__join-link">Join now</a>
                  </p>
                  
    
    
    <p class="linkedin-tc__text text-color-text-low-emphasis text-xs pb-2 contextual-sign-in-modal__terms-and-conditions m-auto w-[320px] pt-2 babybear:w-full" data-impression-id="linkedin-tc__button-skip-tc-text">
      By clicking Continue to join or sign in, you agree to LinkedIn’s <a href="/legal/user-agreement?trk=linkedin-tc_auth-button_user-agreement" target="_blank" data-tracking-control-name="linkedin-tc_auth-button_user-agreement" data-tracking-will-navigate="true">User Agreement</a>, <a href="/legal/privacy-policy?trk=linkedin-tc_auth-button_privacy-policy" target="_blank" data-tracking-control-name="linkedin-tc_auth-button_privacy-policy" data-tracking-will-navigate="true">Privacy Policy</a>, and <a href="/legal/cookie-policy?trk=linkedin-tc_auth-button_cookie-policy" target="_blank" data-tracking-control-name="linkedin-tc_auth-button_cookie-policy" data-tracking-will-navigate="true">Cookie Policy</a>.
    </p>
  
              </div>
                      
            </div>

<!---->          </section>
        </div>
      </div>
    </div>
  
<!----><!---->    </div>
  

      
    
    
    

    
    

      

    

      <div class="cta-modal overflow-hidden container-raised z-10 fixed bottom-3 right-3 min-h-[56px] p-2 babybear:hidden windows-app-upsell windows-app-upsell--msft flex flex-col p-2 w-[359px] !bg-[#F1F8FA] opacity-90 backdrop-blur-[2px] z-1" data-impression-id="public_jobs_windows-app-upsell_cta-modal" role="dialog" aria-labelledby="cta-modal-header" aria-describedby="cta-modal-subheader">
          

          

        
        <div class="windows-app-upsell__linkedin-title-container pt-[6px] mb-1.5 flex align-center">
          <icon class="windows-app-upsell__linkedin-bug-icon block w-[21px] h-[21px]" data-svg-class-name="windows-app-upsell__linkedin-bug-icon-svg w-[21px] h-[21px]" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/euqjj7tf5wvr33frd3x1jj9s"></icon>
          <p class="windows-app-upsell__linkedin-title uppercase text-xs text-color-text-secondary leading-[21px] ml-1">
            LinkedIn
          </p>
        </div>
        <p class="windows-app-upsell__title font-sans text-md text-color-text-accent-4-hover font-semibold leading-regular mb-1">
          LinkedIn is better on the app
        </p>
        <p class="windows-app-upsell__body font-sans text-sm text-color-text-secondary leading-regular">
          Don’t have the app? Get it in the Microsoft Store.
        </p>
        <a class="windows-app-upsell__cta btn-sm btn-secondary-emphasis mt-2 mb-[6px] w-fit" href="ms-windows-store://pdp/?ProductId=9WZDNCRFJ4Q7&amp;mode=mini&amp;cid=guest_desktop_upsell" data-tracking-client-ingraph data-tracking-control-name="public_jobs_windows-app-upsell_cta" data-tracking-will-navigate>
          Open the app
        </a>
      

        <button class="cta-modal__dismiss-btn absolute h-4 w-4 p-1 top-2 right-2 hover:cursor-pointer focus:outline focus:outline-2 focus:outline-color-action" data-tracking-control-name="public_jobs_windows-app-upsell_dismiss" aria-label="Dismiss">
          <icon class="cta-modal__dismiss-icon block h-2 w-2 onload" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/adzjokfylbe8pvjr9h8iv96mw"></icon>
        </button>
      </div>
  
  
    </div>
    <code id="disableOneTapOnInitIfCsm" style="display: none"><!--false--></code>
  

<!---->
        
    
    
    

    
    
    
    

    
    

      

    

      <div class="cta-modal overflow-hidden container-raised z-10 fixed bottom-3 right-3 min-h-[56px] p-2 babybear:hidden windows-app-upsell windows-app-upsell--msft flex flex-col p-2 w-[359px] !bg-[#F1F8FA] opacity-90 backdrop-blur-[2px] z-1 z-1" data-impression-id="public_jobs_windows-app-upsell_cta-modal" role="dialog" aria-labelledby="cta-modal-header" aria-describedby="cta-modal-subheader">
          

          

        
        <div class="windows-app-upsell__linkedin-title-container pt-[6px] mb-1.5 flex align-center">
          <icon class="windows-app-upsell__linkedin-bug-icon block w-[21px] h-[21px]" data-svg-class-name="windows-app-upsell__linkedin-bug-icon-svg w-[21px] h-[21px]" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/euqjj7tf5wvr33frd3x1jj9s"></icon>
          <p class="windows-app-upsell__linkedin-title uppercase text-xs text-color-text-secondary leading-[21px] ml-1">
            LinkedIn
          </p>
        </div>
        <p class="windows-app-upsell__title font-sans text-md text-color-text-accent-4-hover font-semibold leading-regular mb-1">
          Know when new jobs open up
        </p>
        <p class="windows-app-upsell__body font-sans text-sm text-color-text-secondary leading-regular">
          Never miss a job alert with the new LinkedIn app for Windows.
        </p>
        <a class="windows-app-upsell__cta btn-sm btn-secondary-emphasis mt-2 mb-[6px] w-fit" href="ms-windows-store://pdp/?ProductId=9WZDNCRFJ4Q7&amp;mode=mini&amp;cid=guest_desktop_upsell_job2" data-tracking-client-ingraph data-tracking-control-name="public_jobs_windows-app-upsell_cta" data-tracking-will-navigate>
          Get the app
        </a>
      

        <button class="cta-modal__dismiss-btn absolute h-4 w-4 p-1 top-2 right-2 hover:cursor-pointer focus:outline focus:outline-2 focus:outline-color-action" data-tracking-control-name="public_jobs_windows-app-upsell_dismiss" aria-label="Dismiss">
          <icon class="cta-modal__dismiss-icon block h-2 w-2 onload" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/adzjokfylbe8pvjr9h8iv96mw"></icon>
        </button>
      </div>
  
  
  

        
    

    <div id="toasts" class="toasts fixed z-8 babybear:right-4 mamabear:right-4 papabear:min-h-[96px] invisible
        top:auto bottom-4 left-4 papabear:w-[400px]
        toasts--bottom" type="bottom">
    

    <template id="toast-template">
      <div class="toast container-raised flex
          toast--bottom
          transition ease-accelerate duration-xxslow
          " data-id="toast">
        <div class="toast__message flex flex-1 babybear:items-center mamabear:items-center papabear:items-start py-2 px-1.5" data-id="toast__message" role="alert" tabindex="-1">
          <div class="toast__message-content-container" data-id="toast__message-content-container">
            <p class="toast__message-content font-sans text-sm opacity-90 inline babybear:self-center mamabear:self-center papabear:self-start" data-id="toast__message-content"></p>
          </div>
        </div>
        <button class="toast__dismiss-btn cursor-pointer babybear:self-center mamabear:self-center papabear:self-start pt-3 pb-2 papabear:py-2 pl-0.5 pr-0" data-id="toast__dismiss-btn" aria-label="Close">
          <svg width="24" height="24" class="fill-color-icon"><path d="M13 4.32 9.31 8 13 11.69 11.69 13 8 9.31 4.31 13 3 11.69 6.69 8 3 4.31 4.31 3 8 6.69 11.68 3Z"></path></svg>
        </button>
      </div>
    </template>
      <template id="toast-icon-caution">
        <icon class="text-color-icon-caution toast__icon w-3 h-3 shrink-0 mr-2" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/bk9xca6x9l1fga1tbzame3i3l"></icon>
      </template>
      <template id="toast-icon-error">
        <icon class="text-color-icon-negative toast__icon w-3 h-3 shrink-0 mr-2" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/8c0098stai8lcqypn95r47dew"></icon>
      </template>
      <template id="toast-icon-gdpr">
        <icon class="text-color-icon-neutral toast__icon w-3 h-3 shrink-0 mr-2" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/a9phzx7id2abubo45lgookfd"></icon>
      </template>
      <template id="toast-icon-notify">
        <icon class="text-color-icon-neutral toast__icon w-3 h-3 shrink-0 mr-2" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/4xg53nt8deu1y7tb1t3km8tfh"></icon>
      </template>
      <template id="toast-icon-success">
        <icon class="text-color-icon-positive toast__icon w-3 h-3 shrink-0 mr-2" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/9zhm3eh2dq7vh2muo8xnfikxh"></icon>
      </template>
    <template id="toast-cta">
      <a class="toast__cta cta-link font-medium ml-0.5 text-sm text-inherit inline" target="_blank"></a>
    </template>
  </div>
  

        <section id="json-refs">
          <code id="isGraphQLEnabled" style="display: none"><!--true--></code>
          <code id="requestSubdomain" style="display: none"><!--"in"--></code>
          <code id="pageKey" style="display: none"><!--"d_jobs_guest_search"--></code>
          <code id="resultsPerPage" style="display: none"><!--25--></code>
            <code id="totalResults" style="display: none"><!--151833--></code>
          <code id="i18n_redirected_from_deleted_alert" style="display: none"><!--"This job alert has been deactivated."--></code>
          <code id="isRedirectedFromDeletedAlert" style="display: none"><!--false--></code>
            <code id="currentSearchId" style="display: none"><!--"DDdnuKLvZknVutnJguZdFQ=="--></code>
            <code id="currentJobId" style="display: none"><!--"4297713391"--></code>
<!----><!---->        </section>
      

            <script src="https://static.licdn.com/aero-v1/sc/h/4rfvieeqozea5c2teruygcmt9" async></script>
<!---->          
          <script src="https://static.licdn.com/aero-v1/sc/h/15hr2fuo14sdxzgrq9h12k8d9" async defer></script>
      
          
<!----><!---->  
      </body>
    </html>
  
  """
soup = bs(html_doc, 'html.parser')

for link in soup.find_all('a'):
    if 'base-card__full-link' in link.get('class', []):
        print(link.get('href'))
n=input("e")
driver.quit()