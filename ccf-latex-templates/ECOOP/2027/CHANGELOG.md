LIPICS Style - CHANGELOG

* 11/05/2023 lipics-v2021 v3.1.3
  * Bugfix
      * changed order of loading hyperxmp and hyperref to avoid minor bug when using lastest version of hyperxmp

* 04/05/2021 lipics-v2021 v3.1.2
  * New feature
        * added optional \subtitle
        * revised displaying of swhids (hid contextual information)
  * Bugfix
        * fixed problem with numberwithinsect in combination with thm-restate,cleveref, autoref (This fixes #15)
        * Fixing "supplemenatary" typo #14

* 25/02/2021 lipics-v2021 v3.1.1
  * Bugfix
        * corrected typo

* 04/01/2021 lipics-v2021 v3.1.0
    * New feature
        * added documentclass option pdfa to explicitly enable generation of PDF according PDF/A standard
    * Bugfix
        * fixed problems when using old versions of hyperxmp package (This fixes #11)

* 09/12/2020 LIPIcs-v2021 v3.0.1
    * Bugfix
        * fixed bug related to unavailable sRGB.icc (This fixes #10)

* 01/12/2020 LIPIcs-v2021 v3.0
    * New Feature
        * more compact presentation of author information (email address and homepage URL only as logo)
        * adjustment of document licence to CC-BY 4.0
        * added anonymization (documentclass option "anonymous") also for \relatedversion and \supplement macros; resolves #9
        * added \claimqedhere to be used in claimproof environments (similar to qedhere in proof environments); resolves #4
        * added new macro \flag to display a flag or logo near the funding information as requested by some funding agencies (e.g. ERC grant)
        * added \proofsubparagraph to allow structuring of proofs
        * added new macros \relatedversiondetails and \supplementdetails to collect information regarding related version/supplementary material in a more structured way
        * added new theorem-like environments 'conjecture' and 'observation'
        * added support to produce PDFs according PDF/A-3B standard
    * Minor changes
        * revised style of procedure environment provided by algorithm2e package
    * Bugfix
        * fixed bug related to loaded but unused algorithm package (This fixes #2)
        * fixed bug related to outdated algorithm2e package (This fixes #3)
        * minor issues related to cleveref package (n-dash, oxford comma)

* 29/04/2020 LIPIcs-v2019 v2.2.1
    * Minor changes
        * export of several page numbers (end top matter, start/end bibliography, start appendix) into aux-file
        * renamed heading of \supplement macro to "Supplementary Material"

* 19/07/2019 LIPIcs-v2019 v2.2
    * New Feature
        * explicitly defined/named colors used in style to ease reusing them (requires load of package xcolor instead of color)
        * added document option "authorcolumns" to activate displaying author details in two columns (only allowed for more than 6 authors)
        * revised style of algorithm environments provided by algorithm or algorithm2e packages
        * added qed-like symbol to mark end of e.g. definitions (command \lipicsEnd)
    * Bugfix
        * fixed problem caused by "\\" in title macro

* 06/06/2019 LIPIcs-v2019 v2.1
    * New Feature
        * added document option "anonymous" to make author related information anonymous (e.g. for double-blind review)
    * Bugfix
        * fixed problems with using thm-restate (added new documentclass option thm-restate)
        * fixed bug when using algorithm2e package and cleveref package
        * fixed problems with texorpdfstring in author macro
        * fixed spacing variation between author name and orcid symbol
        * capitalised labels when using autoref (e.g. section -> Section)


* 10/12/2018 LIPIcs-v2019 v2.0
    * New Features
        * support of metadata in PDF file (e.g. author, title, keywords)
        * revised displaying of author-related funding acknowledgements (now displayed as part of the funding block instead of footnotes)
        * added support for cleveref package (new document option 'cleveref')
        * added support for using autoref for theorem-like environments (new document option 'autoref')
        * added new environment claim and claimproof to realize sub-proofs
        * added new environment proposition
    * Bugfixes
        * fixed problems with theorem-like environments when using cleveref and autoref (see new features above)
        * switched several URL from http to https
        * fixed problems with using of ACM 2012 classification (deactivated subjclass and revised support of ccsdesc macro)
    * Minor changes
        * moved ORCID symbol behind author name (according https://orcid.org/content/journal-display-guidelines)
        * added separator \and to split several affiliations
        * added warnings when package 'enumitem' or 'paralist' are loaded; they manipulate the pre-defined enumeration styles and are partly incompatible
        * preloaded package 'microtype' in style
        * revised spacings/font sizes for top matter

* 09/04/2018 LIPIcs-v2018 v1.5
    * Bugfixes
        * Fixed problem with page style in case of many authors
        * Fixed aggregation of authors for ToC file

* 15/03/2018 LIPIcs-v2018 v1.4
    * Bugfixes
        * Fixed enumerations
        * Fixed aggregation of authors for ToC file

* 26/02/2018 LIPIcs-v2018 v1.3
    * Bugfixes
        * Fixed \hideLIPIcs
        * Fixed enumerations
        * Fixed typo
        * Revised display of ORCIDs following recommendation by ORCID

* 06/02/2018 LIPIcs-v2018 v1.2
    * Release of LIPIcs-v2018
        * revised author macro \author{name}{affil}{email}{orcid}{funding}
        * added support for ORCIDs
        * switched to ACM 2012 classification system
        * added new macros for extended metadata \category, \relatedversion, \supplement, \funding, \acknowledgements
        * added warnings for missing mandatory metadata
        * added preconfigured enumeration styles based on the enumerate package
        * added option \hideLIPIcs to hide all LIPIcs related information
        * added support for line numbers
    * Bugfixes
        * fixed copyright line
        * added warning when using outdated subfig package due to incompatibilities in preloaded subcaption package
        * fixed bug when using MnSymbol package
        * fixed bug in numbering in theorem-like environments used in appendix
        * fixed problems in ToC file
