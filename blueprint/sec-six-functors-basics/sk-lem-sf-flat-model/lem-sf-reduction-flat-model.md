+++
id = "lem-sf-reduction-flat-model"
kind = "lemma"
title = "Reduction of the flat model"
lean = ["AlgebraicGeometry.Etale.reductionModIdeal_flatModel", "AlgebraicGeometry.ProEtale.flatModel_reduction"]
order = 2178
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-etale-site", "def-weil-pbc-proetale-site", "lem-exc-constant-inverse-image-flat", "lem-sf-flat-model"]
+++
Let $A_{E,m}$ and $A_{E,n}$ be two finite coefficient stages with
$m\leq n$, let $T$ be a scheme on which $\ell$ is invertible, let
$K\in D^b_c(T,A_{E,n})$ be a bounded constructible complex of
$A_{E,n}$-modules on the small pro-étale site or on the small étale
site, and let $P\cong K$ be a bounded flat model of $K$ in degrees
$[a,b]$ in the sense of [lem-sf-flat-model]: each $P^q$ is a flat
$A_{E,n}$-module sheaf and $P^q=0$ for $q\notin[a,b]$. Write
$K_m=K\otimes^L_{A_{E,n}}A_{E,m}$ for the reduction of $K$. Then
$P\otimes_{A_{E,n}}A_{E,m}$ is a bounded flat model of $K_m$ in the
same interval:

$$
K_m\cong P\otimes_{A_{E,n}}A_{E,m},\qquad
(P\otimes_{A_{E,n}}A_{E,m})^q=0\quad(q\notin[a,b]),
$$

and each term $P^q\otimes_{A_{E,n}}A_{E,m}$ is a flat
$A_{E,m}$-module sheaf. Consequently the reduction $K_m$ has finite
Tor amplitude in $[a,b]$ as soon
as $K$ does.
