+++
id = "lem-weil-pbc-proper-immersion-closed"
kind = "lemma"
title = "Proper immersions are closed immersions"
order = 450
lean = ["AlgebraicGeometry.IsClosedImmersion.of_universallyClosed", "AlgebraicGeometry.IsProper.isClosed_range"]
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-proper-closed-image"]
+++
A universally closed morphism which is an immersion (more generally, which
is a homeomorphism onto its image and surjective on stalks) is a closed
immersion. In particular a proper [def-weil-pbc-scheme-conventions] immersion
is a closed immersion, and its image is closed.
