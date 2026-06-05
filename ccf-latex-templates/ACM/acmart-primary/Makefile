#
# Makefile for acmart package
#
# This file is in public domain
#

PACKAGE=acmart


PDF = $(PACKAGE).pdf acmguide.pdf


all:  ${PDF}
	cd samples && ${MAKE} $@

%.pdf:  %.dtx   $(PACKAGE).cls
	pdflatex $<
	- bibtex $*
	pdflatex $<
	- makeindex -s gind.ist -o $*.ind $*.idx
	- makeindex -s gglo.ist -o $*.gls $*.glo
	pdflatex $<
	while ( grep -q '^LaTeX Warning: Label(s) may have changed' $*.log) \
	do pdflatex $<; done


acmguide.pdf: $(PACKAGE).dtx $(PACKAGE).cls
	pdflatex -jobname acmguide $(PACKAGE).dtx
	- bibtex acmguide
	pdflatex -jobname acmguide $(PACKAGE).dtx
	while ( grep -q '^LaTeX Warning: Label(s) may have changed' acmguide.log) \
	do pdflatex -jobname acmguide $(PACKAGE).dtx; done

%.cls:   %.ins %.dtx
	pdflatex $<

%-tagged.cls:   %.ins %.dtx
	pdflatex $<




.PRECIOUS:  $(PACKAGE).cfg $(PACKAGE).cls $(PACKAGE)-tagged.cls

docclean:
	$(RM)  *.log *.aux \
	*.cfg *.glo *.idx *.toc \
	*.ilg *.ind *.out *.lof \
	*.lot *.bbl *.blg *.gls *.cut *.hd \
	*.dvi *.ps *.thm *.tgz *.zip *.rpi
	cd samples && ${MAKE} $@


clean: docclean
	$(RM)  $(PACKAGE).cls $(PACKAGE)-tagged.cls 
	cd samples && ${MAKE} $@

distclean: clean
	$(RM)  *.pdf 
	cd samples && ${MAKE} $@

#
# Archive for the distribution. Includes typeset documentation
#
archive:  all clean
	COPYFILE_DISABLE=1 tar -C .. -czvf ../$(PACKAGE).tgz --exclude '*~' --exclude '*.tgz' --exclude '*.zip'  --exclude CVS --exclude '.git*' $(PACKAGE); mv ../$(PACKAGE).tgz .

zip:  all clean
	zip -r  $(PACKAGE).zip * -x '*~' -x '*.tgz' -x '*.zip' -x CVS -x 'CVS/*'

# distros
distros: all docclean
	zip -r acm-distro.zip  \
	acmart.pdf acmguide.pdf samples *.cls ACM-Reference-Format.* \
	--exclude samples/sample-acmengage*
	zip -r acmengage-distro.zip samples/sample-acmengage* \
	samples/*.bib \
	acmart.pdf acmguide.pdf  *.cls ACM-Reference-Format.*

acmcp.zip: all acmart.cls
	zip $@ $+

