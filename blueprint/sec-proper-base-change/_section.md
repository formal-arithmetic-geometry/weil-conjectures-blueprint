+++
id = "sec-proper-base-change"
kind = "section"
title = "Proper Base Change"
order = 1626
uses = ["sec-curve-estimates"]
+++
**Content.** For a proper morphism $f\colon X\to Y$, any base change $g\colon Y'\to Y$ and any torsion sheaf $F$ on $X_{\mathrm{et}}$, the exchange morphism [sk-def-exchange] $g^{-1}Rf_*F\to Rf'_*g'^{-1}F$ is an isomorphism. For a coefficient ring $\Lambda$ which is torsion as an abelian group, the property $\mathrm{PBC}_\Lambda$ [sk-def-pbc] is first shown equivalent to injective acyclicity $\mathrm{IA}_\Lambda$ [sk-def-ia] in [sk-thm-iff]: base changes of injective $\Lambda$-module sheaves are $f'_*$-acyclic, so by the acyclicity criterion [sk-thm-acyclicity] only the degree-zero exchange is left, which holds because both stalks compute sections over the same closed geometric fibre. The projective line is then handled directly in [sk-thm-p1], using the curve calculations of §[sec-curve-estimates], their invariance under separably closed field extension, and a comparison over strictly henselian bases. Chow's lemma [sk-thm-chow-projective], finite morphisms, the symmetric product $(\Pone)^n\to\Pqn$, and composition and cancellation of PBC via the Grothendieck spectral sequence [det-thm-groth-ss] reduce every proper $f$ to $\Pone$ [sk-thm-reduction], still for torsion $\Lambda$. Reduction from $\Lambda$ to the rings $\Lambda/p\Lambda$ and dévissage of torsion sheaves then give arbitrary coefficient rings in [sk-thm-properbasechange].

**Key theorem.**

- Thm [sk-thm-properbasechange] (proper base change): for $f$ proper and $F$ torsion, $g^{-1}Rf_*F\xrightarrow{\sim}Rf'_*g'^{-1}F$ for every cartesian square. Used in §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-six-functors], §[sec-trace-formula], §[sec-poincare-duality], §[sec-purity-real-sheaves], §[sec-fourier-transform], §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general], §[sec-zeta-weil].
- Thm [sk-thm-p1] (PBC for the projective line): for every scheme $S$ the projection $\Pone_S\to S$ satisfies PBC. Used in §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-six-functors], §[sec-poincare-duality], §[sec-algebraic-groups-lie-algebras], §[sec-purity-real-sheaves], §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general].
- Thm [sk-thm-iff] (PBC $\Leftrightarrow$ IA): for $\Lambda$ torsion as an abelian group, a proper $f$ satisfies $\mathrm{PBC}_\Lambda$ if and only if base changes of injective $\Lambda$-module sheaves have vanishing higher direct images. Used in §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-deligne-laumon-a1].

**References.**

- Stacks Project: `095T` (proper base change theorem); the section follows the Stacks Project proof.
