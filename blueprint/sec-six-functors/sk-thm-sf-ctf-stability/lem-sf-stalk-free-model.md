+++
id = "lem-sf-stalk-free-model"
kind = "lemma"
title = "Finite free models of the geometric stalks"
order = 2335
uses = ["def-weil-finite-tor-amplitude", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "lem-exc-residue-tor-test"]
+++
Let $A=A_{E,n}$, and let $K$ be a bounded complex of $A$-modules on a
small étale site whose cohomology
sheaves are constructible, of finite
Tor amplitude in $[a,b]$. Then
for every geometric point
$\bar x$ the stalk $K_{\bar x}$ is isomorphic in $D(A)$ to a bounded
complex of finite free $A$-modules concentrated in degrees $[a,b]$.

## Proof

The converse direction of [lem-exc-residue-tor-test] is proved by
constructing precisely this model: the stalk $K_{\bar x}$ is a bounded
complex with finitely generated cohomology over the Artinian local ring
$A$, the minimal-resolution construction of that proof produces a
bounded-above complex of finite free $A$-modules representing it whose
differentials have entries in the maximal ideal, tensoring it with
$\kappa=A/(\varpi_E)$ kills all differentials, and Nakayama's lemma
together with the assumed vanishing of $K\otimes^L_A\kappa$, which holds
in $[a,b]$ by the definition of finite Tor amplitude, forces every term
outside $[a,b]$ to vanish. That model is the asserted bounded complex of
finite free modules.
