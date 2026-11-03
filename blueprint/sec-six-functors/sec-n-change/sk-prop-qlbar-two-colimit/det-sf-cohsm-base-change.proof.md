+++
kind = "proof"
of = "det-sf-cohsm-base-change"
uses = ["thm-asd-smooth-tensor", "lem-pur-co-smooth-composition", "sk-prop-geo-p1-adjunction"]
+++
*Step 1: the three elementary cases.* (a) For $p:\mathbf P^1_S\to S$ with the
adjunction $Rp_*\dashv p^*(1)[2]$ of [sk-prop-geo-p1-adjunction], the unit
(built from the cycle class of the diagonal and proper base change) and the
counit (the trace and the projection formula) are compatible with base change
$g$. Hence the transpose of the composite in the statement, for this $p$, is
the canonical identification $g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$; so $\beta_N$ is an
isomorphism. (b) For an open immersion $j$, $j^!=j^*$ with counit the counit
of $j_!\dashv j^*$, extension by zero commutes with base change, and $\beta_N$
is the identification $g'^*j^*=j'^*g^*$. Combining (a) and (b) with
$\mathbf A^1=\mathbf P^1\setminus\infty$ and iterating over coordinates gives the
case of $a:\mathbf A^d_S\to S$, where $a^!=a^*(d)[2d]$ and $\beta_N$ is the
ordinary identification. (c) For a separated étale $e$, $e^!=e^*$ with counit
the sum over the geometric sheets of $e_!$; both commute with base change, and
$\beta_N$ is again the ordinary inverse-image identification.

*Step 2: composition.* For composable $h_1,h_2$, the counit of
$R(h_2h_1)_!\dashv(h_2h_1)^!$ is the composite of the counits under the
composition isomorphism, and base change for $R(-)_!$ is compatible with
composition ([Stacks, Tag 0F7L](https://stacks.math.columbia.edu/tag/0F7L)). Substituting into the definition, $\beta$ for
$h_2h_1$ is the composite of $h_1^*$-shifted $\beta$ for $h_2$ and $\beta$ for
$h_1$, under the composition isomorphisms; so if the $\beta$'s of $h_1$ and
$h_2$ are isomorphisms, so is that of $h_2h_1$ (compare
[lem-pur-co-smooth-composition]). The same holds for restriction to opens
of the source: for $u:U\hookrightarrow X$ open, $u'^*\beta^f_N$ corresponds to
$\beta^{fu}_N$ under $u^*f^!\simeq(fu)^!$.

*Step 3: charts.* Cover $X$ by opens $U$ with $f|_U=v\circ a\circ e$ as in the
local structure of smooth morphisms ($v:V\to S$ open, $a:\mathbf A^d_V\to V$,
$e:U\to\mathbf A^d_V$ separated étale). By Steps 1–2, the restriction of
$\beta_N$ to $U'=U\times_XX'$ is the composite of the isomorphisms of the
three elementary cases, hence an isomorphism. The $U'$ cover $X'$, and
isomorphisms are detected on an open covering, so $\beta_N$ is an
isomorphism. For $N=\Lambda_S$ this is $g'^*\omega_f\simeq\omega_{f'}$.

*Step 4: compatibility with the tensor maps.* The tensor map is the transpose
of $(1\otimes\epsilon_\Lambda)\circ\mathrm{PF}$, with $\mathrm{PF}$ the projection
formula ([thm-asd-smooth-tensor]). The compact-support base-change isomorphism
is compatible with the projection formula and $g^*$ commutes with
$\otimes^{\mathbf L}$; so applying $g^*$ to this composite and transposing gives,
on one side, $\beta_N\circ g'^*(\text{tensor map})$ and, on the other,
(tensor map for $f'$)$\circ(1\otimes\beta_\Lambda)$; uniqueness of transposes
gives the commutativity of the square.
