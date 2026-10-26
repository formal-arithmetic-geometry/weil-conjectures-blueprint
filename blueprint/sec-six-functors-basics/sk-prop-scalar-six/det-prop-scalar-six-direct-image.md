+++
id = "det-prop-scalar-six-direct-image"
kind = "lemma"
title = "Coefficient comparison for ordinary direct image"
order = 2472
uses = ["det-prop-scalar-six-pullback", "det-prop-scalar-six-ctf", "sk-prop-ctf-finite-comparison", "sk-cor-pe-bounded-continuity", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sf-ctf-stability"]
+++
Let $f\colon X\to Y$ be a morphism of standing schemes and $\Lambda\to\Lambda'$ a listed
coefficient map. For $K\in\D(X_{\mathrm{proét}},\Lambda)$ let
$$
\gamma_{f,K}\colon(Rf_*K)_{\Lambda'}\longrightarrow Rf_*f^*\bigl((Rf_*K)_{\Lambda'}\bigr)\simeq Rf_*\bigl((f^*Rf_*K)_{\Lambda'}\bigr)\xrightarrow{Rf_*((\epsilon_K)_{\Lambda'})}Rf_*(K_{\Lambda'})
$$
be the composite of the unit of $f^*\dashv Rf_*$ on $\D(-_{\mathrm{proét}},\Lambda')$, the
pullback identification of [det-prop-scalar-six-pullback] (1), and the extension of
scalars of the counit $\epsilon_K\colon f^*Rf_*K\to K$. Then:

1. $\gamma_{f,K}$ is an isomorphism for $K\in\Dctf(X,\Lambda)$; both sides lie in
   $\Dctf(Y,\Lambda')$.
2. $\gamma$ is natural in $K$, compatible with composition
   ($\gamma_{gf,K}=Rg_*(\gamma_{f,K})\circ\gamma_{g,Rf_*K}$ under $R(gf)_*=Rg_*Rf_*$), and
   compatible with the units and counits of $f^*\dashv Rf_*$ over $\Lambda$ and $\Lambda'$:
   $\gamma_{f,f^*N}\circ(\eta_N)_{\Lambda'}$ is the unit $\eta_{N_{\Lambda'}}$ composed with the
   pullback identification.
