+++
id = "prose-02-01"
kind = "hidden"
title = "Why the pro-étale site, and the plan"
order = 896
+++
Every coefficient sheaf and every operation in these notes lives on
$X_{\mathrm{pro\acute et}}$, the pro-étale site of Bhatt and Scholze (BS). The
reason for working there is that $\ell$-adic sheaves are inverse limits
of torsion sheaves, and on the étale site inverse limits are not exact,
so that $\ell$-adic cohomology has to be defined by hand as a limit of
torsion cohomology. On $X_{\mathrm{pro\acute et}}$ sequential limits of sheaves behave
well, and $\ell$-adic sheaves become ordinary module sheaves over a
single sheaf of rings. For this to be useful we need two things from the
site. First, limits must be computable. We show that $X_{\mathrm{pro\acute et}}$ has a
basis of affine objects on which taking sections is exact
(Theorem [sk-thm-pe-weakly-contractible-basis]), and this makes products and
sequential limits exact. These objects are spectra of w-contractible
rings, over which every faithfully flat ind-étale cover splits, and
they play the role that strictly henselian local rings play on the
étale site. Second, we must not lose the torsion theory: the
comparison theorems say that for sheaves coming from the étale site,
pro-étale and étale cohomology agree, so that the classical results
with finite coefficients remain available, and that continuous
$\ell$-adic cohomology is recovered as pro-étale cohomology.
The exactness results are what allow us, in Section “Coefficients, constructible complexes and the main theorem”, to
treat $\ell$-adic sheaves as module sheaves, and the comparison theorems
are what allow the torsion arguments of
Sections “Proper base change”, “Construction of the exceptional inverse image”
and “The exceptional inverse image preserves constructibility” to be carried out on the étale site.

Throughout this section, schemes are arbitrary unless a result states a
finiteness hypothesis, because objects of $X_{\mathrm{pro\acute et}}$ are in general
neither Noetherian nor of finite type, even when $X$ is a variety. The standing
assumption that schemes are of finite type over $k$ resumes in
Section “Coefficients, constructible complexes and the main theorem”.

The objects one has in mind are inverse limits of étale $X$-schemes.
Being such a limit is a condition on a presentation, which is awkward to
work with, so we take as objects the weakly étale $X$-schemes of the
following definition. This class is defined by flatness conditions, so it is stable under
base change and composition, and membership in it is local for the
Zariski topology (Lemma [sk-lem-pe-weakly-etale-stability]). Conversely,
after a faithfully flat refinement every weakly étale scheme becomes
a limit of étale schemes (Theorem [sk-thm-pe-indetale-refinement]).
