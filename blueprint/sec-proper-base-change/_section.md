+++
id = "sec-proper-base-change"
kind = "section"
title = "Proper Base Change"
order = 1529
uses = ["sec-abelian-varieties", "sec-curve-estimates", "sec-nagata-compactification", "sec-picard-framework", "sec-proetale-coefficients", "sk-thm-chow-projective", "sk-cor-curve-invariance", "sk-def-exchange", "sk-def-pbc-conventions", "sk-lem-curve-dense-open", "sk-lem-curve-normalization", "sk-lem-pbc-finite", "sk-prop-curve-artin-schreier", "sk-thm-br", "sk-thm-curve-package", "sk-thm-curveestimate"]
+++
**Content.** For a proper morphism $f\colon X\to Y$, any base change $g\colon Y'\to Y$ and any torsion sheaf $F$ on $X_{\mathrm{et}}$, the exchange morphism [sk-def-exchange] $g^{-1}Rf_*F\to Rf'_*g'^{-1}F$ is an isomorphism. The property PBC [sk-def-pbc] is first shown equivalent to injective acyclicity IA [sk-def-ia] in [sk-thm-iff]: with $\mathbb{Z}/r$-coefficients, base changes of injectives are $f'_*$-acyclic, so by the acyclicity criterion [sk-thm-acyclicity] only the degree-zero exchange is left, which holds because both stalks compute sections over the same closed geometric fibre. The projective line is then handled directly in [sk-thm-p1], using the curve calculations of §[sec-curve-estimates], their invariance under separably closed field extension, and a comparison over strictly henselian bases. Chow's lemma [sk-thm-chow], finite morphisms, the symmetric product $(\Pone)^n\to\Pqn$, and composition and cancellation of PBC via the Grothendieck spectral sequence [det-thm-groth-ss] reduce every proper $f$ to $\Pone$ [sk-thm-reduction]. Dévissage from prime to arbitrary torsion coefficients then gives [sk-thm-properbasechange].

**Key theorem.**

- Thm [sk-thm-properbasechange] (proper base change): for $f$ proper and $F$ torsion, $g^{-1}Rf_*F\xrightarrow{\sim}Rf'_*g'^{-1}F$ for every cartesian square. Used in §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-six-functors], §[sec-trace-formula], §[sec-poincare-duality], §[sec-purity-real-sheaves], §[sec-fourier-transform], §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general], §[sec-zeta-weil].
- Thm [sk-thm-p1] (PBC for the projective line): for every scheme $S$ the projection $\Pone_S\to S$ satisfies PBC. Used in §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-six-functors], §[sec-poincare-duality], §[sec-algebraic-groups-lie-algebras], §[sec-purity-real-sheaves], §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general].
- Thm [sk-thm-iff] (PBC $\Leftrightarrow$ IA): a proper $f$ satisfies PBC if and only if base changes of injective $\mathbb{Z}/r$-sheaves have vanishing higher direct images, for all primes $r$. Used in §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-deligne-laumon-a1].

**References.**

- Stacks Project: `095T` (proper base change theorem); the section follows the Stacks Project proof.
