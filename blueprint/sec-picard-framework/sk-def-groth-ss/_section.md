+++
id = "sk-def-groth-ss"
kind = "section"
title = "Composable pair with acyclicity; the couple of a double complex"
order = 597
lean = ["CategoryTheory.Functor.IsAcyclicComposablePair", "CategoryTheory.SpectralSequence.Abutment"]
+++
*Definition (sketch).*

Let $\mathcal A\xrightarrow{\,F\,}\mathcal B\xrightarrow{\,G\,}\mathcal C$
be additive functors, where $\mathcal A$ and $\mathcal B$ are Grothendieck
abelian categories (so they have enough injectives and the right derived
functors $R^nF$, $R^nG$, $R^n(G\circ F)$ are computed on injective
resolutions) and $\mathcal C$ is
abelian. An object $B\in\mathcal B$ is *$G$-acyclic* if $R^qG(B)=0$ for
$q>0$, and $(F,G)$ is a *composable pair with acyclicity* if $F(I)$
is $G$-acyclic for every injective $I\in\mathcal A$.

Let $E$ be a first-quadrant cohomological spectral sequence in
$\mathcal C$ starting at $E_2$, and put
$E_\infty^{p,q}:=E_{p+q+2}^{p,q}$ (from this page on the differentials
into and out of $(p,q)$ vanish). An *abutment* of $E$ to a family of
objects $(H^n)_{n\geq0}$ of $\mathcal C$ is a decreasing filtration of
each $H^n$ by subobjects

$$
H^n=F^0H^n\supseteq F^1H^n\supseteq\cdots\supseteq F^{n+1}H^n=0
$$

such that $F^pH^n/F^{p+1}H^n\cong E_\infty^{p,q}$ whenever $p+q=n$.

For a first-quadrant double complex $D^{\bullet,\bullet}$ in $\mathcal C$,
let $\operatorname{Tot}(D)$ be its total complex. Filtering
$\operatorname{Tot}(D)$ by either degree gives a bigraded exact couple,
and its derived couples give the two spectral sequences of $D$. The image
filtration
$F^pH^n=\operatorname{im}\bigl(H^n(F^p\operatorname{Tot}D)\to
H^n(\operatorname{Tot}D)\bigr)$ is an abutment of each of the two spectral
sequences of $D$ to $H^\bullet(\operatorname{Tot}D)$; in the first quadrant
it is finite in each degree, so convergence is automatic.
