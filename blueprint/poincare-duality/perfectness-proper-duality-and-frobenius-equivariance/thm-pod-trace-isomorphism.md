+++
id = "thm-pod-trace-isomorphism"
kind = "theorem"
title = "Trace isomorphism"
order = 3826
uses = ["conventions-coefficient-categories-and-basic-operations", "cor-pod-constant-coefficients", "cor-pur-finite-stage-smooth-dualizing-complex", "def-pur-smooth-trace", "def-weil-frobenius-coefficient-twists", "def-weil-poincare-trace-cup", "prop-cohomological-finiteness", "thm-pod-proper-poincare-duality"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let the field stage be $\Lambda \in \{ E,\overline{\mathbf Q}_{\ell }\}$ of the datum, and let $\Lambda _X$ be the constant sheaf with its canonical strict Weil structure. The trace map $\operatorname {tr}^{(-d)}_X$ of [conventions-coefficient-categories-and-basic-operations], Definition 1.89, is the composite of the normalized smooth trace (through the canonical orientation $\eta _X$ of Corollary 8.53) with the shift comparison and the twist elimination of Definition 1.49:

$$
\operatorname {tr}^{(-d)}_X:\   H^{2d}(X,\Lambda )\xrightarrow {\  \sim \  }\Lambda (-d)
$$

is an isomorphism, and so is the twisted form

$$
\operatorname {tr}_X:\   H_c^{2d}\bigl(X,\Lambda (d)\bigr)\xrightarrow {\  \sim \  }\Lambda .
$$

For the constant sheaf on the geometrically connected $X$, the geometric Frobenius $F$ acts as the identity on $H^0(X,\Lambda )\cong \Lambda$ (the constant-sheaf degree-zero cohomology, by Proposition 1.58, and the geometric Frobenius acting trivially on the constant object) and by $q^d$ on $H^{2d}(X,\Lambda )\cong \Lambda (-d)$ (the trace being the counit, and the twist normalization of Definition 1.49 giving $q^{-d}$ on $\Lambda (d)$ and $q^d$ on $\Lambda (-d)$).

## Proof

By [cor-pod-constant-coefficients] at $i=0$ (with $X$ proper, so $H_c^0=H^0$, by [thm-pod-proper-poincare-duality]), the trace–cup pairing is perfect at degree $0$, i.e. $H^{2d}(X,\Lambda (d))\cong H^0(X,\Lambda )^\vee \cong \Lambda$, and the isomorphism is the map induced by the trace, by [def-weil-poincare-trace-cup] (the $\eta _X$-counit composite sent through the canonical orientation of the purity chapter, with the normalization of [def-pur-smooth-trace]); this is

$$
\operatorname {tr}_X:H^{2d}\bigl(X,\Lambda (d)\bigr) \xrightarrow {\  \sim \  }\Lambda
$$

and its untwisting gives $\operatorname {tr}^{(-d)}_X$, the definition of the trace map in [conventions-coefficient-categories-and-basic-operations] (after the compact-support comparison for the proper structure morphism). For the Frobenius action, $H^0(X,\Lambda )\cong \Lambda$ with $F$ acting as the identity is [prop-cohomological-finiteness]; for the top degree, the $F$-action on $\Lambda _X(d)$ in the trace is the twist normalization $q^{-d}$, of [def-weil-frobenius-coefficient-twists], so the untwisted form $\Lambda (-d)$ carries the $q^d$-action, again by [def-weil-frobenius-coefficient-twists].
