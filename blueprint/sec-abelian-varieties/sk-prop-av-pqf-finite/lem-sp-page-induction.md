+++
id = "lem-sp-page-induction"
kind = "lemma"
title = "Page induction"
lean = ["CategoryTheory.SpectralSequence.Hom.isIso_hom", "CategoryTheory.SpectralSequence.Hom.isIso_pageInfinity"]
order = 518
uses = ["def-sp-spectral-sequence"]
+++
Let $\varphi:E\to E'$ be a morphism of spectral sequences
[def-sp-spectral-sequence] starting at the page $r_0$. If $\varphi$ is an
isomorphism on the page $E_{r_0}$, then it is an isomorphism on every page
$E_r$, $r\geq r_0$. In particular, for first-quadrant cohomological spectral
sequences starting at $E_2$, an isomorphism on the $E_2$-page is an
isomorphism on the stable terms
$E_\infty^{p,q}=E_{p+q+2}^{p,q}$.
