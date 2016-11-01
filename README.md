# darkWebBot
Dark Web Crawler for crawling the hidden onion sites and indexing them in Solr

Requirements - 
- TOR
- SOLR
- POLIPO
- SCRAPY (using Python)


Make sure all the above are installed before running the project.

Before Proceeding - 

Solr dependencies - 
- Create a new core
- Make sure no data in core - http://localhost:8983/solr/core_name/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true
- cd solr_dir/server/solr/core_name/conf/
- mv managed-schema schema_backup.xml
- mv solrconfig.xml solrconfig_backup.xml
- cp darkWebBot/managed-schema .
- cp darkWebBot/solrconfig.xml .
- restart solr

Polipo dependencies - 
- Check if directory /etc/polipo/ exists, if not create it
- cd /etc/polipo/
- sudo mv darkWebBot/config .
- restart polipo


To run - 
cd testPolipo/
scrapy crawl darkWebBot -o items.json -t json
