+++
kind = "proof"
of = "proposition-additivity-trace-classes--1"
order = 942004
uses = ["lemma-external-duality-trace-morphism", "definition-trace-morphism", "definition-trace-class-local-terms", "proposition-six-operations-dctf"]
+++
By Lemma [lemma-external-duality-trace-morphism], the coefficient map $u$
determines a supported class
$\tilde u:Rc_!\Qbarl_C\to K\boxtimes\mathbb D_XK$.
The trace class is the image of $e_K\circ\tilde u$ under the additive
map from kernels $Rc_!\Qbarl_C\to R\Delta_{X*}\omega_X$ to
$H^0(\Fix(c),\omega_{\Fix(c)})$; here $e_K$ is the evaluation kernel
of Definition [definition-trace-morphism]. This is
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_traceClassOfKernel`.
The same description applies to $u'$ and $u''$.

Apply the exact functor $-\boxtimes N$ to the given triangle for
$N=\mathbb D_XK,\mathbb D_XK',\mathbb D_XK''$. Verdier duality sends
$\eta\circ\epsilon=0$ to
$\mathbb D_X(\epsilon)\circ\mathbb D_X(\eta)=0$.
The maps induced by these dual morphisms commute with the three rows;
the evaluation kernels are dinatural, and the supported classes are
compatible with the rows by the two assumed coefficient identities.

The three rows therefore satisfy
`CategoryTheory.Pretriangulated.comp_eq_add_of_distTriang`. Its proof
forms the homotopy pullback of the row for $\mathbb D_XK$ along
$K''\boxtimes\mathbb D_XK''\to K''\boxtimes\mathbb D_XK$ and lifts the
supported classes to it. The first three vanishing assumptions identify
the required lifts. The defect of additivity vanishes on
$K'\boxtimes\mathbb D_XK$ and on $K\boxtimes\mathbb D_XK''$, hence
factors through $(K'\boxtimes\mathbb D_XK'')[1]$ and is zero by the
fourth assumption. Thus

$$
e_K\circ\tilde u=e_{K'}\circ\tilde u'+e_{K''}\circ\tilde u''.
$$

Applying the additive map from kernels to trace classes proves the claim.
