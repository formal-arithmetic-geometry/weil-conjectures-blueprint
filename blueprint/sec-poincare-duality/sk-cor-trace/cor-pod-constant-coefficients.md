+++
id = "cor-pod-constant-coefficients"
kind = "theorem"
title = "Constant coefficients"
order = 2587
tags = ["latex:corollary"]
uses = ["def-pod-coefficient-dual-on-x", "def-pur-smooth-trace", "def-weil-poincare-trace-cup", "prop-cohomological-finiteness", "prop-pod-degree-of-the-pairing", "thm-pod-degreewise-perfectness-over-a-field", "thm-pod-derived-poincare-duality", "thm-pod-identification-of-the-comparison", "thm-pod-proper-poincare-duality"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), restrict to the field stage $\Lambda\in\{E,\Qlb\}$, and put $K=\Lambda _X$ (perfect, with canonical evaluation the unit identification). Poincare duality is the perfect pairing

$$
H_c^i(X,\Lambda )\times H^{2d-i}\bigl(X,\Lambda (d)\bigr) \longrightarrow \Lambda ,
$$

equivalently the line-valued pairing

$$
H_c^i(X,\Lambda )\times H^{2d-i}(X,\Lambda ) \longrightarrow \Lambda (-d),
$$

for every $i\in \mathbf Z$. If $X$ is geometrically connected, then, by the $i=0$ case together with the cohomological finiteness of Proposition 1.58,

$$
H_c^{2d}\bigl(X,\Lambda (d)\bigr)\cong \Lambda , \qquad H_c^{2d}(X,\Lambda )\cong \Lambda (-d),
$$

with the first isomorphism induced by the trace map; the same holds with $H_c$ replaced by $H$ if $X$ is proper.

## Proof

Step 1: the coefficient dual of the constant object. For $K=\Lambda _X$, $K^\vee =R\mathcal Hom_X(\Lambda _X,\Lambda _X)=\Lambda _X$ with the unit identification as the canonical evaluation, by the internal-Hom with the unit object of [def-pod-coefficient-dual-on-x]; therefore

$$
K^\vee (d)[2d]=\Lambda _X(d)[2d].
$$

Step 2: the pairings. By [thm-pod-derived-poincare-duality] the derived pairing is perfect, and by [thm-pod-degreewise-perfectness-over-a-field] the degreewise pairings

$$
H_c^i(X,\Lambda )\times H^{2d-i}\bigl(X,\Lambda (d)\bigr)\to \Lambda
$$

are perfect; the line-valued form is the twist elimination of [prop-pod-degree-of-the-pairing]. Step 3: the top degree. Perfectness at $i=0$ gives $H^{2d}(X,\Lambda (d))\cong H_c^0(X,\Lambda )^\vee$. For $X$ geometrically connected, the constant sheaf has $H_c^0(X,\Lambda )\cong \Lambda$ and, for the proper case, $H^0(X,\Lambda )\cong \Lambda$ with the geometric Frobenius acting as the identity, by [prop-cohomological-finiteness]; the field-stage degree-zero cohomology is the one used here. The dual is therefore $\Lambda$, and the displayed isomorphisms $H_c^{2d}(X,\Lambda (d))\cong \Lambda$, $H_c^{2d}(X,\Lambda )\cong \Lambda (-d)$ follow, the second being the first transcribed along the twist $H^{2d}(X,\Lambda (d))\cong H^{2d}(X,\Lambda )\otimes \Lambda (d)$ of [prop-pod-degree-of-the-pairing]. Step 4: the identification with the trace. The degree-zero adjoint of the pairing is, by [thm-pod-identification-of-the-comparison], the transpose of the pairing under the duality isomorphism; the composite

$$
H^{2d}(X,\Lambda (d))\xrightarrow {\  \sim \  }H_c^0(X,\Lambda )^\vee \cong \Lambda
$$

is therefore the map sending the fundamental class to $1$, the normalization of the smooth trace in [def-pur-smooth-trace], so it is exactly the trace map of [def-weil-poincare-trace-cup]; its untwisted form is $\operatorname {tr}^{(-d)}_X$. The last assertion (for the proper case, $H_c$ replaced by $H$) is the proper comparison of [thm-pod-proper-poincare-duality].
