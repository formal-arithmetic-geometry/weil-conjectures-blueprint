+++
id = "lem-sc-cech-spectral"
kind = "lemma"
title = "The Cech-to-cohomology spectral sequence"
order = 641
uses = ["thm-sp-double-complex-spectral-sequences"]
lean = ["CategoryTheory.Sheaf.exists_cechToDerivedSpectralSequence"]
+++
Let $\mathcal C$ be an essentially small site with fibre products, $X$ an object of
$\mathcal C$, $\mathfrak U=\{U_i\to X\}$ a family of morphisms generating
a covering sieve of $X$, and $F$ an abelian sheaf on $\mathcal C$. There is
a convergent first-quadrant spectral sequence

$$
E_2^{pq}=\check H^p(\mathfrak U,\underline H^q(F))
\Longrightarrow H^{p+q}(X,F),
$$

where $\underline H^q(F)$ is the presheaf
$V\mapsto H^q(V,F)$ and $\check H^p(\mathfrak U,-)$ is
Cech cohomology with respect to $\mathfrak U$. We apply this to the
étale site $X_{\Et}$ of a scheme $X$ and to the Zariski site.
