+++
id = "lem-sf-kunneth-coherence"
kind = "lemma"
title = "Coherence of the relative product"
order = 2533
uses = ["def-compact-support-direct-image-detailed", "def-sf-pf", "lem-sf-mate", "prop-compactification-coherence-detailed", "prop-sf-pf-coherence", "thm-sf-comp-composition", "thm-sf-kunneth-relative", "thm-sf-pf-finite"]
+++
In the setting of [thm-sf-kunneth-relative], the isomorphism
$R(f\times_Bg)_!(K\boxtimes L)\cong Rf_!K\otimes^LRg_!L$ is compatible with

1. **(i)** the symmetry $K\boxtimes L\cong L\boxtimes K$;
1. **(ii)** the triple product: the two iterated isomorphisms
$R(f\times_Bg\times_Bh)_!(K\boxtimes L\boxtimes M)\cong (Rf_!K\otimes^LRg_!L)\otimes^LRh_!M$ and
$Rf_!K\otimes^L(Rg_!L\otimes^LRh_!M)$ agree;
1. **(iii)** base change of the base $B'\to B$;
1. **(iv)** the projection formula of [def-sf-pf].

Consequently the $n$-fold products, and the closed-subscheme compact-support forms of
[thm-sf-kunneth-relative], are defined without ambiguity.
