+++
id = "thm-sp-grothendieck"
kind = "theorem"
title = "Grothendieck spectral sequence"
order = 546
lean = ["CategoryTheory.Functor.exists_grothendieckSpectralSequence", "CategoryTheory.Functor.grothendieckSpectralSequence", "CategoryTheory.Functor.nonempty_grothendieckSpectralSequence_page_two_iso", "CategoryTheory.Functor.grothendieckSpectralSequence_abutsTo", "CategoryTheory.Functor.grothendieckSpectralObjectFunctor", "CategoryTheory.Functor.grothendieckBottomEdgeMap", "CategoryTheory.Functor.grothendieckLeftEdgeMap"]
uses = ["def-sp-composite-acyclicity", "def-sp-convergence", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-left-exact-additive", "def-sp-truncation-couple", "lem-sp-couple-morphism", "lem-sp-edge-collapse", "lem-sp-kinjective-computes", "thm-sp-half-plane-convergence", "thm-sp-if-e1"]
+++
Let $\mathcal A\xrightarrow{F}\mathcal B\xrightarrow{G}\mathcal C$ be left
exact additive functors with $\mathcal A$, $\mathcal B$ Grothendieck abelian
and $\mathcal C$ abelian, such that $F$ sends injectives to $G$-acyclics (as
for a composable pair [def-sp-composite-acyclicity]). For every $X\in\mathcal A$ there is a
functorial first-quadrant spectral sequence whose $E_2$-page is

$$
 E_2^{p,q}=R^pG\bigl(R^qF(X)\bigr)
$$

and which converges to $R^{p+q}(G\circ F)(X)$; its edge maps in degree $n$
have directions $R^nG(F(X))\to R^n(G\circ F)(X)\to G(R^nF(X))$, and the
spectral sequence depends functorially on $X$.
