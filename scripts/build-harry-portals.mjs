#!/usr/bin/env node
/**
 * One-shot generator: portals.yml for Harry Nguyen (new grad / systems / ML infra).
 * Run: node scripts/build-harry-portals.mjs
 */

import { writeFileSync } from 'fs';

/** @type {Record<string, { ats: 'gh'|'ashby'|'lever', slug: string }>} */
const ATS = {
  'Affirm': { ats: 'gh', slug: 'affirm' },
  'Airtable': { ats: 'gh', slug: 'airtable' },
  'Anduril Industries': { ats: 'gh', slug: 'andurilindustries' },
  'Anthropic': { ats: 'gh', slug: 'anthropic' },
  'Asana': { ats: 'gh', slug: 'asana' },
  'Block': { ats: 'gh', slug: 'block' },
  'Brex': { ats: 'gh', slug: 'brex' },
  'Chime': { ats: 'gh', slug: 'chime' },
  'Cohere': { ats: 'ashby', slug: 'cohere' },
  'Coursera': { ats: 'gh', slug: 'coursera' },
  'Credit Karma': { ats: 'gh', slug: 'creditkarma' },
  'Databricks': { ats: 'gh', slug: 'databricks' },
  'Datadog': { ats: 'gh', slug: 'datadog' },
  'Discord': { ats: 'gh', slug: 'discord' },
  'Dropbox': { ats: 'gh', slug: 'dropbox' },
  'Duolingo': { ats: 'gh', slug: 'duolingo' },
  'Figma': { ats: 'gh', slug: 'figma' },
  'Flexport': { ats: 'gh', slug: 'flexport' },
  'GitLab': { ats: 'gh', slug: 'gitlab' },
  'Gusto': { ats: 'gh', slug: 'gusto' },
  'HubSpot': { ats: 'gh', slug: 'hubspot' },
  'Instacart': { ats: 'gh', slug: 'instacart' },
  'Klaviyo': { ats: 'gh', slug: 'klaviyo' },
  'Lyft': { ats: 'gh', slug: 'lyft' },
  'MongoDB': { ats: 'gh', slug: 'mongodb' },
  'Notion': { ats: 'ashby', slug: 'notion' },
  'Nuro': { ats: 'gh', slug: 'nuro' },
  'Okta': { ats: 'gh', slug: 'okta' },
  'PagerDuty': { ats: 'gh', slug: 'pagerduty' },
  'Palantir Technologies': { ats: 'lever', slug: 'palantir' },
  'Pinterest': { ats: 'gh', slug: 'pinterest' },
  'Postman': { ats: 'gh', slug: 'postman' },
  'Reddit': { ats: 'gh', slug: 'reddit' },
  'Robinhood': { ats: 'gh', slug: 'robinhood' },
  'Roblox': { ats: 'gh', slug: 'roblox' },
  'Rubrik': { ats: 'gh', slug: 'rubrik' },
  'Samsara': { ats: 'gh', slug: 'samsara' },
  'Scale AI': { ats: 'gh', slug: 'scaleai' },
  'SoFi': { ats: 'gh', slug: 'sofi' },
  'Spotify': { ats: 'lever', slug: 'spotify' },
  'Stripe': { ats: 'gh', slug: 'stripe' },
  'Twitch': { ats: 'gh', slug: 'twitch' },
  'Udemy': { ats: 'gh', slug: 'udemy' },
  'Unity Technologies': { ats: 'gh', slug: 'unity3d' },
  'Cloudflare': { ats: 'gh', slug: 'cloudflare' },
};

