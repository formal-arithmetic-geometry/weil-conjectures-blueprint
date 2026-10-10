+++
id = "sec-smooth-base-change"
kind = "section"
title = "Smooth Base Change"
order = 1363
uses = ["sec-curve-estimates"]
+++
**Content.** For a Cartesian square with $f\colon X\to S$ smooth and $g\colon T\to S$ quasi-compact quasi-separated, the base-change map $f^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ of [sk-def-bc] is an isomorphism for torsion $\mathcal F$ of orders invertible on $S$. The section follows the Stacks Project's second, shorter proof. Degree zero holds for any flat finitely presented $f$ with geometrically reduced fibres [sk-prop-deg0]. Passing to filtered colimits reduces to $\mathbb Z/n$-coefficients, and the étale-local normal form [sk-prop-normal-form] reduces to affine smooth curves $X\to S$. Then one inducts on $q$ [sk-lem-induction], with two lanes that contradict each other. The counterexample lane uses injectivity of the critical map [sk-prop-injectivity] and minimal counterexamples [sk-lem-minimal], [sk-lem-failure-field] to turn a first failure into a universal curve-test datum with $R^qh_*(\mathbb Z/d)\neq0$ over a normal base with algebraically closed function field [sk-lem-universal-datum]. The curve-test lane shows that this sheaf vanishes [sk-thm-vanishing]. For $q\ge2$ this is cohomological dimension of affine curves. For $q=1$ it combines torsors [sk-prop-input-torsors], field-extension invariance and the spreading of Galois covers [sk-prop-input-spreading].

**Key theorem.**

- Thm [sk-thm-smooth-base-change] (smooth base change): for $f$ smooth, $g$ qcqs and $\mathcal F$ torsion of orders invertible on $S$, $f^{-1}R^qg_*\mathcal F\xrightarrow{\sim}R^qh_*e^{-1}\mathcal F$ for all $q$. Used in §[sec-smooth-purity], §[sec-six-functors], §[sec-zeta-weil].
- Thm [sk-thm-vanishing] (vanishing in the universal curve test): for $X\to S$ affine smooth of relative dimension one over a normal $S$ with algebraically closed fraction field $L$, and $K/L$ an extension of algebraically closed fields, $R^qh_*(\mathbb Z/d)=0$ for $q\ge1$ along $X\times_S\operatorname{Spec}K\to X$. Used in §[sec-fourier-transform].
- Prop [sk-prop-input-torsors] (torsors and étale $H^1$): $M$-torsors on $Y_{\mathrm{\acute et}}$, equivalently finite étale $Y$-schemes with simply transitive $M$-action, are classified by $H^1(Y_{\mathrm{\acute et}},\underline M)$. Used in §[sec-purity-real-sheaves].

**References.**

- Stacks Project, the smooth base change theorem and its second proof: `0EYU` (theorem), `0F02` (property $BC(f,n,q)$), `0F03`, `0F06`, `0F07`, `0F08` (counterexample lemmas).
- Stacks Project, degree zero and normal forms: `0EYS`, `0EZX`, `0A3H` (flat base change in degree zero); `0EY5`, `054L`, `0EY4` (étale-local structure of smooth morphisms); `09Z9` (étale covers of normal schemes).
- Stacks Project, spreading of Galois covers: `0EZJ`, `0EYJ` (main statements); `09EB`, `0EYG`, `0EYH`, `0EYI` (tame ramification); `0EYE`, `0EY6`, `0EY9`, `0EYB` (purity and extension in depth $\ge2$); `031S`, `0337`, `05D5`, `0BQ5`, `0EY3` (depth, completions, spreading out).
- Stacks Project: `02NE` (torsors and $H^1$).
- J. S. Milne, *Lectures on Étale Cohomology*, III.3 (torsors and $H^1$).
