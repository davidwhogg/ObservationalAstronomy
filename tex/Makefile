ALL= \
	astronomy.pdf \
	syllabus.pdf \
	findobject.pdf \
	celestial.pdf \
	starrynight.pdf \
	ecliptic.pdf \
	exoplanets.pdf \
	galclass.pdf \
	moon.pdf \
	planets.pdf \
	milkyway.pdf \
	galaxies.pdf \
	deepsky.pdf \
	starspec.pdf \
	lenses.pdf \
	firstlook.pdf \
	dialing.pdf \
	observing.pdf \
	moonview.pdf \
	saturn.pdf \
	observing.pdf

DEPEND_TEX= \
	inventory.tex \
	telescope.tex  \
	preamble.tex \
	celestial_questions.tex \
	telescope_questions.tex \
	rotation_orbit_questions.tex \
	constellation_questions.tex \
	finding_questions.tex \
	stars_questions.tex \
	variable_questions.tex \
	galaxies_questions.tex \
	jupiter_text.tex \
	starspec_text.tex  \
	moon_questions.tex \
	planets_questions.tex  \
	pmoons_questions.tex  \
	precession_questions.tex \
	tides_questions.tex  \
	small_questions.tex  \
	celestial_text.tex \
	exoplanets_text.tex  \
	moon_text.tex  \
	planets_text.tex \
	ecliptic_text.tex  \
	deepsky_text.tex  \
	lenses_text.tex \
	sn_info.tex  \
	galaxies_text.tex  \
	milkyway_text.tex \
	firstlook_text.tex  \
	saturn_text.tex  \
	moonview_text.tex \
	dialing_text.tex \
	observing_text.tex  \
	starrynight_text.tex \
	syllabus_text.tex

%.dvi: %.tex 
	latex $*; bibtex $*; latex $*; latex $*

%.pdf: %.dvi $(DEPEND_TEX)
	dvips -Ppdf -N0 -o $*.ps $*.dvi
	ps2pdf $*.ps
	rm $*.ps

astronomy.pdf: astronomy.dvi $(DEPEND_TEX)
	dvips -Ppdf -N0 -o astronomy.ps astronomy.dvi
	ps2pdf astronomy.ps
	rm astronomy.ps

all: $(ALL)

fullclean:
	rm $(ALL) *.log *.dvi *.aux *.bbl *.blg

dummy:
