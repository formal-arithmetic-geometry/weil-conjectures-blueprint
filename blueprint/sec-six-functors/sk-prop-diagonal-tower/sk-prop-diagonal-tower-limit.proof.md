+++
kind = "proof"
of = "det-prop-diagonal-tower-limit"
+++
(1) The pro-étale site is replete and products of sheaves on it are exact
([sk-prop-pe-replete], [sk-prop-pe-products]); hence for an inverse system
with surjective transition maps $R\varprojlim$ is the ordinary limit. This
applies to the systems $\mathbf Z/\ell^\bullet$ and $\mu_{\ell^\bullet}$: on a
weakly contractible affine, taking sections is exact and the transition maps
stay surjective, so the Milnor complex
$\prod_n K_n\xrightarrow{1-\mathrm{shift}}\prod_nK_n$ computing
$R\varprojlim$ has no cohomology in degree one. Thus
$R\varprojlim\mathbf Z/\ell^n=\Zl$ and $R\varprojlim\mu_{\ell^n}=\Zl(1)$. The
functor $\Delta_*$ is exact and preserves limits, which gives the first
formula. In general, a derived direct image $Rg_*$ and $R\varprojlim$ are
both right adjoints of exact functors (inverse image and the constant-system
functor), so both preserve K-injective complexes, and their derived functors
commute (Stacks, Tag 099L). Evaluation of an inverse system at one level is
right adjoint to an exact functor too, so it preserves injectives, and the
derived direct image of a system is computed levelwise.

(2) $\Zl(1)$ is free of rank one on the pro-étale cover given by the system
of primitive $\ell^n$-th roots of unity, and its reduction modulo $\ell^n$ is
$\mu_{\ell^n}$ with the transition maps of [det-prop-diagonal-tower-system](3).
Tensoring with a sheaf which is locally free of rank one is exact, and on the
trivializing cover it is the identity functor, so it commutes with products
and with $R\varprojlim$; these properties are local.

(3) By (1) and [det-prop-diagonal-tower-system](3), $R\varprojlim c_\bullet$
has source $\Delta_*\Zl$ and target $\Zl(1)[2]$; by
[det-prop-diagonal-tower-system](2) it equals the derived completion of
$\partial$, so in particular source and target are derived $\ell$-complete.
The limit morphism is a priori linear over the constant sheaf
$\underline{\mathbf Z_\ell}$. The map from $\underline{\mathbf Z_\ell}$ to the
completed coefficient sheaf $\Zl$ is flat and an isomorphism modulo every
$\ell^n$; hence restriction of scalars is an equivalence between derived
complete objects over $\Zl$ and derived complete objects over
$\underline{\mathbf Z_\ell}$ (Stacks, Tag 099I, as in
[sk-lem-integral-models](1)). So the morphism comes from a unique
$\Zl$-linear morphism $\delta_{\Zl}$. Its reduction modulo $\ell^n$ is the
$n$-th level of $c_\bullet$, because reduction commutes with $R\varprojlim$ on
these systems (the level-$n$ term of a derived complete object is its
reduction), and these levels are the torsion cycle classes by
[det-prop-diagonal-tower-system](4).
