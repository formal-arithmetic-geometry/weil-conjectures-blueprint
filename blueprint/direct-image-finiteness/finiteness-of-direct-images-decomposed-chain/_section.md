+++
id = "finiteness-of-direct-images-decomposed-chain"
kind = "section"
title = "Finiteness of direct images: decomposed chain"
order = 3199
uses = ["cor-galois-open-subgroups", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-extension-by-zero", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit-detailed", "lem-weil-pbc-constructible-serre", "lem-weil-pbc-constructible-subobjects-noetherian", "lem-weil-pbc-finite-direct-image-exact", "lem-weil-pbc-finite-pushforward-constructible-noetherian", "lem-weil-pbc-finite-stalk-formula", "lem-weil-pbc-geometric-stalk-conservative", "sbc-def-coefficient-conventions", "thm-galois-fundamental", "thm-galois-lc-etale"]
+++
Throughout this section $k$ is a field of characteristic prime to $N$,
$\Lambda$ is the finite commutative ring annihilated by $N$ of
[sbc-def-coefficient-conventions], and schemes are of finite type
over $k$; such schemes are Noetherian, quasi-compact, and
quasi-separated. The small etale site of a scheme $X$ and the
notions lisse and constructible are the ones of
def:weil-pbc-constructible-complexes of the ambient-foundations chapter; for a
finite abelian group $M$ the symbol $\underline M$ denotes the constant
$\Lambda$-sheaf, and for a locally closed immersion $j$ the functor
$j_!$ denotes the extension by zero along it, i.e. the composite of
the extension by zero of the open immersion into the closure with the
direct image of the closed immersion, with the stalk description
$(j_!G)_{\bar x}=G_{\bar x}$ for $\bar x$ lying in the open part and
$0$ otherwise, as in def:weil-pbc-extension-by-zero of
the proper-base-change chapter.
