
PREFIX = /usr/local

menge: menge.sh menge.awk menge.tsv
	cat menge.sh > $@
	echo 'exit 0' >> $@
	echo "#EOF" >> $@
	tar cz menge.awk menge.tsv >> $@
	chmod +x $@

test: menge.sh
	shellcheck -s sh menge.sh

clean:
	rm -f menge

install: menge
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f menge $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/menge

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/menge

.PHONY: test clean install uninstall
