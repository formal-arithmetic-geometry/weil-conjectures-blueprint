+++
kind  = "proof"
of    = "def-weil-weil-sheaf-complex"
uses = ["det-prop-sfb-finite-extension-compatibility", "sk-prop-sfb-qlbar-colimit-x", "lem-sfb-extend-subfield-constructible", "lem-sfb-extend-to-qlbar-constructible", "sk-thm-sfb-qlbar-two-colimit", "def-weil-finite-coefficient-point"]
+++
*The Jordan block.* On $Y=\operatorname{Spec}k$, evaluation at the point is exact
on $\Lambda_Y$-modules ([def-weil-finite-coefficient-point]), so
$\Hom_{\Dbc(Y,\Lambda)}(\Lambda_Y,\Lambda_Y[1])=H^1(Y_{\mathrm{proét}},\Lambda_Y)=0$.
In $D(\Mod_{\mathrm W}(Y,\Lambda))$, on the other hand,
$\Hom(\Lambda,\Lambda[1])=\operatorname{Ext}^1_{\Mod_{\mathrm W}}(\Lambda,\Lambda)$
contains the class of a nonsplit extension $0\to\Lambda\to J\to\Lambda\to0$ of
Weil modules, for instance $J=\Lambda_Y^2$ with $\theta$ given by a unipotent
Jordan block.

*Extension of scalars.* For $E\subset F$ finite inside $\Qlb$, $F_Y$ and
$\overline{\mathbf Q}_{\ell,Y}$ are flat over $E_Y$
([det-prop-sfb-finite-extension-compatibility] (1)), so $M\mapsto M_F$ and
$M\mapsto M_{\Qlb}$ are exact. Since $g_Y^*$ is monoidal and
$g_Y^*F_Y\cong F_Y$, there is a natural isomorphism
$g_Y^*(M_F)\cong(g_Y^*M)_F$, and $(M,\theta)\mapsto(M_F,\theta_F)$ is an exact
functor $\Mod_{\mathrm W}(Y,E)\to\Mod_{\mathrm W}(Y,F)$ commuting with the
forgetful functors. It induces a triangulated functor on derived categories with
$H^i(K_F)=H^i(K)_F$, which preserves bounded complexes with constructible
cohomology ([lem-sfb-extend-subfield-constructible],
[lem-sfb-extend-to-qlbar-constructible]); the same holds for $\Qlb$. Moreover
$M\to M_{\Qlb}$ is injective for every $F_Y$-module $M$: by
[sk-prop-sfb-qlbar-colimit-x], $\overline{\mathbf Q}_{\ell,Y}=\varinjlim_{F'}F'_Y$,
and $F'\cong F^{[F':F]}$ as condensed $F$-modules with $F$ a direct summand, so
$F'_Y$ is a free $F_Y$-module having $F_Y$ as a direct summand.

*(1) Strict Weil complexes.* Let $(K,\theta)$ be a strict Weil complex over
$\Qlb$. By [sk-thm-sfb-qlbar-two-colimit] (2) there are a finite
$E\subset\Qlb$ and $K_E\in\Dbc(Y,E)$ with $K\cong(K_E)_{\Qlb}$. As $g_Y^*$ commutes
with extension of scalars, $\theta$ and $\theta^{-1}$ are morphisms between
objects defined over $E$. By [sk-thm-sfb-qlbar-two-colimit] (1) with $r=0$ they
come from morphisms $\theta_F,\theta'_F$ over some finite $F\supset E$, and after
enlarging $F$ the identities $\theta_F\theta'_F=\mathrm{id}$ and
$\theta'_F\theta_F=\mathrm{id}$ hold over $F$. So
$(K,\theta)\cong((K_E)_F,\theta_F)_{\Qlb}$. If $K$ is a sheaf, then
$H^i((K_E)_F)_{\Qlb}=H^i(K)=0$ for $i\neq0$, hence $H^i((K_E)_F)=0$ by
injectivity of $M\to M_{\Qlb}$, and $(K_E)_F$ is a sheaf. A morphism of strict
Weil complexes between objects defined over $F$ comes from a morphism over some
finite $F'\supset F$ by [sk-thm-sfb-qlbar-two-colimit] (1), and the identity
expressing compatibility with $\theta$ holds after enlarging $F'$.

