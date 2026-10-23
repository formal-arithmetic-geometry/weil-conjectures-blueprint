+++
id = "lem-sf-tensor-ctf"
kind = "lemma"
title = "The derived tensor product on the finite-Tor subcategories"
order = 2841
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-sf-flat-model", "lem-sf-tor-sheaf-constructible", "thm-constructible-serre"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, $n\geq1$, put
$A=A_{E,n}$, and let $X$ be a
finite-type
$k$-scheme. Let $K\in D^b_{ctf}(X,A)$ have
finite Tor amplitude in $[a,b]$,
and let $M\in D^b_c(X,A)$ be
bounded constructible.
Then:

1. **(i)** $K\otimes_A^LM$ belongs to $D^b_c(X,A)$;
1. **(ii)** if in addition $M\in D^b_{ctf}(X,A)$ has finite Tor amplitude
in $[c,d]$, then $K\otimes_A^LM$ belongs to $D^b_{ctf}(X,A)$, with
finite Tor amplitude in $[a+c,b+d]$.
