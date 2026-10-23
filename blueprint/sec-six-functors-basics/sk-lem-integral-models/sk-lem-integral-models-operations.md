+++
id = "det-lem-integral-models-operations"
kind = "lemma"
title = "Inverse image, tensor product and extension by zero preserve $D^b_c(-,\\mathcal O_E)$"
order = 2189
uses = ["sk-prop-integral-criterion", "det-prop-sfb-cartesian-coefficients-finite-free", "sk-prop-sfb-cartesian-coefficients"]
+++
Let $E/\mathbf Q_\ell$ be finite and all schemes Noetherian.

1. For $f\colon X\to Y$ and $K\in\Dbc(Y,\cO_E)$, $f^*K\in\Dbc(X,\cO_E)$.
2. For $K,M\in\Dbc(X,\cO_E)$, $K\otimes^{\mathbf L}_{\cO_{E,X}}M\in\Dbc(X,\cO_E)$ (no completion is
   needed).
3. For a locally closed immersion $a=i\circ u\colon S\hookrightarrow\overline S\hookrightarrow X$
   and $L\in\Dbc(S,\cO_E)$, $a_!L=i_*u_!L\in\Dbc(X,\cO_E)$.
4. For $a$ as in (3), $L\in D(S_{\mathrm{proét}},\cO_E)$ and $M\in D(X_{\mathrm{proét}},\cO_E)$,
   $(a_!L)\otimes^{\mathbf L}M\simeq a_!(L\otimes^{\mathbf L}a^*M)$.
