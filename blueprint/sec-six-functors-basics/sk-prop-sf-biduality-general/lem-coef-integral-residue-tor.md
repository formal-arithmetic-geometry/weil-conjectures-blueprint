+++
id = "lem-coef-integral-residue-tor"
kind = "lemma"
title = "The residue reduction controls integral Tor amplitude"
order = 2477
uses = ["sk-def-sfb-bounded-constructible", "det-prop-integral-criterion-reductions", "def-weil-finite-tor-amplitude", "lem-exc-residue-tor-test", "sk-thm-existence"]
+++
Let $R=\mathcal O_E$, regarded as a condensed ring, and let
$K\in D^b_c(X,R)$ be an object of the condensed bounded constructible
category ([sk-def-sfb-bounded-constructible]), with reductions
$K_n=K\otimes^L_{\mathcal O_{E,X}}(A_{E,n})_X$. If $K_1$ has
cohomology in $[a,b]$, then every $K_n$ has Tor amplitude
in $[a,b]$. Consequently

$$
D^b_c(X,R)=D^b_{ctf}(X,R)
$$

for this DVR coefficient category, as recorded in [sk-thm-existence]. This does not equate
constructibility with site-perfectness on the whole scheme.
