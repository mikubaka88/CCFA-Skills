#
# Makefile for acmart samples
#
# This file is in public domain
#

ENGINE = pdflatex

BIBENGINE = bibtex


TEX =  $(shell grep '\\file' samples.ins | sed 's/^[^{]*{//' | sed 's/}.*//')

PDF = ${TEX:%.tex=%.pdf}

all: ${PDF}

%.tex: samples.ins samples.dtx
	pdflatex $<

acmart.cls : ../acmart.cls
	cp $< $@

ACM-Reference-Format.bst: ../ACM-Reference-Format.bst
	cp $< $@

acm-jdslogo.png: ../acm-jdslogo.png
	cp $< $@

%.bbx: ../%.bbx
	cp $< $@

%.cbx: ../%.cbx
	cp $< $@

%.dbx: ../%.dbx
	cp $< $@


%.pdf: %.tex acmart.cls ACM-Reference-Format.bst
	${ENGINE} $*
	- ${BIBENGINE} $*
	${ENGINE} $*
	while ( grep -q 'Warning: .* may have changed' $*.log) \
	  do ${ENGINE} $*; done


acmcp.pdf: acm-jdslogo.png

acmsmall-biblatex.pdf: BIBENGINE=biber

acmsmall-biblatex.pdf: acmauthoryear.bbx acmauthoryear.cbx acmdatamodel.dbx 

sigconf-biblatex.pdf: BIBENGINE=biber

sigconf-biblatex.pdf: acmdatamodel.dbx acmnumeric.bbx acmnumeric.cbx

sigconf-lualatex.pdf: ENGINE=lualatex

acmsmall-tagged.pdf: ENGINE = lualatex-dev

docclean:
	${RM} acmart.cls \
	acmart-tagged.cls \
	ACM-Reference-Format.bst \
	*.log *.aux *.out \
	*.bbl *.blg *.cut *.toc \
	acm-jdslogo.png \
	*.run.xml *.bcf *.html 

clean: docclean
	$(RM) *.tex


distclean: clean
	${RM} ${PDF}
