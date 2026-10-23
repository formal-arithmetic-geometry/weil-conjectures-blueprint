+++
id = "det-sp-composition-comparisons"
kind = "lemma"
title = "Composition of adjunctions and of coefficient comparisons"
order = 3055
uses = ["det-sp-reduction-direct-image", "det-sp-reduction-exceptional", "det-sp-tower-gluing", "det-sp-integral-adjunction-bijection"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions $d$
and $e$, and $A\to B$ a map of finite rings killed by a power of $\ell$.

1. Composing the adjunctions $Rf_{!,A}\dashv f^!_A$ and $Rg_{!,A}\dashv g^!_A$
   identifies $(g\circ f)^!_A\simeq f^!_Ag^!_A$, compatibly with
   $R(g\circ f)_{!,A}\simeq Rg_{!,A}Rf_{!,A}$; the counit of the composite
   adjunction is $\varepsilon_g\circ Rg_!(\varepsilon_f g^!)$.
2. For $M\in\Dctf(X_{\mathrm{proét}},A)$ and $K\in\Dctf(Z_{\mathrm{proét}},A)$,
   $$
   b^{g\circ f}(M)=Rg_{!,B}(b^f(M))\circ b^g(Rf_{!,A}M),
   \qquad
   c^{g\circ f}_{A,B}(K)=f_B^!c^g_{A,B}(K)\circ c^f_{A,B}(g_A^!K),
   $$
   in $\Dctf(Z_{\mathrm{proét}},B)$ and $\Dctf(X_{\mathrm{proét}},B)$ respectively.
3. The tower versions of these composition isomorphisms evaluate at each level to
   the finite ones and preserve normalized towers; for $E=\Ql$, $R\varprojlim$
   gives the integral composition isomorphisms
   $R(g\circ f)_{!,\Zl}\simeq Rg_{!,\Zl}Rf_{!,\Zl}$ and
   $(g\circ f)^!_{\Zl}\simeq f^!_{\Zl}g^!_{\Zl}$ on $\Dbc(-,\Zl)$.
