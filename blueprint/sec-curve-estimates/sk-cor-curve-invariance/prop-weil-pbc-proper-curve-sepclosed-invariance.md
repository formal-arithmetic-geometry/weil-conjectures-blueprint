+++
id = "prop-weil-pbc-proper-curve-sepclosed-invariance"
kind = "theorem"
title = "Proper curve invariance over separably closed fields"
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isSepClosed"]
order = 1249
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-curve-constructible-primary-reduction", "lemma-weil-pbc-curve-dense-open-reduction", "lemma-weil-pbc-curve-locally-constant-reduction", "lemma-weil-pbc-curve-normalization-constant", "lemma-weil-pbc-curve-separably-closed-passage", "lemma-weil-pbc-finite-pushforward-extension-zero", "lemma-weil-pbc-universal-homeomorphism-coverings", "lemma-weil-pbc-universal-homeomorphism-site-equivalence", "prop-weil-pbc-algebraically-closed-extension", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $k\subseteq k'$ be separably closed fields, $C$ a proper $k$-scheme of
dimension at most one, and $F$ a torsion etale sheaf. Then

$$
H^q(C,F)\xrightarrow{\sim}H^q(C_{k'},F|)
$$

for every $q$.
