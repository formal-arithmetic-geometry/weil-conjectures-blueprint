+++
id = "lem-sc-cech-spectral"
kind = "lemma"
title = "The Cech-to-cohomology spectral sequence"
order = 600
uses = ["thm-sp-double-complex-spectral-sequences"]
lean = ["CategoryTheory.Sheaf.exists_cechToDerivedSpectralSequence"]
+++
Let $\mathcal C$ be a site with fibre products, $X$ an object of
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

## Proof

Choose an injective resolution $F\to I^{\bullet}$ of abelian sheaves on
$\mathcal C$ and consider the double complex
$C^{pq}:=C^p(\mathfrak U,I^q)$, where
$C^p(\mathfrak U,G)=\prod_{i_0,\dots,i_p}G(U_{i_0}\times_X\dots\times_XU_{i_p})$
is the (alternating) Cech complex of the family $\mathfrak U$ (the fibre
products exist in $\mathcal C$). For each
$V=U_{i_0}\times_X\dots\times_XU_{i_p}$ the restriction of $I^\bullet$ to
$\mathcal C/V$ is again an injective resolution of $F|_V$ (restriction to
the localization has an exact left adjoint), so
$H^q(I^\bullet(V))=H^q(V,F)$. Its cohomology in the second direction is
therefore $C^p(\mathfrak U,\underline H^q(F))$, because taking cohomology
commutes with the products defining the Cech complex;
so the first spectral sequence of the double complex
[thm-sp-double-complex-spectral-sequences] has

$$
E_1^{pq}=C^p(\mathfrak U,\underline H^q(F)),\qquad
E_2^{pq}=\check H^p(\mathfrak U,\underline H^q(F)).
$$

The total complex of $C^{\bullet\bullet}$ computes
$H^{p+q}(X,F)$: for each $q$, an injective abelian sheaf is injective as
a presheaf, and the Cech complex of an injective presheaf with respect to
a family generating a covering sieve is exact in positive degrees with
$H^0=I^q(X)$ (it is $\operatorname{Hom}$ from the exact complex of free
presheaves attached to the family into $I^q$). So the second spectral
sequence collapses onto the bottom edge, the natural map
$I^\bullet(X)\to\operatorname{Tot}C^{\bullet\bullet}$ is a
quasi-isomorphism, and the total cohomology is
$H^{p+q}(I^\bullet(X))=H^{p+q}(X,F)$. The first spectral sequence of
a double complex converges to the cohomology of the total
complex by [thm-sp-double-complex-spectral-sequences] (*reference: Stacks Project, Homological
Algebra: spectral sequences of double complexes*).
