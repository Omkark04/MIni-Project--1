from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from ..models import JobListing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import requests
import os
import re

# Category detection mapping
CATEGORY_KEYWORDS = {
    "Advocate": ["advocate", "lawyer", "legal", "attorney"],
    "Arts": ["art", "design", "creative", "artist", "graphic design"],
    "Automation Testing": ["automation", "testing", "qa", "quality assurance", "selenium"],
    "BlockChain": ["blockchain", "crypto", "bitcoin", "ethereum", "smart contract"],
    "Business Analyst": ["business analyst", "ba", "business analysis"],
    "Civil Engineer": ["civil engineer", "civil engineering", "construction"],
    "Data Science": ["data scientist", "data science", "machine learning", "ai", "artificial intelligence"],
    "Database": ["database", "sql", "dba", "database administrator"],
    "DevOps": ["devops", "aws", "azure", "cloud", "kubernetes", "docker"],
    ".Net": [".net", "c#", "asp.net", "dotnet"],
    "ETL": ["etl", "data warehouse", "informatica", "talend"],
    "Electrical": ["electrical", "electronics", "electrical engineer"],
    "HR": ["hr", "human resources", "recruiter", "talent acquisition"],
    "Hadoop": ["hadoop", "big data", "spark", "hive"],
    "Health and Fitness": ["health", "fitness", "wellness", "trainer"],
    "Java": ["java", "spring", "j2ee", "java developer"],
    "Mechanical": ["mechanical", "mechanical engineer"],
    "Network": ["network", "security", "cyber", "network engineer"],
    "Operations": ["operations", "operation manager", "logistics"],
    "PMO": ["pmo", "project management", "program manager"],
    "Python": ["python", "django", "flask", "python developer"],
    "SAP": ["sap", "sap developer", "sap consultant"],
    "Sales": ["sales", "account executive", "business development"],
    "Testing": ["testing", "tester", "quality assurance", "manual testing"],
    "Web Design": ["web design", "ui/ux", "frontend", "html", "css", "javascript"]
}

def detect_category(title, company):
    """Detect category based on job title"""
    if not title or title == "N/A":
        return None
    
    title_lower = title.lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return category
    
    return None

def download_image(img_url, folder_path, filename):
    """Download image from URL and save to specified folder"""
    try:
        if not img_url or 'static.licdn.com' in img_url:
            return None
            
        response = requests.get(img_url, timeout=10)
        if response.status_code == 200:
            filepath = os.path.join(folder_path, filename)
            with default_storage.open(filepath, 'wb') as f:
                f.write(response.content)
            return filepath
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None

