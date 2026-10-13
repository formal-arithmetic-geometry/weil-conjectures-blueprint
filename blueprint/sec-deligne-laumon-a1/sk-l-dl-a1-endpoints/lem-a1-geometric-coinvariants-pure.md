+++
id = "lem-a1-geometric-coinvariants-pure"
kind = "lemma"
title = "Purity of the geometric coinvariants"
order = 3074
uses = ["def-weil-frobenius-module-weights", "def-weil-punctual-weights", "def-wf-fundamental-representation", "p-linear-filtration"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.isPureOfWeightOver_geometricCoinvariants"]
+++
Let $X_0$ be a scheme locally of finite type over $k_0=\mathbf F_q$,
$X=X_0\otimes k$, and let $\mathcal F$ be a lisse Weil sheaf on $X_0$
which is punctually $\iota$-pure of weight $w$. Its *geometric
coinvariants* are $W:=\Gamma(X,\mathcal F^\vee)^\vee$, the dual of the
global sections of the dual sheaf, with the Frobenius $F_W$ dual to the
one induced by the Weil structure. When $X$ is connected, with geometric
fundamental representation $V$ ([def-wf-fundamental-representation]),
$\Gamma(X,\mathcal F^\vee)=(V^\vee)^{\pi_1(X)}=(V_{\pi_1(X)})^\vee$, so $W$
is the coinvariant quotient $V_{\pi_1(X)}$ — the maximal geometrically
constant quotient of $\mathcal F$ — with its induced Frobenius; in
general $\Gamma(X,-)$ is a product over the connected components of $X$.
Then $(W,F_W)$ is $\iota$-pure of weight $w$ (possibly $W=0$).