*(2) Hom groups.* Let $\Lambda$ be $F$ or $\Qlb$. For a $\Lambda_Y$-module $M$
put $\operatorname{Ind}M=\bigoplus_{n\in\mathbf Z}(g_Y^n)^*M$, a Weil module
with $\theta$ the isomorphism
$g_Y^*\operatorname{Ind}M=\bigoplus_n(g_Y^{n+1})^*M\to\operatorname{Ind}M$
that matches the summands. The functor $\operatorname{Ind}$ is exact, as $g_Y^*$
and direct sums are exact, and left adjoint to the forgetful functor: a map of
Weil modules $\operatorname{Ind}M\to(N,\theta_N)$ is determined by its
restriction $M\to N$ to the summand $n=0$, the other components being forced by
compatibility with $\theta_N$. For a Weil module $(N,\theta_N)$ the counit
$\varepsilon:\operatorname{Ind}N\to N$, which is the iterate of $\theta_N$ on
the $n$-th summand, sits in a short exact sequence of Weil modules

$$
0\to\operatorname{Ind}N\xrightarrow{\ 1-s\ }\operatorname{Ind}N
\xrightarrow{\ \varepsilon\ }N\to0,
$$

where $s$ maps the $n$-th summand to the $(n+1)$-st by
$(g_Y^n)^*(\theta_N^{-1})$. Summand by summand this is
$N\otimes_{\mathbf Z}$ of the exact sequence
$0\to\mathbf Z[t^{\pm1}]\xrightarrow{1-t}\mathbf Z[t^{\pm1}]\to\mathbf Z\to0$.
Applied termwise to a complex $K$ of Weil modules it gives a distinguished
triangle
$\operatorname{Ind}\operatorname{For}K\to\operatorname{Ind}\operatorname{For}K
\to K\to$ in $D(\Mod_{\mathrm W}(Y,\Lambda))$. Since $\operatorname{Ind}$ and
$\operatorname{For}$ are exact and adjoint, the adjunction passes to derived
categories, and $\Hom(\operatorname{Ind}\operatorname{For}K,L[r])
=\Hom(\operatorname{For}K,\operatorname{For}L[r])$. Applying $\Hom(-,L[r])$ to
the triangle therefore gives the long exact sequence

$$
\cdots\to\Hom_{\mathrm W}(K,L[r])\xrightarrow{\operatorname{For}}
\Hom(\operatorname{For}K,\operatorname{For}L[r])\xrightarrow{\ 1-\varphi\ }
\Hom(\operatorname{For}K,\operatorname{For}L[r])\to
\Hom_{\mathrm W}(K,L[r+1])\to\cdots,
$$

with $\Hom_{\mathrm W}$ computed in $D(\Mod_{\mathrm W}(Y,\Lambda))$, hence in
$D^b_{c,\mathrm W}(Y,\Lambda)$ for $K,L$ there, the middle terms in
$D(Y_{\mathrm{proét}},\Lambda)$, and
$\varphi(h)=\theta_L[r]\circ Lg_Y^*(h)\circ\theta_K^{-1}$.

Now let $K,L\in D^b_{c,\mathrm W}(Y,E)$. Extension of scalars commutes with
$\operatorname{Ind}$, $\operatorname{For}$, $s$ and $\varepsilon$, so it maps the
sequence for $(K_F,L_F)$ to the one for $(K_{F'},L_{F'})$ and to the one for
$(K_{\Qlb},L_{\Qlb})$, compatibly. Filtered colimits of exact sequences of
abelian groups are exact, so the colimit over $F\supset E$ of the sequences for
$(K_F,L_F)$ is exact and maps to the sequence for $(K_{\Qlb},L_{\Qlb})$. On the
terms $\Hom(\operatorname{For}K_F,\operatorname{For}L_F[r])$ this map is the
isomorphism of [sk-thm-sfb-qlbar-two-colimit] (1), applied to
$\operatorname{For}K,\operatorname{For}L\in\Dbc(Y,E)$. By the five lemma it is an
isomorphism on the terms $\Hom_{\mathrm W}$, which is (2).

*(3) Weil complexes.* Let $K\in D^b_{c,\mathrm W}(Y,\Qlb)$; we induct on the
number of nonzero cohomology sheaves. If there is at most one, $K\cong G[-m]$
for a Weil sheaf $G$, which descends to a Weil sheaf over some finite $F$ by (1).
Otherwise let $m$ be the top degree and consider the truncation triangle
$\tau^{<m}K\to K\to H^m(K)[-m]\xrightarrow{\delta}(\tau^{<m}K)[1]$ in
$D^b_{c,\mathrm W}(Y,\Qlb)$. By induction $\tau^{<m}K\cong A_{\Qlb}$ and
$H^m(K)[-m]\cong B_{\Qlb}$ with $A,B$ over finite extensions, which we may take
to be a common $E$. By (2) with $r=1$, $\delta$ comes from some
$\delta_F:B_F\to A_F[1]$ over a finite $F\supset E$. The cocone $C$ of $\delta_F$
lies in the triangulated subcategory $D^b_{c,\mathrm W}(Y,F)$, and as extension
of scalars is triangulated, $C_{\Qlb}$ is a cocone of $\delta$, hence
$C_{\Qlb}\cong K$.
