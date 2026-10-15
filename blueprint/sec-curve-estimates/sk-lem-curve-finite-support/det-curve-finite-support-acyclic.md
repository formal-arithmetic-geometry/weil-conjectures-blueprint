+++
id = "det-curve-finite-support-acyclic"
kind = "lemma"
title = "Sheaves supported on finitely many closed points"
uses = ["lem-weil-pbc-zero-dimensional-cohomology", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-geometric-stalk-conservative", "def-sc-field-extension"]
+++
Let $k$ be algebraically closed, $C$ a separated scheme of finite type over
$k$ of dimension at most one, $Z\subseteq C$ a finite set of closed points
with its reduced structure, $i:Z\hookrightarrow C$, and $F$ an abelian sheaf
on $C_{\mathrm{ét}}$ with $F_{\bar x}=0$ for every geometric point $\bar x$
not lying over $Z$. Then:

1. the unit $F\to i_*i^{-1}F$ is an isomorphism;
2. $H^q(C,F)=0$ for $q>0$ and
   $H^0(C,F)\xrightarrow{\sim}\bigoplus_{z\in Z}F_{\bar z}$;
3. for an extension $k\subseteq k'$ of algebraically closed fields, the
   pullback $F_{k'}$ is supported on $Z_{k'}$, which is the set of points
   $z\otimes k'$, its stalks there are $F_{\bar z}$, and the pullback map
   $H^q(C,F)\to H^q(C_{k'},F_{k'})$ is an isomorphism for all $q$.
