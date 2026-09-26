+++
id = "sk-prop-nagata-sketch-zmt"
kind = "section"
title = "Zariski's Main Theorem and affine-space immersions"
order = 180
lean = ["AlgebraicGeometry.Scheme.Hom.exists_isOpenImmersion_isAffineHom_of_locallyQuasiFinite", "AlgebraicGeometry.exists_immersion_affineSpace_of_quasiAffine"]
+++
*Proposition (sketch).*

Let $S$ be qcqs.

2pt
1. **(i)** *(Zariski's Main Theorem.)* A separated, finite-type,
everywhere quasi-finite morphism $f:X\to S$ factors as
$X\xrightarrow{j}T\xrightarrow{p}S$ with $j$ a quasi-compact open immersion
and $p$ finite; if $f$ is locally of finite presentation, $T$ may be taken
finite and of finite presentation over $S$. In particular $f$ is
quasi-affine.
1. **(ii)** A quasi-affine $S$-scheme locally of finite type over $S$ admits
an $S$-immersion into some $\mathbb A^n_S$.

## Proof

(i) Let $N_f$ be the normalization of $S$ in $X$, i.e. the relative
integral closure $\nu_f:N_f\to S$ with
$\nu_{f*}\mathcal O_{N_f}$ the integral closure of $\mathcal O_S$ in
$f_*\mathcal O_X$. Then $\nu_f$ is integral, and because $f$ is everywhere
quasi-finite the canonical $\iota_f:X\to N_f$ is a quasi-compact open
immersion — this is the classical form of the theorem, 02LR, with
the quasi-finite-locus input 03GW. Writing $\nu_f$ as a filtered
limit of finite morphisms and using quasi-compactness of $\iota_f(X)$, the
open immersion already factors through a finite stage $T\to S$, which gives
the stated factorization (05F7, with the finite-presentation
refinement 0F2N). Since a finite morphism is affine, $T\to S$ is
affine, and an open immersion into an affine $S$-scheme is quasi-affine over
$S$; hence $f$ is quasi-affine.

(ii) A quasi-affine scheme is a quasi-compact open subscheme of
$\operatorname{Spec}$ of its ring of global sections. Over a qcqs base this
may be checked on a finite affine cover of $S$; on an affine chart
$\operatorname{Spec}A\subseteq S$ the finite-type hypothesis gives finitely
many sections $t_1,\dots,t_n$ of $\mathcal O_X$ generating the relevant
$A$-algebra, and $(t_1,\dots,t_n)$ defines an $S$-morphism
$X\to\mathbb A^n_S$ which is an immersion. This is 04II.
