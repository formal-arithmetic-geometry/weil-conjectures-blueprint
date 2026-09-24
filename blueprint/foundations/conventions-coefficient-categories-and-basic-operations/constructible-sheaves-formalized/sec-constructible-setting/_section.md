+++
id = "sec-constructible-setting"
kind = "section"
title = "Setting"
order = 1439
+++
We keep the conventions of [etale-sheaves-along-a-complementary-open-closed-pair]: schemes live in a
universe $u$; the coefficient category $\mathcal A$ is Grothendieck abelian
with morphisms in $\mathrm{Type}\,(u+1)$; $\et X$ is the small étale site
of $X$ and $\shv{\et X}$ the category of $\mathcal A$-valued sheaves on it;
$g^*\dashv g_*$ is the pullback–pushforward adjunction along a morphism $g$
and $j_!$ the extension by zero along an open immersion. Whenever
finiteness of stalks is mentioned, $\mathcal A$ is moreover concrete over
$\mathrm{Type}\,(u+1)$, and finiteness refers to the underlying set. The
case of interest is $\mathcal A=\mathrm{Mod}_\Lambda$ for a finite ring
$\Lambda$ (in the $\ell$-adic formalism $\Lambda=\Z/\ell^n\Z$); some
statements are only claimed in this case and say so.

A geometric point of $X$ is a morphism $\bar x\colon\spec\Omega\to X$ with
$\Omega$ separably closed; the stalk $\mathcal F_{\bar x}$ is the fibre of
$\mathcal F$ at the corresponding point of the site $\et X$.

The scheme structures $Z_k$ on the strata are part of the datum; by
[lemma-constructible-immersion-independence] below the condition does
not depend on them.
