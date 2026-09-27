+++
id = "sk-thm-sf-kunneth-verdier"
kind = "section"
title = "Künneth–Verdier isomorphism"
order = 2224
uses = ["sk-def-sf-kv-maps", "sk-lem-sf-ctf-generation", "sk-lem-sf-kunneth-star", "sk-prop-sf-biduality-general", "sk-prop-sf-closed-unit", "sk-prop-sf-localization", "sk-thm-regular", "sk-thm-smooth-purity"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_externalProduct_verdierDual", "AlgebraicGeometry.Etale.hasKunnethComparisons"]
+++
*Theorem (sketch).*

The three maps of [sk-def-sf-kv-maps] are isomorphisms, natural in their
variables: the exceptional Künneth $\alpha$, the external Hom $\beta$, and
in particular, for $X,Y$ separated of finite type over $k$ and
$M\in\Dctf(X,\Lambda)$, $N\in\Dctf(Y,\Lambda)$,

$$
\kappa_{M,N}:M\boxtimes\mathbb D_YN\ \xrightarrow{\ \sim\ }\
\RHom\bigl(p_Y^*N,Rp_X^!M\bigr).
$$

## Proof

*The map $\alpha$.* Take first a constant auxiliary coefficient. For
smooth $f_i$ of relative dimension $d_i$, [sk-thm-smooth-purity] identifies
$Rf_i^!$ with $Lf_i^*(d_i)[2d_i]$, and its compatibility with base change and
with composition identifies the smooth product comparison with the ordinary
pullback–tensor comparison and the sum of the twists; the smooth trace is the
exceptional counit under this orientation, and its base-change square is the
adjoint of the same purity comparison, using the adjunction coherence of
fix-prop-adjunctions and the mate calculus [sk-lem-sf-mate]. Closed immersions are handled by supported
localization [sk-prop-sf-localization] together with the closed-immersion unit
[sk-prop-sf-closed-unit] and the case $Q=\Lambda_Z$ of
[sk-lem-sf-kunneth-star]; the regular case carries the fundamental class of
[sk-thm-regular]. An affine factorization of a general $f_i$ into a closed
immersion followed by a smooth projection gives the map locally. Finite
pushforward, open localization and the generation
[sk-lem-sf-ctf-generation] then remove the constant-coefficient
restriction. Hence $\alpha$ is invertible.

*The map $\beta$.* Dévissage in both $E_i$, by
[sk-lem-sf-ctf-generation], reduces to $E_i=Rh_{i!}\Lambda_{U_i}$ with
$h_i=g_ij_i$, $g_i$ finite and $j_i$ open. Tensor–Hom and the exceptional
adjunction give $\RHom(E_i,L_i)\simeq Rh_{i*}Rh_i^!L_i$
([sk-thm-sf-tensor-hom]). With $h=h_1\times h_2$ the comparison becomes

$$
Rh_{1*}Rh_1^!L_1\boxtimes Rh_{2*}Rh_2^!L_2
\xrightarrow[\text{twice}]{\ \mathrm{Ku}_*\ }
Rh_*\bigl(Rh_1^!L_1\boxtimes Rh_2^!L_2\bigr)
\xrightarrow{\ Rh_*\alpha\ }
Rh_*Rh^!\bigl(L_1\boxtimes L_2\bigr),
$$

the first arrow being [sk-lem-sf-kunneth-star] in each factor and the second
the $\alpha$ just proved. Taking ordinary and then exceptional adjoints
identifies this composite with the specified $\beta$: both paths become the
tensor product of the two evaluation maps after the projection formula. Hence
$\beta$ is invertible.

*The map $\kappa$.* Apply $\beta$ to the pairs $(\Lambda_X,M)$ and
$(N,\omega_Y)$, then $\RHom(1,\alpha)$ for the identification
$M\boxtimes\omega_Y\simeq Rp_X^!M$, which is $\alpha$ for
$\operatorname{id}_X\times a_Y$. Their composite is $\kappa_{M,N}$ by
[sk-def-sf-kv-maps] (iv), and both factors have just been shown invertible.

Uses: `\Cref{def:sf-kv-maps}`, `\Cref{lem:sf-ctf-generation}`, `\Cref{lem:sf-kunneth-star}`, `\Cref{prop:sf-biduality-general}`, `\Cref{prop:sf-closed-unit}`, `\Cref{prop:sf-localization}`, `\Cref{thm:regular}`, `\Cref{thm:smooth-purity}`
