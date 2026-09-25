+++
id = "sk-prop-trace-adic"
kind = "section"
title = "Adic realization"
order = 2384
uses = ["sk-d-setup", "sk-d-six", "sk-d-weil", "sk-p-trace-coeff", "sk-prop-sf-trace-perfectness", "sk-thm-sf-ctf-stability"]
+++
*Proposition (sketch).*

Write $A_n=A_{E,n}$. Call a system
$K_\bullet=(K_n,t_{n+1,n})_{n\ge1}$ with $K_n\in D^b_{ctf}(X,A_n)$
*normalized* if $K_n\otimes^{\mathrm L}_{A_n}A_j\xrightarrow{\sim}K_j$
for $j\le n$, and *uniform* if the $K_n$ share a cohomological range and
Tor amplitude.

3pt
1. **(i)** *Realization.* For a normalized uniform system the derived
limit $K_{\mathcal O_E}=R\varprojlim_nK_n$ is derived complete, lies in the
same range, and satisfies
$K_{\mathcal O_E}\otimes^{\mathrm L}_{\mathcal O_E}A_n\cong K_n$ for every
$n$, compatibly with the transitions.
1. **(ii)** *Compact cohomology and stalks.* The systems
$R\Gamma_c(X,K_n)$ and $(K_n)_{\bar y}$ are normalized systems of perfect
$A_n$-complexes, and realization commutes with both:
$$
R\Gamma_c(X,K_{\mathcal O_E})\cong R\varprojlim_nR\Gamma_c(X,K_n),
\qquad
(K_{\mathcal O_E})_{\bar y}\cong R\varprojlim_n(K_n)_{\bar y},
$$
both perfect over $\mathcal O_E$, and the isomorphisms are equivariant for
the global and local Frobenius operators.
1. **(iii)** *Rationalization and coefficient-field extension.*
$D^b_c(X,E)=D^b_c(X,\mathcal O_E)[1/\varpi]$ has the same objects as the
integral category and morphisms
$\operatorname{Hom}_{\mathcal O_E}(-,-)\otimes_{\mathcal O_E}E$; it is
idempotent complete, and the canonical functor to its Karoubi envelope is an
exact equivalence. Exact $\mathcal O_E$-linear functors and natural
transformations between integral categories transport to the rational ones.
Consequently every $E$-stage object is the rationalization of an integral
system — a lattice — and every $E$-stage morphism is $\varpi^{-N}u$ for
an integral $u$ and some $N$. The $\overline{\mathbf Q}_\ell$-stage is the filtered colimit over
finite $E/\mathbf Q_\ell$, so each of its objects and morphisms is already represented
at a finite stage.

These are the realization statements of
Bhatt–Scholze (Lemma 6.7.16 and §§6.5, 6.7) and Stacks 09AW.

## Proof

(i) The assertion is local, and on a local model the tower is the reduction
tower $L\otimes^{\mathrm L}(P_n)$ of a bounded complex $L$ of finite locally
free modules, with the quotient transitions. Since
$R\varprojlim_n(P_n)=\mathcal O_E$ and $L$ is a bounded finite-locally-free
complex, $R\varprojlim_n\bigl(L\otimes^{\mathrm L}(P_n)\bigr)=L$, so the
derived-limit projections give $L\xrightarrow{\sim}K_{\mathcal O_E}$ on that
model. Derived completeness and the reduction isomorphisms
$K_{\mathcal O_E}\otimes^{\mathrm L}A_n\cong K_n$ follow, and the range is
read off the local models; uniformity of the bounds is what makes the limit
stay in a fixed range.

(ii) Each level is perfect by [sk-prop-sf-trace-perfectness], and the
transitions are morphisms of perfect complexes by naturality of
$R\Gamma_c$ and of stalks; normalizedness of the two systems is
normalizedness of $K_\bullet$ together with the coefficient-reduction
isomorphisms for $Ra_{X!}$ and for $L\bar y^*$, which hold by
[sk-thm-sf-ctf-stability]. Applying (i) over the point $s$ to
$R\Gamma_c(X,K_n)$ and stalkwise to $(K_n)_{\bar y}$ gives the displayed
isomorphisms; a derived-complete complex whose reductions are perfect with
uniform bounds is itself perfect. Equivariance holds because the global and
local Frobenius operators are built from $\varphi^{[m]}$, which commutes with
the transitions by the strict Weil structure at each level
([sk-d-weil]).

(iii) All of this is the construction of the rational category: it is
*defined* as the localization $D^b_c(X,\mathcal O_E)[1/\varpi]$, with the
same objects and with morphisms tensored up to $E$, so the descent of
field-stage objects to integral models is tautological and clearing
denominators is writing an element of
$\operatorname{Hom}\otimes_{\mathcal O_E}E$ as $\varpi^{-N}u$. Idempotent
completeness, and hence the equivalence with the Karoubi envelope, is proved
from the localized $t$-structure; transport of exact functors and of natural
transformations is their $\mathcal O_E$-linearity. For $\overline{\mathbf Q}_\ell$, a filtered
colimit of categories has every object and every morphism represented at a
finite stage, and two representatives agree after a further finite extension.

Uses: [sk-d-setup], [sk-d-six], [sk-d-weil], [sk-p-trace-coeff], [sk-prop-sf-trace-perfectness], [sk-thm-sf-ctf-stability]
