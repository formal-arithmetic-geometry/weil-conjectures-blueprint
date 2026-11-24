+++
id = "prose-06-09"
kind = "hidden"
title = "Smooth morphisms (1)"
order = 557
+++
Let $f:X\to S$ be smooth of relative dimension $d$. Extending the formula
$\href{@theorem-existence-exceptional-inverse-image}{p^!}=p^*\href{@definition-tate-twists}{(1)}[2]$ for $p:\mathbf P^1_S\to S$, we show in
Proposition [proposition-exceptional-inverse-image-smooth-morphism] that
$\href{@theorem-existence-exceptional-inverse-image}{f^!N}\simeq f^*N\otimes^{\mathbf L}\omega_f$ with $\omega_f$ locally
isomorphic to [$A(d)[2d]$](@definition-tate-twists). We need this formula in the proof of [generic constructibility](@theorem-generic-constructibility-base-change-rj) below, because
it must control $Rf_*L$ for a locally constant sheaf $L$. Indeed, we know nothing about $Rf_*L$ directly, whereas the [finiteness theorem](@theorem-results-from-etale-theory) and [proper base change](@theorem-results-from-etale-theory) control [$Rf_!$](@proposition-construction-independence-rf-shriek). With the formula, however, the adjunction $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ becomes a duality between
$Rf_*L$ and [$Rf_!$](@proposition-construction-independence-rf-shriek) of the twisted dual of $L$
(Lemma [lemma-smooth-morphisms-locally-constant-sheaves]). On a manifold, Poincaré duality exchanges ordinary and compactly supported cohomology in the same way.

For example, let $f:\mathbf G_m\to\operatorname{Spec}\bar k$ and
$L=A=\Fell$. The [localization triangle](@proposition-extension-zero-restriction-closed-subscheme) for the origin of
$\mathbf A^1$ and $R\Gamma_c(\mathbf A^1_{\bar k},A)\simeq \href{@definition-tate-twists}{A(-1)}[-2]$
give $R\Gamma_c(\mathbf G_m,A)\simeq\fib\bigl(\href{@definition-tate-twists}{A(-1)}[-2]\to A\bigr)$.
Hence $H^1_c=A$ and $H^2_c=\href{@definition-tate-twists}{A(-1)}$ are the only nonzero groups, and
$R\Gamma_c(\mathbf G_m,\href{@definition-tate-twists}{A(1)}[2])$ has cohomology [$A(1)$](@definition-tate-twists) in degree
$-1$ and $A$ in degree $0$. Its dual has $A$ in degree $0$ and
[$A(-1)$](@definition-tate-twists) in degree $1$. This is indeed $R\Gamma(\mathbf G_m,A)$,
with $H^1=\href{@definition-tate-twists}{A(-1)}$ given by the Kummer torsors.

The duality must also commute with base change. This requires the [base
change isomorphism](@definition-exceptional-base-change-finite) $g'^*\href{@theorem-existence-exceptional-inverse-image}{f^!}\simeq \href{@theorem-existence-exceptional-inverse-image}{f'^!}g^*$ for smooth $f$, and for it the
local form $\omega_f|_U\simeq \href{@definition-tate-twists}{A_U(d)}[2d]$ on charts suffices. A global identification of $\omega_f$ with [$A_X(d)[2d]$](@definition-tate-twists), by contrast, needs a trace map for $f$; it is part of [smooth purity](@theorem-smooth-purity-all-admissible-coefficients)
(Chapter [chap-Smooth-purity]). For the local form we use that, Zariski locally on $X$ and $S$, a smooth morphism $f:X\to S$ factors as an étale morphism to some
$\mathbf A^d_S$ followed by the projection to $S$, and the next lemma treats these two kinds of morphisms.
