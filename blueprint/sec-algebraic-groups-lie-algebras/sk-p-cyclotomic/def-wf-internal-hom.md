+++
id = "def-wf-internal-hom"
kind = "definition"
title = "Internal Hom"
lean = ["AlgebraicGeometry.Etale.WeilComplex.internalHomFrobenius", "AlgebraicGeometry.Etale.DerivedCategoryFiniteTor.derivedHom"]
order = 2914
uses = ["def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "sk-def-sfb-bounded-constructible", "sk-thm-sf-ctf-stability"]
+++
Let $\Lambda\in\{E,\Qlb\}$. On $\Dbc(X,\Lambda)\subseteq D(X_{\mathrm{proét}},\Lambda)$
([sk-def-sfb-bounded-constructible]) the internal Hom $R\mathcal Hom_{\Lambda_X}(-,-)$
is the restriction of the derived internal Hom of $\Lambda_X$-modules, computed from a
$K$-injective replacement in its second variable; it preserves $\Dbc$ by
[sk-thm-sf-ctf-stability]. For Weil complexes $(K,\varphi_K)$, $(L,\varphi_L)$ with
$K,L\in\Dbc(X,\Lambda)$ ([sk-def-sf-weil-complexes], [def-weil-weil-sheaf-complex]) the
internal-Hom Frobenius is the composite

$$
\Phi_X^*R\mathcal Hom_{\Lambda_X}(K,L)\stackrel{\sim}{\to}
R\mathcal Hom_{\Lambda_X}(\Phi_X^*K,\Phi_X^*L)
\xrightarrow{R\mathcal Hom(\varphi_K^{-1},\varphi_L)}
R\mathcal Hom_{\Lambda_X}(K,L).
$$

For $L=\Lambda_X$ with $\varphi_L=\varphi_\Lambda$ this is the contragredient datum of
[sk-def-sf-weil-complexes].
