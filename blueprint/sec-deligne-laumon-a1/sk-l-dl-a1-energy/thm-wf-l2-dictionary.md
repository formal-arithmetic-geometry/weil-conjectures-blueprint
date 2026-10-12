+++
id = "thm-wf-l2-dictionary"
kind = "theorem"
title = "The Fourier-analytic weight of a pure real sheaf equals its weight"
order = 3100
uses = ["cor-rp-euler-product", "def-weil-frobenius-module-weights", "def-weil-punctual-weights", "def-wf-iota-real", "def-wf-l2-norm", "def-wf-l2-series", "lem-a1-affine-hc0", "lem-a1-middle-extension-endpoints", "lem-rp-even-tensor-positivity", "lem-wf-conjugate-tensor-traces", "lem-wf-l2-radius", "lem-wf-l2-upper", "lem-zl-log-det-identity", "p-linear-spectra"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.l2Weight_eq_of_isReal"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, and let $\mathcal G$ be a nonzero lisse
$\iota$-real Weil sheaf, punctually
$\iota$-pure of weight $w$. Then

$$
\|\mathcal G\|=w
$$

in the $L^2$-weight parameter of [def-wf-l2-norm].