/** @type {Array<[string, string, string?]>} [name, careersUrl, scanQueryHint] */
const WEB = [
  ['1Password', 'https://1password.com/careers/'],
  ['Benchling', 'https://www.benchling.com/careers/'],
  ['Box', 'https://www.box.com/careers'],
  ['Chainalysis', 'https://www.chainalysis.com/careers/'],
  ['Coinbase', 'https://www.coinbase.com/careers'],
  ['Confluent', 'https://careers.confluent.io/'],
  ['DoorDash', 'https://careers.doordash.com/'],
  ['DraftKings', 'https://careers.draftkings.com/'],
  ['Grammarly', 'https://www.grammarly.com/careers'],
  ['Navan', 'https://navan.com/careers'],
  ['OpenAI', 'https://openai.com/careers'],
  ['OpenSea', 'https://opensea.io/careers'],
  ['Plaid', 'https://plaid.com/careers/'],
  ['Quora', 'https://www.quora.com/careers'],
  ['Ramp', 'https://ramp.com/careers'],
  ['Rippling', 'https://www.rippling.com/careers'],
  ['Sentry', 'https://sentry.io/careers/'],
  ['Snyk', 'https://snyk.io/careers/'],
  ['Uber', 'https://www.uber.com/us/en/careers/'],
  ['Wealthfront', 'https://www.wealthfront.com/careers'],
  ['Yelp', 'https://yelp.careers/us/en/'],
  ['Zillow', 'https://zillow.wd5.myworkdayjobs.com/Zillow_Group_External'],
  ['Google', 'https://careers.google.com/jobs/results/'],
  ['Microsoft', 'https://careers.microsoft.com/us/en/search-results'],
  ['Apple', 'https://jobs.apple.com/en-us/search'],
  ['Amazon', 'https://www.amazon.jobs/en/search'],
  ['Meta', 'https://www.metacareers.com/jobs/'],
  ['Netflix', 'https://jobs.netflix.com/search'],
  ['Airbnb', 'https://careers.airbnb.com/positions/'],
  ['Waymo', 'https://careers.withwaymo.com/jobs/search'],
  ['Salesforce', 'https://careers.salesforce.com/en/jobs/'],
  ['NVIDIA', 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite'],
  ['Tesla', 'https://www.tesla.com/careers/search/'],
  ['Snowflake', 'https://careers.snowflake.com/us/en/search-results'],
  ['Snap Inc.', 'https://careers.snap.com/jobs'],
  ['LinkedIn', 'https://careers.linkedin.com/jobs'],
  ['Slack', 'https://slack.com/careers'],
  ['ByteDance', 'https://jobs.bytedance.com/en/position'],
  ['Atlassian', 'https://www.atlassian.com/company/careers/all-jobs'],
  ['Shopify', 'https://www.shopify.com/careers'],
  ['Twilio', 'https://www.twilio.com/en-us/company/jobs'],
  ['Zoom', 'https://careers.zoom.us/jobs/search'],
  ['Workday', 'https://www.workday.com/en-us/company/careers.html'],
  ['X', 'https://careers.twitter.com/en/roles.html'],
  ['Bloomberg', 'https://careers.bloomberg.com/job/search'],
  ['Qualtrics', 'https://www.qualtrics.com/careers/us/en/search-results'],
  ['Splunk', 'https://careers.cisco.com/global/en/search-results'],
  ['ServiceNow', 'https://careers.servicenow.com/jobs/'],
  ['Autodesk', 'https://autodesk.wd1.myworkdayjobs.com/Ext'],
  ['Redfin', 'https://careers.redfin.com/us/en/search-results'],
  ['PayPal', 'https://paypal.eightfold.ai/careers'],
  ['Electronic Arts (EA)', 'https://ea.gr8people.com/jobs'],
  ['Intuit', 'https://jobs.intuit.com/search-jobs'],
  ['Wayfair', 'https://www.wayfair.com/careers/jobs'],
  ['VMware', 'https://careers.broadcom.com/'],
  ['Indeed', 'https://www.indeed.com/cmp/Indeed/jobs'],
  ['DocuSign', 'https://careers.docusign.com/search-jobs'],
  ['MathWorks', 'https://www.mathworks.com/company/jobs/opportunities.html'],
  ['Tableau Software', 'https://careers.salesforce.com/en/jobs/'],
  ['Red Hat', 'https://redhat.wd5.myworkdayjobs.com/jobs/'],
  ['Cisco', 'https://careers.cisco.com/global/en/search-results'],
  ['Hulu', 'https://jobs.disneycareers.com/'],
  ['Capital One', 'https://www.capitalonecareers.com/search-jobs'],
  ['Adobe', 'https://careers.adobe.com/us/en/search-results'],
  ['IBM', 'https://www.ibm.com/careers/search'],
  ['Intel Corporation', 'https://jobs.intel.com/en/search-jobs'],
  ['Oracle', 'https://careers.oracle.com/en/sites/jobsearch/jobs'],
  ['Qualcomm', 'https://careers.qualcomm.com/careers-home/jobs'],
  ['SAP', 'https://jobs.sap.com/search/'],
  ['Visa', 'https://careers.smartrecruiters.com/Visa'],
  ['Goldman Sachs', 'https://higher.gs.com/results'],
  ['J.P. Morgan', 'https://careers.jpmorgan.com/us/en/search-results'],
  ['General Motors', 'https://search-careers.gm.com/en/jobs/'],
  ['Verkada', 'https://www.verkada.com/careers/'],
  ['Acorns', 'https://www.acorns.com/careers/'],
  ['Wish', 'https://www.wish.com/careers'],
  ['Expedia', 'https://careers.expediagroup.com/jobs/'],
  ['Grubhub', 'https://careers.grubhub.com/'],
  ['ZipRecruiter', 'https://www.ziprecruiter.com/careers'],
  ['Yext', 'https://www.yext.com/careers'],
  ['Mastercard', 'https://careers.mastercard.com/us/en/search-results'],
  ['American Express', 'https://aexp.eightfold.ai/careers'],
  ['IXL Learning', 'https://www.ixl.com/company/careers'],
  ['Yahoo', 'https://www.yahooinc.com/careers/'],
  ['Bank of America', 'https://careers.bankofamerica.com/en-us/search-results'],
  ['BCG', 'https://careers.bcg.com/global/en/search-results'],
  ['Samsung', 'https://www.samsung.com/us/careers/'],
  ['Sony', 'https://www.sonyjobs.com/search-jobs'],
  ['Booking.com', 'https://jobs.booking.com/careers'],
  ['Palo Alto Networks', 'https://jobs.paloaltonetworks.com/en/search-jobs'],
  ['Nintendo', 'https://careers.nintendo.com/job-openings/'],
  ['Dell', 'https://jobs.dell.com/en/search-jobs'],
  ['Logitech', 'https://jobs.logitech.com/careers'],
  ['Veeva Systems', 'https://careers.veeva.com/'],
  ['McKinsey', 'https://www.mckinsey.com/careers/search-jobs'],
  ['eBay', 'https://jobs.ebayinc.com/us/en/search-results'],
  ['Hewlett Packard Enterprise', 'https://careers.hpe.com/us/en/search-results'],
  ['NetApp', 'https://careers.netapp.com/search-jobs'],
  ['Motorola Solutions', 'https://careers.motorolasolutions.com/'],
  ['Canva', 'https://www.lifeatcanva.com/en/jobs/'],
  ['Epic Games', 'https://www.epicgames.com/site/en-US/careers/jobs'],
  ['Ripple', 'https://ripple.com/careers/all-jobs/'],
  ['Faire', 'https://www.faire.com/careers'],
  ['SpaceX', 'https://www.spacex.com/careers/'],
  ['Fanatics', 'https://www.fanaticsinc.com/careers'],
  ['Bolt', 'https://bolt.eu/careers/'],
  ['Lacework', 'https://www.fortinet.com/corporate/careers'],
  ['Tempus Labs', 'https://www.tempus.com/careers/'],
  ['Fireblocks', 'https://www.fireblocks.com/careers/'],
  ['Gemini', 'https://www.gemini.com/careers'],
  ['Upgrade', 'https://www.upgrade.com/careers/'],
  ['Better', 'https://better.com/about-us/careers'],
  ['Activision Blizzard', 'https://careers.activision.com/search-results'],
  ['Jump Trading', 'https://www.jumptrading.com/careers'],
  ['Hudson River Trading', 'https://www.hudsonrivertrading.com/careers/'],
  ['Jane Street', 'https://www.janestreet.com/join-jane-street/open-roles/'],
  ['Citadel', 'https://www.citadel.com/careers/open-roles/'],
  ['D.E. Shaw', 'https://www.deshaw.com/careers'],
  ['Optiver', 'https://optiver.com/working-at-optiver/career-opportunities/'],
  ['Two Sigma', 'https://careers.twosigma.com/careers/'],
  ['Akuna Capital', 'https://akunacapital.com/careers/'],
  ['DRW', 'https://drw.com/work-at-drw/'],
  ['IMC', 'https://www.imc.com/us/careers/'],
  ['Chicago Trading Company', 'https://www.chicagotrading.com/careers/'],
  ['Belvedere Trading', 'https://www.belvederetrading.com/careers/'],
  ['Cruise', 'https://getcruise.com/careers'],
  ['Hugging Face', 'https://apply.workable.com/huggingface/'],
  ['AMD', 'https://careers.amd.com/careers-home/jobs'],
  ['Walmart', 'https://careers.walmart.com/'],
  ['Lucid Motors', 'https://lucidmotors.com/careers'],
  ['Gecko Robotics', 'https://www.geckorobotics.com/careers'],
  ['SurveyMonkey', 'https://www.momentive.ai/en/careers/'],
  ['TuSimple', 'https://www.tusimple.com/careers'],
  ['Circle', 'https://www.circle.com/en/careers'],
  ['Citrix', 'https://www.cloud.com/careers'],
  ['Secureframe', 'https://secureframe.com/careers'],
  ['GoodLeap', 'https://www.goodleap.com/careers/'],
  ['Klarna', 'https://www.klarna.com/careers/'],
  ['Attentive', 'https://www.attentive.com/careers'],
  ['Workato', 'https://www.workato.com/careers'],
  ['Cityblock Health', 'https://www.cityblock.com/careers'],
  ['6Sense', 'https://6sense.com/about-us/careers/'],
  ['iCapital Network', 'https://www.icapital.com/careers/'],
  ['Caris', 'https://www.carislifesciences.com/careers/'],
  ['Vice Media', 'https://company.vice.com/careers/'],
  ['Hive AI', 'https://thehive.ai/about/careers'],
  ['WeWork', 'https://www.wework.com/careers'],
];

const COMPANY_ORDER = [
  ...Object.keys(ATS),
  ...WEB.map(([n]) => n),
].sort((a, b) => a.localeCompare(b));

const ROLE_QUERY =
  '"Software Engineer" OR "Backend Engineer" OR "New Grad" OR "University Grad" OR "Early Career" OR intern OR "ML Engineer" OR "Infrastructure" OR "Platform Engineer" OR SRE OR "Distributed Systems"';

function yamlEntry(name, lines) {
  return `  - name: ${name}\n${lines.map((l) => `    ${l}`).join('\n')}\n`;
}

function ghEntry(name, slug) {
  const url = `https://job-boards.greenhouse.io/${slug}`;
  const api = `https://boards-api.greenhouse.io/v1/boards/${slug}/jobs`;
  return yamlEntry(name, [
    `careers_url: ${url}`,
    `api: ${api}`,
    `notes: "Greenhouse API — scanned by scan.mjs (zero-token)."`,
    `enabled: true`,
  ]);
}

function ashbyEntry(name, slug) {
  return yamlEntry(name, [
    `careers_url: https://jobs.ashbyhq.com/${slug}`,
    `notes: "Ashby API — scanned by scan.mjs (zero-token)."`,
    `enabled: true`,
  ]);
}

function leverEntry(name, slug) {
  return yamlEntry(name, [
    `careers_url: https://jobs.lever.co/${slug}`,
    `notes: "Lever API — scanned by scan.mjs (zero-token)."`,
    `enabled: true`,
  ]);
}

function webEntry(name, url) {
  const host = new URL(url).hostname;
  return yamlEntry(name, [
    `careers_url: ${url}`,
    `scan_method: websearch`,
    `scan_query: 'site:${host} ${ROLE_QUERY}'`,
    `notes: "Careers site — use /career-ops scan (agent Playwright) or paste URLs to data/pipeline.md; not scanned by scan.mjs API."`,
    `enabled: true`,
  ]);
}

const header = `# Portal Scanner Configuration — Harry Nguyen
# Generated for new grad / intern: backend, distributed systems, ML infra, platform, SRE.
# scan.mjs scans Greenhouse/Ashby/Lever entries only; other companies need agent scan or manual pipeline URLs.

location_filter:
  always_allow:
    - "United States"
    - "Atlanta"
    - "Georgia"
  allow:
    - "Remote"
    - "United States"
    - "USA"
    - "Atlanta"
    - "Georgia"
    - "Hybrid"
    - "US"
  block:
    - "India"
    - "Bengaluru"
    - "Bangalore"
    - "United Kingdom"
    - "London"
    - "Germany"
    - "Berlin"
    - "France"
    - "Paris"
    - "Singapore"
    - "Japan"
    - "Tokyo"
    - "Brazil"
    - "São Paulo"
    - "China"
    - "Beijing"
    - "Shanghai"

title_filter:
  positive:
    - "Software Engineer"
    - "Backend Engineer"
    - "Systems Engineer"
    - "Platform Engineer"
    - "Infrastructure Engineer"
    - "Site Reliability"
    - "SRE"
    - "ML Engineer"
    - "Machine Learning"
    - "AI Engineer"
    - "Distributed Systems"
    - "New Grad"
    - "University Grad"
    - "Early Career"
    - "Intern"
    - "Internship"
    - "Graduate"
    - "University"
    - "Entry Level"
    - "Performance Engineer"
    - "Cloud Engineer"
    - "DevOps"
    - "SWE"
    - "C++"
    - "Go Engineer"
    - "Founding Engineer"
  negative:
    - ".NET"
    - "iOS"
    - "Android"
    - "PHP"
    - "Ruby on Rails"
    - "Embedded"
    - "Firmware"
    - "FPGA"
    - "ASIC"
    - "Salesforce Admin"
    - "SAP Consultant"
    - "Mainframe"
    - "COBOL"
    - "Account Executive"
    - "Recruiter"
    - "Customer Success Manager"
  seniority_boost:
    - "New Grad"
    - "University"
    - "Intern"
    - "Early Career"
    - "Graduate"

search_queries:
  - name: Greenhouse — New Grad SWE
    query: 'site:job-boards.greenhouse.io OR site:boards.greenhouse.io "New Grad" OR "University Grad" OR intern "Software Engineer" OR "Backend"'
    enabled: true

  - name: Ashby — New Grad SWE
    query: 'site:jobs.ashbyhq.com "New Grad" OR intern OR "Early Career" "Software Engineer" OR "Backend" OR "Infrastructure"'
    enabled: true

  - name: Lever — New Grad SWE
    query: 'site:jobs.lever.co "New Grad" OR intern "Software Engineer" OR "Backend" OR "Platform"'
    enabled: true

  - name: Greenhouse — ML / Infra
    query: 'site:job-boards.greenhouse.io "ML Engineer" OR "Machine Learning Infrastructure" OR "Inference" OR "ML Platform" intern OR "New Grad"'
    enabled: true

  - name: Levels.fyi style — Big Tech new grad
    query: '"new grad" "software engineer" 2027 OR 2026 site:careers.google.com OR site:careers.microsoft.com OR site:metacareers.com OR site:amazon.jobs'
    enabled: true

  - name: Simplify — SWE intern
    query: '"software engineer intern" OR "swe intern" backend distributed systems'
    enabled: true

  - name: LinkedIn — Atlanta SWE new grad
    query: 'site:linkedin.com/jobs "Software Engineer" "New Grad" Atlanta OR Remote United States'
    enabled: true

tracked_companies:

`;

const seen = new Set();
const entries = [];

for (const name of COMPANY_ORDER) {
  if (seen.has(name)) continue;
  seen.add(name);
  const ats = ATS[name];
  if (ats) {
    if (ats.ats === 'gh') entries.push(ghEntry(name, ats.slug));
    else if (ats.ats === 'ashby') entries.push(ashbyEntry(name, ats.slug));
    else if (ats.ats === 'lever') entries.push(leverEntry(name, ats.slug));
    continue;
  }
  const web = WEB.find(([n]) => n === name);
  if (web) entries.push(webEntry(web[0], web[1]));
}

// Block was Square in user list — alias
if (!seen.has('Square')) {
  entries.push(webEntry('Square', 'https://block.xyz/careers'));
}

const out = header + entries.join('\n');
writeFileSync('portals.yml', out, 'utf-8');
console.log(`Wrote portals.yml — ${entries.length} companies (${Object.keys(ATS).length} API-scannable)`);
