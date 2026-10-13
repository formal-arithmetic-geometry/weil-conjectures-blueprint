+++
id = "sk-d-six"
kind = "definition"
title = "The geometric operation package"
order = 2612
uses = ["sk-d-setup"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations"]
tags = ["sketch"]
+++
Over a base scheme $s$, use the pro-étale functors

$$
f^*,\quad Rf_*,\quad Rf_!,\quad f^!,\quad\otimes_A^{\mathrm L},\quad\RHom_A,
$$

with the adjunctions $f^*\dashv Rf_*$ and $Rf_!\dashv f^!$, the latter whenever
$f$ is compactifiable and $Rf_!$ has a right adjoint. Here $f^*$ and $f^!$
already denote derived functors; the functors and the two adjunctions are
given, not part of the package. A *geometric operation package* consists of the
coefficient subcategories $D^b_{ctf}(X,A)$ of [sk-d-setup] together with:

- for every $a_X:X\to s$, a *dualizing complex* $\omega_X$ with
  $\omega_X\simeq a_X^!A$ whenever $a_X$ is compactifiable, a normalization
  $\omega_s\simeq A_s$, and dualizing composition isomorphisms
  $f^!\omega_Y\simeq\omega_X$;
- isomorphisms $Rf_!\simeq Rf_*$ for proper $f$,
  $Rg_!Rf_!\simeq R(gf)_!$, and $R(\mathrm{id}_X)_!\simeq\mathrm{id}$;
- $!$-base change isomorphisms $g^*Rf_!\simeq Rf'_!g'^*$ for Cartesian squares;
- the projection formula $Rf_!K\otimes_A^{\mathrm L}L\simeq Rf_!(K\otimes_A^{\mathrm L}f^*L)$,
  natural in both variables;
- a monoidal structure on every $f^*$, compatible with the braidings of the
  derived categories (these braidings carry the Koszul sign: the braiding of
  $A_X[1]$ with itself is $-1$).

These data satisfy the coherence conditions: the unit axioms of
$R(\mathrm{id})_!\simeq\mathrm{id}$ against composition; at $f=\mathrm{id}$, the
maps $Rf_!\simeq Rf_*$, $\omega_s\simeq A_s$, $f^!\omega\simeq\omega$ and the unit
of the monoidal structure of $f^*$ are the identity isomorphisms; $Rf_!\simeq Rf_*$
and $f^!\omega_Y\simeq\omega_X$ are compatible with composition; and $!$-base
change is compatible with vertical pasting of Cartesian squares. Put

$$
\begin{gathered}
D_XK=\RHom_A(K,\omega_X),\qquad
R\Gamma_c(X,K)=Ra_{X!}K,\qquad
M\boxt N=p_X^*M\otimes_A^{\mathrm L}p_Y^*N.
\end{gathered}
$$

Finally, two canonical maps are required to be invertible. *Biduality:* for
$K\in D^b_{ctf}(X,A)$, the evaluation-adjoint map $K\to D_XD_XK$ is an
isomorphism. *Künneth–Verdier:* if $s$ is the spectrum of a field, then for
$X$, $Y$ quasi-compact and compactifiable over $s$, $M\in D^b_{ctf}(X,A)$ and
$N\in D^b_{ctf}(Y,A)$, the canonical map
$M\boxt D_YN\to\RHom_A(p_Y^*N,p_X^!M)$ on $X\times_sY$, built from the monoidal
structure of $p_Y^*$, the projection formula for $p_X$, $!$-base change, the
identification $\omega_Y\simeq a_Y^!A$ and the counit of $Ra_{Y!}\dashv a_Y^!$,
is an isomorphism.
Coherence always means equality of component morphisms in ordinary categories.
