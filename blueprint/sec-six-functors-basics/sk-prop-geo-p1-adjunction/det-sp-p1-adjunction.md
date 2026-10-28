+++
id = "det-sp-p1-adjunction"
kind = "lemma"
title = "Triangle identities for the projective-line adjunction"
order = 2619
uses = ["det-sp-p1-trace", "thm-amb-p1-adjunction", "sk-prop-pe-unbounded-classical"]
+++
With the notation of [det-sp-p1-trace], let $\varepsilon_K$ and $\eta_M$ be the
counit and unit displayed in [sk-prop-geo-p1-adjunction]. Then for all $M$ on $\mathbf P^1_S$
and $K$ on $S$ (in $D(-_{\mathrm{ét}},\Lambda_n)$, and hence on the classical
pro-étale categories and on $\Dctf$):

$$
\varepsilon_{Rq_*M}\circ Rq_*(\eta_M)=\mathrm{id}_{Rq_*M},\qquad
q^*(\varepsilon_K)(1)[2]\circ\eta_{q^*K(1)[2]}=\mathrm{id}_{q^*K(1)[2]}.
$$

Hence $Rq_*\dashv q^*(-)(1)[2]$ with unit $\eta$ and counit $\varepsilon$, and both
are compatible with base change on $S$. The adjunction restricts to the
categories $\Dctf(-_{\mathrm{proét}},\Lambda_n)$.
