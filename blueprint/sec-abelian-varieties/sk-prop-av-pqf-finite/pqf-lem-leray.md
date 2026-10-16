+++
id = "pqf-lem-leray"
kind = "lemma"
title = "Leray spectral sequence"
lean = ["AlgebraicGeometry.Scheme.Modules.exists_leraySpectralSequence"]
order = 542
uses = ["pqf-def-cohomology", "thm-sp-grothendieck"]
+++
Let $f:X\to Y$ be a morphism of schemes and $\mathcal F$ a
quasi-coherent $\mathcal O_X$-module. There is a spectral sequence

$$
E_2^{p,q}=\mathrm H^p\bigl(Y,R^qf_*\mathcal F\bigr)
\quad\Longrightarrow\quad \mathrm H^{p+q}(X,\mathcal F).
$$
