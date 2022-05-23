# Backend speed test
Bench for testing backend solutions performance. Based on Docker containers and JMeter.

## Currently tested solutions
- Beego (Go)
- Symfony (PHP)
- Django (Python)

Latest test results: <a href="http://it-test.net/backend-speed-test/" target="_blank">http://it-test.net/backend-speed-test/</a>

## Configure
Set executable permissions to repository files (`chmod -R +x .`)

Config file: `./config.yml` (will be created automatically, if not exist)

Example:  <a href="environment/bst/template.config.yml" target="_blank">template.config.yml</a>

## Start test
Start all test cases:
`python ./start.py`

Start specific test case:
`python ./start.py <test-case>`

## Reports
`./data/reports/<test-case>`

## Requriments
- Python 3.9+ (and: `pip install -r ./requirements.txt`)
- Docker 20.10.14+
- Docker Compose 2+
- Java 8+

## SSL
Self-signed <a href="environment/ssl" target="_blank">ssl certificate</a> for testing
