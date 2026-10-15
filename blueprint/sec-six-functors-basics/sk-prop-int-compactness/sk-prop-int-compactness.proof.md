+++
kind = "proof"
of = "sk-prop-int-compactness"
uses = ["sk-thm-constructible-compactness", "sk-lem-int-integral-heart", "sk-lem-int-ext", "sk-prop-ind-heart", "sk-cor-ind-heart-ii", "sk-lem-finite-window", "sk-prop-pe-products", "sk-prop-pe-left-complete", "sk-thm-sfb-proper-base-change", "sk-lem-proper-unbounded-window", "sk-lem-proper-unbounded-window-ii"]
+++
*Compactness.* The rational proof ([sk-thm-constructible-compactness]) used
three facts about $\Cons(X,\Lambda)$: it is an essentially small abelian
category closed under extensions, Ext out of a constructible sheaf commutes
with filtered colimits, and the uniform Ext bound. These are
[sk-lem-int-integral-heart] and [sk-lem-int-ext] for $\mathcal O_E$. The
proofs of [sk-prop-ind-heart] and [sk-cor-ind-heart-ii] then give an exact
fully faithful realization of
$\IndCons(X,\mathcal O_E)=\operatorname{Ind}(\Cons(X,\mathcal O_E))$ in
$\Mod(X_{\mathrm{proét}},\mathcal O_E)$, closed under extensions and under
kernels and cokernels of its own morphisms, and the bound $\Ext^q(C,B)=0$ in
$\Mod(X_{\mathrm{proét}},\mathcal O_E)$ for $q>d_C$ and
$B\in\IndCons(X,\mathcal O_E)$. Truncations are taken in the full subcategory
$\Dic(X,\mathcal O_E)$ of complexes with cohomology in
$\IndCons(X,\mathcal O_E)$, which is closed under direct sums and truncations
and contains $\Loc(\Dbc(X,\mathcal O_E))$; the latter need not be stable under
truncation.

The proof of [sk-lem-finite-window] applies with these hypotheses, since
products of sheaves on the pro-étale site are exact and its derived category
is left complete ([sk-prop-pe-products], [sk-prop-pe-left-complete]). Its key
step is the lower tail. Continuity only covers systems with a common lower
bound, while objects of $\Loc(\Dbc(X,\mathcal O_E))$ may be unbounded below.
Along the tower of good truncations, uniform Ext vanishing makes the relevant
tower of Hom groups eventually constant, so the $\varprojlim^1$ term in the
Milnor sequence vanishes. As a result, $\Hom(C,K[m])$, computed in
$D(X_{\mathrm{proét}},\mathcal O_E)$, depends only on the degrees $[m-d_C,m]$
of $K$. On a finite range of degrees, Ext commutes with direct sums by
continuity, and induction on the length of the range shows that $\Hom(C,-)$
commutes with direct sums. Finite truncation of the source extends this to all
of $\Dbc(X,\mathcal O_E)$.

*Proper direct image of $\Dbc$.* This is the integral case of
[sk-thm-sfb-proper-base-change].

*Direct sums.* Let $d$ bound the dimensions of the fibres of $p$. On a weakly
contractible affine $V\to Y$, proper direct image of a torsion sheaf has
cohomology in degrees $\le2d$ (Stacks, Tag 095U), and since $\Gamma(V,-)$ is
exact this bounds cohomology of sections. The reductions of a constructible
sheaf live in degrees $[-1,0]$, and one derived inverse limit adds at most one
degree, so $Rp_*$ of a constructible sheaf has cohomology in degrees
$[0,2d+1]$. By continuity for bounded below systems, the same bound holds for
objects of $\IndCons(X,\mathcal O_E)$: for $N=\varinjlim_iN_i$ with
$N_i\in\Cons(X,\mathcal O_E)$, one has $H^qRp_*N=\varinjlim_iH^qRp_*N_i$, and
these lie in $\IndCons(Y,\mathcal O_E)$ because each $H^qRp_*N_i$ is
constructible by the previous paragraph. Now the proofs of
[sk-lem-proper-unbounded-window] and [sk-lem-proper-unbounded-window-ii]
apply: in a fixed degree $q$, $H^qRp_*K$ depends only on the degrees
$[q-2d-1,q]$ of $K$, and on such a finite range direct sums commute with
$Rp_*$ by induction on the length. This holds for arbitrary families in
$\Dic(X,\mathcal O_E)$, with no common lower bound. Finally, the objects of
$\Loc(\Dbc(X,\mathcal O_E))$ whose direct image lies in
$\Loc(\Dbc(Y,\mathcal O_E))$ form a localizing subcategory containing
$\Dbc(X,\mathcal O_E)$, hence everything.
