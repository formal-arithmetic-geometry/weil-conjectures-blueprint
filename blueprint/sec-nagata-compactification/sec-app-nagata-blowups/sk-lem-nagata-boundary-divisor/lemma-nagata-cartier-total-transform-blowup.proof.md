+++
kind  = "proof"
of    = "lemma-nagata-cartier-total-transform-blowup"
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-extended-ideal-affine-chart", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-chart", "prop-nagata-rees-graded"]
+++
Work over an affine open $\operatorname{Spec}(A)\subseteq T$ on which
$\mathcal L=(x)$ with $x$ a non-zero-divisor. A standard chart of the
blow-up has ring $A[I/a]\subseteq A_a$. If
$x(y/a^n)=0$ in this chart, then $a^mxy=0$ in $A$ for some $m$; regularity
of $x$ gives $a^my=0$, hence $y/a^n=0$. Thus the image of $x$ is regular
on every blow-up chart. It generates the extended ideal there, so these
local equations make $\mathcal L\mathcal O_{T'}$ an effective Cartier
ideal, hence an invertible one.
