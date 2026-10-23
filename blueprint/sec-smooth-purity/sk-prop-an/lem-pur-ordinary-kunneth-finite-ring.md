+++
id = "lem-pur-ordinary-kunneth-finite-ring"
kind = "lemma"
title = "Ordinary Kunneth at a finite coefficient ring"
order = 2914
uses = ["def-kun-derived-tensor", "def-kun-kunneth-map", "def-weil-finite-field-fiber", "def-weil-pbc-derived-categories", "def-weil-scheme-morphism-properties", "lem-kun-0f10", "lem-kun-0f12", "thm-kun-0f1p"]
+++
Let $k$ be the algebraically closed field of
[def-weil-finite-field-fiber], and let $X,Y$ be
separated finite-type
$k$-schemes. Put $A=\mathcal O_E/\pi_E^n$, for $E/\mathbf Q_\ell$ finite, $n\geq1$, and $\ell\neq\operatorname{char}(k)$.
For $K\in D(X_{\mathrm{et}},A)$ and
$L\in D(Y_{\mathrm{et}},A)$ in the
derived categories,
write $K\boxtimes_A^L L=p_X^*K\otimes_A^Lp_Y^*L$, using the
derived tensor product.
The exterior-product map is an isomorphism

$$
R\Gamma(X,K)\otimes_A^LR\Gamma(Y,L)
\longrightarrow R\Gamma(X\times_kY,K\boxtimes_A^L L).
$$
