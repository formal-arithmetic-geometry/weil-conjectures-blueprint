+++
id = "lemma-weil-pbc-universal-homeomorphism-descent-datum"
kind = "lemma"
title = "Canonical etale descent across a universal homeomorphism"
order = 1770
+++
**Status.** Bypassed by the formalized route: Lemma [lemma-weil-pbc-universal-homeomorphism-site-equivalence] is proved in Lean following the second proof of Tag `04DZ` (graph descent, the section trick and fibre-degree induction), which does not go through the canonical descent datum.

Let $u:X_0\to X$ be a universal homeomorphism. For every etale
$V_0\to X_0$, the two pullbacks to $X_0\times_XX_0$ have a unique
isomorphism whose restriction along the diagonal is the identity. This
isomorphism is a descent datum and is compatible with morphisms, identities,
and composition.

## Proof

A universal homeomorphism is integral, surjective, and universally
injective. Hence the diagonal

$$
\Delta:X_0\longrightarrow X_0\times_XX_0
$$

is a closed immersion and is surjective on points. On affine charts it is
therefore defined by a nil ideal: if
$X=\operatorname{Spec}A$ and $X_0=\operatorname{Spec}B$, the multiplication
$B\otimes_AB\to B$ is surjective and its kernel is contained in every prime
ideal.

We first record the nil-ideal calculation used below. If $R\to R/J$ has
$J$ nil, reduction gives an equivalence between etale $R$-algebras and
etale $R/J$-algebras. For a finitely presented affine etale algebra this is
checked on a Jacobian presentation

$$
((R/J)[T_1,\ldots,T_m]/(f_1,\ldots,f_m))_g
$$

with the relevant Jacobian minor invertible. Lift the finitely many
coefficients and $g$ to $R$. The same minor remains invertible after
localization because an element invertible modulo a nil ideal is invertible.
Existence of a lift of a morphism follows by successively correcting the
images of the $T_i$ modulo the powers of the finitely generated nil ideal
appearing in those coefficients; the inverse Jacobian gives the correction.
The process is finite because that finitely generated subideal is nilpotent.
If two lifts agree modulo $J$, their difference lies in $J$; the same
linearized equations and inverse Jacobian force equality, one nilpotence
power at a time. General etale schemes are glued from such affine pieces;
the uniqueness just proved makes the overlap maps and their cocycle
equations lift uniquely.

Apply this nil-invariance to $\Delta$. The two pullbacks
$p_1^*V_0$ and $p_2^*V_0$ restrict along $\Delta$ to the same etale
$X_0$-scheme $V_0$. Thus there is a unique isomorphism

$$
\alpha:p_1^*V_0\xrightarrow{\sim}p_2^*V_0,\qquad
\Delta^*\alpha=\operatorname{id}_{V_0}.
$$

On $X_0\times_XX_0\times_XX_0$, both
$p_{23}^*\alpha\circ p_{12}^*\alpha$ and $p_{13}^*\alpha$ restrict to the
identity along the small diagonal. That diagonal is again a surjective
closed immersion defined by a nil ideal, so uniqueness gives the cocycle
equation. If $a:V_0\to W_0$ is a morphism, the two composites
$p_2^*a\circ\alpha_V$ and $\alpha_W\circ p_1^*a$ have the same diagonal
restriction and hence are equal. Taking $a$ to be an identity or a
composite proves the asserted identity and composition compatibilities.
