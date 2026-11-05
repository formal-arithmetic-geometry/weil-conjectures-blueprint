+++
kind = "proof"
of = "proposition-relative-affine-line--1"
order = 1354002
uses = ["definition-constructible-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "theorem-pure-lisse-sheaves-over-relative", "proposition-composition-base-change-rf-shriek", "lemma-weight-bounds-partitions", "lemma-weights-exact-sequence"]
+++
Choose a finite mixed filtration
$0=G_0\subset\cdots\subset G_n=G$, with successive quotients
punctually pure of weights $v_a\leq w$. The exact sequences of
$R^ip_!$ and Lemma [lemma-weights-exact-sequence] reduce the assertion
to these quotients. Fix one such quotient $H$, of weight $v$.

We first construct a relative-line stratification of $H$. This is a
finite sequence of open–closed decompositions whose pieces are either
quasi-finite over $Y_0$, or open in a relative affine line
$\mathbf A^1_{V_0}$ over a locally closed subscheme $V_0$ of $Y_0$,
surjective over $V_0$, and carrying a lisse restriction of $H$.
All restrictions remain punctually pure of weight $v$ by
Proposition [proposition-weights-under-usual-operations].

The construction uses Noetherian induction on closed subsets of $Y_0$.
For a nonempty reduced closed subscheme $T_0$, choose an integral
affine open $V_0\subset T_0$ and a dense open
$U_0\subset\mathbf A^1_{V_0}$ on which the pulled-back sheaf is
lisse. The generic-lissity lemma gives this open over $k_0$.
A nonzero polynomial vanishing on its complement has a nonzero
leading coefficient $b$. Over $W_0=D(b)\subset V_0$, every fibre
meets $U_0$, and the complement has finite fibres. Thus the open
piece is surjective over $W_0$, and its reduced closed complement
is quasi-finite over $Y_0$. Apply the induction hypothesis to the
reduced closed complement of $W_0$ in $T_0$ and glue the two
decompositions. The empty case is quasi-finite. To pass from
$Y_{0,\mathrm{red}}$ to $Y_0$, use the decomposition of
$\mathbf A^1_{Y_0}$ into the empty open and the closed subscheme
$\mathbf A^1_{Y_{0,\mathrm{red}}}$.

Now induct on this stratification. The quasi-finite pieces satisfy
the bound by Lemma [lemma-finite-quasi-finite-direct-images]. On
a lisse relative-line piece $U_0\to V_0$, apply
Theorem [theorem-pure-lisse-sheaves-over-relative]: the morphism is
smooth of relative dimension one, with nonempty affine fibres.
Compose with the quasi-finite immersion $V_0\to Y_0$. The
composition isomorphism of
Proposition [proposition-composition-base-change-rf-shriek] and
the composition lemma for weight bounds preserve the bound $v+i$.
Here Lean passes from sheaf bounds to complex bounds by the finite
truncation tower before composing the direct images.

For an open–closed decomposition $U_0\xrightarrow jX_0\xleftarrow iZ_0$
and a structure map $h:X_0\to Y_0$, the localization triangle gives
an exact sequence
$$
R^r(hj)_!j^*H\longrightarrow R^rh_!H
\longrightarrow R^r(hi)_!i^*H.
$$
The bounds for the outer terms give the bound for the middle term
by Lemma [lemma-weights-exact-sequence], as in
Lemma [lemma-weight-bounds-partitions](1). Repeating this proves
the bound for the stratified pure quotient. Finally $v_a+r\leq w+r$
for every quotient of the mixed filtration, and induction through
its short exact sequences gives the assertion for $G$.
