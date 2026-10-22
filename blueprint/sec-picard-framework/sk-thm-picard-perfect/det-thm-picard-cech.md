+++
id = "det-thm-picard-cech"
kind = "theorem"
title = "Čech-to-derived"
order = 715
uses = ["det-def-groth-ss"]
lean = ["CategoryTheory.Sheaf.exists_cechToDerivedSpectralSequence"]
+++
Let $\mathcal C$ be an essentially small site with fibre products, $X\in\Ob(\mathcal C)$
and $\mathfrak U=\{U_i\to X\}_{i\in I}$ a family of morphisms generating a covering
sieve of $X$. For an abelian sheaf $F$ on $\mathcal C$ there is a first-quadrant spectral sequence

$$
E_2^{p,q}=\Cech^p\bigl(\mathfrak U,\ \mathcal H^q(F)\bigr)
\ \Longrightarrow\ H^{p+q}(X,F),
$$

where $\mathcal H^q(F)$ is the presheaf $V\mapsto H^q(V,F)$.
