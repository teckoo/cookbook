# TODO

## Important and Urgent
* study maven test 
* figure PyCharm/Python execute TestSuite calling TestCase
* numpy, pandas, pyspark API usage

## Important and Not-Urgent
* AWS study
    - Linux Academy
    - Qwiklabs
    - A Cloud Guru
    - Safari: Study Guide
* Security training
* Python
    - Numpy, pandas
    - PySpark
* Scala
* Go 

# DONE log

## 2019-01
01/17
* wrapper to call pci-detokenization function 25447
    update install instruction
    - bootstrap script
    - execute.sh pythonpath
    /tada/code/tada_core_services/config/resources/
* unit test story 22618

01/16
* push to EMR and test pci-detokenization, fix spark log property
* bootstrap script


01/15
* test data with pci token/detokenization, it's completed
* worked with turing-support team to figure out the cause to NPI authorization error at EOD finnaly
* I am fixing it now

01/14
* update deturing_api
* test on NPI client secret, 
* need help on PCI client for 

01/11
* interviews
* required trainings
* test sample with actual service

01/10
* worked with Maninder on defining de-tokenzie config with json format 
    - define config actual parameters required
        do_tokenization.execute(),
    - currently support delimited file 
    - need to have a config
        * header/trailer (default for 0)
        * delimitor: (e.g. tab, comma, pipe)

01/09
* did a manual deployment of de-tokenization code in EMR, 
    - try the install, found version mismatch in dependency package (requests), keep notes in bootstrap script. 
    - run the de-tokenization script, 
    - need turing column details, talked to Maninder

01/08
* pytest de-tokenization code/test
    - write mock test functions for calling wrapper in do_detokenization
    - run de-tokenization test
* helped Manoj on processing parquet files
* helped on SFStoS3 test (Divya and Pratap)

01/07
* Done with coding on de-token (done)
* setup turing_component environment (done)
* setup pytest for de-tokenization code from Madhavi 
    - run pytest for existing turing_component project (done)
    - run her de-tokenization test

01/03
* rdt_data_transformation/turing_component/turing_component/do_tokenization/do_tokenization.py
    - make a new file to do_detokenization.py
    - https://jira.kdc.capitalone.com/browse/ASCENT-25447
* unittest for wrapper
* maven/TestSuite/TestCase, find a place to set python path

Retro: 
* S3 bucket policy, assume role problem held the entire team for 3 days.
* prod release with tag, fallback/revert strategy.
* update working code in git in time, e.g lambda functions.

Thorn: 
* search existing code for usage reference is hard, e.g. chamber of secret, AWS proxy on CAT1.
* need some sort of integration test on QA for result verification

01/02
* use AWS proxy to get security token, assume-role on CAT2 and copy files to CAT1
* figured out why EMR was not triggered by SQS messages. (nohup & fix)

## 2018-12
12/28
* proxy setting with regular username/passwd on CAT1

12/26
* EFG PGP key update Routes for decryption

12/24
* assume role

12/20
* Mock on file open (30mins)
* TestSuite/TestCase (30mins)
* maven test plugin (1hr)
* AWS step functions ()

12/19
* submitted Route form, got approved, need to work with EFG to test 
* chamber of secret fixed (Pratap)
* helped on tokenization (Madhavi)
* TadaUtils (Ramana)

12/17
* write a public key location
* encrypt "Hello world" sample and send it to EFG
* request them to do decryption for verification


12/14
* GPG documentation
https://confluence.kdc.capitalone.com/display/ASCENT/GPG+key+pair+setup+for+encryption+and+decryption
* figure PyCharm/Python execute TestSuite calling TestCase (1hr)


12/13
* Generated GPG private keys
* Helped on SFS to S3 transmission

12/12
* started to work on GPG key generation 
* helped on move files from SFS to EC2 to S3
* ACG: complete exam prep couse (1hr)

12/11
* fixed git code merge error
* helped to fix wrapper issue

12/10
* helped Pratap on setting parameters to EMR encryption
* helped on bootstrap scripts for package installation
* debug SFS transmission

12/7
* Helped Ramada prepare package requirements.txt for EMR bootstrap
* Help Pratap on wrapper calling pop

12/6
* PGP encryption/decryption
* Key generation, need to find the procedure for production env
* work with Shruthi, Pratap, Ramana to show them how to create virtual env
* Need them to merge their refactored code to project repo to continue the unit test

12/4
 * helped Pratap fixing S3 copy problem
 * refactor execute.sh shell script and wrapper Python code
 * continue to write unit test for S3 listener module

12/3
 *	went through confluence pages
 *	check out code in develop branch
 *	unit tests to existing code

