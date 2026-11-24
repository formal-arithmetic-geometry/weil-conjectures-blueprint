+++
id = "proposition-dctf-x-qbar-2-colimit"
kind = "proposition"
title = "$\\Dctf(X,\\Qbar)$ as a $2$-colimit"
order = 649
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit", "AlgebraicGeometry.ProEtale.finiteCoefficientDescentTwoColimit"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field"]
+++
Extension of scalars identifies

$$
\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)}\simeq\mathop{\text{2-colim}}_{E\subset\overline{\mathbf Q}_\ell}\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,E)}
$$

as ordinary categories. In other words, every object of [$D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)$](@definition-constructible-sheaves) is isomorphic to
$K_{\overline{\mathbf Q}_\ell}$ for some finite $E$ and some $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,E)}$, and for
$K,L\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,E)}$ extension of scalars induces a bijection

$$
\varinjlim_{F\supset E}\Hom_{\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,F)}}(K_F,L_F)
\xrightarrow{\sim}\Hom_{\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)}}(K_{\overline{\mathbf Q}_\ell},L_{\overline{\mathbf Q}_\ell}),
$$

the colimit running over finite extensions $F$ of $E$ in $\overline{\mathbf Q}_\ell$.