def scrape_linkedin_jobs(keywords="Data Scientist", location="Germany", category=None):
    # Configure Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Remove for debugging
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    jobs_data = []
    
    try:
        print("🚀 Starting LinkedIn scraper...")
        
        # Create images folder
        images_folder = 'job_images'
        media_root = default_storage.location
        full_images_path = os.path.join(media_root, images_folder)
        os.makedirs(full_images_path, exist_ok=True)
        
        # Use direct URL with parameters
        url = f"https://www.linkedin.com/jobs/search/?keywords={keywords.replace(' ', '%20')}&location={location.replace(' ', '%20')}"
        print(f"🌐 Navigating to: {url}")
        driver.get(url)
        
        # Wait for page to load
        print("⏳ Waiting for page to load...")
        time.sleep(5)
        
        # Scroll to load more results
        print("📜 Scrolling to load more jobs...")
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        # Get the page source
        page_source = driver.page_source
        
        # Parse with BeautifulSoup
        soup = bs(page_source, 'html.parser')
        
        # Find job cards
        job_selectors = [
            'div[class*="base-card"]',
            'li[class*="jobs-search-results__list-item"]',
            'div[class*="job-card-container"]'
        ]
        
        job_cards = []
        for selector in job_selectors:
            job_cards = soup.select(selector)
            if job_cards:
                print(f"✅ Found {len(job_cards)} job cards with selector: {selector}")
                break
        
        if not job_cards:
            job_cards = soup.find_all(['div', 'li'], class_=lambda x: x and any(keyword in str(x).lower() for keyword in ['job', 'card', 'result']))
        
        print(f"📊 Found {len(job_cards)} total job cards")
        
        for i, card in enumerate(job_cards[:20]):  # Limit for testing
            try:
                # Extract job information
                title = "N/A"
                company = "N/A"
                location_text = "N/A"
                link = "N/A"
                date = "N/A"
                img_url = None
                img_filename = None
                
                # Title
                title_selectors = [
                    'h3[class*="base-search-card__title"]',
                    'h3[class*="job-card-title"]',
                    '.artdeco-entity-lockup__title',
                    'h2', 'h3'
                ]
                
                for selector in title_selectors:
                    title_elem = card.select_one(selector)
                    if title_elem and title_elem.get_text(strip=True):
                        title = title_elem.get_text(strip=True)
                        break
                
                # Company
                company_selectors = [
                    'h4[class*="base-search-card__subtitle"]',
                    'a[class*="job-card-container__company-name"]',
                    '.artdeco-entity-lockup__subtitle'
                ]
                
                for selector in company_selectors:
                    company_elem = card.select_one(selector)
                    if company_elem and company_elem.get_text(strip=True):
                        company = company_elem.get_text(strip=True)
                        break
                
                # Location
                location_selectors = [
                    'span[class*="job-search-card__location"]',
                    'span[class*="job-card-container__metadata-item"]'
                ]
                
                for selector in location_selectors:
                    location_elem = card.select_one(selector)
                    if location_elem and location_elem.get_text(strip=True):
                        location_text = location_elem.get_text(strip=True)
                        break
                
                # Link
                link_selectors = [
                    'a[class*="base-card__full-link"]',
                    'a[class*="job-card-container__link"]',
                    'a[href*="/jobs/"]'
                ]
                
                for selector in link_selectors:
                    link_elem = card.select_one(selector)
                    if link_elem and link_elem.get('href'):
                        link = link_elem.get('href')
                        if link.startswith('/'):
                            link = f"https://www.linkedin.com{link}"
                        break
                
                # Image
                img_elem = card.find('img')
                if img_elem:
                    img_url = (img_elem.get('data-delayed-url') or 
                              img_elem.get('src') or 
                              img_elem.get('data-ghost-url'))
                    
                    if img_url and 'static.licdn.com' not in img_url:
                        safe_company = re.sub(r'[^\w\s-]', '', company).strip()
                        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
                        img_filename = f"{safe_company}_{safe_title}_{i}.jpg"
                        img_filename = re.sub(r'[-\s]+', '_', img_filename)[:100]
                        
                        download_image(img_url, images_folder, img_filename)
                
                # Detect category
                detected_category = detect_category(title, company)
                # Use provided category if specified, otherwise use detected
                final_category = category if category else detected_category
                
                # Only save if we have valid data
                if title != "N/A" and company != "N/A":
                    # Create or update job listing
                    job, created = JobListing.objects.get_or_create(
                        title=title,
                        company=company,
                        location=location_text,
                        defaults={
                            'category': final_category,
                            'date_posted': date,
                            'job_link': link,
                            'image_url': img_url,
                            'image_filename': img_filename
                        }
                    )
                    
                    jobs_data.append({
                        'title': title,
                        'company': company,
                        'location': location_text,
                        'category': final_category,
                        'date': date,
                        'link': link,
                        'image_url': img_url,
                        'image_filename': img_filename,
                        'created': created
                    })
                    
                    print(f"✅ Processed: {title} at {company} | Category: {final_category}")
                else:
                    print(f"⚠️ Skipped incomplete job card: {card.get_text()[:100]}...")
                
            except Exception as e:
                print(f"❌ Error parsing job card {i}: {e}")
                continue
        
        print(f"🎉 Successfully processed {len(jobs_data)} valid jobs")
        return jobs_data
        
    except Exception as e:
        print(f"💥 Critical error in scraper: {e}")
        return []
    finally:
        driver.quit()
        print("🔚 Browser closed")

class Command(BaseCommand):
    help = 'Scrape LinkedIn jobs'
    
    def add_arguments(self, parser):
        parser.add_argument('--keywords', type=str, default='Data Scientist', help='Job keywords to search')
        parser.add_argument('--location', type=str, default='Germany', help='Location to search')
        parser.add_argument('--category', type=str, help='Job category')
    
    def handle(self, *args, **options):
        keywords = options['keywords']
        location = options['location']
        category = options['category']
        
        self.stdout.write(f"🔍 Scraping LinkedIn jobs for '{keywords}' in '{location}'")
        if category:
            self.stdout.write(f"🏷️ Category: {category}")
        
        results = scrape_linkedin_jobs(keywords, location, category)
        
        self.stdout.write(
            self.style.SUCCESS(f'✅ Successfully scraped {len(results)} jobs')
        )