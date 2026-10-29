+++
id = "k1-reduced-constant-lower-shriek-reduction-data"
kind = "definition"
title = "ReducedConstantLowerShriekReductionData"
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-curve-setting", "def-weil-pbc-eight-curve-assertions", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.IsCurve.ReducedConstantLowerShriekReductionData"]
order = 1773
+++
Let $k$ be an algebraically closed field, $f:X\to\operatorname{Spec}k$ a curve [def-weil-pbc-curve-setting] with $X$ reduced, $j:U\to X$ an open immersion, and $r$ a prime. Put $\Lambda=\mathbf Z/r\mathbf Z$, and for a scheme $W$ let $\Lambda_W/(r)$ denote the constant sheaf of $\Lambda$-modules on $W_{\Et}$ with value $\Lambda/r\Lambda$. The *reduction data* for $(f,j,r)$ is the following existential proposition: there exist a scheme $Y$, a morphism $\nu:Y\to X$, a dense open $V\subseteq X$, a scheme $U'$ and morphisms $j':U'\to Y$, $\nu':U'\to U$, such that $\nu$ is finite and surjective, $f\circ\nu$ is smooth [def-sbc-smooth-morphisms], $\nu$ restricted over $V$ is an isomorphism, $j'$ is an open immersion, the square $(j',\nu',\nu,j)$ is cartesian [def-weil-pbc-scheme-conventions], and $j'_!(\Lambda_{U'}/(r))$ [def-weil-pbc-extension-by-zero] satisfies the eight assertions for $f\circ\nu:Y\to\operatorname{Spec}k$ [def-weil-pbc-eight-curve-assertions].
