+++
id = "direct-and-inverse-image-and-the-exchange-morphism"
kind = "section"
title = "Direct and inverse image and the exchange morphism"
order = 1185
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-cohomology-resolution-independent", "prop-weil-pbc-geometric-stalks-exact", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
The two functors and the comparison map that the whole proper-base-change
question is about. Direct image [def-weil-pbc-direct-image]; inverse image
[def-weil-pbc-inverse-image], exact [prop-weil-pbc-inverse-image-exact], with
a derived adjunction [prop-weil-pbc-inverse-image-derived-adjunction]. Then
extension by zero along an etale map [def-weil-pbc-etale-sum-extension], the
exact left adjoint that makes etale restriction preserve injectives
[lem-weil-pbc-etale-restriction-injectives], and with those the computation of
the higher direct images on etale objects for a quasi-compact quasi-separated
morphism [lem-weil-pbc-qcqs-higher-direct-image].

Those two etale-restriction statements are filed under pointed neighbourhoods
in the source, which is neither what they are about nor where they are used;
they are here, ahead of the lemma that needs them, and the direct-image
computation moves after them. A cartesian square carries
a *chosen* identification [def-weil-pbc-cartesian-square-detailed], and the
underived [def-weil-pbc-underived-exchange-detailed] and derived
[def-weil-pbc-derived-exchange-detailed] exchange morphisms are the mates it
determines — named maps, not unnamed isomorphisms, which is what lets the
coherence equations [lem-weil-pbc-exchange-identity-pasting] be stated at
all.
