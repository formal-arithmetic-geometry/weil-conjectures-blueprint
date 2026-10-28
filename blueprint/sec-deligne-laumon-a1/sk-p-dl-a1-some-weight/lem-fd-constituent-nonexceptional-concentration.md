+++
id = "lem-fd-constituent-nonexceptional-concentration"
kind = "lemma"
title = "Concentration of the zero-extension transform for a constituent-nonexceptional input"
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isZero_higherLowerShriek_realifiedKernel", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.higherLowerShriekRealifiedKernelIso", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isNonexceptional_dual", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isIrreducibleLisse_twistedDual", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isNonexceptional_twistedDual"]
order = 4228
uses = ["def-a1-constituent-nonexceptional", "def-fd-kernel", "def-fd-transform", "def-wf-constant-weil-twist", "def-wf-fundamental-representation", "lem-a1-affine-hc0", "lem-a1-affine-hc2", "lem-fd-as-characters", "lem-fd-realified-kernel-real", "lem-fd-stalk-formula", "lem-zl-affine-curve-range", "prop-functor-package", "rem-dl-a1-conventions"]
+++
In the conventions of [rem-dl-a1-conventions], let
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion with
$U_0=\mathbf A^1_{k_0}\setminus S_0$, and let $\mathcal M$ be a nonzero
irreducible lisse Weil sheaf on $U_0$ which is
constituent-nonexceptional in the sense of
[def-a1-constituent-nonexceptional]. No unramifiedness at infinity and
no geometric irreducibility is assumed.

1. For every $a\in k$ the twisted compact-support cohomology is
   concentrated in degree one:
   $$
   H^q_c\bigl(U,\,\mathcal M\otimes\mathcal L_{\psi(ax)}|_U\bigr)=0
   \qquad(q\neq1).
   $$
2. For every $b\in\Qlb^\times$ the twisted dual
   $\mathcal M^\dagger:=\mathcal M^\vee\otimes\mathcal B_b$, with the
   constant Weil twist of [def-wf-constant-weil-twist], is again a
   nonzero irreducible lisse Weil sheaf on $U_0$ which is
   constituent-nonexceptional.
3. The Fourier–Deligne transforms $\operatorname{FT}_\psi(j_!\mathcal M)$
   and $\operatorname{FT}_{\psi^{-1}}(j_!\mathcal M^\dagger)$ of
   [def-fd-transform] are concentrated in degree $0$. If moreover
   $\mathcal M$ is punctually $\iota$-pure of weight $w$ and
   $\mathcal K$ is the realified kernel of [lem-fd-realified-kernel-real]
   (formed with $\iota(b)=q^w$), then
   $$
   R^\nu p_{2,!}\mathcal K=0\qquad(\nu\neq1),
   $$
   and $\operatorname{FT}_\psi(j_!\mathcal M)$ is a direct summand of the
   sheaf $R^1p_{2,!}\mathcal K$.
