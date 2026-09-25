+++
id = "lem-a1-affine-hc2"
kind = "lemma"
title = "Description of $H_c^2$ on an affine curve"
order = 2838
uses = ["def-weil-ordinary-compact-cohomology", "def-wf-fundamental-representation", "def-wf-monodromy-data", "def-wf-tate-twist", "lem-wf-smooth-dualizing-complex", "p-real-sections", "thm-pod-global-verdier-duality"]
+++
Let $U_0$ be a smooth geometrically connected affine curve, let
$U=U_0\times_{k_0}k$, and let $\mathcal F$ be a lisse Weil sheaf on
$U_0$ with local generic fiber $V=\mathcal F_{\bar\eta}$ (a
geometric generic stalk of [def-wf-fundamental-representation]).
In the compactly
supported cohomology of
[def-weil-ordinary-compact-cohomology] there is a canonical
Frobenius-equivariant isomorphism

$$
H_c^2(U,\mathcal F)\;\simeq\;V_{\pi_1(U)}(-1),
$$

where the coinvariants are formed for the geometric monodromy action of
[def-wf-monodromy-data] and $(-1)$ is the
Tate twist $(-1)$.

## Proof

Apply the global Verdier duality of [thm-pod-global-verdier-duality]
in dimension one. It identifies the dual of
$H_c^2(U,\mathcal F)$ with

$$
H^{-2}\bigl(U,\mathbb D_U\mathcal F\bigr),
$$

where $\mathbb D_U\mathcal F=R\operatorname{Hom}(\mathcal F,\omega_U)$
and, by the smooth dualizing complex of [lem-wf-smooth-dualizing-complex]
in dimension one, $\omega_U\simeq\Qlb(1)[2]$: hence
$\mathbb D_U\mathcal F\simeq\mathcal F^\vee(1)[2]$, and therefore
$H^{-2}(U,\mathbb D_U\mathcal F)=H^0(U,\mathcal F^\vee(1))$. Global sections of a lisse
sheaf are the invariants of the geometric representation of
[def-wf-fundamental-representation] [p-real-sections], so
$H^0(U,\mathcal F^\vee(1))=(V^\vee(1))^{\pi_1(U)}$. Dualizing turns
invariants of $V^\vee$ into coinvariants of $V$, and turns the twist
$(1)$ into $(-1)$, which gives the displayed isomorphism (the
Frobenius equivariance is the one induced by the Weil structure on the
twist, [def-wf-tate-twist]).
