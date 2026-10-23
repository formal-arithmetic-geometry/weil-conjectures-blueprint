+++
id = "thm-pqf-zmt-factorization"
kind = "theorem"
title = "Zariski's main theorem: the quasi-finite factorization"
lean = ["AlgebraicGeometry.Scheme.Hom.exists_isOpenImmersion_isFinite_of_locallyQuasiFinite", "AlgebraicGeometry.Scheme.Hom.FiniteApproximation", "AlgebraicGeometry.Scheme.Hom.nonempty_finiteApproximation_of_isIntegralHom", "AlgebraicGeometry.Scheme.Hom.exists_finiteApproximation_of_isIntegralHom", "AlgebraicGeometry.Scheme.Hom.exists_isOpenImmersion_isFinite_locallyOfFinitePresentation"]
order = 310
uses = ["def-weil-pbc-scheme-conventions", "pqf-def-quasifinite", "thm-pqf-immersion-descent"]
+++
Let $f:X\to S$ be a
separated morphism of finite
type which is everywhere
quasi-finite, with $S$
quasi-compact and quasi-separated. Then there exist a scheme $T$, a
quasi-compact open
immersion $j:X\hookrightarrow T$ and a
finite morphism
$p:T\to S$ with $f=p\circ j$. If $f$ is moreover locally of finite
presentation, then $T$ can be chosen so that $p$ is finite and of finite
presentation.
