+++
id = "lem-sf-kunneth-coherence"
kind = "lemma"
title = "Coherence of the relative product"
order = 2189
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

## Proof

The isomorphism of [thm-sf-kunneth-relative] is, by its proof in this
chapter, the composite of the composition law [thm-sf-comp-composition] of
[def-compact-support-direct-image-detailed] — whose coherence, including the
independence of the compactification and the identifications
$Rf_!\cong Rf_*$ for proper $f$, is [prop-compactification-coherence-detailed]
of the proper-base-change chapter — the exchange $\operatorname{Ex}_!$ of
axiom (A2), which is the compact-support base-change theorem of the
compact-support chapter, and the projection transformation of [def-sf-pf], which is axiom
(A3) and is discharged by [thm-sf-pf-finite] together with
[prop-sf-pf-coherence] below. Each of the four assertions is therefore
an identity between composites of canonical maps attached to the same pasted
squares; such identities are the content of [lem-sf-mate], pasting the
squares and using the pentagon of [prop-compactification-coherence-detailed]:
(i) and (ii) reduce to the coherence of the symmetry and
the associativity of $\otimes^L$ with $\operatorname{PF}$
([prop-sf-pf-coherence]), and (iii)–(iv) to the
coherence of $\operatorname{Ex}_!$ with itself and with
$\operatorname{PF}$ in the pasted squares, which is the same mate identity.
