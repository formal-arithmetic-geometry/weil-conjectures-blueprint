+++
id = "prop-sf-hom-ctf-bounded-projective"
kind = "theorem"
title = "Derived internal Hom with a bounded projective complex"
order = 3422
tags = ["latex:proposition"]
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "def-weil-site-perfect-complex", "lem-sf-flat-model", "lem-sf-hom-finite-projective", "lem-sf-tensor-ctf", "prop-sf-dualizable", "prop-sf-dualizable-hom"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, $n\geq1$, and put
$\Lambda=A_{E,n}$. Let $X$ be a finite-type $k$-scheme and let
$P$ be a bounded complex of finite projective $\Lambda_X$-modules with
$P^i=0$ for $i\notin[c,d]$; by
[def-weil-site-perfect-complex] such a $P$ is perfect on the
coefficient site. Let $M\in D^b_{ctf}(X,\Lambda)$ have finite Tor
amplitude in $[a,b]$. Then

$$
R\mathcal H om_X(P,M)\cong P^\vee\otimes_{\Lambda_X}^LM,
\qquad P^\vee=R\mathcal H om_X(P,\Lambda_X),
$$

and $R\mathcal H om_X(P,M)$ lies in $D^b_{ctf}(X,\Lambda)$ with finite
Tor amplitude in $[a-d,b-c]$. In particular the internal Hom is closed on
$D^b_{ctf}(X,\Lambda)$ whenever its first variable is a bounded complex of
finite projective modules.

## Proof

The hypothesis of [prop-sf-dualizable-hom] is satisfied by $P$: a
bounded complex of finite projective $\Lambda_X$-modules is bounded
constructible, the finite projective modules being locally constant with
finite stalks, and it has finite Tor amplitude in its own degree range
$[c,d]$, because a bounded-above complex of flat sheaves is K-flat and
tensoring it with a module sheaf in degree zero produces a complex
concentrated in $[c,d]$, which is the criterion of
[lem-sf-flat-model]; the finite projective modules are flat. Hence the
identification $R\mathcal H om_X(P,M)\cong P^\vee\otimes_{\Lambda_X}^LM$
holds by [prop-sf-dualizable-hom]. By
[lem-sf-hom-finite-projective] the dual $P^\vee$ is termwise the
finite projective module $\mathcal H om_X(P^i,\Lambda_X)$, so $P^\vee$
is again a bounded complex of finite projective modules, now with terms in
degrees $[-d,-c]$, and it is perfect in the sense of
[def-weil-site-perfect-complex] by [prop-sf-dualizable]; the same
argument as for $P$ gives $P^\vee\in D^b_{ctf}(X,\Lambda)$ with finite
Tor amplitude in $[-d,-c]$. Therefore
[lem-sf-tensor-ctf](ii) applies to the pair $(P^\vee,M)$, giving that
$P^\vee\otimes_{\Lambda_X}^LM$ lies in $D^b_{ctf}(X,\Lambda)$ with finite
Tor amplitude in $[a-d,b-c]$.
