+++
id = "thm-pod-trace-isomorphism"
kind = "theorem"
title = "Trace isomorphism"
order = 2444
uses = ["cor-cbc-proper-coincidence", "cor-pod-constant-coefficients", "cor-pur-finite-stage-smooth-dualizing-complex", "def-pod-trace-cup-reading", "def-pur-smooth-trace", "def-weil-frobenius-coefficient-twists", "def-weil-poincare-trace-cup", "prop-cohomological-finiteness", "thm-pod-proper-poincare-duality"]
+++
In the Poincare duality conventions of this chapter (the fixed setting; $X_0$ not necessarily proper), let the field stage be $\Lambda \in \{ E,\overline{\mathbf Q}_{\ell }\}$ of the datum, and let $\Lambda _X$ be the constant sheaf with its canonical strict Weil structure. The trace map $\operatorname {tr}_X$ of [def-weil-poincare-trace-cup], in the reading of [def-pod-trace-cup-reading], is the counit of $Ra_{X!}\dashv Ra_X^!$ read through the canonical orientation $\eta _X$ of [cor-pur-finite-stage-smooth-dualizing-complex] (the normalized smooth trace), and

$$
\operatorname {tr}_X:\   H_c^{2d}\bigl(X,\Lambda (d)\bigr)\xrightarrow {\  \sim \  }\Lambda
$$

is an isomorphism, and so is its untwisted form (the twist elimination)

$$
\operatorname {tr}^{(-d)}_X:\   H_c^{2d}(X,\Lambda )\xrightarrow {\  \sim \  }\Lambda (-d).
$$

For the constant sheaf on the geometrically connected $X$, the geometric Frobenius $F$ acts as the identity on $H^0(X,\Lambda )\cong \Lambda$ and by $q^d$ on $H_c^{2d}(X,\Lambda )\cong \Lambda (-d)$. If $X_0$ is proper, then $H_c^{2d}=H^{2d}$ and $\operatorname {tr}^{(-d)}_X:H^{2d}(X,\Lambda )\xrightarrow{\sim}\Lambda (-d)$ is an isomorphism, with $F$ acting by $q^d$ on $H^{2d}(X,\Lambda)$.
