+++
id = "def-weil-pbc-projection-formula-map"
kind = "definition"
title = "Projection-formula map"
order = 1320
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-module-pushforward-pullback", "def-weil-pbc-proetale-operations"]
+++
Let $\Lambda$ be a commutative condensed ring, with coefficient sheaves
$\Lambda_X=p_X^*\Lambda$ ([sk-def-sfb-pulled-back-coefficients]); the
construction works verbatim for any morphism of ringed topoi. For
$f:X\to Y$, $K\in D(X_{\Proet},\Lambda)$, and $P\in D(Y_{\Proet},\Lambda)$,
define

$$
 \pi_{f,K,P}:(Rf_*K)\otimes_{\Lambda_Y}^LP
 \longrightarrow Rf_*(K\otimes_{\Lambda_X}^LLf^*P)
$$

as the adjoint of the tensor product of the counit $Lf^*Rf_*K\to K$ with
$Lf^*P$, using the module pullback and pushforward of
[sk-def-sfb-module-pushforward-pullback] and their derived functors
[def-weil-pbc-proetale-operations].
