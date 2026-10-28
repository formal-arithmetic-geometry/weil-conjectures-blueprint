+++
id = "det-prop-scalar-six-tensor-hom"
kind = "lemma"
title = "Coefficient comparison for tensor product and internal Hom"
order = 2821
uses = ["det-prop-scalar-six-ctf", "det-prop-scalar-six-direct-image", "det-prop-scalar-six-exceptional", "sk-thm-sf-ctf-stability"]
+++
Let $\Lambda\to\Lambda'$ be a listed coefficient map and $X$ a standing scheme.

1. For $K,M\in\D(X_{\mathrm{proét}},\Lambda)$ there is a natural isomorphism
   $(K\otimes^{\mathbf L}_{\Lambda_X}M)_{\Lambda'}\simeq K_{\Lambda'}\otimes^{\mathbf L}_{\Lambda'_X}M_{\Lambda'}$, making
   extension of scalars a symmetric monoidal functor.
2. For $K,M\in\Dctf(X,\Lambda)$ the map
   $$
   v_{K,M}\colon\bigl(R\mathcal Hom_{\Lambda_X}(K,M)\bigr)_{\Lambda'}\longrightarrow R\mathcal Hom_{\Lambda'_X}(K_{\Lambda'},M_{\Lambda'}),
   $$
   transpose under $-\otimes^{\mathbf L}K_{\Lambda'}\dashv R\mathcal Hom(K_{\Lambda'},-)$ of
   $(R\mathcal Hom(K,M))_{\Lambda'}\otimes^{\mathbf L}K_{\Lambda'}\simeq(R\mathcal Hom(K,M)\otimes^{\mathbf L}K)_{\Lambda'}\xrightarrow{(\mathrm{ev})_{\Lambda'}}M_{\Lambda'}$,
   is an isomorphism in $\Dctf(X,\Lambda')$.
